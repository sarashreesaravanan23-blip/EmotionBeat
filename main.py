import pygame
import sys
import cv2
import numpy as np
from mood_detector import MoodDetector
from recommender import MusicRecommender
from visualizer import show_mood_chart

def main():
    pygame.init()

    # Window setup
    WIDTH, HEIGHT = 650, 450
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("EmotionBeat - Mood Music Player")
    font = pygame.font.SysFont(None, 30)

    # Load background video
    video = cv2.VideoCapture("background.mp4")

    # Load modules
    mood_detector = MoodDetector()
    recommender = MusicRecommender("dataset.csv")

    current_song = None

    def play_song(song_path):
        nonlocal current_song
        try:
            pygame.mixer.music.load(song_path)
            pygame.mixer.music.play()
            current_song = song_path
        except:
            print("Error: Cannot play song:", song_path)

    def stop_song():
        pygame.mixer.music.stop()

    def draw_text(text, x, y):
        img = font.render(text, True, (255, 255, 255))
        screen.blit(img, (x, y))

    def button(label, x, y, w, h):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        pygame.draw.rect(screen, (40, 40, 40), (x, y, w, h))
        if x < mouse[0] < x + w and y < mouse[1] < y + h:
            pygame.draw.rect(screen, (70, 70, 70), (x, y, w, h))
            if click[0] == 1:
                pygame.time.delay(200)
                return True

        draw_text(label, x + 15, y + 10)
        return False

    detected_mood = "None"
    playing_song = "None"

    # MAIN LOOP
    while True:

        # Read video frame
        ret, frame = video.read()
        if not ret:
            video.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Restart video
            ret, frame = video.read()

        # Convert frame to pygame surface
        frame = cv2.resize(frame, (WIDTH, HEIGHT))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_surface = pygame.surfarray.make_surface(np.rot90(frame))

        # Draw video as background
        screen.blit(frame_surface, (0, 0))

        # Overlay text + UI
        draw_text("🎵 EmotionBeat – Mood Music Player", 120, 20)
        draw_text(f"Selected Mood: {detected_mood}", 50, 90)
        draw_text(f"Now Playing: {playing_song}", 50, 130)

        # Mood buttons
        if button("Happy", 50, 200, 150, 45):
            detected_mood = "happy"
            playing_song = recommender.get_song("happy")
            play_song(playing_song)

        if button("Sad", 250, 200, 150, 45):
            detected_mood = "sad"
            playing_song = recommender.get_song("sad")
            play_song(playing_song)

        if button("Calm", 450, 200, 150, 45):
            detected_mood = "calm"
            playing_song = recommender.get_song("calm")
            play_song(playing_song)

        if button("Energetic", 50, 260, 200, 45):
            detected_mood = "energetic"
            playing_song = recommender.get_song("energetic")
            play_song(playing_song)

        # STOP MUSIC button
        if button("STOP MUSIC", 300, 260, 200, 45):
            stop_song()
            playing_song = "None"

        # SHOW CHART button
        if button("Show Mood Chart", 200, 330, 250, 45):
            show_mood_chart("dataset.csv")

        # Exit handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop_song()
                pygame.quit()
                sys.exit()

        pygame.display.update()


if __name__ == "__main__":
    main()
