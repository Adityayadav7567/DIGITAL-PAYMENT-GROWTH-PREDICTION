import pandas as pd
import os
import glob
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

 
# STEP 1: PROJECT FOLDER PATH
 

project_path = "/Users/adityayadav/Downloads/UPI_Growth_Prediction"

# Excel files are directly inside this folder
raw_path = project_path

# Output folder
processed_path = os.path.join(project_path, "data", "processed")

os.makedirs(processed_path, exist_ok=True)


 
# STEP 2: FIND ALL EXCEL FILES
 

excel_files = glob.glob(os.path.join(raw_path, "*.xlsx"))

print("Total Excel files found:", len(excel_files))

if len(excel_files) == 0:
    raise FileNotFoundError("No Excel files found in project folder!")


 
# STEP 3: READ ALL EXCEL FILES
 

dataframes = []

for file in excel_files:

    df = pd.read_excel(file)

    # Remove extra spaces from column names
    df.columns = df.columns.astype(str).str.strip()

    dataframes.append(df)

    print(
        "Loaded:", os.path.basename(file),
        "| Rows:", len(df)
    )


 
# STEP 4: COMBINE ALL DATASETS
 

upi_data = pd.concat(dataframes, ignore_index=True)

print("\nCombined Dataset Shape:", upi_data.shape)

print("\nColumn Names:")
print(upi_data.columns.tolist())


 
# STEP 5: CLEAN COLUMN NAMES


upi_data.columns = upi_data.columns.astype(str).str.strip()


 
# STEP 6: CONVERT NUMERIC COLUMNS


numeric_columns = [
    "No. of Banks live on UPI",
    "Volume (In Mn.)",
    "Value (In Cr.)"
]

for col in numeric_columns:

    if col not in upi_data.columns:
        raise ValueError(f"Column not found: {col}")

    upi_data[col] = (
        upi_data[col]
        .astype(str)
        .str.replace(",", "", regex=False)
        .str.replace("\t", "", regex=False)
        .str.strip()
    )

    upi_data[col] = pd.to_numeric(
        upi_data[col],
        errors="coerce"
    )



# STEP 7: CONVERT MONTH COLUMN



if "Month" not in upi_data.columns:
    raise ValueError("Month column not found!")

upi_data["Month"] = pd.to_datetime(
    upi_data["Month"].astype(str).str.strip(),
    format="%B-%Y",
    errors="coerce"
)



# STEP 8: SORT DATA CHRONOLOGICALLY


upi_data = upi_data.sort_values(
    by="Month"
).reset_index(drop=True)



# STEP 9: CHECK MISSING VALUES


print("\nMissing Values:")
print(upi_data.isnull().sum())

print("\nDuplicate Months:")
print(upi_data["Month"].duplicated().sum())



# STEP 10: DISPLAY FINAL DATASET


print("\nFirst 5 Records:")
print(upi_data.head())

print("\nLast 5 Records:")
print(upi_data.tail())

print("\nFinal Dataset Shape:")
print(upi_data.shape)



# STEP 11: SAVE CLEANED DATASET


output_file = os.path.join(
    processed_path,
    "UPI_Combined_Data.csv"
)

upi_data.to_csv(output_file, index=False)

print("\n==========================================")
print("DATA COMBINED SUCCESSFULLY!")
print("==========================================")

print("Saved File:", output_file)
 


file_path = "/Users/adityayadav/Downloads/UPI_Growth_Prediction/data/processed/UPI_Combined_Data.csv"

upi_data = pd.read_csv(file_path)

print("Dataset Shape:", upi_data.shape)

print("\nFirst 5 Rows:")
print(upi_data.head())

print("\nLast 5 Rows:")
print(upi_data.tail())

print("\nMissing Values:")
print(upi_data.isnull().sum())

print("\nDuplicate Months:")
print(upi_data["Month"].duplicated().sum())

print("\nData Types:")
print(upi_data.dtypes)




# =====================================
# STEP 1: LOAD DATASET
# =====================================

file_path = "/Users/adityayadav/Downloads/UPI_Growth_Prediction/data/processed/UPI_Combined_Data.csv"

upi_data = pd.read_csv(file_path)

