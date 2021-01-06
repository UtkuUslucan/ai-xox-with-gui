import tkinter.messagebox
import tkinter as tk
from tkinter import *
import random

root=tk.Tk()
root.title("Artificial Intelligence Tic-Tac-Toe")
root.geometry("700x500+650+250")
root.resizable(False,False)
root.configure(background='DimGrey')

player_x_turn = True
game_over = False
number_of_turns = 0
AI_mode = False
AI_level = 1

PlayerX=IntVar()
PlayerO=IntVar()

PlayerX.set(0)
PlayerO.set(0)

def number_empty():
    btnList = [button1, button2, button3, button4, button5, button6, button7, button8, button9]
    empty = 0
    for button in btnList:
        if button["text"] == " ":
            empty += 1
    return empty




def block_x():
    if (button1["text"] == " ") and (button2["text"] == "X") and (button3["text"] == "X"):
        place_mark(button1)
    elif (button1["text"] == "X") and (button2["text"] == " ") and (button3["text"] == "X"):
        place_mark(button2)
    elif (button1["text"] == "X") and (button2["text"] == "X") and (button3["text"] == " "):
        place_mark(button3)

    elif (button4["text"] == " ") and (button5["text"] == "X") and (button6["text"] == "X"):
        place_mark(button4)
    elif (button5["text"] == " ") and (button4["text"] == "X") and (button3["text"] == "X"):
        place_mark(button5)
    elif (button6["text"] == " ") and (button4["text"] == "X") and (button5["text"] == "X"):
        place_mark(button6)

    elif (button7["text"] == " ") and (button8["text"] == "X") and (button9["text"] == "X"):
        place_mark(button7)
    elif (button8["text"] == " ") and (button7["text"] == "X") and (button9["text"] == "X"):
        place_mark(button8)
    elif (button9["text"] == " ") and (button7["text"] == "X") and (button8["text"] == "X"):
        place_mark(button9)

    elif (button1["text"] == " ") and (button4["text"] == "X") and (button7["text"] == "X"):
        place_mark(button1)
    elif (button4["text"] == " ") and (button1["text"] == "X") and (button7["text"] == "X"):
        place_mark(button4)
    elif (button7["text"] == " ") and (button1["text"] == "X") and (button4["text"] == "X"):
        place_mark(button7)

    elif (button2["text"] == " ") and (button5["text"] == "X") and (button8["text"] == "X"):
        place_mark(button2)
    elif (button5["text"] == " ") and (button2["text"] == "X") and (button8["text"] == "X"):
        place_mark(button5)
    elif (button8["text"] == " ") and (button2["text"] == "X") and (button5["text"] == "X"):
        place_mark(button8)

    elif (button3["text"] == " ") and (button6["text"] == "X") and (button9["text"] == "X"):
        place_mark(button3)
    elif (button6["text"] == " ") and (button3["text"] == "X") and (button9["text"] == "X"):
        place_mark(button6)
    elif (button9["text"] == " ") and (button3["text"] == "X") and (button6["text"] == "X"):
        place_mark(button9)

    elif (button1["text"] == " ") and (button5["text"] == "X") and (button9["text"] == "X"):
        place_mark(button1)
    elif (button5["text"] == " ") and (button1["text"] == "X") and (button9["text"] == "X"):
        place_mark(button5)
    elif (button9["text"] == " ") and (button1["text"] == "X") and (button5["text"] == "X"):
        place_mark(button9)
    
    elif (button3["text"] == " ") and (button5["text"] == "X") and (button7["text"] == "X"):
        place_mark(button3)
    elif (button5["text"] == " ") and (button3["text"] == "X") and (button7["text"] == "X"):
        place_mark(button5)
    elif (button7["text"] == " ") and (button3["text"] == "X") and (button5["text"] == "X"):
        place_mark(button7)
    else:
        place_in_empty_space(random.randint(1, number_empty()))
        
