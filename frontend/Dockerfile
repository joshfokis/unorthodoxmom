FROM node

WORKDIR /app/frontend
COPY package.json /app/frontend

RUN npm install
RUN npm install bulma
RUN npm install --save-dev @fortawesome/fontawesome-free

EXPOSE 3000
CMD ["npm", "start"]