# --- MODULES --- #
from tkinter import *
import random
import Homescreen

# --- FUNCTIONS --- #
def btn_clicked(window):
    '''closes tictactoe, opens homescreen'''
    window.destroy()
    Homescreen.homescreen()

def back(window):
    '''closes current game, opens main menu'''
    window.destroy()
    main_menu()

def buttons_disable(button_list):
    '''disables the 3x3 buttons for tictactoe'''
    for x in button_list:
        x.configure(state=DISABLED)

def restart(button_list, player_X,player_O, img_list):                             
    '''restarts game data'''
    for x in range(len(button_list)):
        button_list[x].configure(image= img_list[x], state=NORMAL)
    player_X.clear()
    player_O.clear()
    if (score_X>=3) or (score_O>=3) or total>=9:
        new.destroy()

def main_menu():
    '''first to launch from home screen. this is where game mode will be chosen'''

    # --- MAIN & GUI --- #
    window = Tk()
    window.geometry("480x720")
    window.configure(bg = "#ffffff")
    
    canvas = Canvas(
        window,
        bg = "#ffffff",
        height = 720,
        width = 480,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = "TicTacToe_assets\menu_background.png")
    background = canvas.create_image(
        240, 360,
        image=background_img)

    img0 = PhotoImage(file = "TicTacToe_assets/quit_menu_icon.png")
    quit_btn = Button(
        image = img0,
        borderwidth = 0,
        cursor = "hand2",
        activebackground = "#303030",
        highlightthickness = 0,
        command = lambda:btn_clicked(window),
        relief = "flat")

    quit_btn.place(
        x = 119, y = 476,
        width = 236,
        height = 94)

    img1 = PhotoImage(file = "TicTacToe_assets/m_player_icon.png")
    multi_btn = Button(
        image = img1,
        borderwidth = 0,
        cursor = "hand2",
        activebackground = "#303030",
        highlightthickness = 0,
        command = lambda:tictactoe(window,"Multiplayer"),
        relief = "flat")

    multi_btn.place(
        x = 119, y = 348,
        width = 236,
        height = 94)

    img2 = PhotoImage(file = "TicTacToe_assets/s_player_icon.png")
    single_btn = Button(
        image = img2,
        borderwidth = 0,
        cursor = "hand2",
        activebackground = "#303030",
        highlightthickness = 0,
        command = lambda:tictactoe(window,"Single Player"),
        relief = "flat")

    single_btn.place(
        x = 118, y = 222,
        width = 236,
        height = 94)

    # Launch Mainloop #
    window.resizable(False, False)
    window.mainloop()

