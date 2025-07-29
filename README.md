# 🎮 Tic Tac Toe (Kółko i Krzyżyk) – Python Game Project

An interactive Tic Tac Toe game developed in Python using the Pygame library.
This project is part of my portfolio and was built with a strong focus on code quality, modular design, user interaction, and multimedia handling (graphics, sound, and UI).

---

## 🖼️ Screenshot

<img width="994" height="783" alt="image" src="https://github.com/user-attachments/assets/63c165c4-a5f2-4dda-abf0-3eb838e06e60" />


---

## 🔽 Download the game (.exe)

No need to install Python – just download and play!

👉 **[Download Windows version (.exe)](https://github.com/Alicja16/Kolko_i_Krzyzyk/releases/latest)**

---

## ⚙️ Technologies & Design Approach

| Element                | 	Implementation                                         |
|------------------------|-----------------------------------------------------|
| Language               | Python 3                                            |
| Graphics Library       | Pygame                                              |
| Build `.exe`           | PyInstaller (`main.spec`)                           |
| Modularity             | Separated into `main.py` and `functions.py`         |
| Media Management       | Organized into `gallery/` and `sounds/` folders     |
| Sound Handling         | Background music + click effects with mute option   |
| Threading              | `threading.Thread` used for music playback          |

🧪 **As an experimental feature**, I incorporated Python’s `threading` library—despite Pygame’s built-in sound system—to demonstrate and test custom thread-based audio control. This was both a conceptual and technical exercise to expand my understanding of multithreading in Python.

---

## 🧠 Game Features

- 🖼️ Animated start screen with a "Start" button
- 🔊 Toggle buttons for music and sound effects (on/off)
- ❎ Random player selection (X or O)
- 🧩 Win and draw detection logic
- 🔁 Option to restart the game or return to main menu
- 🎵 Background music and interactive sound effects
- 🎨 "Glow" text effect using `pygame.Surface`
- 🖱️ Full mouse interaction: click detection, graphics scaling, and board rendering
