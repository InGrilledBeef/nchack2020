# Date: 2020-12-29
# Authors: Ingrid and Nusha
# Purpose: Winter themed Jeopardy game for the 2020 NCHACK hackathon

from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as font

# Settings
# Start Window
root = Tk()
root.title("Winter Jeopardy")
root.resizable(False, False)
root.iconbitmap("WJ.ico")

# Game Window
top = Toplevel()
top.withdraw()
top.resizable(False, False)
top.iconbitmap("WJ.ico")

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
    instructions.iconbitmap("WJ.ico")
    root.withdraw()
    instructionslbl = Label(instructions, text="To enter the Jeopardy game, press the “start” button. Organize players into Team 1 and Team 2; \nteams are recommended, but not limited to be between 1-10 players each.\nTo win, one team must collect at least 30 ornaments on their tree before the other. \nTeams obtain ornaments by alternately pressing the button to a corresponding winter topic and an ornament quantity, \nresponding with the appropriate question to the answer revealed. \n(Response must be given in question format, ex. “What is Tennis?” NOT “Tennis”.) \nIf a team is unable to decide on a response, or the response is incorrect, the opposing team claims their points. \nA volunteer host player may press a team’s button to distribute points accordingly. \nAs you descend the table, the ornament value increases, but so does the trivia difficulty; choose wisely! \nYou will know your team has won when the end screen appears, congratulating the winning team. \nThis Winter Jeopardy is a great outlet to enjoy a virtual challenge with your friends on a cold day. \nGrab your hot chocolate, and get ready for a festive race!")
    instructionslbl.pack()
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
    image_replacement(0, 0)
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
    questions = [["Actor who played Grinch in the 2000 hit: How the Grinch Stole Christmas.",
              "This artist makes $2m a year from her hit christmas song.",
              "Using three snowballs and decorations, this figure can be made outdoors.",
              "The number of days of Kwanzaa.",
              "A Canadian Winter sport."],
             ["A movie: a couple who plans to go on vacation for Christmas rush to organize a party\nwhen they discover their daughter is coming home for the holidays.",
              "The year the song Jingle Bell Rock was originally published (ending in 0).",
              "The more popular date for gift purchasing between: Black Friday or Cyber Monday.",
              "Name of goals set in place by individuals for the New Year’s.",
              "A turn in figure skating that resembles an infinity sign."],
             ["The author of A Christmas Carol.",
              "George Micheal (Wham!) sang this song in 1985.",
              "The continent best known for celebrating Christmas in the warm.",
              "Winter Holiday also known as “the Festival of Lights”.",
              "The form of skiing where skiers travel across a flat surface."],
             ["Buddy the Elf’s father’s first name in Elf.",
              "The final lyric:\n\nThe party's on\nThe feelin's here\nThat only comes\nThis time of year\n………………",
              "This device is used to create artificial snow.",
              "The century in which caroling became a Christmas tradition.",
              "This sport uses the force of Flotation."],
             ["This set of letters was written by the same author behind The Lord of The Rings.",
              "This movie’s Christmas soundtrack won Best Musical Album for Children\nat the 50th Grammy Awards.",
              "During Hibernation, bears can go this many days without food and water (multiple of 10).",
              "The century in which the term X-mas was invented.",
              "Snowboarding was first introduced in this year’s Winter Olympics."]]

    global posx
    global posy
    posx = x
    posy = y

    # New screen
    global question_screen
    question_screen = Toplevel()
    question_screen.resizable(False, False)
    question_screen.iconbitmap("WJ.ico")
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
    answers = [["Who is Jim Carrey?", "Who is Mariah Carey?", "What is a Snowman?", "What is 7?", "What is Hockey?"],
           ["What is Christmas with the Kranks?", "When is 1970?", "What is Black Friday?", "What are resolutions?", "What is a figure eight?"],
           ["Who is Charles Dickens?", "What is Last Christmas?", "What is Australia/Oceania?", "What is Hanukkah?", "What is Cross-country skiing?"],
           ["Who is Walter?", "What is Simply having a wonderful Christmas time?", "What is a Snow cannon?", "When is the 13th century?", "What is snowshoeing?"],
           ["What are the Father Christmas Letters?", "What is A Green And Red Christmas - The Muppets?", "What is 240?", "When is the 16th century?", "When is 1998?"]]

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
            score[r].append(r+1)

    # Awards points accordingly
    if team == 1:
        team1_score += score[row][col]
    elif team == 2:
        team2_score += score[row][col]

    image_replacement(team1_score, team2_score)
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


