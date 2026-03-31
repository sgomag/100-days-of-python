import os
from tkinter import *
import pandas
import random

PATH_ALL_WORDS = "data/french_words.csv"
PATH_TO_LEARN = "data/words_to_learn.csv"
BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- GET LIST OF WORDS TO LEARN ------------------------------- #

if os.path.exists(PATH_TO_LEARN):
    words_df = pandas.read_csv(PATH_TO_LEARN)
else:
    words_df = pandas.read_csv(PATH_ALL_WORDS)
    words_df.to_csv(PATH_TO_LEARN, index=False)

words_dict = words_df.to_dict(orient="records")

# ---------------------------- FUNCTIONS ------------------------------- #
def next_card_right(dictionary):
    global flip_timer
    window.after_cancel(flip_timer)
    # Update CSV file
    words_dict.remove(dict(word_pair))
    updated_df = pandas.DataFrame(words_dict)
    updated_df.to_csv(PATH_TO_LEARN, index=False)
    # Repeat
    get_random_word(dictionary)

def next_card_wrong(dictionary):
    global flip_timer
    window.after_cancel(flip_timer)
    # Repeat
    get_random_word(dictionary)

def get_random_word(dictionary):
    global flip_timer, word_pair
    word_pair = list((random.choice(dictionary)).items())
    language, word = word_pair[0]
    canvas.itemconfig(language_text, text=language, fill="black")
    canvas.itemconfig(word_text, text=word, fill="black")
    canvas.itemconfig(canvas_image, image=front_image)
    flip_timer = window.after(3000, flip_card)

def flip_card():
    global word_pair
    language, word = word_pair[1]
    canvas.itemconfig(language_text, text=language, fill="white")
    canvas.itemconfig(word_text, text=word, fill="white")
    canvas.itemconfig(canvas_image, image=back_image)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800 , height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400,526/2)
language_text = canvas.create_text(400, 170, text="", font=("Ariel", 30, "italic"))
word_text = canvas.create_text(400, 270, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# BUTTONS
right_img = PhotoImage(file="images/right.png")
button_right = Button(image=right_img, highlightthickness=0)
button_right.config(bd=0, anchor="center", command=lambda:next_card_right(words_dict))
button_right.grid(column=0, row=1)

wrong_img = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=wrong_img, highlightthickness=0)
button_wrong.config(bd=0, anchor="center", command=lambda:next_card_wrong(words_dict))
button_wrong.grid(column=1, row=1)

# ---------------------------- PROGRAM ------------------------------- #
word_pair = []
flip_timer = 0
get_random_word(words_dict)

window.mainloop()