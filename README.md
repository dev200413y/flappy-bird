🐦 Flappy Bird Clone (Python + Pygame)

This is a faithful clone of the iconic **Flappy Bird** game, built using **Python** and **Pygame**. The implementation is designed for learners and aspiring game developers to understand real-time event handling, physics simulation, sprite-based rendering, and game loop management.

## 📦 Features
* 🎮 Pixel-perfect clone of the original Flappy Bird
* 🎧 Built-in sound effects and smooth animations
* 💥 Collision detection with pipes and ground
* 🔁 Infinite pipe generation logic
* 🧠 Modular and maintainable code structure
* 
## 📁 Project Structure
```
flappy-bird-clone/
│
├── gallery/
│   ├── audio/              # Game sounds
│   │   ├── die.wav
│   │   ├── hit.wav
│   │   ├── point.wav
│   │   ├── swoosh.wav
│   │   └── wing.wav
│   │
│   └── sprites/            # Game assets
│       ├── base.png
│       ├── background.png
│       ├── bird.png
│       ├── message.png
│       ├── pipe.png
│       ├── 0.png → 9.png   # Score digits
│
├── main.py                 # Core game logic
└── README.md               # This documentation file
```

## 🚀 Getting Started

### 🛠 Prerequisites

Ensure Python and Pygame are installed on your system.

```bash
python --version
pip install pygame
```

### ▶️ Running the Game

```bash
python main.py
```

Once the game starts, press the `SPACEBAR` or `UP ARROW` key to flap the bird.

## 🧠 How It Works
* **welcomeScreen()** – Displays the welcome UI and waits for player input to begin.
* **mainGame()** – Contains the main game loop, score tracking, and pipe handling.
* **isGameOver()** – Handles all collision logic and game-over triggers.
* **getRandomPipe() / createPipe()** – Randomizes the placement of pipes.
* **GAME\_SPRITES & GAME\_SOUNDS** – All game assets are preloaded for optimized rendering and audio playback.

## 🐛 Error Handling
The code includes basic error handling for:
* Missing sprite/audio files
* Failed pipe generation
* Runtime errors during asset loading
The game will exit gracefully and log appropriate messages in case of failure.

## 🎯 Future Enhancements
Here’s a forward-looking roadmap to scale the project:
* 🏆 Leaderboard & High Score Persistence (JSON/SQLite)
* 📱 Mobile Compatibility (Kivy or Pygbag for browser builds)
* 🧩 Add Power-ups (shield, speed boost)
* 🧠 Machine Learning Bot (play Flappy Bird using AI agent)
* 🎨 Skin/Theme Switcher (custom birds and backgrounds)