def place_O_to_win():
    if (button1["text"] == " ") and (button2["text"] == "O") and (button3["text"] == "O"):
        place_mark(button1)
    elif (button1["text"] == "O") and (button2["text"] == " ") and (button3["text"] == "O"):
        place_mark(button2)
    elif (button1["text"] == "O") and (button2["text"] == "O") and (button3["text"] == " "):
        place_mark(button3)

    elif (button4["text"] == " ") and (button5["text"] == "O") and (button6["text"] == "O"):
        place_mark(button4)
    elif (button5["text"] == " ") and (button4["text"] == "O") and (button3["text"] == "O"):
        place_mark(button5)
    elif (button6["text"] == " ") and (button4["text"] == "O") and (button5["text"] == "O"):
        place_mark(button6)

    elif (button7["text"] == " ") and (button8["text"] == "O") and (button9["text"] == "O"):
        place_mark(button7)
    elif (button8["text"] == " ") and (button7["text"] == "O") and (button9["text"] == "O"):
        place_mark(button8)
    elif (button9["text"] == " ") and (button7["text"] == "O") and (button8["text"] == "O"):
        place_mark(button9)

    elif (button1["text"] == " ") and (button4["text"] == "O") and (button7["text"] == "O"):
        place_mark(button1)
    elif (button4["text"] == " ") and (button1["text"] == "O") and (button7["text"] == "O"):
        place_mark(button4)
    elif (button7["text"] == " ") and (button1["text"] == "O") and (button4["text"] == "O"):
        place_mark(button7)

    elif (button2["text"] == " ") and (button5["text"] == "O") and (button8["text"] == "O"):
        place_mark(button2)
    elif (button5["text"] == " ") and (button2["text"] == "O") and (button8["text"] == "O"):
        place_mark(button5)
    elif (button8["text"] == " ") and (button2["text"] == "O") and (button5["text"] == "O"):
        place_mark(button8)

    elif (button3["text"] == " ") and (button6["text"] == "O") and (button9["text"] == "O"):
        place_mark(button3)
    elif (button6["text"] == " ") and (button3["text"] == "O") and (button9["text"] == "O"):
        place_mark(button6)
    elif (button9["text"] == " ") and (button3["text"] == "O") and (button6["text"] == "O"):
        place_mark(button9)

    elif (button1["text"] == " ") and (button5["text"] == "O") and (button9["text"] == "O"):
        place_mark(button1)
    elif (button5["text"] == " ") and (button1["text"] == "O") and (button9["text"] == "O"):
        place_mark(button5)
    elif (button9["text"] == " ") and (button1["text"] == "O") and (button5["text"] == "O"):
        place_mark(button9)
    
    elif (button3["text"] == " ") and (button5["text"] == "O") and (button7["text"] == "O"):
        place_mark(button3)
    elif (button5["text"] == " ") and (button3["text"] == "O") and (button7["text"] == "O"):
        place_mark(button5)
    elif (button7["text"] == " ") and (button3["text"] == "O") and (button5["text"] == "O"):
        place_mark(button7)
    

def AI():
    global AI_level, game_over
    if number_empty() == 8:
        if button5["text"] == " ":
            place_mark(button5)
        else:
            place_mark(button1)
    elif AI_level == 1:
        place_in_empty_space(random.randint(1, number_empty()))
    elif AI_level == 2:
        block_x()
    elif AI_level == 3:
        place_O_to_win()
        check_win()
        if not game_over:
            block_x()



def place_in_empty_space(number):
    empty_space = 0
    btn = [button1, button2, button3, button4, button5, button6, button7, button8, button9]
    for myButton in btn:  
        if myButton["text"] == " ":
            empty_space +=1
            if empty_space == number:
                print(empty_space)
                place_mark(myButton)

def simple_AI():
    global AI_mode, AI_level
    AI_mode = True
    AI_level = 1
    #tkinter.messagebox.showinfo("Playing AI!", "You'r playing with Simple AI")
    statusTxt['text'] = "Player\nVS\nSimple AI"
    lblPlayerO['text'] = "COMPUTER"
    lblPlayerX['text'] = "PLAYER"
    lblPlayerO['font'] = ('Arial',18,'bold')
    lblPlayerX['width'] = "8"
    lblPlayerO['width'] = "9"
    lblPlayerO['height'] = "1"
    statusTxt['padx'] = "34"


