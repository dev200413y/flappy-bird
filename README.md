Flappy Bird Game
Description
A Python-based implementation of the classic Flappy Bird game using the Pygame library. Players control a bird, navigating it through a series of pipes by flapping its wings to avoid collisions and achieve a high score by passing through pipe gaps.
Features

Welcome Screen: Displays a start screen with a bird, background, and message prompting the player to begin.
Game Loop: Handles bird movement, pipe generation, collision detection, and score tracking.
Random Pipes: Pipes are generated with random gap positions for varied gameplay.
Score Display: Real-time score display using digit sprites.
Sound Effects: Includes sounds for flapping, collisions, scoring, and game over.
Error Handling: Robust asset loading with error messages for missing or corrupted files.

Requirements

Python 3.x
Pygame (pip install pygame)

Installation

Clone the repository:git clone https://github.com/your-username/flappy-bird.git


Navigate to the project directory:cd flappy-bird


Install dependencies:pip install pygame


Ensure the gallery folder contains:
Sprites: bird.png, background.png, pipe.png, base.png, message.png, 0.png to 9.png.
Audio: die.wav, hit.wav, point.wav, swoosh.wav, wing.wav.



How to Play

Run the game:python flappy_bird.py


Press Spacebar or Up Arrow on the welcome screen to start.
Use Spacebar or Up Arrow to flap the bird’s wings and navigate through pipe gaps.
Avoid pipes, ground, or ceiling to continue playing.
Press Escape to quit.
Score increases by 1 per pipe gap passed.

Controls

Spacebar / Up Arrow: Flap wings.
Escape: Quit game.

File Structure

flappy_bird.py: Main game script.
gallery/sprites/: Sprite images (bird, pipes, background, etc.).
gallery/audio/: Sound effect files.

Game Mechanics

Bird Movement: Gravity pulls the bird down; flapping moves it up.
Pipes: Pairs of pipes (upper and lower) move left, with new pipes added as old ones exit.
Collisions: Game ends on contact with pipes, ground, or ceiling.
Scoring: Points awarded for passing pipe gaps, with sound feedback.

Notes

Runs at 32 FPS with a 289x511 pixel resolution.
Requires all assets in the gallery folder to function.
Includes error handling for asset loading and pipe generation.

Contributing
Submit pull requests or open issues for bugs, features, or enhancements.
License
MIT License. See LICENSE for details.
