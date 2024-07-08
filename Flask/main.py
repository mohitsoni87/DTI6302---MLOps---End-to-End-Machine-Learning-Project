import tensorflow as tf

from tensorflow.keras.models import load_model
from tensorflow.keras.metrics import Accuracy
import logging
# Function to perform inference and monitor metrics
print(True)
def predict_and_monitor(input_data):
    predictions = model.predict(input_data)
    accuracy_metric.update_state(true_labels, predictions)
    accuracy = accuracy_metric.result().numpy()

    # Log metrics
    logging.info(f'Accuracy: {accuracy}')

    # Example: TensorBoard logging
    with tf.summary.create_file_writer('logs').as_default():
        tf.summary.scalar('accuracy', accuracy, step=global_step)

    return predictions

# Load the TensorFlow model
model = load_model('/Users/mohit/MyFolder/uOttawa/Summer24/DTI6302-MLOps/MLOps-E2E-Machine-Learning-Project/cnn_model')

# Initialize logging
logging.basicConfig(filename='model_monitoring.log', level=logging.INFO)

# Initialize metrics
accuracy_metric = Accuracy()

# Example usage
input_data = ...
predictions = predict_and_monitor(input_data)
