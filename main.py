import tkinter as tk
import random
from PIL import Image, ImageTk

# Constants
CHOICES = ["rock", "paper", "scissors"]

# Setup
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("600x650")
root.config(bg="white")

def load_images(path, size=(150,150)):
    img = Image.open(path)
    img = img.resize(size, Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(img)


# Load images (replace 'rock.png', etc. with your image file paths)
rock_img = load_images("rockpaperscissorsimages/rock.png")
paper_img = load_images("rockpaperscissorsimages/paper.png")
scissors_img = load_images("rockpaperscissorsimages/scissors.png")
images = {"rock": rock_img, "paper": paper_img, "scissors": scissors_img}

# ===== TOP TEXT =====
top_label = tk.Label(root, text="Pick your option", font=("Comic Sans MS", 20), bg="white")
top_label.pack(pady=10)

# ===== PLAYER CHOICE SECTION =====
choice_frame = tk.Frame(root, bg="white")
choice_frame.pack()

button_frame = tk.Frame(root, bg="white")
button_frame.pack()

# Image display
for choice in CHOICES:
    img = images[choice]
    img_label = tk.Label(choice_frame, image=img, bg="white", borderwidth=2, relief="solid")
    img_label.pack(side=tk.LEFT, padx=10)

    btn = tk.Button(button_frame, text=choice.capitalize(), font=("Comic Sans MS", 12),
                    command=lambda c=choice: start_game(c))
    btn.pack(side=tk.LEFT, padx=35, pady=5)

# ===== COMPUTER THINKING ANIMATION =====
thinking_label = tk.Label(root, text="", font=("Comic Sans MS", 16), bg="white")
thinking_label.pack(pady=20)

# ===== RESULT SECTION =====
result_frame = tk.Frame(root, bg="white")
result_frame.pack(pady=10)

player_result_label = tk.Label(result_frame, text="", font=("Comic Sans MS", 12), bg="white")
player_result_label.grid(row=0, column=0, padx=20)

computer_result_label = tk.Label(result_frame, text="", font=("Comic Sans MS", 12), bg="white")
computer_result_label.grid(row=0, column=2, padx=20)

# Image labels for results (initially empty, updated on play)
player_choice_img = tk.Label(result_frame, image=None, bg="white", borderwidth=2, relief="ridge", width=150, height=150)
player_choice_img.grid(row=1, column=0)

vs_label = tk.Label(result_frame, text="VS", font=("Comic Sans MS", 16), bg="white")
vs_label.grid(row=1, column=1)

computer_choice_img = tk.Label(result_frame, image=None, bg="white", borderwidth=2, relief="ridge", width=150, height=150)
computer_choice_img.grid(row=1, column=2)

# ===== FINAL RESULT =====
final_result_label = tk.Label(root, text="", font=("Comic Sans MS", 18, "bold"), bg="white")
final_result_label.pack(pady=20)

# ===== FUNCTIONS =====

def winner(player, npc):
    if player == npc:
        return "It's a tie!"
    elif (player == "rock" and npc == "scissors") or \
         (player == "paper" and npc == "rock") or \
         (player == "scissors" and npc == "paper"):
        return "You win!"
    else:
        return "I win!"

def start_game(player_choice):
    # Clear previous content
    thinking_label.config(text="")
    final_result_label.config(text="")
    player_result_label.config(text="")
    computer_result_label.config(text="")
    player_choice_img.config(image="", text="")
    computer_choice_img.config(image="", text="")

    # Animate thinking
    animate_thinking(0, player_choice)

def animate_thinking(dot_count, player_choice):
    dots = "." * (dot_count % 4)
    thinking_label.config(text=f"Computer is thinking{dots}")
    if dot_count < 12:
        root.after(300, animate_thinking, dot_count + 1, player_choice)
    else:
        finish_game(player_choice)

def finish_game(player_choice):
    npc_choice = random.choice(CHOICES)

    # Show both choices
    player_result_label.config(text=f"Player picked: {player_choice.capitalize()}")
    computer_result_label.config(text=f"Computer picked: {npc_choice.capitalize()}")

    player_choice_img.config(image=images[player_choice])
    computer_choice_img.config(image=images[npc_choice])

    # Show result
    result_text = winner(player_choice, npc_choice)
    final_result_label.config(text=f"Result: {result_text}")

# Run mainloop
root.mainloop()