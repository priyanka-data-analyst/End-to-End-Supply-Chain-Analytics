import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder

# 1. LOAD DATA
try:
    df = pd.read_csv('DataCoSupplyChainDataset.csv', encoding='latin-1')
    print("✅ Data Loaded Successfully!")
except FileNotFoundError:
    print("❌ Error: 'DataCoSupplyChainDataset.csv' not found.")
    exit()

# 2. DATA CLEANING & SELECTION
# Select relevant columns
features = ['Type', 'Shipping Mode', 'Customer Segment', 'Order Region',
            'Order Country', 'Days for shipment (scheduled)']
target = 'Late_delivery_risk'

# Create a clean copy
data = df[features + [target]].copy()

# Fill any missing values (just in case)
data = data.dropna()

# ---------------------------------------------------------
# 2.5 SAVE THE CLEANED FILE (New Step)
# ---------------------------------------------------------
data.to_csv('cleaned_supply_chain_data.csv', index=False)
print("💾 SUCCESS: 'cleaned_supply_chain_data.csv' has been saved to your folder!")

# 3. PREPROCESSING
le = LabelEncoder()
# Convert text to numbers so the CSV is ready for ML
for col in ['Type', 'Shipping Mode', 'Customer Segment', 'Order Region', 'Order Country']:
    data[col] = le.fit_transform(data[col])

# 4. VISUALIZATION
print("📊 Generating Graph... Check your taskbar.")
plt.figure(figsize=(10, 6))
sns.countplot(x='Shipping Mode', hue='Late_delivery_risk', data=df)
plt.title('Late Deliveries by Shipping Mode (0=On Time, 1=Late)')
plt.show()

# 5. TRAIN MODEL
X = data.drop(target, axis=1)
y = data[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 6. RESULTS
predictions = model.predict(X_test)
print("\n" + "="*30)
print("🎯 SUPPLY CHAIN RISK MODEL RESULTS")
print("="*30)
print(classification_report(y_test, predictions))