def medium_AI():
    global AI_mode, AI_level
    AI_mode = True
    AI_level = 2
    #tkinter.messagebox.showinfo("Playing AI!", "You'r playing with Medium AI")
    statusTxt['text'] = "Player\nVS\nMedium AI"
    lblPlayerO['text'] = "COMPUTER"
    lblPlayerX['text'] = "PLAYER"
    lblPlayerO['font'] = ('Arial',18,'bold')
    lblPlayerX['width'] = "8"
    lblPlayerO['width'] = "9"
    lblPlayerO['height'] = "1"
    statusTxt['padx'] = "28"

def hard_AI():
    global AI_mode, AI_level
    AI_mode = True
    AI_level = 3
    #tkinter.messagebox.showinfo("Playing AI!", "You'r playing with Hard AI")
    statusTxt['text'] = "Player\nVS\nHard AI"
    lblPlayerO['text'] = "COMPUTER"
    lblPlayerX['text'] = "PLAYER"
    lblPlayerO['font'] = ('Arial',18,'bold')
    lblPlayerX['width'] = "8"
    lblPlayerO['width'] = "9"
    lblPlayerO['height'] = "1"
    statusTxt['padx'] = "48"

def AI_off():
    global AI_mode
    AI_mode = False
    #tkinter.messagebox.showinfo("Player VS Player", "AI is off.")
    statusTxt['text'] = "Player\nVS\nPlayer"
    lblPlayerX['text'] = "PLAYER X"
    lblPlayerO['text'] = "PLAYER O"
    lblPlayerO['font'] = ('Arial',20,'bold')
    lblPlayerO['width'] = "8"
    statusTxt['padx'] = "56"

def place_mark(button):
    global player_x_turn, AI_mode, game_over
    if player_x_turn:
        button["text"] = "X"
        player_x_turn = False
    else:
        button["text"] = "O"
        player_x_turn = True
    button["state"] = DISABLED
    check_win()
    if AI_mode and not game_over and not player_x_turn:
        AI()



def enable_buttons():
    button1['state'] = NORMAL
    button2['state'] = NORMAL
    button3['state'] = NORMAL
    button4['state'] = NORMAL
    button5['state'] = NORMAL
    button6['state'] = NORMAL
    button7['state'] = NORMAL
    button8['state'] = NORMAL
    button9['state'] = NORMAL
def disable_buttons():
    button1['state'] = DISABLED
    button2['state'] = DISABLED
    button3['state'] = DISABLED
    button4['state'] = DISABLED
    button5['state'] = DISABLED
    button6['state'] = DISABLED
    button7['state'] = DISABLED
    button8['state'] = DISABLED
    button9['state'] = DISABLED

