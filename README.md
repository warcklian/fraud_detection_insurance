
markdown
Copiar
Editar
# 🛡️ Fraud Detection Insurance Dashboard

**Author**: Jorge Octavio Gómez González  
**Email**: [warcklian696@gmail.com](mailto:warcklian696@gmail.com)  
**GitHub**: [warcklian](https://github.com/warcklian)  
**LinkedIn**: [Jorge Octavio Gómez González](https://www.linkedin.com/in/jorge-octavio-gómez-gonzález-8a0510b4)

---

A professional fraud detection and visualization dashboard designed to analyze insurance fraud predictions. This project uses machine learning (scikit-learn) and provides an interactive Streamlit dashboard for real-time data exploration and decision support.

---

## 📁 Project Structure

```text
fraud_detection_insurance/
│
├── data/                  # Raw datasets
├── reports/               # CSV reports with fraud predictions
├── models/                # Trained models (Pickle or Joblib)
├── visualizations/        # Exported plots and images
├── notebooks/             # Prototyping and exploratory notebooks
├── dashboard_fraude.py    # Main Streamlit dashboard script
├── predict.py             # Script to load and generate predictions
├── train_model.py         # Model training and export script
├── requirements.txt       # Python dependency list
├── init_git_project.bat   # Git automation script (optional)
└── README.md              # This file
⚙️ Requirements
Tested environment:


Python 3.10
Required libraries:


streamlit==1.16.0
pandas==2.2.3
seaborn==0.13.2
matplotlib==3.8.4
scikit-learn==1.3.2
joblib==1.4.2
💾 Install Dependencies

pip install -r requirements.txt
💡 You can create a virtual environment for better isolation:


python -m venv venv
venv\Scripts\activate     # On Windows
source venv/bin/activate  # On Linux/Mac
🚀 Usage
1. Train the model

python train_model.py
➡️ This generates a trained model in the models/ directory.

2. Predict fraud probabilities

python predict.py
➡️ This creates the reports/fraud_predictions_report.csv with prediction results.

3. Launch the dashboard

streamlit run dashboard_fraude.py
🔗 Opens the interactive dashboard at: http://localhost:8501

✅ Features in the dashboard:
Filter by fraud or non-fraud

Adjust probability threshold

Real-time updates with @st.cache

Histogram of predicted probabilities

Scatter plot of income vs fraud risk

🧠 Core Features
📊 Interactive filters for binary fraud classification

🎚️ Threshold slider to adjust fraud prediction sensitivity

🖼️ Real-time histogram and scatter plots (Seaborn + Matplotlib)

🔄 Efficient data caching for responsiveness

📈 Metric summaries to assist decision making

📝 License
This project is licensed under the MIT License.

🤝 Contributing
Feel free to:

Fork this repository

Submit pull requests

Create issues

Share your ideas or improvements

📌 Version
Last updated: 2025-05-10

Thanks for using this project!
If you found it helpful, consider ⭐ starring the repository.
