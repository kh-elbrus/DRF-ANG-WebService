FROM node:14.15.0-alpine as builder

LABEL MAINTAINER khalmukhamedov.e@gmail.com

RUN mkdir /app
WORKDIR /app
RUN adduser -D ang-user
RUN chown -R ang-user:ang-user /app/
RUN chmod -R 777 /app/
COPY ./frontend-app/package.json ./frontend-app/package-lock.json /app/frontend-app/
RUN npm install
COPY ./frontend-app /app
RUN npm run build

FROM nginx:1.19.10-alpine
RUN rm -rf /usr/share/nginx/html/*
COPY --from=builder /app/dist/frontend-app /usr/share/nginx/html
COPY ./nginx/nginx.conf /etc/nginx/conf.d/default.conf
