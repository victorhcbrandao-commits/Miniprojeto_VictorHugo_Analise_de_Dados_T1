# 🛒 Retail Data Analysis

**Python · Pandas · Data Cleaning · Exploratory Data Analysis**

🇺🇸 **English** | [🇧🇷 Português](README.pt-BR.md)

> Transforming a large retail dataset into clean, structured, and analysis-ready data using Python and Pandas.

> This project was originally developed as part of a **Data Analytics with Python program** and was later reorganized for professional portfolio presentation.

---

## 📌 Project Overview

The **Retail Data Analysis** project explores a large retail dataset containing information about customers, purchases, and products.

The original dataset contains approximately **830,000 records** and presents common real-world data quality challenges, including:

- empty columns;
- duplicate records;
- inconsistent data types;
- categorical variables requiring validation;
- date fields requiring conversion.

The project implements a complete data preparation and exploratory analysis workflow using **Python and Pandas**, transforming the raw dataset into a clean and structured dataset ready for further analysis.

The workflow follows the general process:

```text
Raw Retail Dataset
        │
        ▼
Data Inspection
        │
        ▼
Data Quality Assessment
        │
        ▼
Cleaning & Transformation
        │
        ▼
Exploratory Analysis
        │
        ▼
Processed Dataset
        │
        ▼
Business Insights
```

---

## 🗂️ Dataset

The project uses a retail dataset containing customer, purchase, and product information.

The original dataset contains:

```text
830,000 rows
14 columns
```

Main attributes include:

| Column | Description |
|---|---|
| `DATA` | Purchase date |
| `CO_ID` | Purchase identifier |
| `CL_ID` | Customer identifier |
| `CL_GENERO` | Customer gender |
| `CL_EC` | Customer marital status |
| `CL_FHL` | Number of children |
| `CL_SEG` | Customer segment |
| `PR_ID` | Product identifier |
| `PR_CAT` | Product category |
| `PR_NOME` | Product name |

The raw dataset also contained four completely empty columns:

```text
Unnamed: 10
Unnamed: 11
Unnamed: 12
Unnamed: 13
```

These columns were identified during the data quality assessment and removed during processing.

---

## 🔎 Data Quality Assessment

Before performing the analysis, the dataset was inspected for common data quality issues.

The assessment included:

- missing values;
- duplicate records;
- invalid dates;
- empty product categories;
- missing purchase identifiers;
- unnecessary empty columns;
- data type consistency.

The analysis identified **96,553 duplicate records** in the original dataset.

After cleaning and duplicate removal, the final dataset contains:

```text
733,447 records
```

This represents approximately **88% of the original dataset**, preserving the majority of the information while removing duplicated observations.

---

## 🧹 Data Cleaning & Transformation

The processing stage prepares the raw dataset for reliable analysis.

Main transformations include:

```text
Raw data
   │
   ├── Remove empty columns
   │
   ├── Validate purchase identifiers
   │
   ├── Convert dates
   │
   ├── Normalize data types
   │
   ├── Handle missing values
   │
   ├── Validate product categories
   │
   └── Remove duplicate records
   │
   ▼
Clean dataset
```

### Date conversion

The `DATA` column is converted into a proper datetime format, allowing reliable temporal analysis.

### Purchase identifiers

`CO_ID` is treated as an identifier rather than a numerical measure.

### Missing values

The project checks the `CL_FHL` field and applies median imputation when missing values are present.

### Duplicate removal

Duplicate observations are removed before performing the exploratory analysis.

### Empty columns

Columns containing only null values are removed automatically.

---

## 📊 Exploratory Data Analysis

After cleaning the dataset, descriptive statistics and grouped analyses are performed to identify patterns in customer and purchase behavior.

### Number of children

The `CL_FHL` variable presents the following descriptive statistics:

| Metric | Value |
|---|---:|
| Mean | 1.15 |
| Median | 0 |
| Standard deviation | 1.42 |
| Mode | 0 |
| Minimum | 0 |
| Maximum | 4 |

Quartiles:

```text
25% → 0 children
50% → 0 children
75% → 2 children
```

This indicates that a significant portion of customers in the dataset have no children.

---

## 🛍️ Product Category Analysis

The cleaned dataset allows the identification of the categories with the highest purchase volume.