def tictactoe(main, game_mode):
    '''tictactoe game proper'''

    # closes main menue
    main.destroy()

    # --- MAIN & GUI --- #
    window=Tk()

    window.geometry("480x720")
    window.configure(bg = "#ffffff")
    canvas = Canvas(
        window,
        bg = "#ffffff",
        height = 720,
        width = 480,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = "TicTacToe_assets/background.png")
    background = canvas.create_image(
        240, 360,
        image=background_img)

    img0 = PhotoImage(file = "TicTacToe_assets/img0.png")
    bottom_right = Button(
        image = img0,
        borderwidth = 0,
        cursor = "hand2",
        activebackground = "#BFDDD4",
        highlightthickness = 0,
        command = lambda:ButtonEffect(player_X,player_O,9,button_list,game_mode),
        relief = "flat")

    bottom_right.place(
        x = 303, y = 502,
        width = 127,
        height = 127)

    img1 = PhotoImage(file = "TicTacToe_assets/img1.png")
    center_tile = Button(
        image = img1,
        borderwidth = 0,
        cursor = "hand2",
        activebackground = "#BFDDD4",
        highlightthickness = 0,
        command = lambda:ButtonEffect(player_X,player_O,5,button_list,game_mode),
        relief = "flat")

    center_tile.place(
        x = 176.33, y = 375.33,
        width = 127,
        height = 127)

    img2 = PhotoImage(file = "TicTacToe_assets/img2.png")
    top_left = Button(
        image = img2,
        borderwidth = 0,
        cursor = "hand2",
        activebackground = "#BFDDD4",
        highlightthickness = 0,
        command = lambda:ButtonEffect(player_X,player_O,1,button_list,game_mode),
        relief = "flat")

    top_left.place(
        x = 49, y = 248,
        width = 127,
        height = 127)

    img3 = PhotoImage(file = "TicTacToe_assets/img3.png")
    bottom_left = Button(
        image = img3,
        borderwidth = 0,
        cursor = "hand2",
        activebackground = "#BFDDD4",
        highlightthickness = 0,
        command = lambda:ButtonEffect(player_X,player_O,7,button_list,game_mode),
        relief = "flat")

    bottom_left.place(
        x = 49, y = 502,
        width = 127,
        height = 127)

    img4 = PhotoImage(file = "TicTacToe_assets/img4.png")
    top_right = Button(
        image = img4,
        borderwidth = 0,
        cursor = "hand2",
        activebackground = "#BFDDD4",
        highlightthickness = 0,
        command = lambda:ButtonEffect(player_X,player_O,3,button_list,game_mode),
        relief = "flat")

    top_right.place(
        x = 303, y = 248,
        width = 127,
        height = 127)

    img5 = PhotoImage(file = "TicTacToe_assets/img5.png")
    right = Button(
        image = img5,
        borderwidth = 0,
        cursor = "hand2",
        activebackground = "#BFDDD4",
        highlightthickness = 0,
        command = lambda:ButtonEffect(player_X,player_O,6,button_list,game_mode),
        relief = "flat")

    right.place(
        x = 303, y = 375.33,
        width = 127,
        height = 127)

    img6 = PhotoImage(file = "TicTacToe_assets/img6.png")
    bottom = Button(
        image = img6,
        borderwidth = 0,
        cursor = "hand2",
        activebackground = "#BFDDD4",
        highlightthickness = 0,
        command = lambda:ButtonEffect(player_X,player_O,8,button_list,game_mode),
        relief = "flat")

    bottom.place(
        x = 176.33, y = 502,
        width = 127,
        height = 127)

    img7 = PhotoImage(file = "TicTacToe_assets/img7.png")
    left = Button(
        image = img7,
        borderwidth = 0,
        cursor = "hand2",
        activebackground = "#BFDDD4",
        highlightthickness = 0,
        command = lambda:ButtonEffect(player_X,player_O,4,button_list,game_mode),
        relief = "flat")

    left.place(
        x = 49, y = 375.33,
        width = 127,
        height = 127)

    img8 = PhotoImage(file = "TicTacToe_assets/img8.png")
    top = Button(
        image = img8,
        borderwidth = 0,
        cursor = "hand2",
        activebackground = "#BFDDD4",
        highlightthickness = 0,
        command = lambda:ButtonEffect(player_X,player_O,2,button_list,game_mode),
        relief = "flat")

    top.place(
        x = 176.33, y = 248,
        width = 127,
        height = 127)

    img9 = PhotoImage(file = "TicTacToe_assets/img9.png")
    restart_btn = Button(
        image = img9,
        borderwidth = 0,
        cursor = "hand2",
        activebackground = "#464242",
        highlightthickness = 0,
        command = lambda:restart(button_list,player_X,player_O,img_list),
        relief = "flat")

    restart_btn.place(
        x = 55, y = 74,
        width = 146,
        height = 60)

    img10 = PhotoImage(file = "TicTacToe_assets/img10.png")
    quit_btn = Button(
        image = img10,
        borderwidth = 0,
        cursor = "hand2",
        activebackground = "#464242",
        highlightthickness = 0,
        command = lambda:back(window),
        relief = "flat")

    quit_btn.place(
        x = 279, y = 74,
        width = 146,
        height = 60)
    button_list=[top_left,top,top_right,left,center_tile,right,bottom_left,bottom,bottom_right]
    img_list=[img2,img8,img4,img7,img1,img5,img3,img6,img0]
    
    # initialize move lists of players
    player_X=[]
    player_O=[]

    # Launch Mainloop #
    window.resizable(False, False)
    window.mainloop()

