import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

# File paths
train_file = "KDDTrain+.csv"
test_file = "KDDTest+.csv"

# Column names for NSL-KDD dataset
columns = [
    "duration", "protocol_type", "service", "flag", "src_bytes", "dst_bytes",
    "land", "wrong_fragment", "urgent", "hot", "num_failed_logins", "logged_in",
    "num_compromised", "root_shell", "su_attempted", "num_root",
    "num_file_creations", "num_shells", "num_access_files", "num_outbound_cmds",
    "is_host_login", "is_guest_login", "count", "srv_count", "serror_rate",
    "srv_serror_rate", "rerror_rate", "srv_rerror_rate", "same_srv_rate",
    "diff_srv_rate", "srv_diff_host_rate", "dst_host_count",
    "dst_host_srv_count", "dst_host_same_srv_rate",
    "dst_host_diff_srv_rate", "dst_host_same_src_port_rate",
    "dst_host_srv_diff_host_rate", "dst_host_serror_rate",
    "dst_host_srv_serror_rate", "dst_host_rerror_rate",
    "dst_host_srv_rerror_rate", "label"
]

# Load data
train_data = pd.read_csv(train_file, header=None, names=columns)
test_data = pd.read_csv(test_file, header=None, names=columns)

# Drop irrelevant columns
irrelevant_cols = ["num_outbound_cmds", "is_host_login"]
train_data.drop(columns=irrelevant_cols, inplace=True)
test_data.drop(columns=irrelevant_cols, inplace=True)

# Identify categorical and numerical columns
categorical_cols = ["protocol_type", "service", "flag"]

# Select only numerical columns (ensure no categorical ones are included)
numerical_cols = train_data.select_dtypes(include=['float64', 'int64']).columns.tolist()
numerical_cols = [col for col in numerical_cols if col != 'label']  # Exclude label column

print("Numerical columns:", numerical_cols)

# Initialize LabelEncoders for categorical columns
label_encoders = {}

for col in categorical_cols:
    le = LabelEncoder()
    combined_data = pd.concat([train_data[col], test_data[col]], axis=0)
    le.fit(combined_data)
    train_data[col] = le.transform(train_data[col])
    test_data[col] = le.transform(test_data[col])
    label_encoders[col] = le

# Convert numerical columns to float and scale
scaler = MinMaxScaler()

# Convert numerical columns to float
train_data[numerical_cols] = train_data[numerical_cols].astype(float)
test_data[numerical_cols] = test_data[numerical_cols].astype(float)

# Apply MinMax scaling
train_data[numerical_cols] = scaler.fit_transform(train_data[numerical_cols])
test_data[numerical_cols] = scaler.transform(test_data[numerical_cols])

# Save preprocessed datasets
train_data.to_csv("preprocessed_train.csv", index=False)
test_data.to_csv("preprocessed_test.csv", index=False)

print("Preprocessing complete. Preprocessed data saved.")
