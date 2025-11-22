# visualizer.py

import pandas as pd
import matplotlib.pyplot as plt

def show_mood_chart(dataset_path):
    df = pd.read_csv(dataset_path)
    df.columns = [col.strip().title() for col in df.columns]

    mood_col = next((col for col in df.columns if 'mood' in col.lower() or 'emotion' in col.lower()), None)

    if mood_col:
        mood_counts = df[mood_col].value_counts()
        plt.figure(figsize=(7, 5))
        mood_counts.plot(kind='bar', color='skyblue')
        plt.title('Mood Distribution in Dataset')
        plt.xlabel('Mood')
        plt.ylabel('Number of Songs')
        plt.tight_layout()
        plt.show()
    else:
        print("❌ No mood column found in dataset.")
