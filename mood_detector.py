class MoodDetector:
    def detect(self, text):
        text = text.lower()

        if "happy" in text or "joy" in text or "good" in text:
            return "happy"
        if "sad" in text or "upset" in text or "cry" in text:
            return "sad"
        if "calm" in text or "peace" in text:
            return "calm"
        if "energy" in text or "excited" in text:
            return "energetic"

        return "calm"   # default
