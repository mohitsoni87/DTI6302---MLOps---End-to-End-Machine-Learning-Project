# Use an official TensorFlow Serving runtime as a parent image
FROM emacski/tensorflow-serving:latest-linux_arm64

# Copy your SavedModel to the container's model directory
COPY /Users/mohit/MyFolder/uOttawa/Summer24/DTI6302-MLOps/MLOps-E2E-Machine-Learning-Project/cnn_model /models/cnn_model/1

# Specify the model name environment variable
ENV MODEL_NAME=cnn_model

# Expose the model serving port (default for TensorFlow Serving)
EXPOSE 8501

# Set the working directory
WORKDIR /Users/mohit/MyFolder/uOttawa/Summer24/DTI6302-MLOps/MLOps-E2E-Machine-Learning-Project/target-models/cnn_model/1

# Define the command to run TensorFlow Serving with logging
CMD ["tensorflow_model_server", "--port=8501", "--rest_api_port=8502", "--model_name=cnn_model", "--model_base_path=/models/cnn_model/1", "--monitoring_config_file=/logs/config.yaml"]