| Product Category | Records |
|---|---:|
| ALIMENTOS | 384,197 |
| HIGIENE | 137,702 |
| LIMPEZA | 128,632 |
| BEBIDAS | 38,264 |
| PET | 28,553 |
| ACESSORIOS | 12,871 |
| N/D | 3,228 |

**ALIMENTOS** represents the largest category in the dataset by a significant margin.

---

## 👥 Customer Analysis

The project also evaluates purchase activity by customer gender.

Unique purchase identifiers by gender:

| Gender | Purchases |
|---|---:|
| Female | 9,615 |
| Male | 8,856 |

Average number of children:

| Gender | Average |
|---|---:|
| Male | 1.21 |
| Female | 1.09 |

These aggregations provide an initial view of customer characteristics and purchasing patterns within the dataset.

---

## 💡 Key Findings

The analysis highlights several characteristics of the retail dataset:

- The original dataset contains **830,000 records**, demonstrating the ability to process a relatively large dataset using Pandas.
- **96,553 duplicate records** were identified and removed.
- The final cleaned dataset contains **733,447 records**.
- `ALIMENTOS` is the dominant product category by transaction records.
- The median number of children per customer is **0**.
- Female customers account for a slightly higher number of unique purchase identifiers than male customers.
- Converting dates and identifiers into appropriate data types improves the reliability of subsequent analysis.

The project demonstrates how systematic data cleaning can transform raw operational data into a reliable dataset for analytical exploration.

---

## 🛠️ Tech Stack

### Data Processing

`Python` · `Pandas`

### Data Handling

`CSV` · `csv.DictReader`

### Analysis

`Descriptive Statistics` · `Data Aggregation` · `Data Cleaning`

### Development

`Git` · `GitHub` · `VS Code`

---

## 📁 Project Structure

```text
retail-data-analysis/
│
├── data/
│   │
│   ├── raw/
│   │   └── Varejo.csv
│   │
│   └── processed/
│       └── df_limpo.csv
│
├── src/
│   └── retail_analysis.py
│
├── .gitignore
├── README.md
├── README.pt-BR.md
└── requirements.txt
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/victorhcbrandao/retail-data-analysis.git
```

### 2. Navigate to the project

```bash
cd retail-data-analysis
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the environment

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Analysis

Make sure the original dataset is available at:

```text
data/raw/Varejo.csv
```

Then run:

```bash
python src/retail_analysis.py
```

The script performs the complete workflow:

```text
Import
   ↓
Data Quality Assessment
   ↓
Cleaning
   ↓
Transformation
   ↓
Descriptive Statistics
   ↓
Grouped Analysis
   ↓
Export
```

---

## 📤 Output Dataset

After processing, the cleaned dataset is exported to:

```text
data/processed/df_limpo.csv
```

The processed dataset contains **733,447 records** after removing duplicated observations and unnecessary columns.

---

## 🔬 Analysis Workflow

The project demonstrates a reproducible data analysis workflow:

```text
                ┌───────────────────┐
                │   Varejo.csv      │
                │   830K records    │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │ Data Inspection   │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │ Quality Checks    │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │ Data Cleaning     │
                │ & Transformation  │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │ 733K Clean Rows   │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │ Exploratory       │
                │ Analysis          │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │ Business Insights │
                └───────────────────┘
```

---

## 📈 Possible Improvements

Potential future improvements include:

- additional exploratory visualizations;
- customer segmentation analysis;
- temporal purchasing analysis;
- product affinity analysis;
- automated data quality tests;
- logging and monitoring;
- modularization of the analysis pipeline;
- interactive dashboard using Streamlit or Power BI.

---

## 🎯 About the Project

This project demonstrates practical experience with **data cleaning, transformation, validation, descriptive statistics, and exploratory data analysis using Python**.

It was originally developed during my **Data Analytics with Python training** and was later reorganized into a portfolio-ready project.

The project complements more advanced analytics projects by demonstrating strong fundamentals in:

**Python · Pandas · Data Cleaning · Data Quality · Exploratory Data Analysis**

---

## 👨‍💻 Author

**Victor Hugo de Castro Brandão**

Finance | Data Analytics | Financial Technology

[GitHub](https://github.com/victorhcbrandao) · [LinkedIn](https://www.linkedin.com/in/victorhugodecastro/)