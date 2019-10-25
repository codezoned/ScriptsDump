#!/bin/bash


read -p 'Give a name to your project: ' PROJECT_NAME
read -p 'Specify the path of your react-project (the path of the directory that contains package.json): ' REACT_PATH
read -p 'Specify the ip address/your server domain from where you want to serve your app from (use localhost for testing): ' HOST_IP
read -p 'Specify the port to serve from (recommended for testing: 8080): ' HOST_PORT
echo "Sit back while I deploy your react app for you."
echo " "

echo "Setting up nginx..."

sudo apt-get install nginx

sudo rm -rf /etc/nginx/sites-enabled/${PROJECT_NAME}
touch /etc/nginx/sites-enabled/${PROJECT_NAME}

cat >> /etc/nginx/sites-enabled/${PROJECT_NAME} <<-EOF

server {
	listen ${HOST_PORT} default_server;
	root ${REACT_PATH}/build;
	server_name ${HOST_IP};
	index index.html index.htm;
	location / {
	}
}

EOF

echo "Building your React project"
cd ${REACT_PATH}
node scripts/build.js

echo " "
echo "Restarting nginx..."
sudo service nginx restart
echo "Done!"
echo "Your react app is online at ${HOST_IP}:${HOST_PORT}"

