FROM node:12.7-alpine

WORKDIR /usr/src/app

ENV PATH /usr/src/app/node_modules/.bin:$PATH


COPY . .
RUN npm ci

CMD ["npm", "run", "start:prod"]