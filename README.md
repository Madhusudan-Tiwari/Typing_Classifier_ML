# 🧠 Typing Behavior Classifier using Machine Learning

This project captures live typing behavior and classifies the performance of a user based on metrics like typing speed, key delay, accuracy, and backspace usage. It aims to build an intelligent model that can label typing sessions as “efficient” or “needs improvement.”

---

## 📌 Features

- ✅ **Live typing data capture** using Python and `pynput`
- ✅ Calculates metrics: **WPM, key delay, total characters, backspaces, and accuracy**
- ✅ Automatic labeling of sessions based on performance thresholds
- ✅ **CSV logging** of each session
- ✅ **Exploratory Data Analysis (EDA)** and visualization
- ✅ Outlier filtering and data cleaning

---

## 📊 Sample Metrics Logged

Each session records:
- `prompt`: The sentence typed
- `wpm`: Words per minute
- `avg_key_delay`: Average time between key presses (ms)
- `total_chars`: Number of characters typed
- `backspaces`: Number of backspace presses
- `accuracy`: Match with original prompt (%)
- `label`: 1 = Good performance, 0 = Needs improvement

---