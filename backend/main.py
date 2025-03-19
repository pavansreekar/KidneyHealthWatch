from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import os

# Initialize FastAPI app
app = FastAPI()

# Get the absolute path to the model file
model_path = os.path.join(os.path.dirname(__file__), "ckd_model.pkl")

# Load the model
try:
    model = joblib.load(model_path)
except FileNotFoundError:
    raise RuntimeError("ckd_model.pkl file not found. Ensure it's in the backend/ directory.")

# Define input data model
class CKDInput(BaseModel):
    features: list  # Expecting a list of feature values

# Home route
@app.get("/")
def home():
    return {"message": "Welcome to Kidney Health Watch API"}

# Prediction route
@app.post("/predict/")
def predict_ckd(input_data: CKDInput):
    try:
        # Ensure input length matches model expectation
        features = [input_data.features]  # Convert to 2D array
        prediction = model.predict(features)
        result = "Positive" if prediction[0] == 1 else "Negative"
        return {"prediction": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