def check_win():
    if(button1["text"]== "X" and button2["text"]== "X" and button3["text"]== "X"):
        button1.configure(background ="powder blue")
        button2.configure(background ="powder blue")
        button3.configure(background ="powder blue")
        n = int(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "Winner X\nYou have just won a game")
        reset_game()
    if(button4["text"]== "X" and button5["text"]== "X" and button6["text"]== "X"):
        button4.configure(background ="powder blue")
        button5.configure(background ="powder blue")
        button6.configure(background ="powder blue")
        n = int(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "Winner X\nYou have just won a game")
        reset_game()
    if(button7["text"]== "X" and button8["text"]== "X" and button9["text"]== "X"):
        button7.configure(background ="powder blue")
        button8.configure(background ="powder blue")
        button9.configure(background ="powder blue")
        n = int(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "Winner X\nYou have just won a game")
        reset_game()
    if(button1["text"]== "X" and button5["text"]== "X" and button9["text"]== "X"):
        button1.configure(background ="powder blue")
        button5.configure(background ="powder blue")
        button9.configure(background ="powder blue")
        n = int(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "Winner X\nYou have just won a game")
        reset_game()
    if(button3["text"]== "X" and button5["text"]== "X" and button7["text"]== "X"):
        button3.configure(background ="powder blue")
        button5.configure(background ="powder blue")
        button7.configure(background ="powder blue")
        n = int(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "Winner X\nYou have just won a game")
        reset_game()
    if(button1["text"]== "X" and button4["text"]== "X" and button7["text"]== "X"):
        button1.configure(background ="powder blue")
        button4.configure(background ="powder blue")
        button7.configure(background ="powder blue")
        n = int(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "Winner X\nYou have just won a game")
        reset_game()
    if(button2["text"]== "X" and button5["text"]== "X" and button8["text"]== "X"):
        button2.configure(background ="powder blue")
        button5.configure(background ="powder blue")
        button8.configure(background ="powder blue")
        n = int(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "Winner X\nYou have just won a game")
        reset_game()
    if(button3["text"]== "X" and button6["text"]== "X" and button9["text"]== "X"):
        button3.configure(background ="powder blue")
        button6.configure(background ="powder blue")
        button9.configure(background ="powder blue")
        n = int(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "Winner X\nYou have just won a game")
        reset_game()
    if(button1["text"]== "O" and button2["text"]== "O" and button3["text"]== "O"):
        button1.configure(background ="powder blue")
        button2.configure(background ="powder blue")
        button3.configure(background ="powder blue")
        n = int(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "Winner O\nYou have just won a game")
        reset_game()
    if(button4["text"]== "O" and button5["text"]== "O" and button6["text"]== "O"):
        button4.configure(background ="powder blue")
        button5.configure(background ="powder blue")
        button6.configure(background ="powder blue")
        n = int(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "Winner O\nYou have just won a game")
        reset_game()
    if(button7["text"]== "O" and button8["text"]== "O" and button9["text"]== "O"):
        button7.configure(background ="powder blue")
        button8.configure(background ="powder blue")
        button9.configure(background ="powder blue")
        n = int(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "Winner O\nYou have just won a game")
        reset_game()
    if(button1["text"]== "O" and button5["text"]== "O" and button9["text"]== "O"):
        button1.configure(background ="powder blue")
        button5.configure(background ="powder blue")
        button9.configure(background ="powder blue")
        n = int(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "Winner O\nYou have just won a game")
        reset_game()
    if(button3["text"]== "O" and button5["text"]== "O" and button7["text"]== "O"):
        button3.configure(background ="powder blue")
        button5.configure(background ="powder blue")
        button7.configure(background ="powder blue")
        n = int(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "Winner O\nYou have just won a game")
        reset_game()
    if(button1["text"]== "O" and button4["text"]== "O" and button7["text"]== "O"):
        button1.configure(background ="powder blue")
        button4.configure(background ="powder blue")
        button7.configure(background ="powder blue")
        n = int(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "Winner O\nYou have just won a game")
        reset_game()
    if(button2["text"]== "O" and button5["text"]== "O" and button8["text"]== "O"):
        button2.configure(background ="powder blue")
        button5.configure(background ="powder blue")
        button8.configure(background ="powder blue")
        n = int(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "Winner O\nYou have just won a game")
        reset_game()
    if(button3["text"]== "O" and button6["text"]== "O" and button9["text"]== "O"):
        button3.configure(background ="powder blue")
        button6.configure(background ="powder blue")
        button9.configure(background ="powder blue")
        n = int(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "Winner O\nYou have just won a game")
        reset_game()
    else:
        tie_checker()

def reset_globals():
    global player_x_turn, game_over, number_of_turns
    player_x_turn = True
    game_over = False
    number_of_turns = 0

def reset_background_color():
    button1.configure(background ="gainsboro")
    button2.configure(background ="gainsboro")
    button3.configure(background ="gainsboro")
    button4.configure(background ="gainsboro")
    button5.configure(background ="gainsboro")
    button6.configure(background ="gainsboro")
    button7.configure(background ="gainsboro")
    button8.configure(background ="gainsboro")
    button9.configure(background ="gainsboro")

def reset_text():
    button1['text']= " "
    button2['text']= " "
    button3['text']= " "
    button4['text']= " "
    button5['text']= " "
    button6['text']= " "
    button7['text']= " "
    button8['text']= " "
    button9['text']= " "

def reset_game():
    enable_buttons()
    reset_background_color()
    reset_text()
    reset_globals()

def NewGame():
    reset_game()
    PlayerX.set(0)
    PlayerO.set(0)

def exit():
    global root
    yes = tkinter.messagebox.askyesno("Exit","Do you want to exit?")
    if yes:
        root.quit()
    else:
        pass

