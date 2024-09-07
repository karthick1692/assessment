# Use the official Golang image as the base image
FROM golang:1.20-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the Go module files and source code to the container
COPY ./golang/server.go .

# Copy the environment-specific files into the container
COPY ./golang/file-dev.txt ./file-dev.txt
COPY ./golang/file-prod.txt ./file-prod.txt

# Build the Go web server
RUN go build -o server server.go

# Expose port 8080
EXPOSE 8080

# Set an environment variable for the deployment environment (default to DEV)
ENV ENVIRONMENT=DEV

# Command to run the server based on the environment
CMD sh -c "if [ \"$ENVIRONMENT\" = \"PROD\" ]; then cp /app/file-prod.txt /app/file.txt; else cp /app/file-dev.txt /app/file.txt; fi && ./server"