# Convert Month to datetime
upi_data["Month"] = pd.to_datetime(upi_data["Month"])

# Sort by month
upi_data = upi_data.sort_values("Month").reset_index(drop=True)

print("Dataset loaded successfully!")
print(upi_data.head())


# =====================================
# STEP 2: DESCRIPTIVE STATISTICS
# =====================================

print("\nStatistical Summary:")
print(upi_data.describe())




plt.style.use("dark_background")

# COVID PERIOD MARKER
covid_date = pd.Timestamp("2020-03-01")


# STEP 3: UPI TRANSACTION VOLUME

plt.figure(figsize=(13, 5))
plt.gca().set_facecolor("#171B29")

plt.plot(upi_data["Month"], upi_data["Volume (In Mn.)"],
         color="#00E5FF", linewidth=2.5, marker="o", markersize=3)

plt.fill_between(upi_data["Month"], upi_data["Volume (In Mn.)"],
                 color="#00E5FF", alpha=0.12)

plt.axvline(covid_date, color="#FF4D8D", linestyle="--",
            linewidth=2, label="COVID-19 (2020)")

plt.text(pd.Timestamp("2017-06-01"), upi_data["Volume (In Mn.)"].max()*0.85,
         "PRE-COVID", color="#00E5FF", fontsize=11, fontweight="bold")

plt.text(pd.Timestamp("2021-01-01"), upi_data["Volume (In Mn.)"].max()*0.85,
         "POST-COVID", color="#FF4D8D", fontsize=11, fontweight="bold")

plt.title("UPI Transaction Volume: Pre vs Post COVID",
          fontsize=15, fontweight="bold")
plt.xlabel("Year")
plt.ylabel("Volume (In Millions)")
plt.legend()
plt.grid(alpha=0.2, linestyle="--")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("UPI_Volume_COVID_Impact.png", dpi=300)
plt.show()


# STEP 4: UPI TRANSACTION VALUE

plt.figure(figsize=(13, 5))
plt.gca().set_facecolor("#171B29")

plt.plot(upi_data["Month"], upi_data["Value (In Cr.)"],
         color="#FF4D8D", linewidth=2.5, marker="o", markersize=3)

plt.fill_between(upi_data["Month"], upi_data["Value (In Cr.)"],
                 color="#FF4D8D", alpha=0.12)

plt.axvline(covid_date, color="#00E5FF", linestyle="--",
            linewidth=2, label="COVID-19 (2020)")

plt.title("UPI Transaction Value: Pre vs Post COVID",
          fontsize=15, fontweight="bold")
plt.xlabel("Year")
plt.ylabel("Value (In Crores)")
plt.legend()
plt.grid(alpha=0.2, linestyle="--")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("UPI_Value_COVID_Impact.png", dpi=300)
plt.show()


# STEP 5: BANKS LIVE ON UPI

plt.figure(figsize=(13, 5))
plt.gca().set_facecolor("#171B29")

plt.plot(upi_data["Month"], upi_data["No. of Banks live on UPI"],
         color="#A78BFA", linewidth=2.5, marker="o", markersize=3)

plt.fill_between(upi_data["Month"], upi_data["No. of Banks live on UPI"],
                 color="#A78BFA", alpha=0.12)

plt.axvline(covid_date, color="#FF4D8D", linestyle="--",
            linewidth=2, label="COVID-19 (2020)")

plt.title("Banks Live on UPI: Pre vs Post COVID",
          fontsize=15, fontweight="bold")
plt.xlabel("Year")
plt.ylabel("Number of Banks")
plt.legend()
plt.grid(alpha=0.2, linestyle="--")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("UPI_Banks_COVID_Impact.png", dpi=300)
plt.show()



# =====================================
# STEP 6: MONTHLY GROWTH CALCULATION
# =====================================

upi_data["Volume Growth (%)"] = (
    upi_data["Volume (In Mn.)"].pct_change() * 100
)

upi_data["Value Growth (%)"] = (
    upi_data["Value (In Cr.)"].pct_change() * 100
)

upi_data["Bank Growth (%)"] = (
    upi_data["No. of Banks live on UPI"].pct_change() * 100
)

