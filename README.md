
# ✋ Rock Paper Scissors – Hand Gesture (Python)

A real-time **Rock Paper Scissors game** controlled using **hand gestures** with a webcam.  
Built using **Python, OpenCV, and MediaPipe**, this project detects hand gestures and lets you play against the computer.

The project is implemented in **three progressive versions**, showing feature-by-feature development.

---

## 📂 Project Structure

```

rock-paper-scissors-hand-gesture/
├── rps_basic_countdown.py
├── rps_with_score.py
├── rps_score_and_reset.py
└── README.md

````

---

## 🔹 Project Versions

### 1️⃣ Basic Version (Countdown Only)
**File:** `rps_basic_countdown.py`

- Hand gesture Rock Paper Scissors
- Countdown animation **3 → 2 → 1 → SHOW**
- No score tracking

---

### 2️⃣ Score Version
**File:** `rps_with_score.py`

- Countdown animation
- Player vs Computer **score counter**
- Stable gameplay (no fast flickering)

---

### 3️⃣ Final Version (Recommended ⭐)
**File:** `rps_score_and_reset.py`

- Countdown animation
- Score counter
- **Gesture-based score reset**
  - ✋✋ Show **both hands open** to reset scores
- Most complete and polished version

---

## 🛠 Technologies Used
- Python 3.10 / 3.11  
- OpenCV  
- MediaPipe  

---

## ⚙️ Installation

Make sure **Python 3.10 or 3.11** is installed  
(**Do not use Python 3.14**)

Install required libraries:
```bash
py -3.11 -m pip install opencv-python mediapipe numpy
````

---

## ▶️ How to Run

1. Open **Command Prompt**
2. Go to the project folder:

```bash
cd path/to/ai-hand-gesture-rock-paper-scissors
```

3. Run any version:

```bash
py -3.11 rps_basic_countdown.py
```

```bash
py -3.11 rps_with_score.py
```

```bash
py -3.11 rps_score_and_reset.py
```

4. Press **Q** to quit the game.

---

## ✋ Hand Gestures Used

| Gesture            | Action                      |
| ------------------ | --------------------------- |
| ✊ Fist             | Rock                        |
| ✌ Two fingers      | Scissors                    |
| 🖐 Open hand       | Paper                       |
| ✋✋ Both hands open | Reset score (final version) |

---

## 🎯 Learning Outcomes

* Computer vision basics
* Hand landmark detection
* Gesture recognition logic
* Real-time game development
* State management & cooldown handling

---

## 🚀 Future Improvements

* Sound effects
* Winner animations
* GUI enhancements
* Game mode selection
* Demo GIF for README

---

## 👨‍💻 Author

**Jatin**

⭐ If you like this project, consider starring the repository!




