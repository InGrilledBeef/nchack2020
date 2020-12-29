# Date: 2020-12-28
# Author: Ingrid and Nusha
# Purpose: Winter themed Jeopardy game for the 2020 NCHACK hackathon

from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as font

# Settings
# Start Window
root = Tk()
root.title("Winter Jeopardy")
root.resizable(False, False)

# Game Window
top = Toplevel()
top.withdraw()
top.resizable(False, False)

# Team Scores
global team1_score
global team2_score
team1_score = 0
team2_score = 0

# Functions

def open_instructions():
    # opens game instructions
    global instructions
    instructions = Toplevel()
    root.withdraw()
    go_back = Button(instructions, text="GO BACK TO START SCREEN", command=start_screen).pack()
    

def start_screen():
    # Opens start
    instructions.withdraw()
    root.deiconify()

def start_game():
    # Opens board 
    global top
    global board_img
    global board_bg
    top.deiconify()
    root.withdraw()
    board_img = ImageTk.PhotoImage(Image.open("Backgrounds/JeopardyBoard.png"))
    board_bg = Label(top, image=board_img).grid(row=0, column=0, rowspan=6, columnspan=5)
    frames()
    game_buttons()
    

def game_buttons(): # Game buttons
    # TV/Books
    tv1 = Button(top, text = "1 ORNAMENT", padx=58, pady=27, command = lambda: open_question(0, 0, 10, 117)).place(x=10, y=117)
    tv2 = Button(top, text = "2 ORNAMENTS", padx=56, pady=27, command = lambda: open_question(1, 0, 10, 215)).place(x=10, y=215) 
    tv3 = Button(top, text = "3 ORNAMENTS", padx=56, pady=27, command = lambda: open_question(2, 0, 10, 313)).place(x=10, y=313) 
    tv4 = Button(top, text = "4 ORNAMENTS", padx=56, pady=27, command = lambda: open_question(3, 0, 10, 411)).place(x=10, y=411)
    tv5 = Button(top, text = "5 ORNAMENTS", padx=56, pady=27, command = lambda: open_question(4, 0, 10, 509)).place(x=10, y=509)


    # Music
    music1 = Button(top, text = "1 ORNAMENT", padx=58, pady=27, command = lambda: open_question(0, 1, 224, 117)).place(x=224, y=117)
    music2 = Button(top, text = "2 ORNAMENTS", padx=56, pady=27, command = lambda: open_question(1, 1, 224, 215)).place(x=224, y=215)
    music3 = Button(top, text = "3 ORNAMENTS", padx=56, pady=27, command = lambda: open_question(2, 1, 224, 313)).place(x=224, y=313)
    music4 = Button(top, text = "4 ORNAMENTS", padx=56, pady=27, command = lambda: open_question(3, 1, 224, 411)).place(x=224, y=411)
    music5 = Button(top, text = "5 ORNAMENTS", padx=56, pady=27, command = lambda: open_question(4, 1, 224, 509)).place(x=224, y=509)

    # Season
    season1 = Button(top, text = "1 ORNAMENT", padx=58, pady=27, command = lambda: open_question(0, 2, 438, 117)).place(x=438, y=117)
    season2 = Button(top, text = "2 ORNAMENTS", padx=56, pady=27, command = lambda: open_question(1, 2, 438, 215)).place(x=438, y=215)
    season3 = Button(top, text = "3 ORNAMENTS", padx=56, pady=27, command = lambda: open_question(2, 2, 438, 313)).place(x=438, y=313)
    season4 = Button(top, text = "4 ORNAMENTS", padx=56, pady=27, command = lambda: open_question(3, 2, 438, 411)).place(x=438, y=411)
    season5 = Button(top, text = "5 ORNAMENTS", padx=56, pady=27, command = lambda: open_question(4, 2, 438, 509)).place(x=438, y=509)

    # Holidays
    holidays1 = Button(top, text = "1 ORNAMENT", padx=58, pady=27, command = lambda: open_question(0, 3, 654, 117)).place(x=654, y=117)
    holidays2 = Button(top, text = "2 ORNAMENTS", padx=56, pady=27, command = lambda: open_question(1, 3, 654, 215)).place(x=654, y=215)
    holidays3 = Button(top, text = "3 ORNAMENTS", padx=56, pady=27, command = lambda: open_question(2, 3, 654, 313)).place(x=654, y=313)
    holidays4 = Button(top, text = "4 ORNAMENTS", padx=56, pady=27, command = lambda: open_question(3, 3, 654, 411)).place(x=654, y=411)
    holidays5 = Button(top, text = "5 ORNAMENTS", padx=56, pady=27, command = lambda: open_question(4, 3, 654, 509)).place(x=654, y=509)

    # Sports
    sports1 = Button(top, text = "1 ORNAMENT", padx=58, pady=27, command = lambda: open_question(0, 4, 866, 117)).place(x=866, y=117)
    sports2 = Button(top, text = "2 ORNAMENTS", padx=56, pady=27, command = lambda: open_question(1, 4, 866, 215)).place(x=866, y=215)
    sports3 = Button(top, text = "3 ORNAMENTS", padx=56, pady=27, command = lambda: open_question(2, 4, 866, 313)).place(x=866, y=313)
    sports4 = Button(top, text = "4 ORNAMENTS", padx=56, pady=27, command = lambda: open_question(3, 4, 866, 411)).place(x=866, y=411)
    sports5 = Button(top, text = "5 ORNAMENTS", padx=56, pady=27, command = lambda: open_question(4, 4, 866, 509)).place(x=866, y=509)

    global button_list
    button_list = [[tv1, tv2, tv3, tv4, tv5],
                   [music1, music2, music3, music4, music5],
                   [season1, season2, season3, season4, season5],
                   [holidays1, holidays2, holidays3, holidays4, holidays5],
                   [sports1, sports2, sports3, sports4, sports5]
                   ]


