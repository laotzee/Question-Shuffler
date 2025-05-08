import tkinter
from tkinter import messagebox, filedialog

TITLE = "Qffle"
TITLE_REPORT = "Session's performance"
TITLE_NO_FILE = "No file given"
DETAIL_NO_FILE = "You must have questions somewhere :("
TITLE_NO_CSV = "No CSV file given"
DETAIL_NO_CSV = "Qffle only support CSV for now :("
PADX = 100


FLASH_CARD_FRONT = "resources/card_front_new.png"
FLASH_CARD_BACK = "resources/card_back_new.png"
RIGHT = "resources/check.png"
WRONG = "resources/cross.png"
SWAP = "resources/repeat.png"
BG = "#E4D1B9"
WHITE = "#FFFFF0"
BLACK = "#333333"
LANG_FONT = ("Courier", 25, "bold")
WORD_FONT = ("Courier", 20, "bold")


CARD_WIDTH = 800 * 1.5
CARD_HEIGHT = 526 *1.5

ICON_WIDTH = 128 *1.5
ICON_HEIGHT = 128 *1.5

HEADING_HEIGHT_RATIO = CARD_HEIGHT / 3.7
QUESTION_HEIGHT_RATIO = CARD_HEIGHT / 1.8

TEXT_BORDER_RATIO =  CARD_WIDTH * 0.6
TEXT_WIDTH_POS = CARD_WIDTH / 2

