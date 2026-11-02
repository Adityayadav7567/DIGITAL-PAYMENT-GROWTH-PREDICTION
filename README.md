#  UPI Growth Analysis & Prediction in India

A Data Science and Machine Learning project that analyzes the growth of India's Unified Payments Interface (UPI) using monthly NPCI statistics from April 2016 to September 2026. The project explores transaction volume, transaction value, and bank participation, with a focus on changes in digital payment adoption around the COVID-19 period. It also applies Multiple Linear Regression to predict next-month UPI transaction volume.

## 📌 Project Overview

UPI has transformed India's digital payment ecosystem by enabling instant bank-to-bank transactions. This project uses historical monthly data to understand the expansion of UPI and explore whether machine learning can help predict future transaction activity.

The project covers:
- Exploratory Data Analysis (EDA)
- Monthly transaction trend analysis
- Pre-COVID vs Post-COVID trend comparison
- Correlation analysis
- Feature engineering
- Multiple Linear Regression
- Model evaluation and visualization

## 🎯 Objectives

- Analyze the growth of UPI transaction volume and value.
- Study the increase in the number of banks live on UPI.
- Compare UPI adoption trends before and after the COVID-19 reference point.
- Identify relationships between key UPI variables.
- Build a machine learning model to predict next-month transaction volume.
- Evaluate model performance using regression metrics.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming |
| Pandas | Data cleaning and manipulation |
| NumPy | Numerical computations |
| Matplotlib | Data visualization |
| Seaborn | Correlation heatmap |
| Scikit-learn | Machine learning and evaluation |
| Spyder / Jupyter Notebook | Development environment |

## 📂 Dataset Information

**Source:** [NPCI – UPI Product Statistics](https://www.npci.org.in/product/upi/product-statistics)

The dataset contains monthly UPI statistics from April 2016 to September 2026.

**Dataset features:**
- `Month` – Monthly observation date
- `No. of Banks live on UPI` – Number of banks participating in UPI
- `Volume (In Mn.)` – Number of transactions in millions
- `Value (In Cr.)` – Transaction value in crores

**Dataset summary:**
- Original annual Excel files: 11
- Combined monthly records: 126
- Feature-engineered records: 122
- Model input features: 13

## 🔍 Exploratory Data Analysis

The project includes the following visualizations:

### 1. UPI Transaction Volume Trend
Analyzes the monthly increase in UPI transaction volume over the study period.

### 2. UPI Transaction Value Trend
Shows the growth in the total monetary value of UPI transactions.

### 3. Banks Live on UPI
Visualizes the expansion of participating banks over time.

### 4. Pre-COVID vs Post-COVID Analysis
Highlights the difference in observed UPI growth trends around the March 2020 reference point.

### 5. Correlation Heatmap
Examines relationships between transaction volume, transaction value, and participating banks.

## ⚙️ Data Preprocessing & Feature Engineering

The following steps were performed:

1. Loaded multiple annual Excel datasets.
2. Combined them into a single monthly dataset.
3. Converted numerical columns into appropriate data types.
4. Converted the Month column into datetime format.
5. Sorted observations chronologically.
6. Checked missing values and duplicate records.
7. Created lag features for previous 1, 2, and 3 months.
8. Created 3-month rolling averages.
9. Extracted Year and Month features.
10. Created next-month prediction targets.

**Engineered features include:**
- `Volume_Lag_1`, `Volume_Lag_2`, `Volume_Lag_3`
- `Value_Lag_1`, `Value_Lag_2`, `Value_Lag_3`
- `Volume_Rolling_Mean_3`
- `Value_Rolling_Mean_3`
- `Year`
- `Month_Number`

## 🤖 Machine Learning Model

**Algorithm:** Multiple Linear Regression

The model uses 13 input features to predict next-month UPI transaction volume.

**Train-Test Split:**
- Training observations: 97 (80%)
- Testing observations: 25 (20%)
- Split method: Chronological (without random shuffling)

### 📊 Model Performance

| Evaluation Metric | Result |
|---|---:|
| R² Score | 0.9014 |
| MAE | 763.68 |
| MSE | 749,745.60 |
| RMSE | 865.88 |

The model achieved an R² score of approximately 0.90 on the test set, indicating that it explains around 90.14% of the variation in the test observations.

*Note: Error metrics are expressed in the target variable's unit (millions of transactions). These results are based on the current chronological test split and do not guarantee future prediction accuracy.*

## 📈 Actual vs Predicted Visualization

The project compares actual and predicted transaction volume across the 25 test observations to assess how closely the model follows the observed trend.

## 📁 Project Structure

```text
UPI-Growth-Analysis-and-Prediction/
│
├── data/
│   └── processed/
│       ├── UPI_Combined_Data.csv
│       ├── UPI_EDA_Data.csv
│       └── UPI_Feature_Engineered.csv
│
├── graphs/
│   ├── volume_trend.png
│   ├── value_trend.png
│   ├── banks_trend.png
│   ├── correlation_heatmap.png
│   └── actual_vs_predicted.png
│
├── UPI_Growth_Analysis.py
├── README.md
└── requirements.txt
```

*The structure above is a suggested repository layout. Adjust filenames and folders to match the files you actually upload.*

## 🚀 Installation & Usage

**1. Clone the repository**

```bash
git clone https://github.com/your-username/UPI-Growth-Analysis-and-Prediction.git
```

**2. Navigate to the project directory**

```bash
cd UPI-Growth-Analysis-and-Prediction
```

**3. Install dependencies**

```bash
pip install pandas numpy matplotlib seaborn scikit-learn openpyxl
```

**4. Run the Python script**

```bash
python UPI_Growth_Analysis.py
```

Make sure the dataset files are placed in the paths expected by the script.

## 🔮 Future Scope

- Implement and compare Decision Tree Regression.
- Predict next-month transaction value.
- Explore seasonal patterns in UPI transactions.
- Evaluate the model on newer unseen monthly observations.
- Compare regression models using consistent evaluation metrics.
- Explore additional economic and digital adoption indicators.

## ⚠️ Limitations

- The analysis uses a limited historical dataset.
- Only a chronological 80:20 train-test split was used.
- Strong time trends may influence correlations and model performance.
- The COVID comparison is descriptive and does not establish causation.
- Further validation is required before using predictions operationally.

## 👨‍💻 Author

**Aditya Yadav**

B.Tech – Computer Science and Engineering

- GitHub: [Adityayadav7567](https://github.com/Adityayadav7567)
- LinkedIn: [Aditya Yadav](https://www.linkedin.com/in/adityayadav7567/)

---

⭐ If you find this project useful, consider giving the repository a star!

**Built with Python, Data Science & Machine Learning.**
