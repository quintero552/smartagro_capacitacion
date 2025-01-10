# Description: Dockerfile for the backend service
# Author: Ovidiu Mura
# *** Multi-stage build ***

FROM node:22

WORKDIR /app

COPY package.json package.json

RUN npm install

COPY . .

CMD ["npm", "start"]