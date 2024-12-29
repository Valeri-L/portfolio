# Dockerfile for the frontend
FROM node:18 as frontend

WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application
COPY . .

# Build the application

RUN npm run build

# # Use a lightweight web server for static files
FROM nginx:stable-alpine

COPY --from=frontend /app/dist /usr/share/nginx/html

COPY /nginx/nginx.conf /etc/nginx/conf.d

# Expose port
EXPOSE 3000


CMD ["nginx", "-g", "daemon off;"]