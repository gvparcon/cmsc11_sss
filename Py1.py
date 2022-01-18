# --- IMPORT --- #
from tkinter import *
from tkinter import scrolledtext
from datetime import datetime, date
import Homescreen

today = date.today()
now = datetime.now()

def py1():
    # --- FUNCTIONS --- #
    def btn_clicked(window):
        '''closes messaging, opens homescreen'''
        window.destroy()
        Homescreen.homescreen()
    
    def load_messages():
        '''reads the stored messages from Messages.txt'''
        
        # initialize tuple
        stored_messages = tuple()

        # read file, store data into tuple
        with open('Messages.txt', 'r') as file:
            for index, item in enumerate(file):
                if index%3 == 1:
                    timestamp = item.strip()
                elif index%3 == 2:
                    message = item.strip()
                    
                    # if message is from Py 1, replace with 'You'
                    if message[3] == '1':
                        message = message.replace('Py 1', 'You', 1)

                    stored_messages += ((timestamp, message, ''), )
                    
        for tpl in stored_messages:               
            for item in tpl:
                chatbox.insert(END, item)

    def send_message():
        '''stores messages on Messages.txt'''

        # input
        inp = text_area.get(1.0,"end-1c")
        message = 'Py 1: ' + inp
        text_area.delete(1.0,"end-1c") #empties input bar 

        # set time_stamp
        day = today.strftime('%m/%d/%y')
        hour = now.strftime('%H:%M')
        time_stamp = f'{day} {hour}'

        # store data
        with open('Messages.txt', 'a') as file:
            file.write(f'\n{time_stamp}\n{message}\n')

        # update chatbox
        message = 'You: ' + inp
        chatbox.insert(END, time_stamp)
        chatbox.insert(END, message)
        chatbox.insert(END, '')

    # --- MAIN and GUI --- #
    window = Tk()

    window.geometry("480x720")
    window.configure(bg = "#e1dfdf")
    canvas = Canvas(
        window,
        bg = "#e1dfdf",
        height = 720,
        width = 480,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = "Messenger_assets/background.png")
    background = canvas.create_image(
        240, 359,
        image=background_img)

    # Send Button #
    img0 = PhotoImage(file = "Messenger_assets/img0.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = send_message,
        relief = "flat")

    b0.place(
        x = 368, y = 604,
        width = 82,
        height = 39)

    frame = Frame(window)

    # Input Text Field #
    text_area = scrolledtext.ScrolledText(window, wrap=WORD,
                                        width=40, height=2,
                                        font=("Arial", 10), 
                                        fg = "midnight blue",
                                        background = "#CDD1FC")
    text_area.place(                 
        x = 40, y = 600)
    # placing cursor in text area
    text_area.focus()

    # Convo Box #
    scroll_frame = Frame(window)
    scroll_bar = Scrollbar(
        scroll_frame, 
        orient=VERTICAL)
    
    chatbox = Listbox(scroll_frame, 
        width=50,  
        height=25, 
        yscrollcommand=scroll_bar.set, 
        bg="#F7FF96", 
        fg="midnight blue",
        selectforeground="lightsteelblue1", 
        selectbackground="MediumPurple1")
        
    scroll_bar.config(command = chatbox.yview_moveto(0))
    scroll_bar.pack(side=RIGHT, fill=Y)
    scroll_frame.place(x=120, y=120,)
    chatbox.pack()

    # loads messages into Convo Box
    load_messages()

    # Home Icon #
    home_icon = PhotoImage(file =  "Homescreen_assets/home_button.png")
    home_btn = Button(
        image = home_icon,
        bg = "#FCFAFD",
        borderwidth = 0,
        cursor = "hand2",
        activebackground = "#FCFAFD",
        highlightthickness = 0,
        command = lambda:btn_clicked(window),
        relief = "flat"
        )
    
    home_btn.place(
        x = 240, y = 696,
        anchor=CENTER
        )
    
    # Launch Mainloop #
    frame.pack()

    window.resizable(False, False)
    window.mainloop()