import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

# Load the log data
data = pd.read_csv('logs.csv')  # Ensure you have your log data in 'logs.csv'

# Select the relevant features for training
features = ['feature1', 'feature2', 'feature3']
X = data[features]

# Initialize the Isolation Forest model
model = IsolationForest(contamination=0.1, random_state=42)

# Train the model
model.fit(X)

# Save the trained model to a file
joblib.dump(model, 'anomaly_detection_model.joblib')

print("Model trained and saved successfully.")
