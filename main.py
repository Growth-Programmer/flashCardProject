from tkinter import *
import pandas
import random
import time

# Adds current card to a dictionary. Easy to get key and value of the current card.
current_card = {}

# Dictionary of words that are not learned by the user. Used in later methods.
to_learn_data = {}

try:
    to_learn_frame = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn_data = original_data.to_dict(orient='records')
else:
    to_learn_data = to_learn_frame.to_dict(orient='records')


# Flips card to English translation.
def card_flip():
    # UI change to demonstrate a card from French words to English.
    canvas.itemconfig(card_image, image=card_back_image)
    canvas.itemconfig(language_text, fill="white", text="English")
    canvas.itemconfig(word_text, fill="white", text=current_card["English"])


def next_card():
    global current_card, flip_timer

    # Cancels any current timers.
    window.after_cancel(flip_timer)

    # Resets everytime the method is called.
    current_card = random.choice(to_learn_data)

    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(card_image, image=card_front_image)

    # After 3 seconds (3000 ms), the window will call the "card_flip" function. Also, restarts the timer.
    flip_timer = window.after(3000, func=card_flip)
    print(current_card)


# Checks what words are known
def is_known():
    # If the word is known by the user, it is removed from to_learn dictionary.
    to_learn_data.remove(current_card)
    next_card()

    # Creates a new data frame from the "to_learn_data" with the known card removed from the dictionary.
    new_data = pandas.DataFrame(to_learn_data)
    new_data.to_csv("data/words_to_learn.csv", index=False)

    next_card()


# Window color
light_green = "#97e6a0"

# User Interface
window = Tk()

flip_timer = window.after(3000, func=card_flip)

# Images
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

# Window
window.title("Flash Card Game")
window.config(bg='#97e6a0', pady=50, padx=50)

# Canvas
canvas = Canvas(width=800, height=526, bg=light_green, highlightbackground=light_green)
canvas.grid(row=0, column=0, columnspan=2)
card_image = canvas.create_image(400, 263, image=card_front_image)

# Text
language_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

# Buttons
known_button = Button(image=right_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=0)

unknown_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=1)

# Starts the flash card game.
next_card()

# Keeps the window open until closed.
window.mainloop()
