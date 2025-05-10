# 🛡️ Fraud Detection Insurance Dashboard

**Author**: Jorge Octavio Gómez González  
**Email**: warcklian696@gmail.com  
**GitHub**: [warcklian](https://github.com/warcklian)  
**LinkedIn**: [Jorge Octavio Gómez González](https://www.linkedin.com/in/jorge-octavio-gómez-gonzález-8a0510b4)

---

A professional fraud detection and visualization dashboard designed to analyze insurance fraud predictions. This project uses machine learning (scikit-learn) and provides an interactive Streamlit dashboard for real-time data exploration and decision support.

---

## 📁 Project Structure


fraud_detection_insurance/
│
├── data/ # Raw datasets
├── reports/ # CSV reports with fraud predictions
├── models/ # Trained models (Pickle or Joblib)
├── visualizations/ # Exported plots and images
├── notebooks/ # Prototyping and exploratory notebooks
├── dashboard_fraude.py # Main Streamlit dashboard script
├── predict.py # Script to load and generate predictions
├── train_model.py # Model training and export script
├── requirements.txt # Python dependency list
├── init_git_project.bat # Git automation script (optional)
└── README.md # This file


---

## ⚙️ Requirements

Tested with the following Python version and package versions:

```text
Python 3.10

Required libraries:
- streamlit==1.16.0
- pandas==2.2.3
- seaborn==0.13.2
- matplotlib==3.8.4
- scikit-learn==1.3.2
- joblib==1.4.2

Install all dependencies using:

pip install -r requirements.txt


Note: You can create a virtual environment first for better isolation:

python -m venv venv
venv\Scripts\activate   # on Windows
source venv/bin/activate   # on Linux/Mac

🚀 Usage
1. Train the model

python train_model.py

This will generate the model and save it in the models/ directory.

2. Predict fraud probabilities

python predict.py

This will create reports/fraud_predictions_report.csv.

3. Launch the dashboard

streamlit run dashboard_fraude.py

This opens an interactive dashboard at http://localhost:8501, where you can:

Filter by fraud predictions

Adjust threshold sliders

View visual reports with charts

🧠 Core Features
Interactive filters for binary fraud classification

Probability threshold adjustment

Histogram & scatter plots using Seaborn

Real-time data refresh with st.cache

Visual and metric summaries of fraud detection

📝 License
This project is licensed under the MIT License.

🤝 Contributing
Feel free to fork this repo, create issues, or submit pull requests. Feedback and suggestions are always welcome!

📌 Version
Last updated: 2025-05-10

Thank you for using this project. If you found it helpful, feel free to ⭐ star the repo!


¿Deseas que también genere una versión en español del README.md?