def open_question(row, col, x, y):
    # Opens the question screen
    
    # Questions
    questions = [["Actor who played Grinch in the 2000 hit: How the Grinch Stole Christmas",
              "This artist makes $2m a year from her hit christmas song.",
              "Using three snowballs and decorations, this figure can be made at home.",
              "How many days of Kwanzaa are there? (Number)",
              "Canadian Winter sport"],
             ["Name the movie: a couple who plans to go on vacation for Christmas rush to organize a party when they discover their daughter is coming home for the holidays",
              "The year the song Jingle Bell Rock was originally published (ending in 0)",
              "Which is more popular for gift purchasing: Black Friday or Cyber Monday?",
              "Name of goals set in place by individuals for the New Year’s",
              "A turn in figure skating that resembles an infinity sign"],
             ["The author of A Christmas Carol",
              "George Micheal (Wham!) sang this song in 1985",
              "Which continent is best known for celebrating Christmas in the warm?",
              "Which Winter Holiday is also known as “ the Festival of Lights “ ?",
              "Form of skiing where skiers travel across a flat surface"],
             ["Buddy the Elf’s father’s first name in Elf",
              "Finish the lyrics.\n\nThe party's on\nThe feelin's here\nThat only comes\nThis time of year",
              "This device is used to create artificial snow",
              "Which century did caroling become a Christmas tradition?",
              "This sport uses the force of Flotation."],
             ["This set of letters was written by the same author behind The Lord of The Rings",
              "This movie’s Christmas soundtrack won Best Musical Album for Children at the 50th Grammy Awards.",
              "During Hibernation, bears can go this many days without food and water.",
              "In what century was the term X-mas invented?",
              "Snowboarding was first introduced in this year’s Winter Olympics"]]

    global posx
    global posy
    posx = x
    posy = y

    # New screen
    global question_screen
    question_screen = Toplevel()
    question_screen.resizable(False, False)
    top.withdraw()

    # define font
    global myFont
    global myFont1
    myFont = font.Font(family='Comic Sans', size=20, weight='bold')
    myFont1 = font.Font(family='Comic Sans', size=20)
    
    questionlbl = Label(question_screen, text=questions[row][col])
    questionlbl['font'] = myFont
    questionlbl.grid(row=0, column=1)

    global reveal_answer
    
    reveal_answer = Button(question_screen, text="Reveal Answer", command=lambda: show_answer(row, col))
    reveal_answer['font'] = myFont1
    reveal_answer.grid(row=1, column=1)
    
