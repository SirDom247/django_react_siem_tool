import joblib
import pandas as pd

# Load the trained model
model = joblib.load('anomaly_detection_model.joblib')

def detect_anomalies(data):
    # Extract features from the data
    features = ['feature1', 'feature2', 'feature3']
    df = pd.DataFrame([data], columns=features)
    
    # Predict anomalies
    anomaly_score = model.decision_function(df)
    is_anomaly = model.predict(df)
    
    result = {
        'anomaly_score': anomaly_score[0],
        'is_anomaly': bool(is_anomaly[0] == -1)  # -1 indicates anomaly in Isolation Forest
    }
    
    return result
