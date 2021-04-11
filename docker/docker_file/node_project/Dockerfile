FROM node:alpine

WORKDIR /mydata

COPY ./package.json ./package.json
COPY ./index.js ./index.js


EXPOSE 8080
EXPOSE 8000

RUN npm install

ENTRYPOINT [ "npm", "start" ]