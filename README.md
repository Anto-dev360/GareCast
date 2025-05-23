# 🚆 GareCast – Weekly prediction of traffic at SNCF stations

> A deep learning project to estimate weekly train station traffic in France, based on open data from SNCF.

---

## 🎯 Goal

**GareCast** aims to predict the estimated number of passengers per week and per SNCF station, based on annual passenger data made public by SNCF.
The educational objective is to leverage skills in deep learning (regression), temporal data processing, visualization, and application deployment.

---

## 📊 Datasets Used

- **Annual Station Attendance (SNCF)**
[→ Link to the dataset](https://ressources.data.sncf.com/explore/dataset/frequentation-gares/)
(Data from 2015 to 2022, all stations combined)

- **Planned Enhancements**:
- Calendar (school vacations, public holidays, seasonality)
- (Optional) Weather by region
- (Optional) Cultural/tourist events (upcoming)

---

## 🧠 Technical Approach

1. Data Preprocessing: Cleaning, selecting relevant variables, and redistributing them from year to week.
2. Temporal Enrichment: Adding features such as month, season, or week.
3. Deep Learning Modeling: Dense network trained with Keras/TensorFlow, evaluated using RMSE, MAE, and R².
4. Results Visualization: Interactive Streamlit application to visualize predictions by station.
5. Optimization & Validation: GridSearch or single cross-validation on hyperparameters.

---

## 🔮 Development Outlook

- Transition to daily granularity (if data is available).
- Integration of real-time data (weather, SNCF disruptions).
- Cross-referencing with local cultural/tourist events to explain certain peaks.
- Classification of weeks into traffic zones (normal, heavy, critical).
- Possible deployment via Docker container.

---

## 📦 Libraries

- [`pandas`](https://pandas.pydata.org/) – tabular data manipulation
- [`numpy`](https://numpy.org/) – efficient numerical computation
- [`matplotlib`](https://matplotlib.org/) – static visualization
- [`seaborn`](https://seaborn.pydata.org/) – statistical visualization based on matplotlib
- [`plotly`](https://plotly.com/python/) – interactive visualization
- [`tensorflow`](https://www.tensorflow.org/) / [`keras`](https://keras.io/) – building and training neural networks
- [`scikit-learn`](https://scikit-learn.org/stable/) – machine learning tools and evaluation metrics
- [`streamlit`](https://streamlit.io/) – creating web interfaces for Data projects
- [`holidays`](https://pypi.org/project/holidays/) – Manage public holidays by country
- [`datetime`](https://docs.python.org/3/library/datetime.html) – Manipulate dates
- [`requests`](https://docs.python-requests.org/en/latest/) – Access REST APIs (weather, events, etc.)

---

## 📁 Project Structure

GareCast/
│
├── .github/                  # GitHub workflows (CI/CD pipelines)
├── config/
│   └── settings.py           # Configuration constants (dataset URLs, parameters, etc.)
├── data/                     # Data directory
│   ├── raw/                  # Raw input data (kept empty with .gitkeep)
│   └── processed/            # Processed datasets (kept empty with .gitkeep)
├── src/
│   ├── app.py                # Main application entry point (Streamlit app)
│   ├── config/
│   │   └── settings.py       # Local config for src if any
│   └── core/                 # Core functional modules
│       ├── data_loading.py   # Data loading and ingestion functions
│       ├── evaluation.py     # Model evaluation utilities and metrics
│       ├── model.py          # Model architecture and training logic
│       ├── preprocessing.py  # Data preprocessing and feature engineering
│       └── visualization.py  # Visualization helpers for plots and charts
├── tests/                    # Unit and integration tests
├── Dockerfile                # Production Docker image definition
├── Dockerfile.dev            # Development Docker image definition
├── pyproject.toml            # Project metadata and tooling config (ruff, isort)
├── requirements.txt          # Python dependencies
├── README.md                 # Project overview and documentation
├── roadmap.md                # Development roadmap and future plans
└── run_test.ps1              # PowerShell script to run tests locally

---

## 🚀 Launch Instructions

To run the GareCast application locally using Docker, follow these steps:

1. Open a terminal and build the Docker image:

   ```bash
   docker build -t garecast-app .

2. Run the Docker container, exposing port 8501:

   ```bash
   docker run -p 8501:8501 garecast-app

3. Open your web browser and access the app at http://localhost:8501.

---

## 📌 Author

This project is part of the **AI Developer – RNCP38616** program, blocks 3 and 5.
It is intended for educational purposes but can be extended to real-world use cases in railway planning or optimization.
Application deployed under the MIT license

---

