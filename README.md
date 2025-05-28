🧠 fMRI Brain Task Classification
A simulated brain activity classification pipeline using synthetic fMRI BOLD signals. The project generates realistic voxel activation patterns across different cognitive tasks (e.g., memory, language, motor) and classifies them using PCA + SVM. It is deployed using Streamlit Cloud for interactive use.

🚀 Live Demo
👉 Launch the Streamlit App

📂 Project Structure
bash

📁 fMRI-Brain-Task-Classifier/
├── app.py                  # Streamlit application script
├── pca_model.pkl           # Trained PCA dimensionality reduction model
├── task_classifier.pkl     # Trained SVM classifier
├── requirements.txt        # Dependencies for Streamlit Cloud
├── synthetic_fmri.ipynb    # Notebook for data simulation and model training
└── README.md               # Project description
🧪 Project Overview
This project simulates and classifies fMRI brain data by:

Simulating voxel-level BOLD activity for tasks like:

Memory recall

Language comprehension

Motor function

Introducing subject variability and an age factor

Applying PCA for dimensionality reduction

Training an SVM model to classify tasks based on reduced features

Deploying the model via Streamlit Cloud

📊 Dataset Details
The synthetic dataset simulates multiple aspects of real fMRI data:

🧬 Voxel-wise activity for each task

👤 Subject variability to simulate inter-individual differences

👵 Age factor to reflect cognitive and signal changes across age

🔉 Noise to emulate scanner and neural variability

Each row represents one subject-task combination.

🧠 Model Workflow
Generate data with realistic patterns for each task

Reduce dimensionality using PCA

Train classifier (SVM) on PCA outputs

Deploy with Streamlit for easy user input + predictions

📈 How to Use
Upload a CSV file with fMRI features (simulated or real)

The app will:

Transform it using PCA

Predict the cognitive task

View the prediction results live in the app

🛠 Requirements
nginx

streamlit
numpy
pandas
scikit-learn
joblib

Install locally with:

bash

pip install -r requirements.txt



📚 Technologies Used
Python

Scikit-learn

PCA

SVM

Streamlit

🧑‍💻 Author
Shrutaswini [github.com/Shrutaswini]

Feel free to connect on LinkedIn

💡 Future Ideas
Add task difficulty modeling

Test with real open-source fMRI datasets (e.g., HCP, OpenNeuro)

Include visualization of voxel activations
