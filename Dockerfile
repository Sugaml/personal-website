# Use an official Nginx image
FROM nginx:alpine

# Set the working directory inside the container
WORKDIR /usr/share/nginx/html

# Copy the HTML file to the container
COPY . /usr/share/nginx/html/

# Expose port 80 to allow access to the web server
EXPOSE 80

# Start Nginx server
CMD ["nginx", "-g", "daemon off;"]