print("\nMonthly Growth Data:")
print(
    upi_data[
        ["Month", "Volume Growth (%)",
         "Value Growth (%)", "Bank Growth (%)"]
    ].tail(10)
)


# =====================================
# STEP 7: CORRELATION ANALYSIS
# =====================================

correlation_data = upi_data[
    [
        "No. of Banks live on UPI",
        "Volume (In Mn.)",
        "Value (In Cr.)"
    ]
]

correlation_matrix = correlation_data.corr()

print("\nCorrelation Matrix:")
print(correlation_matrix)

plt.figure(figsize=(8, 6))

sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Between UPI Variables")
plt.tight_layout()
plt.show()


# =====================================
# STEP 8: SAVE EDA DATASET
# =====================================

output_path = "/Users/adityayadav/Downloads/UPI_Growth_Prediction/data/processed/UPI_EDA_Data.csv"

upi_data.to_csv(output_path, index=False)

print("\nEDA completed successfully!")
print("EDA dataset saved at:", output_path)



# =====================================
# STEP 9: FEATURE ENGINEERING
# =====================================

# Previous month data
upi_data["Volume_Lag_1"] = upi_data["Volume (In Mn.)"].shift(1)
upi_data["Value_Lag_1"] = upi_data["Value (In Cr.)"].shift(1)

# Two months previous data
upi_data["Volume_Lag_2"] = upi_data["Volume (In Mn.)"].shift(2)
upi_data["Value_Lag_2"] = upi_data["Value (In Cr.)"].shift(2)

# Three months previous data
upi_data["Volume_Lag_3"] = upi_data["Volume (In Mn.)"].shift(3)
upi_data["Value_Lag_3"] = upi_data["Value (In Cr.)"].shift(3)

# Three-month rolling average
upi_data["Volume_Rolling_Mean_3"] = (
    upi_data["Volume (In Mn.)"].rolling(window=3).mean()
)

upi_data["Value_Rolling_Mean_3"] = (
    upi_data["Value (In Cr.)"].rolling(window=3).mean()
)

# Date features
upi_data["Year"] = upi_data["Month"].dt.year
upi_data["Month_Number"] = upi_data["Month"].dt.month


# =====================================
# STEP 10: CREATE TARGET VARIABLES
# =====================================

# Next month's volume and value
upi_data["Target_Volume"] = (
    upi_data["Volume (In Mn.)"].shift(-1)
)

upi_data["Target_Value"] = (
    upi_data["Value (In Cr.)"].shift(-1)
)

# Classification target:
# 1 = Next month's volume increases
# 0 = Next month's volume does not increase

upi_data["Target_Growth"] = (
    upi_data["Target_Volume"] >
    upi_data["Volume (In Mn.)"]
).astype(int)


# =====================================
# STEP 11: REMOVE MISSING ROWS
# =====================================

upi_data = upi_data.dropna().reset_index(drop=True)


# =====================================
# STEP 12: CHECK FINAL DATASET
# =====================================

print("\nFeature Engineering Completed!")

print("\nFinal Dataset Shape:")
print(upi_data.shape)

print("\nFeature Columns:")
print(upi_data.columns.tolist())

print("\nTarget Distribution:")
print(upi_data["Target_Growth"].value_counts())

print("\nFirst 5 Records:")
print(upi_data.head())


# =====================================
# STEP 13: SAVE FEATURE DATASET
# =====================================

feature_output_path = os.path.join(
    processed_path,
    "UPI_Feature_Engineered.csv"
)

upi_data.to_csv(feature_output_path, index=False)

print("\nFeature Engineered Dataset Saved:")
print(feature_output_path)


# =====================================
# STEP 14: TRAIN-TEST SPLIT
# =====================================

# Input features
feature_columns = [
    "No. of Banks live on UPI",
    "Volume (In Mn.)",
    "Value (In Cr.)",
    "Volume_Lag_1",
    "Value_Lag_1",
    "Volume_Lag_2",
    "Value_Lag_2",
    "Volume_Lag_3",
    "Value_Lag_3",
    "Volume_Rolling_Mean_3",
    "Value_Rolling_Mean_3",
    "Year",
    "Month_Number"
]

