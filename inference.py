import os
import joblib
import numpy as np

# 1. Load the model from the saved path inside the container
def model_fn(model_dir):
    model_path = os.path.join(model_dir, "model", "churn_model.pkl")
    model = joblib.load(model_path)
    return model

# 2. Parse the incoming prediction request (expects JSON with key "inputs")
def input_fn(request_body, request_content_type):
    if request_content_type == "application/json":
        input_data = request_body.get("inputs")  # get input array from JSON
        return np.array(input_data)               # convert to numpy array
    raise Exception(f"Unsupported content type: {request_content_type}")

# 3. Run your model on the input to get predictions
def predict_fn(input_data, model):
    predicted_labels = model.predict(input_data)
    predicted_probabilities = model.predict_proba(input_data)
    return {
        "prediction": predicted_labels.tolist(),       # convert to list for JSON
        "probability": predicted_probabilities[:, 1].tolist()  # probability of positive class
    }

# 4. Format output (SageMaker will convert this dictionary to JSON automatically)
def output_fn(prediction, content_type):
    return prediction
