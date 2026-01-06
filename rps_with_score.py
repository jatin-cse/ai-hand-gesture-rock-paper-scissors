import cv2
import mediapipe as mp
import random
import time

# Camera
cap = cv2.VideoCapture(0)

# MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

# Finger tips
finger_tips = [4, 8, 12, 16, 20]

# Game choices
choices = ["Rock", "Paper", "Scissors"]

# Scores
player_score = 0
computer_score = 0

# Timing control
round_active = False
countdown_start = 0
round_delay = 4   # 3-2-1-SHOW
cooldown = 2
last_result_time = 0

player_choice = ""
computer_choice = ""
winner = ""

def get_winner(player, computer):
    if player == computer:
        return "Draw"
    if (player == "Rock" and computer == "Scissors") or \
       (player == "Scissors" and computer == "Paper") or \
       (player == "Paper" and computer == "Rock"):
        return "You Win!"
    return "Computer Wins!"

def count_fingers(hand, handedness):
    lm = hand.landmark
    label = handedness.classification[0].label
    count = 0

    # Thumb
    if label == "Right":
        if lm[4].x < lm[3].x:
            count += 1
    else:
        if lm[4].x > lm[3].x:
            count += 1

    # Other fingers
    for tip in finger_tips[1:]:
        if lm[tip].y < lm[tip - 2].y:
            count += 1

    return count

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    finger_count = -1

    # Detect hand
    if result.multi_hand_landmarks:
        for hand, handedness in zip(result.multi_hand_landmarks,
                                    result.multi_handedness):
            finger_count = count_fingers(hand, handedness)
            mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)

    current_time = time.time()

    # Start round when valid gesture shown
    if finger_count in [0, 2, 5] and not round_active:
        countdown_start = current_time
        round_active = True

    # Countdown & game logic
    if round_active:
        elapsed = current_time - countdown_start

        if elapsed < 1:
            text = "3"
        elif elapsed < 2:
            text = "2"
        elif elapsed < 3:
            text = "1"
        elif elapsed < 4:
            text = "SHOW"
        else:
            # Decide player move
            if finger_count == 0:
                player_choice = "Rock"
            elif finger_count == 2:
                player_choice = "Scissors"
            elif finger_count == 5:
                player_choice = "Paper"
            else:
                player_choice = ""

            if player_choice and current_time - last_result_time > cooldown:
                computer_choice = random.choice(choices)
                winner = get_winner(player_choice, computer_choice)

                # Update scores
                if winner == "You Win!":
                    player_score += 1
                elif winner == "Computer Wins!":
                    computer_score += 1

                last_result_time = current_time
                round_active = False

        cv2.putText(frame, text, (300, 120),
                    cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 5)

    # Display UI
    cv2.putText(frame, f"Score  You: {player_score}  CPU: {computer_score}",
                (20, 40), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 255, 255), 2)

    cv2.putText(frame, f"Player: {player_choice}", (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.putText(frame, f"Computer: {computer_choice}", (20, 120),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    cv2.putText(frame, winner, (20, 170),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)

    cv2.imshow("Rock Paper Scissors - Hand Gesture", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
