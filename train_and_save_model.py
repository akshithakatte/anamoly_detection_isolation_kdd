import joblib
import numpy as np
from sklearn.ensemble import IsolationForest

# Example training data: Replace this with your actual training data
training_data = np.array([[100, 300], [120, 350], [140, 400], [160, 450], [180, 500]])

# Train Isolation Forest model
model = IsolationForest(contamination=0.05, random_state=42)
model.fit(training_data)

# Save the trained model using joblib
joblib.dump(model, 'isolation_forest_model.joblib')  # Save the model as a .joblib file
print("Model saved successfully!")