def image_replacement(score1, score2):
    global top
    # Frames
    frame1 = LabelFrame(top, text = "Team 1", padx=10, pady=10)  # Inside
    frame1.grid(row=0, column=6, padx=10, pady=10)  # Outside
    frame2 = LabelFrame(top, text = "Team 2", padx=10, pady=10)  # Inside
    frame2.grid(row=1, column=6, padx=10, pady=10)  # Outside

    global tree_img
    global my_img1
    global my_img2
    global my_img3
    global my_img4
    global my_img5
    global my_img6
    global my_img7
    global my_img8
    global my_img9
    global my_img10
    global my_img11
    global my_img12
    global my_img13
    global my_img14
    global my_img15
    global my_img16
    global my_img17
    global my_img18
    global my_img19
    global my_img20
    global my_img21
    global my_img22
    global my_img23
    global my_img24
    global my_img25
    global my_img26
    global my_img27
    global my_img28
    global my_img29
    global my_img30


    tree_img = ImageTk.PhotoImage(Image.open("Tree/1i.png"))
    my_img1 = ImageTk.PhotoImage(Image.open("Tree/2i.png"))
    my_img2 = ImageTk.PhotoImage(Image.open("Tree/3i.png"))
    my_img3 = ImageTk.PhotoImage(Image.open("Tree/4i.png"))
    my_img4 = ImageTk.PhotoImage(Image.open("Tree/5i.png"))
    my_img5 = ImageTk.PhotoImage(Image.open("Tree/6i.png"))
    my_img6 = ImageTk.PhotoImage(Image.open("Tree/7i.png"))
    my_img7 = ImageTk.PhotoImage(Image.open("Tree/8i.png"))
    my_img8 = ImageTk.PhotoImage(Image.open("Tree/9i.png"))
    my_img9 = ImageTk.PhotoImage(Image.open("Tree/10i.png"))
    my_img10 = ImageTk.PhotoImage(Image.open("Tree/11i.png"))
    my_img11 = ImageTk.PhotoImage(Image.open("Tree/12i.png"))
    my_img12 = ImageTk.PhotoImage(Image.open("Tree/13i.png"))
    my_img13 = ImageTk.PhotoImage(Image.open("Tree/14i.png"))
    my_img14 = ImageTk.PhotoImage(Image.open("Tree/15i.png"))
    my_img15 = ImageTk.PhotoImage(Image.open("Tree/16i.png"))
    my_img16 = ImageTk.PhotoImage(Image.open("Tree/17i.png"))
    my_img17 = ImageTk.PhotoImage(Image.open("Tree/18i.png"))
    my_img18 = ImageTk.PhotoImage(Image.open("Tree/19i.png"))
    my_img19 = ImageTk.PhotoImage(Image.open("Tree/20i.png"))
    my_img20 = ImageTk.PhotoImage(Image.open("Tree/21i.png"))
    my_img21 = ImageTk.PhotoImage(Image.open("Tree/22i.png"))
    my_img22 = ImageTk.PhotoImage(Image.open("Tree/23i.png"))
    my_img23 = ImageTk.PhotoImage(Image.open("Tree/24i.png"))
    my_img24 = ImageTk.PhotoImage(Image.open("Tree/25i.png"))
    my_img25 = ImageTk.PhotoImage(Image.open("Tree/26i.png"))
    my_img26 = ImageTk.PhotoImage(Image.open("Tree/27i.png"))
    my_img27 = ImageTk.PhotoImage(Image.open("Tree/28i.png"))
    my_img28 = ImageTk.PhotoImage(Image.open("Tree/29i.png"))
    my_img29 = ImageTk.PhotoImage(Image.open("Tree/30i.png"))
    my_img30 = ImageTk.PhotoImage(Image.open("Tree/31i.png"))

    # Image list
    image_list = [tree_img, my_img1, my_img2, my_img3, my_img4, my_img5, my_img6, my_img7, my_img8, my_img9, my_img10, my_img11, my_img12,
                  my_img13, my_img14, my_img15, my_img16, my_img17, my_img18, my_img19, my_img20, my_img21, my_img22, my_img23,
                  my_img24, my_img25, my_img26, my_img27, my_img28, my_img29, my_img30]

    tree1 = Label(frame1, image=tree_img)
    tree2 = Label(frame2, image=tree_img)

    # Placing image of tree
    if score1 == 0 and score2 == 0:
        tree1.grid(row=0, column=0)
        tree2.grid(row=0, column=0)

    # If a team's score is greater than 30, they win
    if score1 >= 30 or score2 >= 30:
        if score1 > score2:
            win(1, score1, score2)
        else:
            win(2, score1, score2)
    else:
        tree1.grid_forget()
        tree2.grid_forget()
        tree1 = Label(frame1, image=image_list[score1])
        tree2 = Label(frame2, image=image_list[score2])
        tree1.grid(row=0, column=0)
        tree2.grid(row=0, column=0)

def win(team, score1, score2):
    # Closes main screen and opens winner screen
    global top
    top.destroy()
    winner_screen = Toplevel()
    winner_screen.resizable(False, False)
    winner_screen.iconbitmap("WJ.ico")

    # Winner images
    global winner1
    global winner2
    winner1 = ImageTk.PhotoImage(Image.open("Winners/Winner_1.png"))
    winner2 = ImageTk.PhotoImage(Image.open("Winners/Winner_2.png"))
    if team == 1:
        winner1lbl = Label(winner_screen, image=winner1).pack()
    else:
        winner2lbl = Label(winner_screen, image=winner2).pack()


# Start Screen Background
start_screenimg = ImageTk.PhotoImage(Image.open("Backgrounds/StartScreen.png"))
start_bg = Label(image=start_screenimg).grid(row=0, column=0, rowspan=2, columnspan=2)

# Start screen buttons
start_button = Button(root, text="START", padx=100, pady=50, command=start_game).grid(row=0, column=1)
instructions_button = Button(root, text="INSTRUCTIONS", padx=100, pady=50, command=open_instructions).grid(row=1, column=1)



mainloop()
