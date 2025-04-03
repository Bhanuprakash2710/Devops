# Use official Maven image to build the application
FROM maven:3.8.5-openjdk-17 AS builder

# Set working directory inside the container
WORKDIR /app

# Copy the project files
COPY . .

# Build the application (this generates the JAR file inside the target/ directory)
RUN mvn clean package -DskipTests

# Use a lightweight JDK image to run the app
FROM openjdk:17-jdk-slim

# Set working directory
WORKDIR /app

# Copy the JAR file from the builder stage
COPY --from=builder /app/target/student-app.jar student-app.jar

COPY k8s-project-452605-866a5037dcbe.json /app/gcp-key.json

ENV GOOGLE_APPLICATION_CREDENTIALS=/app/gcp-key.json

# Expose the application port
EXPOSE 8080

# Run the Spring Boot application
ENTRYPOINT ["java", "-jar", "student-app.jar"]
