import joblib
import numpy as np
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(script_dir, '..', 'models', 'typing_classifier.pkl')
model = joblib.load(model_path)

print("\n Typing Behavior Classifier Prediction")
print("Enter the following values based on your typing session:")

wpm = float(input(" Words Per Minute (WPM): "))
avg_delay = float(input(" Average Key Delay (in ms): "))
total_chars = int(input(" Total Characters Typed: "))
backspaces = int(input(" Number of Backspaces Used: "))
accuracy = float(input(" Accuracy (%): "))

features = np.array([[wpm, avg_delay, total_chars, backspaces, accuracy]])
prediction = model.predict(features)[0]


if prediction == 1:
    print("\n You are classified as a FAST and ACCURATE typist!")
else:
    print("\n You are classified as a SLOW or INACCURATE typist. Keep practicing!")

