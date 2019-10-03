export PROJECT_NAME=$1

echo "Unhosting your website..."

echo "Removing hosting files..."
sudo rm -rf "/autohost/${PROJECT_NAME}_hostingdata"
echo "Removing nginx configurations..."
sudo rm -rf "/etc/nginx/sites-enabled/${PROJECT_NAME}"
sudo rm -rf "/etc/nginx/sites-available/${PROJECT_NAME}"
echo "Removing supervisor program..."
sudo rm -rf "/etc/supervisor/conf.d/${PROJECT_NAME}.conf"

echo "Done"