def show_answer(row, col):
    # Reveals answer
    # Answer List
    answers = [["Jim Carrey", "Mariah Carey", "Snowman.", "Seven", "Hockey"],
           ["Christmas with the Kranks", "1970", "Black Friday", "Resolution/s", "figure eight"],
           ["Charles Dickens", "Last Christmas", "Australia/Oceania", "Hanukkah", "Cross-country skiing"],
           ["Walter", "Simply having a wonderful Christmas time", "Snow cannon", "13th century", "snowshoeing"],
           ["The Father Christmas Letters", "A Green And Red Christmas - The Muppets", "240", "16th century", "1998"]]

    global question_screen
    global reveal_answer
    reveal_answer = Button(question_screen, text="Reveal Answer", state=DISABLED)   # Disables the button once answer is revealed

    global myFont
    global myFont1
    myFont3 = font.Font(family='Times', size=20)
    answerlbl = Label(question_screen, text=answers[row][col])
    answerlbl['font'] = myFont
    answerlbl.grid(row=2, column=1)

    # Asks for user to choose which team won
    winner_question = Label(question_screen, text="Which team gets the points?")
    winner_question['font'] = myFont3
    winner_question.grid(row=3, column=1)

    # Team buttons
    team1_btn = Button(question_screen, text="Team 1", padx=20, pady=20, command=lambda: points(1, row, col))
    team2_btn = Button(question_screen, text="Team 2", padx=20, pady=20, command=lambda: points(2, row, col))

    team1_btn['font'] = myFont1
    team2_btn['font'] = myFont1

    team1_btn.grid(row=4, column=0)
    team2_btn.grid(row=4, column=2)

def points(team, row, col):
    global team1_score
    global team2_score

    # Create score board
    score = []

    for i in range(5):
        new = []
        score.append(new)

    for r in range(5):
        for c in range(5):
            score[row].append(r+1)

    # Awards points accordingly
    if team == 1:
        team1_score += score[row][col]
    elif team == 2:
        team2_score += score[row][col]

    return_board(row, col)

def return_board(row, col):
    # Returns question board and disables question answered
    global question_screen
    global button_list
    global top
    global posx
    global posy
    question_screen.withdraw()
    top.deiconify()

    if row == 0:
        button_list[row][col] = Button(top, state=DISABLED, padx=58, pady=27, text="1 ORNAMENT").place(x=posx, y=posy)
    else:
        button_list[row][col] = Button(top, state=DISABLED, padx=56, pady=27, text = str(row+1)+ " ORNAMENTS").place(x=posx, y=posy)

def frames():
    global top
    # Frames
    frame1 = LabelFrame(top, text = "Team 1", padx=10, pady=10)  # Inside
    frame1.grid(row=0, column=6, padx=10, pady=10)  # Outside
    frame2 = LabelFrame(top, text = "Team 2", padx=10, pady=10)  # Inside
    frame2.grid(row=1, column=6, padx=10, pady=10)  # Outside

    # Placing image of tree
    global tree_img
    tree_img = ImageTk.PhotoImage(Image.open("Tree/1i.png"))
    tree1 = Label(frame1, image=tree_img).grid(row=0, column=0)
    tree2 = Label(frame2, image=tree_img).grid(row=0, column=0)

def image_replacement():
    my_img1 = ImageTk.PhotoImage(Image.open("Tree/2i.png"))
    my_img2 = ImageTk.PhotoImage(Image.open("Tree/3i.png"))
    my_img3 = ImageTk.PhotoImage(Image.open("Tree/4i.png"))
    my_img4 = ImageTk.PhotoImage(Image.open("Tree/5i.png"))
    my_img5 = ImageTk.PhotoImage(Image.open("Tree/6i.png"))
    my_img6 = ImageTk.PhotoImage(Image.open("Tree/7i.png"))

    # Image list exluding starting image
    image_list = [my_img1, my_img2, my_img3, my_img4, my_img5, my_img6]


# Start Screen Background
start_screenimg = ImageTk.PhotoImage(Image.open("Backgrounds/StartScreen.png"))
start_bg = Label(image=start_screenimg).grid(row=0, column=0, rowspan=2, columnspan=2)

# Start screen buttons
start_button = Button(root, text="START", padx=100, pady=50, command=start_game).grid(row=0, column=1)
instructions_button = Button(root, text="INSTRUCTIONS", padx=100, pady=50, command=open_instructions).grid(row=1, column=1)



mainloop()
