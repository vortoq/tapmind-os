# BeatForge (Simulated music generator)
import random
genres = ["lofi", "trap", "ambient", "chillhop"]

def generate_track():
    genre = random.choice(genres)
    print(f"Generating a {genre} beat with AI...")
    print("✅ Track ready: /music/beat.mp3 (pretend!)")

if __name__ == "__main__":
    generate_track()
