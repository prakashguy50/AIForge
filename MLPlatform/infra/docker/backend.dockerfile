FROM openjdk:17-jdk-slim
WORKDIR /app
COPY target/mlapi-1.0.0.jar mlapi.jar
ENTRYPOINT ["java", "-jar", "mlapi.jar"]
