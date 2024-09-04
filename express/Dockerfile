FROM --platform=linux/amd64 node:14-slim

WORKDIR /express

COPY package.json package.json
COPY package-lock.json package-lock.json

COPY . .

RUN npm install

CMD [ "node", "server.js" ]