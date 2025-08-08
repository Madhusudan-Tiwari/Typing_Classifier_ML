# Typing Behavior Classifier 🧠⌨️

This project uses **Machine Learning** to classify typing sessions based on user behavior like typing speed, accuracy, delays, and backspace usage. It's a hands-on demonstration of how behavioral patterns can be turned into predictive models using basic ML algorithms.

## 🔍 Project Goal

To predict whether a typing session indicates **"good" typing behavior** based on:
- Words Per Minute (WPM)
- Average key delay
- Total characters typed
- Number of backspaces
- Accuracy

## 📁 Project Structure

Typing_Classifier_ML/
├── data/
│ └── typing_dataset.csv # Collected typing sessions
├── models/
│ └── typing_classifier.pkl # Trained ML model
├── notebook/
│ ├── analysis.ipynb # Data cleaning, visualization, model training
│ └── predict.py # Loads model and makes predictions
├── scripts/
│ └── data.py # Script to collect typing data using keyboard listener
└── README.md # Project documentation


## 🧪 Features Tracked
- **WPM**: Words per minute
- **Avg Key Delay**: Delay between keystrokes
- **Backspaces**: Indicates corrections
- **Accuracy**: Similarity to the prompt
- **Label**: 1 = strong session, 0 = needs improvement

## 🧠 Models Used
- Logistic Regression
- K-Nearest Neighbors (KNN)
- Decision Tree

### 🎯 Accuracy Achieved
- Logistic Regression: **100%**
- Decision Tree: **100%**
- KNN: **91%**

## 🧰 Technologies
- Python
- scikit-learn
- pandas
- pynput
- joblib
- matplotlib (for visualization)

## ▶️ How to Run

1. **Collect Typing Data**
   ```bash
   cd scripts
   python data.py

   This launches a prompt, listens to your typing, and logs behavior metrics to data/typing_dataset.csv.

2. **Train the Model**
    Open notebook/analysis.ipynb and run all cells to:

    Clean data

    Visualize metrics

    Train models

    Save the best model to models/typing_classifier.pkl

3. **Make Predictions**

    bash

    cd notebook
    python predict.py

## 🚀 Future Ideas
    Deploy as a web app with live typing analysis

    Detect signs of fatigue or stress based on typing rhythm

    Expand to multi-class classification (e.g. beginner, intermediate, advanced)

## 📌 Author
Made with focus and curiosity by Madhusudan Tiwari.


---