import os
import random

class MusicRecommender:
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path

    def get_song(self, mood):
        folder = "songs"

        # Find matching audio files
        matches = [
            os.path.join(folder, f)
            for f in os.listdir(folder)
            if mood.lower() in f.lower() and f.lower().endswith(".mp3")
        ]

        if not matches:
            return None

        return random.choice(matches)
