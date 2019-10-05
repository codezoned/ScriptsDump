# For React
This works for react apps that are bootstraped with Facebook's create-react-app tool. The script will build and deploy your app
using nginx. It serves a production build of your app. Currently the app only works for cases in which the user does not have any
other nginx configuration. I'm still working on the script to add the app to an already existing nginx configuration.

The script will install nginx on your system. Currently I've only tested it's compatibility with Ubuntu 19.04.

## How to use - 
1. Clone this repository and navigate to /react-autohost
2. Give host.sh executable permissions by `sudo chmod +x ./host.sh`
3. Run `./host.sh`. The script will guide you through the process.

#### Note: Do not enclose your inputs in quotes when you run the script. The path of the react-project (that the script asks for) is the path of the directory which contains your package.json file.
