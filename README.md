![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
# 🎓 Project Title - Automated Data Cleaning & Intelligent Imputation Pipeline for Student Performance Analysis


- Built an end-to-end automated data preprocessing pipeline
- Handled missing data using KNN Imputation
- Detected anomalies using Isolation Forest
- Scaled features for machine learning readiness
- Generated insights through data visualization
---

## 👥 Team

| Name | Role |
|------|------|
| Kavana 1| Team Lead & Pipeline Developer |
| Yuktha M | Data Preprocessing & Analysis |
| Shanu shilpi | Machine Learning & Outlier Detection |
| Sneha Bannatti |  Testing & Validation |

---

## 📌 What This Project Does

Real-world data is messy — it has missing values, outliers, and inconsistent scaling.
This pipeline automates the entire data cleaning process in 4 steps:

1. **Load** raw student data (`student_data.csv`)
2. **Impute** missing values using KNN Imputation (fills gaps using nearest similar students)
3. **Remove Outliers** using Isolation Forest (detects and removes anomalous records)
4. **Scale Features** using StandardScaler (normalizes all numeric columns)
5. **Save** the cleaned dataset as `clean_data.csv`
6. **Visualize** how study time and absences affect final grades

---

## 📊 Output Visualizations

### Study Time vs Final Grade
![Study Time vs Final Grade](outputs/output01.jpeg)

### Absences vs Final Grade
![Absences vs Final Grade](outputs/output02.jpeg)

---

## 🗂️ Project Structure

```
vision-astra-project/
│
├── README.md                  ← You are here
├── LICENSE                    ← MIT License
├── .gitignore                 ← Files excluded from GitHub
│
├── data/
│   ├── student_data.csv       ← Raw input dataset
│   └── clean_data.csv         ← Cleaned output dataset
│
├── src/
│   ├── main.py                ← Data cleaning pipeline
│   └── visualization.py       ← Chart generation
│
└── outputs/
    ├── output01.jpeg          ← Study Time vs Grade chart
    └── output02.jpeg          ← Absences vs Grade chart
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3 | Core language |
| pandas | Data loading and manipulation |
| scikit-learn | KNN Imputer, Isolation Forest, StandardScaler |
| matplotlib | Data visualization |

---

## ▶️ How to Run

**Step 1 — Install dependencies**
```bash
pip install pandas scikit-learn matplotlib
```

**Step 2 — Run the data cleaning pipeline**
```bash
python src/main.py
```

**Step 3 — Generate visualizations**
```bash
python src/visualization.py
```

The cleaned data will be saved as `data/clean_data.csv` and charts saved in `outputs/`.

---

## 🧠 How the Pipeline Works

```
Raw Data (student_data.csv)
        ↓
[1] Check for missing values
        ↓
[2] KNN Imputation → fills missing values using 3 nearest neighbors
        ↓
[3] Isolation Forest → removes outliers (5% contamination threshold)
        ↓
[4] StandardScaler → scales all numeric features to mean=0, std=1
        ↓
Clean Data (clean_data.csv)
        ↓
[5] Visualizations → scatter plots saved as .jpeg
```

---

## 📁 Dataset Info

- **Source:** Student Performance Dataset
- **Records:** ~395 students
- **Key columns:** `studytime`, `absences`, `G1`, `G2`, `G3` (grades), `age`, `failures`, etc.

---

## 🔮 Future Improvements

- Add real-time data processing
- Integrate machine learning prediction models
- Deploy as a web application
- Add interactive dashboards (e.g., Streamlit)

---

## 🎥 Demo Video

> 📹 [https://drive.google.com/file/d/1XpKE8DDv2owY1fh8F5sjB0dGsS2JSAes/view?usp=sharing](#) ← video link

---

