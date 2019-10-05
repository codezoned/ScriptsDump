echo "Please select the appropriate option (press 1 or 2) - "
echo "	1. My server is not serving anything else. This React-app is the only thing I'll be deploying. (Recommended for most users)"
echo "	2. My server is serving another web-app and I want to deploy this react-app on the same url base url with a different path"
echo ">"
read choice

sudo apt-get install nginx

if [[ "${choice}" == "2" ]]
then
	echo "Please enter the subdomain that you'd like your app to be served at."
	echo "For example if your domain is example.com and you want your app to be served at example.com/myApp, enter /myApp"
	read HOST_SUB_URL
	echo "Enter the path of the current nginx file that you're using (include the file extension)"
	read NGINXCONF_PATH
	
	echo "Setting up nginx..."
	

	#touch /etc/nginx/sites-enabled/${NGINXCONF_NAME}.nginxconf
	
	touch nginxLocationBlock
	
	cat >> nginxLocationBlock <<-EOF
	
		location ${HOST_SUB_URL} {
			expires 1h;
			autoindex on;
			alias ${REACT_PATH}/build;
			try_files $uri $uri/ $uri.html /index.html;
		}
	
	EOF
	
	export locationBlock=$(<nginxLocationBlock)
	
	sudo sed '0,/location/i\${locationBlock}' ${NGINXCONF_PATH} # Have a bad feeling about this, hope it works.
