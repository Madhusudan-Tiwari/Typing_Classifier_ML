import time
import random
import os
import pandas as pd
from pynput import keyboard
from difflib import SequenceMatcher

# --------------- PROMPT SENTENCES ---------------
sentences = [
    "The quick brown fox jumps over the lazy dog",
    "Typing fast is a useful skill to have",
    "Machine learning models require good data",
    "Python is an easy language to learn",
    "Never stop exploring new ideas and tools",
    "Accuracy improves with consistent practice",
    "Everyone starts as a beginner in something",
    "Keyboards differ in layout and feel",
    "Small efforts lead to big achievements",
    "Stay focused and keep typing better"
]

prompt_text = random.choice(sentences)

# --------------- INITIALIZE VARIABLES ---------------
session_data = []
backspace_count = 0
typed_text = ""
timestamps = []
start_time = None

print("\n👉 Type this sentence exactly and press Enter when done:")
print("🔤", prompt_text)
print("\nStart typing:")

# --------------- KEYBOARD LISTENER ---------------
def on_press(key):
    global backspace_count, typed_text, timestamps, start_time

    if start_time is None:
        start_time = time.time()

    try:
        if key.char:
            typed_text += key.char
            timestamps.append(time.time())
    except AttributeError:
        pass

    if key == keyboard.Key.backspace:
        backspace_count += 1
    elif key == keyboard.Key.space:
        typed_text += " "
        timestamps.append(time.time())
    elif key == keyboard.Key.enter:
        return False

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

# --------------- METRIC CALCULATIONS ---------------
end_time = time.time()
total_time = end_time - start_time if start_time else 0.01
num_words = len(prompt_text.split())
wpm = (num_words / total_time) * 60

key_delays = [j - i for i, j in zip(timestamps[:-1], timestamps[1:])]
avg_delay = sum(key_delays) / len(key_delays) if key_delays else 0

accuracy = SequenceMatcher(None, typed_text.strip(), prompt_text.strip()).ratio()

# --------------- LABEL RULE (adjustable) ---------------
label = 1 if wpm > 40 and accuracy > 0.85 and backspace_count < 5 else 0

# --------------- DATAFRAME AND CSV LOGGING ---------------
session = {
    'prompt': prompt_text,
    'wpm': round(wpm, 2),
    'avg_key_delay': round(avg_delay * 1000, 2),
    'total_chars': len(typed_text),
    'backspaces': backspace_count,
    'accuracy': round(accuracy * 100, 2),
    'label': label
}

session_data.append(session)
df = pd.DataFrame(session_data)

# --------- Fix for Absolute Path ---------
base_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(base_dir, "..", "data")
data_dir = os.path.abspath(data_dir)
os.makedirs(data_dir, exist_ok=True)

file_name = os.path.join(data_dir, "typing_dataset.csv")
header_needed = not os.path.isfile(file_name) or os.stat(file_name).st_size == 0
df.to_csv(file_name, mode='a', index=False, header=header_needed)


# --------------- PRINT SUMMARY ---------------
print("\n✅ Session recorded!")
print(session)

print("\n🔍 Final check before file write:")
print(df)

file_path = os.path.abspath(file_name)
print(f"📁 Writing to CSV file at: {file_path}")

df.to_csv(file_name, mode='a', index=False, header=header_needed)

print("✅ Data successfully written to file.")