def ButtonEffect(player_X,player_O,position,button_list,game_mode):
    '''creates buttons for tictactoe game'''
    global total, img_X, img_O

    # --- BACKGROUNDS --- #
    img0_X = PhotoImage(file = "TicTacToe_assets/img0_X.png")
    img1_X = PhotoImage(file = "TicTacToe_assets/img1_X.png")
    img2_X = PhotoImage(file = "TicTacToe_assets/img2_X.png")
    img3_X = PhotoImage(file = "TicTacToe_assets/img3_X.png")
    img4_X = PhotoImage(file = "TicTacToe_assets/img4_X.png")
    img5_X = PhotoImage(file = "TicTacToe_assets/img5_X.png")
    img6_X = PhotoImage(file = "TicTacToe_assets/img6_X.png")
    img7_X = PhotoImage(file = "TicTacToe_assets/img7_X.png")
    img8_X = PhotoImage(file = "TicTacToe_assets/img8_X.png")
    img_X=[img2_X,img8_X,img4_X,img7_X,img1_X,img5_X,img3_X,img6_X,img0_X]

    img0_O = PhotoImage(file = "TicTacToe_assets/img0_O.png")
    img1_O = PhotoImage(file = "TicTacToe_assets/img1_O.png")
    img2_O = PhotoImage(file = "TicTacToe_assets/img2_O.png")
    img3_O = PhotoImage(file = "TicTacToe_assets/img3_O.png")
    img4_O = PhotoImage(file = "TicTacToe_assets/img4_O.png")
    img5_O = PhotoImage(file = "TicTacToe_assets/img5_O.png")
    img6_O = PhotoImage(file = "TicTacToe_assets/img6_O.png")
    img7_O = PhotoImage(file = "TicTacToe_assets/img7_O.png")
    img8_O = PhotoImage(file = "TicTacToe_assets/img8_O.png")
    img_O=[img2_O,img8_O,img4_O,img7_O,img1_O,img5_O,img3_O,img6_O,img0_O]
    
    # --- BUTTON EFFECTS --- #
    # when player_X chooses
    if len(player_X) <= len(player_O):
        player_X.append(position)
        button_list[position-1].configure(image = img_X[position-1], state=DISABLED)
    
    # when player_O chooses
    else:                                       
        player_O.append(position)
        button_list[position-1].configure(image = img_O[position-1], state=DISABLED)    
    
    total = len(player_X) + len(player_O)
    
    # check score
    check(player_X,player_O,button_list)
  
    # --- ARTIFICIAL INTELLIGENCE --- #
    # for Single Player mode only, at turn for O, while no draw or win
    if game_mode=="Single Player" and len(player_X)>len(player_O) and total!=9 and score_X < 3 and score_O < 3:
        
        while True:
            # randomly pick button at the 3x3 tictactoe box
            choose = random.randint(1,9) 
            
            # if valid move, execute
            if choose not in player_X and choose not in player_O:
                player_O.append(choose)
                button_list[choose-1].configure(image = img_O[choose-1], state=DISABLED)
                check(player_X,player_O,button_list)
                break
            
    mainloop()
               
def check(player_X, player_O, button_list):
    '''checks score if win, draw, or continue game'''
    global score_X, score_O, new        

    # list of winning combinations
    win_list=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]   
    
    # checks if a player has a winning combination
    for x in win_list:        
        score_X=0
        score_O=0

        for y in x:
            if y in player_X:
                score_X=score_X+1
            if y in player_O:
                score_O=score_O+1
            if score_X==3 or score_O==3:
                break

        if score_X==3 or score_O==3:
            break

    # player_X win condition
    if score_X==3:                                                      
        buttons_disable(button_list)
        new=Toplevel()
        new_label=Label(new,text="Player of X win",font="25")
        new_label.pack()
        
    # player_O win condition
    if score_O==3:                                                      
        buttons_disable(button_list)
        new=Toplevel()
        new_label=Label(new,text="Player of O win",font="25")
        new_label.pack()

    # draw condition
    if len(player_X)+len(player_O)==9 and score_X!=3 and score_O!=3:
        buttons_disable(button_list)
        new=Toplevel()
        new_label=Label(new,text="Draw",font="25")
        new_label.pack()