def htp():
    tkinter.messagebox.showinfo("How to play?","RULES FOR TIC-TAC-TOE\n\n1- The game is played on a grid that's 3 squares by 3 squares\n2- You are X, your friend(or the computer in this case) is O. Players take turns putting their marks in empty squares.\n3- The first player to get 3 of her marks in a row (up, down, across or diagonally) is the winner.\n4- When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.\n\nHOW CAN I WIN AT TIC-TAC-TOE?\n\nTo beat the computer(or at least tie), you need to make use of a little bit of strategy. Strategy means figuring out what you need to do to win.\nPart of your strategy is trying to figure out how to get three X's in a row. The other parts is trying to figure out how to stop the computer from getting three O's in a row.\nAfter you put an X in a square, you start looking ahead. Where's the best place for your next X? You look at the empty squares and decide which ones are good choices--which ones might let you make three X's in a row.\nYou also hova to watch where the computer puts its O. That could change what you do next. If the computer gets two Os in a row, you have to put your next X in the last empty square in that row, or the computer will win. You are forced to play in a particular square or lose the game.\nIf you always pay attention and look ahead, you'll never lose a game of Tic-Tac-Toe. You may not win, but at least you'll tie.")
def about():
    tkinter.messagebox.showinfo("About","Game Source Code:\nYoutube: Greg Poy\nGui Source Code:\nİbrahim Utku Uslucan")
def work():
    tkinter.messagebox.showinfo("How it work?","This Simple AI workings is random module")

def tie_checker():
    if (button1["text"] != ' ' and button2["text"] != ' ' and button3["text"] != ' ' and button4["text"] != ' ' and button5["text"] != ' ' and button6["text"] != ' ' and button7["text"] != ' ' and button8["text"] != ' ' and button9["text"] != ' '):
        button1.configure(background ="indianred")
        button2.configure(background ="indianred")
        button3.configure(background ="indianred")
        button4.configure(background ="indianred")
        button5.configure(background ="indianred")
        button6.configure(background ="indianred")
        button7.configure(background ="indianred")
        button8.configure(background ="indianred")
        button9.configure(background ="indianred")
        tkinter.messagebox.showinfo("Game is tie!", "Game is tie!")
        reset_game()



Tops = Frame(root, bg = 'DimGrey', pady = 2, width=700, height= 100, relief =RIDGE)
Tops.grid(row=0, column=0)

lblTitle = Label(Tops,font=('Arial',20,'bold'), text="Artificial Intelligence Tic-Tac-Toe", bd=21, bg='DimGrey', fg='Cornsilk', justify=CENTER)
lblTitle.grid(row=0,column=0)

MainFrame = Frame(root, bg = 'DimGrey', pady = 2, width=500, height= 700, relief =RIDGE)
MainFrame.grid(row=1, column=0)

RightFrame = Frame(root, bg = 'DarkGrey', pady = 2, relief= FLAT)
RightFrame.place(height=70, width=200, x=500)

buttonFrame = Frame(root,bg = 'DarkGrey', pady = 2, relief= FLAT)
buttonFrame.place(height=540, width=200, x=500, y=180)

statusFrame = Frame(root,bg= 'DimGrey', pady = 2, padx = 2, relief= FLAT)
statusFrame.place(height=120, width=200, x=500,y=80)

BottomFrame = Frame(root, bg = 'DarkGrey', pady = 2, width=200, height= 500, relief= FLAT)
BottomFrame.place(height=200, width=500,y=440)

bottomText = Label(BottomFrame, font=('Arial',20,'bold'), text="İbrahim Utku USLUCAN",bg='DarkGrey', fg='black',justify=CENTER)
bottomText.pack()
bottomText2 = Label(BottomFrame, font=('Arial',10,'bold'), text="utkuuslucan.com",bg='DarkGrey', fg='black',justify=CENTER)
bottomText2.pack()

lblPlayerX = Label(RightFrame, font=('Arial',21,'bold'), text="PLAYER X",padx=2,pady=2, bg='Khaki', relief=FLAT,bd=0,height=1,width=8, justify= LEFT)
lblPlayerX.grid(row=0,column=0)
scorePlayerX = Entry(RightFrame, font=('Arial',20,'bold'), bd=1, fg="black", textvariable= PlayerX, width=6, justify=LEFT,state=DISABLED).grid(row=0,column=1)


