# Use the official Alpine base image
FROM alpine:latest

#Install the curl package
RUN apk add --no-cache curl

#Add the config file to the container
COPY config.txt /app/config.txt

# Define the command to run when the container starts
CMD ["echo", "Hello, World!"]