class MainScreen(tkinter.Tk):


    def __init__(self):
        super().__init__()
        self.title(TITLE)

        self.right_img = None
        self.wrong_img = None
        self.swap_img = None
        self.front_card_img = None
        self.back_card_img = None

        self.card_canvas = None
        self.card_id = None
        self.displayed_content = None
        self.displayed_heading = None
        self.answer_heading = None
        self.question_heading = None

        self.right_answers = 0
        self.wrong_answers = 0
        self.time_passed = 0

        self.current_cards = ("","")
        self.cards = None

        self.main_screen()

    def start(self):
        self.mainloop()

    def image_binding(self):
        """Ties images to the instance so that garbage colector does not
        delete them"""

        self.right_img = tkinter.PhotoImage(file=RIGHT)
        self.wrong_img = tkinter.PhotoImage(file=WRONG)
        self.swap_img = tkinter.PhotoImage(file=SWAP)
        self.front_card_img = tkinter.PhotoImage(file=FLASH_CARD_FRONT)
        self.back_card_img = tkinter.PhotoImage(file=FLASH_CARD_BACK)

    @staticmethod
    def get_file():

        return filedialog.askopenfilename()

    def load_cards(self, cards):
        """Saves cards into an instance variable and configure headings"""

        print(cards)

        if type(cards) == tuple:
            messagebox.showerror(
                title=TITLE_NO_FILE,
                detail=DETAIL_NO_FILE,
            )
            self.finish_session()
        elif type(cards) == str and cards[-4:].lower() != ".csv":
            messagebox.showerror(
                title=TITLE_NO_CSV,
                detail=DETAIL_NO_CSV,
            )
            self.finish_session()

        self.cards = cards["cards"]
        self.question_heading = cards["headings"][0]
        self.answer_heading = cards["headings"][1]
        self.next_card()

    def reset_stats(self):
        """Restart stats for new session"""

        self.right_answers = 0
        self.wrong_answers = 0
        self.time_passed = 0

    def session_report(self):
        """Shows the performance of the session in terms of time, right and
        wrong answer"""

        t = self.time_passed
        r = self.right_answers
        w = self.wrong_answers

        inf = f"Time: {t}\nRight answers: {r}\nWrong answer: {w}"
        tkinter.messagebox.showinfo(
            title=TITLE_REPORT,
            detail=inf,
        )
        self.finish_session()

    def update_score(self, answer):
        """Updates the score depending on the answer. If incorrect, previous
        card goes into the deck"""

        if answer:
            self.right_answers += 1
        else:
            self.cards.append(self.current_cards)
            self.wrong_answers += 1

    @staticmethod
    def finish_session():
        """Manages the end of the session"""

        exit()

    def next_card(self, correct_guess=True):
        """Draws next card from list. If empty deck, shows the stats of the
        session"""

        self.update_score(correct_guess)

        try:
            next_card = self.cards.pop(0)
        except IndexError:
            self.session_report()
        else:
            self.update_card(next_card)

    def update_card(self, new_card):
        """Updates the current card on screen"""

        self.current_cards = new_card
        self.card_canvas.itemconfig(self.card_id,
                                    image=self.front_card_img)
        self.card_canvas.itemconfig(self.displayed_content,
                                    text=self.current_cards[0],
                                    fill=BLACK)
        self.card_canvas.itemconfig(self.displayed_heading,
                                    text=self.question_heading,
                                    fill=BLACK)

    def swap_cards(self):
        """Swaps the content in the cards displayed"""
        if self.card_canvas.itemcget(self.card_id, "image") == str(
                self.back_card_img):

            self.card_canvas.itemconfig(self.card_id,
                                        image=self.front_card_img)
            self.card_canvas.itemconfig(self.displayed_content,
                                        text=self.current_cards[0],
                                        fill=BLACK)
            self.card_canvas.itemconfig(self.displayed_heading,
                                        text=self.question_heading,
                                        fill=BLACK)
        else:
            self.card_canvas.itemconfig(self.card_id,
                                        image=self.back_card_img)
            self.card_canvas.itemconfig(self.displayed_content,
                                        text=self.current_cards[1],
                                        fill=WHITE)
            self.card_canvas.itemconfig(self.displayed_heading,
                                        text=self.answer_heading,
                                        fill=WHITE)

    @staticmethod
    def canvas_creator(frame, width, height):
        """Returns configured canvas"""

        canvas = tkinter.Canvas(master=frame, width=width,
                                height=height, bg=BG,
                                highlightthickness=0)
        return canvas

    def main_screen(self):
        """Manages the GUI functionality"""

        self.image_binding()

        frame1 = tkinter.Frame(self, bg=BG)
        frame2 = tkinter.Frame(frame1, bg=BG)

        right_canvas = self.canvas_creator(frame2, ICON_WIDTH, ICON_HEIGHT)
        wrong_canvas = self.canvas_creator(frame2, ICON_WIDTH, ICON_HEIGHT)
        swap_canvas = self.canvas_creator(frame2, ICON_WIDTH, ICON_HEIGHT)
        self.card_canvas = self.canvas_creator(frame1, CARD_WIDTH, CARD_HEIGHT)

        right_canvas.create_image(ICON_WIDTH/2,
                                  ICON_HEIGHT/2,
                                  image=self.right_img,
                                  tags="right")

        wrong_canvas.create_image(ICON_WIDTH/2,
                                  ICON_HEIGHT/2,
                                  image=self.wrong_img,
                                  tags="wrong")

        swap_canvas.create_image(ICON_WIDTH/2,
                                 ICON_HEIGHT/2,
                                 image=self.swap_img,
                                 tags="swap")

        self.card_id = self.card_canvas.create_image(
            TEXT_WIDTH_POS,
            CARD_HEIGHT/2,
            image=self.front_card_img,
            anchor="center",
        )
        self.displayed_content = self.card_canvas.create_text(
            TEXT_WIDTH_POS,
            QUESTION_HEIGHT_RATIO,
            width=TEXT_BORDER_RATIO,
            font=WORD_FONT,
            )
        self.displayed_heading = self.card_canvas.create_text(
            TEXT_WIDTH_POS,
            HEADING_HEIGHT_RATIO,
            width=TEXT_BORDER_RATIO,
            text=self.question_heading,
            font = LANG_FONT,
        )

        right_canvas.tag_bind("right", "<Button-1>", lambda event:
                            self.next_card(correct_guess=True))

        wrong_canvas.tag_bind("wrong", "<Button-1>", lambda event:
                            self.next_card(correct_guess=False))

        swap_canvas.tag_bind("swap", "<Button-1>", lambda event:
                            self.swap_cards())

        wrong_canvas.pack(side=tkinter.LEFT, pady=(0, PADX), padx=50)
        swap_canvas.pack(side=tkinter.LEFT, pady=(0, PADX), padx=50)
        right_canvas.pack(side=tkinter.LEFT, pady=(0, PADX), padx=50)

        frame1.pack()
        self.card_canvas.pack(expand=True, fill="both")
        frame2.pack()


if __name__ == "__main__":

    screen = MainScreen()