# Input data
X = upi_data[feature_columns]

# Target variables
y_volume = upi_data["Target_Volume"]
y_value = upi_data["Target_Value"]
y_growth = upi_data["Target_Growth"]


# =====================================
# STEP 15: CHRONOLOGICAL SPLITTING
# =====================================

split_index = int(len(upi_data) * 0.80)

# Training data: First 80%
X_train = X.iloc[:split_index]
X_test = X.iloc[split_index:]

y_volume_train = y_volume.iloc[:split_index]
y_volume_test = y_volume.iloc[split_index:]

y_value_train = y_value.iloc[:split_index]
y_value_test = y_value.iloc[split_index:]

y_growth_train = y_growth.iloc[:split_index]
y_growth_test = y_growth.iloc[split_index:]


# =====================================
# STEP 16: CHECK SPLIT
# =====================================

print("\nTraining Data Shape:", X_train.shape)
print("Testing Data Shape:", X_test.shape)

print("\nVolume Training Shape:", y_volume_train.shape)
print("Volume Testing Shape:", y_volume_test.shape)

print("\nValue Training Shape:", y_value_train.shape)
print("Value Testing Shape:", y_value_test.shape)

print("\nGrowth Training Shape:", y_growth_train.shape)
print("Growth Testing Shape:", y_growth_test.shape)

print("\nTraining Period:")
print(upi_data["Month"].iloc[0],
      "to",
      upi_data["Month"].iloc[split_index - 1])

print("\nTesting Period:")
print(upi_data["Month"].iloc[split_index],
      "to",
      upi_data["Month"].iloc[-1])

print("\nTraining Target Distribution:")
print(y_growth_train.value_counts())

print("\nTesting Target Distribution:")
print(y_growth_test.value_counts())



# =====================================
# STEP 17: MULTIPLE LINEAR REGRESSION
# VOLUME PREDICTION
# =====================================

# Create Linear Regression model
volume_model = LinearRegression()

# Train the model
volume_model.fit(X_train, y_volume_train)

# Predict testing data
volume_predictions = volume_model.predict(X_test)


# =====================================
# STEP 18: MODEL EVALUATION
# =====================================

mae = mean_absolute_error(
    y_volume_test,
    volume_predictions
)

mse = mean_squared_error(
    y_volume_test,
    volume_predictions
)

rmse = np.sqrt(mse)

r2 = r2_score(
    y_volume_test,
    volume_predictions
)


# =====================================
# STEP 19: DISPLAY RESULTS
# =====================================

print("\nMULTIPLE LINEAR REGRESSION - VOLUME")

print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R2 Score:", r2)


# =====================================
# STEP 20: ACTUAL VS PREDICTED
# =====================================

volume_results = pd.DataFrame({
    "Actual Volume": y_volume_test.values,
    "Predicted Volume": volume_predictions
})

print("\nActual vs Predicted Volume:")
print(volume_results.to_string(index=False))





# PREMIUM ACTUAL VS PREDICTED GRAPH

plt.style.use("dark_background")
plt.figure(figsize=(12, 6))

plt.plot(y_volume_test.values, "o-", color="#00E5FF",
         linewidth=2.5, label="Actual Volume")

plt.plot(volume_predictions, "s--", color="#FF4D8D",
         linewidth=2.5, label="Predicted Volume")

plt.fill_between(
    range(len(y_volume_test)),
    y_volume_test.values,
    volume_predictions,
    color="#A855F7", alpha=0.15
)

plt.title("UPI TRANSACTION VOLUME: ACTUAL vs PREDICTED",
          fontsize=15, fontweight="bold", pad=18)

plt.xlabel("Test Observations")
plt.ylabel("Volume (In Mn.)")

plt.text(0.02, 0.95,
         f"R² = {r2:.3f}  |  MAE = {mae:.2f}  |  RMSE = {rmse:.2f}",
         transform=plt.gca().transAxes,
         fontsize=10, color="white",
         verticalalignment="top")

plt.legend(frameon=False)
plt.grid(alpha=0.2, linestyle="--")
plt.tight_layout()

plt.savefig("UPI_Prediction_Graph.png", dpi=300)
plt.show()


