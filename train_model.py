import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("ckd_data_cleaned.csv")

# Display dataset columns
print("Dataset Columns:", df.columns)

# Print unique values in classification
print("Unique values in 'classification':", df['classification'].unique())

# Ensure classification is numeric (convert if needed)
df['classification'] = pd.to_numeric(df['classification'], errors='coerce')

# Drop NaN values in classification
df = df.dropna(subset=['classification'])

# Convert classification to integer type
df['classification'] = df['classification'].astype(int)

# Print dataset size after cleaning
print(f"Dataset size after cleaning: {df.shape}")

# If dataset is empty, exit
if df.empty:
    print("Error: No valid data after cleaning. Please check 'classification' column.")
    exit()

# Define feature columns
selected_features = [
    'age', 'bp', 'sg', 'al', 'su', 'bgr', 'bu', 'sc', 'sod', 'pot',
    'hemo', 'pcv', 'wc', 'rc', 'htn', 'dm', 'cad', 'appet', 'pe', 'ane'
]

# Ensure selected features exist
df = df[selected_features + ['classification']]

# Encode categorical features
categorical_cols = ['htn', 'dm', 'cad', 'appet', 'pe', 'ane']
for col in categorical_cols:
    df[col] = LabelEncoder().fit_transform(df[col].astype(str))

# Drop any remaining NaN values
df = df.dropna()

# Extract features and target
X = df[selected_features]
y = df['classification']

# Check if dataset is still empty
if X.empty or y.empty:
    print("Error: Features or labels are empty after processing.")
    exit()

# Split into train & test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Model evaluation
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}\n")

print("Classification Report:\n", classification_report(y_test, y_pred))

# Save model
with open("ckd_model.pkl", "wb") as model_file:
    pickle.dump(model, model_file)

print("Model saved as 'ckd_model.pkl'")
