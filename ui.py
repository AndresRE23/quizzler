from tkinter import *

THEME_COLOR = "#375362"
QUESTION_BG = "#F9F9F9"
TITLE_COLOR = "#FFFFFF"
SCORE_COLOR = "#F1C40F"
FOOTER_COLOR = "#BDC3C7"

FONT_TITLE = ("Arial", 26, "bold")
FONT_QUESTION = ("Arial", 16, "italic")
FONT_SCORE = ("Arial", 12, "bold")
FONT_FOOTER = ("Arial", 9, "italic")

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.title_label = Label(
            text="Play Trivia",
            bg=THEME_COLOR,
            fg=TITLE_COLOR,
            font=FONT_TITLE,
            pady=10
        )
        self.title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

        self.score = Label(
            text="Score: 0",
            bg=THEME_COLOR,
            fg=SCORE_COLOR,
            font=FONT_SCORE
        )
        self.score.grid(row=1, column=1, sticky="e", pady=(0, 10))

        self.canvas = Canvas(
            width=420, height=260,
            bg=QUESTION_BG,
            highlightthickness=0
        )
        self.question = self.canvas.create_text(
            210, 130,
            text="This is a placeholder.",
            font=FONT_QUESTION,
            fill=THEME_COLOR,
            width=380
        )
        self.canvas.grid(row=2, column=0, columnspan=2, pady=20)

        true_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(
            image=true_img,
            highlightthickness=0,
            bd=0,
            bg=THEME_COLOR,
            activebackground=THEME_COLOR,
            cursor="hand2"
        )
        self.true_btn.grid(row=3, column=0, pady=15, padx=15)

        false_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(
            image=false_img,
            highlightthickness=0,
            bd=0,
            bg=THEME_COLOR,
            activebackground=THEME_COLOR,
            cursor="hand2"
        )
        self.false_btn.grid(row=3, column=1, pady=15, padx=15)

        self.footer = Label(
            text="Powered by Open Trivia API",
            bg=THEME_COLOR,
            fg=FOOTER_COLOR,
            font=FONT_FOOTER
        )
        self.footer.grid(row=4, column=0, columnspan=2, pady=(15, 0))

        self.window.mainloop()

