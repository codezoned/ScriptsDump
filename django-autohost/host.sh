#!/bin/bash

export PROJECT_NAME=$1
export PROJECT_DIR=$2
export HOST_IP=$3
export HOST_PORT=$4

echo "Running autohost on ${PROJECT_NAME}..."

#------
HOSTING_DIR="/autohost/${PROJECT_NAME}_hostingdata"
echo "Saving hosting data in ${HOSTING_DIR}"

sudo rm -rf $HOSTING_DIR
sudo mkdir -p $HOSTING_DIR
sudo mkdir "${HOSTING_DIR}/logs"
sudo touch "$HOSTING_DIR/logs/gunicorn-supervisor.log"
sudo touch "$HOSTING_DIR/logs/nginx-access.log"
sudo touch "$HOSTING_DIR/logs/nginx-error.log"

#------
echo "Setting up Gunicorn..."
GUNICORN_SCRIPT="${HOSTING_DIR}/gunicorn-start.sh"

sudo touch $GUNICORN_SCRIPT

cat >> $GUNICORN_SCRIPT <<\EOF
#!/bin/bash
EOF

cat >> $GUNICORN_SCRIPT <<EOF
NAME="${PROJECT_NAME}"
SOCKFILE="${HOSTING_DIR}/run/gunicorn.sock"
DJANGODIR=${PROJECT_DIR}
USER=root
GROUP=webapps
NUM_WORKERS=4
DJANGO_SETTINGS_MODULE=${PROJECT_NAME}.settings
DJANGO_WSGI_MODULE=${PROJECT_NAME}.wsgi
EOF

cat >> $GUNICORN_SCRIPT <<\EOF
echo "Starting ${NAME} as root"
EOF

cat >> $GUNICORN_SCRIPT <<EOF
source "${HOSTING_DIR}/venv/bin/activate"
EOF

cat >> $GUNICORN_SCRIPT <<\EOF
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH
EOF

cat >> $GUNICORN_SCRIPT <<EOF
mkdir "${HOSTING_DIR}/run"

EOF

cat >> $GUNICORN_SCRIPT <<\EOF
exec gunicorn ${DJANGO_WSGI_MODULE}:application \
	--name $NAME \
	--workers $NUM_WORKERS \
	--user=$USER \
	--bind unix:$SOCKFILE 
EOF

sudo chmod u+x $GUNICORN_SCRIPT


#------
python3 -m venv "${HOSTING_DIR}/venv"
source "${HOSTING_DIR}/venv/bin/activate"

pip install -r "${PROJECT_DIR}/requirements.txt"
pip install gunicorn
pip install setproctitle

python "${PROJECT_DIR}/manage.py" collectstatic

deactivate

#-----
echo "Installing dependencies"
sudo apt-get install nginx
sudo apt-get install supervisor

echo "	"
echo "Setting up supervisor"
echo "${PROJECT_NAME}.conf"

sudo rm -rf "/etc/supervisor/conf.d/${PROJECT_NAME}.conf"
sudo cat >> "/etc/supervisor/conf.d/${PROJECT_NAME}.conf" <<EOF
[program:${PROJECT_NAME}]
command=${GUNICORN_SCRIPT}
user = root
stdout_logfile = "${HOSTING_DIR}/logs/gunicorn-supervisor.log"
redirect_stderror = true
EOF

sudo supervisorctl reread
sudo supervisorctl update

echo "	"
echo "Setting up nginx"
echo "Saving nginx configuration at /etc/nginx/sites-available/${PROJECT_NAME}"
sudo rm -rf /etc/nginx/sites-available/${PROJECT_NAME}
sudo rm -rf /etc/nginx/sites-enabled/${PROJECT_NAME}
touch /etc/nginx/sites-available/${PROJECT_NAME}

sudo cat >> /etc/nginx/sites-available/${PROJECT_NAME} <<EOF
upstream ${PROJECT_NAME}_app_server {
	server unix:${HOSTING_DIR}/run/gunicorn.sock fail_timeout=0;
}


server {
	listen ${HOST_PORT};
	server_name ${HOST_IP};
	
	client_max_body_size 4G;
	
	access_log ${HOSTING_DIR}/logs/nginx-access.log;
	error_log ${HOSTING_DIR}/logs/nginx-error.log;
	
	location /static/ {
		alias	$PROJECT_DIR/static/;
	}
	
	location /media/ {
		alias	$PROJECT_DIR/media;
	}
EOF
cat >> /etc/nginx/sites-available/$PROJECT_NAME <<\EOF
	location / {
          proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
          proxy_set_header Host $http_host;
          proxy_redirect off;
        if (!-f $request_filename) {
EOF

cat >> /etc/nginx/sites-available/$PROJECT_NAME <<EOF
            proxy_pass http://${PROJECT_NAME}_app_server;
            break;
        }
    }
    # Error pages
    error_page 500 502 503 504 /500.html;
    location = /500.html {
        root ${PROJECT_DIR}/static/;
	    }
}
EOF

sudo ln -s /etc/nginx/sites-available/${PROJECT_NAME} /etc/nginx/sites-enabled/

sudo nginx -s reload
sudo nginx -s reopen
sudo supervisorctl status $PROJECT_NAME


echo "Your project is up and running at ${HOST_IP}:${HOST_PORT}"



