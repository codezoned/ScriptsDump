# For Node-Express-Mongodb
This script will spin up docker containers of your nodejs app and mongodb process, and will run them in an isolated environment
accessible from the browser, thus deploying your nodejs app with a single command. Mongodb data is **not** lost on container restart.
The script will make a new ubuntu user (with limited permissions) named 'node' and then run your application using that user (this is to increase security).

Please note that this script **will not** install npm and node on your machine. That you'll need to do on your own.

The script requires the following parameters - 
* `NODE_DIRECTORY` - The path of the root directory of your node/expressjs project.
* `PROJECT_NAME` - An arbitrary, easy-to-remember name to give to your project.
* `HOST_PORT` - The port on which your app is set to listen.
* `DATABASE_DIRECTORY` - The path of the directory where you want to store your mongodb data.

## Instructions to run
1. Clone this repository and navigate to node-express-autohost.
2. Give host.sh executable permissions by `sudo chmod +x ./host.sh`
3. Simply run the script as sudo and enter the data it asks for. You must specify absolute paths only. `sudo ./host.sh`

**NOTE**: In your mongodb connection string, you must write `mongodb://mongo:27017/<databaseName>` instead of `mongodb://127.0.0.1:27017/<databaseName>`,
otherwise the script won't work. This is because docker will run mongodb on it's own internal network.

**NOTE**: You must run this script with sudo, as docker requires sudo for most of the stuff it does.
