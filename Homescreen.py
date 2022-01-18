# --- MODULES --- #
from tkinter import *
import time
import TicTacToe
import Calculator
import Py1
import Contacts

# --- FUNCTIONS --- #
def homescreen():
    def clock():
        '''updates time per second by recursion'''

        # store current time 
        hh= time.strftime("%I")
        mm= time.strftime("%M")

        # display time text
        clock_text.config(text= hh + ":" + mm)

        # update every second
        clock_text.after(1000, clock)

    def home_btn_clicked():
        '''since we're already at home, do nothing'''
        pass

    def use_calc(home_window):
        '''close homescreen, launch calc app'''
        home_window.destroy()
        Calculator.calculator()
       
    def use_messsage(home_window):
        '''close homescreen, launch message app'''
        home_window.destroy()
        Py1.py1()

    def use_contacts(home_window):
        '''close homescreen, launch contacts app'''
        home_window.destroy()
        Contacts.contacts()

    def use_tictac(home_window):
        '''close homescreen, launch tictactoe app'''
        home_window.destroy()
        TicTacToe.main_menu()

        
    # --- MAIN and GUI --- #
    home_window = Tk()
    home_window.title("SSS PHONE")
    home_window.geometry("480x720")
    home_window.configure(bg = "#ffffff")

    canvas = Canvas(
        home_window,
        bg = "#ffffff",
        height = 720,
        width = 480,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
        )
    canvas.place(x = 0, y = 0)

    bg_img = PhotoImage(file =  "Homescreen_assets/homescreen_background.png")
    background = canvas.create_image(
        240, 360,
        image=bg_img
        )

    # --- CLOCK --- #
    # due to labels not having transparent background,
    # clock_bg_img is snippet of bg_img, replicating transparent effect
    clock_bg_img = PhotoImage(file =  "Homescreen_assets/clock_background.png")

    global clock_text
    clock_text = Label(
        home_window,
        text = "",
        font =("Inter", 85),
        fg= "#2A2C23",
        image=clock_bg_img,
        compound="center"
        )

    # --- TEXTS --- #
    canvas.create_text(
        240, 238,
        text = "Life without design is erratic.\n-Seneca",
        fill = "#dfffff",
        font = ("Inter-Light", int(12.0)),
        justify="center",
        anchor=CENTER
        )

    canvas.create_text(
        154, 450,
        text = "Tic-Tac-Toe",
        fill = "#2A2C23",
        font = ("Inter", int(11.0)),
        justify="center",
        anchor=CENTER
        )

    canvas.create_text(
        154, 623,
        text = "Calculator",
        fill = "#2A2C23",
        font = ("Inter", int(11.0)),
        justify="center",
        anchor=CENTER
        )

    canvas.create_text(
        325, 450,
        text = "Contacts",
        fill = "#2A2C23",
        font = ("Inter", int(11.0)),
        justify="center",
        anchor=CENTER
        )

    canvas.create_text(
        325, 623,
        text = "Messaging",
        fill = "#2A2C23",
        font = ("Inter", int(11.0)),
        justify="center",
        anchor=CENTER
        )

    # --- BUTTONS --- #
    home_icon = PhotoImage(file =  "Homescreen_assets/home_button.png")
    home_btn = Button(
        image = home_icon,
        bg = "#F0F0F0",
        borderwidth = 0,
        cursor = "hand2",
        activebackground = "#F0F0F0",
        highlightthickness = 0,
        command = home_btn_clicked,
        relief = "flat"
        )

    msg_icon = PhotoImage(file =  "Homescreen_assets/messaging_icon.png")
    msg_app = Button(
        image = msg_icon,
        bg = "#BFDDCB",
        borderwidth = 0,
        cursor = "hand2",
        activebackground = "#BFDDCB",
        highlightthickness = 0,
        command = lambda:use_messsage(home_window),
        relief = "flat"
        )

    contacts_icon = PhotoImage(file =  "Homescreen_assets/contacts_icon.png")
    contacts_app = Button(
        image = contacts_icon,
        bg = "#A7D7E2",
        borderwidth = 0,
        cursor = "hand2",
        activebackground = "#A7D7E2",
        highlightthickness = 0,
        command = lambda:use_contacts(home_window),
        relief = "flat"
        )

    calc_icon = PhotoImage(file =  "Homescreen_assets/calculator_icon.png")
    calc_app = Button(
        image = calc_icon,
        bg = "#DDD1BF",
        borderwidth = 0,
        cursor = "hand2",
        activebackground = "#DDD1BF",
        highlightthickness = 0,
        command = lambda:use_calc(home_window),
        relief = "flat"
        )

    tictac_icon = PhotoImage(file =  "Homescreen_assets/tictac_icon.png")
    tictac_app = Button(
        image = tictac_icon,
        bg = "#BFDDD4",
        borderwidth = 0,
        cursor = "hand2",
        activebackground = "#BFDDD4",
        highlightthickness = 0,
        command = lambda:use_tictac(home_window),
        relief = "flat"
        )

    # --- PLACEMENTS --- #
    clock_text.place(
        x = 0, y = 91,
        height = 128,
        width = 480
        )

    home_btn.place(
        x = 240, y = 696,
        anchor=CENTER
        )

    tictac_app.place(
        x = 121, y = 363.5,
        )

    contacts_app.place(
        x = 292.5, y = 362.5,
        )

    calc_app.place(
        x = 121, y = 535,
        )

    msg_app.place(
        x = 292.5, y = 535,
        )

    # initiate clock
    clock()

    # --- LAUNCH MAINLOOP --- #
    home_window.resizable(False, False)
    home_window.mainloop()