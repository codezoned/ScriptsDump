#!/bin/bash

echo "Note: If you're using mongodb, change your connectin string to mongodb://mongo:27017/<database_name>. None of this will work otherwise."

read -p 'Enter the path to the root directory of your project (the folder that contains package.json) > ' NODE_DIRECTORY
read -p 'What would you like to call this project? > ' PROJECT_NAME
read -p 'Enter the port on which your nodejs app listens > ' HOST_PORT
read -p 'Specify the directory where you want to store your mongodb data > ' DATABASE_DIRECTORY

echo " "
echo "Installing Docker..."

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable edge"
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable edge test"
sudo apt-get update
sudo apt-get install -y docker-ce

sudo curl -L "https://github.com/docker/compose/releases/download/1.22.0/docker-compose-$(uname -s)-$(uname -m)"  -o /usr/local/bin/docker-compose
sudo mv /usr/local/bin/docker-compose /usr/bin/docker-compose
sudo chmod +x /usr/bin/docker-compose

echo " "
echo "Setting up Docker to containerize your app..."


cat >> ${NODE_DIRECTORY}/Dockerfile <<-EOF
FROM node:10-alpine

RUN mkdir -p /home/node/${PROJECT_NAME}/node_modules && chown -R node:node /home/node/${PROJECT_NAME}

WORKDIR /home/node/${PROJECT_NAME}

COPY package*.json ./

USER node

RUN npm install

COPY --chown=node:node . .

EXPOSE 8080

CMD [ "node", "src/index.js" ]
EOF


cat >> ${NODE_DIRECTORY}/.dockerignore <<-EOF
node_modules
npm-debug.log
Dockerfile
.dockerignore
**/.git
.git
.gitignore
EOF


cat >> ${NODE_DIRECTORY}/docker-compose.yml <<-EOF
version: "2"
services:
  app:
    container_name: ${PROJECT_NAME}
    restart: always
    build: .
    ports:
      - "${HOST_PORT}:${HOST_PORT}"
    links:
      - mongo
  mongo:
    container_name: mongo
    image: mongo
    volumes:
      - ${DATABASE_DIRECTORY}:/data/db
    ports:
      - "27017:27017"
EOF

echo " "
echo "Building your application..."
# docker build -t ${PROJECT_NAME} ${NODE_DIRECTORY}

cd ${NODE_DIRECTORY} && docker-compose up -d

echo "Done! Your application is up on localhost:${HOST_PORT}"