lblPlayerO = Label(RightFrame, font=('Arial',20,'bold'), text="PLAYER O",padx=2,pady=2, bg='DarkKhaki', relief=FLAT,bd=0,height=1,width=8)
lblPlayerO.grid(row=1,column=0)
scorePlayerO = Entry(RightFrame, font=('Arial',20,'bold'), bd=1, fg="black", textvariable= PlayerO, width=6, justify=LEFT,state=DISABLED).grid(row=1,column=1)

btnNewGame = Button(buttonFrame, text="New Game",font=('Times 18 bold'), height=1, width=8, bg='gainsboro',bd=1, command=NewGame)
btnNewGame.grid(row=1,columnspan=2,pady=42,padx=45)
btnReset = Button(buttonFrame, text="Reset", font=('Times 18 bold'), height=1, width=8, bg='gainsboro',bd=1, command=reset_game)
btnReset.grid(row=2,columnspan=2)
btnExit = Button(buttonFrame, text="Exit", font=('Times 18 bold'), height=1,width=8, bg='gainsboro', bd=1, command=exit)
btnExit.grid(row=3,columnspan=2,pady=42)

statusTxt = Label(statusFrame, font=('Arial',20,'bold'), text="Player\nVS\nPlayer",bg="DimGrey", fg='Cornsilk',justify=CENTER,padx=56,pady=1)
statusTxt.grid(row=0,column=0)

button1 = Button(MainFrame, text=" ", font=('Times 26 bold'), height = 2, width=6, bg='gainsboro', command=lambda:place_mark(button1))
button1.grid(row=1,column=0, sticky = S+N+E+W)

button2 = Button(MainFrame, text=" ", font=('Times 26 bold'), height = 2, width=6, bg='gainsboro', command=lambda:place_mark(button2))
button2.grid(row=1,column=1, sticky = S+N+E+W)

button3 = Button(MainFrame, text=" ", font=('Times 26 bold'), height = 2, width=6, bg='gainsboro', command=lambda:place_mark(button3))
button3.grid(row=1,column=2, sticky = S+N+E+W)

button4 = Button(MainFrame, text=" ", font=('Times 26 bold'), height = 2, width=6, bg='gainsboro', command=lambda:place_mark(button4))
button4.grid(row=2,column=0, sticky = S+N+E+W)

button5 = Button(MainFrame, text=" ", font=('Times 26 bold'), height = 2, width=6, bg='gainsboro', command=lambda:place_mark(button5))
button5.grid(row=2,column=1, sticky = S+N+E+W)

button6 = Button(MainFrame, text=" ", font=('Times 26 bold'), height = 2, width=6, bg='gainsboro', command=lambda:place_mark(button6))
button6.grid(row=2,column=2, sticky = S+N+E+W)

button7 = Button(MainFrame, text=" ", font=('Times 26 bold'), height = 2, width=6, bg='gainsboro', command=lambda:place_mark(button7))
button7.grid(row=3,column=0, sticky = S+N+E+W)

button8 = Button(MainFrame, text=" ", font=('Times 26 bold'), height = 2, width=6, bg='gainsboro', command=lambda:place_mark(button8))
button8.grid(row=3,column=1, sticky = S+N+E+W)

button9 = Button(MainFrame, text=" ", font=('Times 26 bold'), height = 2, width=6, bg='gainsboro', command=lambda:place_mark(button9))
button9.grid(row=3,column=2, sticky = S+N+E+W)

menubar = Menu(root)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label = "How to play?", command=htp)
helpmenu.add_command(label = "How it work?", command=work)
helpmenu.add_separator()
helpmenu.add_command(label = "About", command=about)
menubar.add_cascade(label = "Help", menu = helpmenu)
AI_menu = Menu(menubar, tearoff=0)
AI_menu.add_command(label = "Simple AI", command=simple_AI)
AI_menu.add_command(label = "Medium AI", command=medium_AI)
AI_menu.add_command(label = "Hard AI", command=hard_AI)
AI_menu.add_separator()
AI_menu.add_command(label = "Turn Off AI", command=AI_off)
menubar.add_cascade(label = "AI", menu = AI_menu)
root.config(menu = menubar)

root.mainloop()
