# --- MODULES --- #
from tkinter import *
import Homescreen

# --- FUNCTIONS --- #
def calculator():
    def btn_home():
        '''closes calc, opens homescreen'''
        window.destroy()
        Homescreen.homescreen()

    def btn_click(number):
        '''displays number on calculator in correct order'''
        
        # store current displayed number
        current = inp_screen.get()

        # delete old, display new (left to right)
        inp_screen.delete(0, END)
        inp_screen.insert(0, str(current) + str(number))

    def btn_clear():
        '''clears screen'''
        inp_screen.delete(0, END)

    def btn_add():
        '''assigns operation to addition'''
        global first_input
        global operation
        
        # store first input and operation
        first_input = inp_screen.get()
        inp_screen.delete(0, END) #clears screen
        operation = "addition"
        
        # passes when no inp was given, avoids error
        try:
            first_input = float(first_input)
        except ValueError:
            pass

    def btn_subtract():                                                
        '''assigns operation to subtraction'''
        global first_input
        global operation
        
        # store first input and operation
        first_input = inp_screen.get()
        inp_screen.delete(0, END) #clears screen
        operation = "subtraction"
        
        # passes when no inp was given, avoids error
        try:
            first_input = float(first_input)
        except ValueError:
            pass

    def btn_multiply():                                                
        '''assigns operation to multiplication'''
        global first_input
        global operation
        
        # store first input and operation
        first_input = inp_screen.get()
        inp_screen.delete(0, END) #clears screen
        operation = "multiplication"
        
        # passes when no inp was given, avoids error
        try:
            first_input = float(first_input)
        except ValueError:
            pass


    def btn_divide():                                                
        '''assigns operation to division'''
        global first_input
        global operation
        
        # store first input and operation
        first_input = inp_screen.get()
        inp_screen.delete(0, END) #clears screen
        operation = "division"
        
        # passes when no inp was given, avoids error
        try:
            first_input = float(first_input)
        except ValueError:
            pass


    def btn_equals():
        '''performs operation'''
        global first_input
        global operation

        # store second input
        second_number = inp_screen.get()
        inp_screen.delete(0, END) #clears screen

        # performs operation  
        if operation == "addition":
            result = first_input + float(second_number)
        elif operation == "subtraction":
            result = first_input - float(second_number)
        elif operation == "multiplication":
            result = first_input * float(second_number)
        elif operation == "division":
            result = first_input / float(second_number)

        # if no operation, end function
        else:
            return
        
        # check if integer or not
        # display result
        if result % 1 == 0:
            inp_screen.insert(0, int(result))
        else:
            inp_screen.insert(0, result)

    # --- MAIN and GUI --- #
    global operation
    operation = ""

    window = Tk()
    window.title("Calculator")
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

    background_img = PhotoImage(file = "Calculator_assets\\background.png")
    canvas.create_image(
        240, 360,
        image=background_img)

    inp_screen = Entry(
        font=("Calibri 45"),
        bd = 0,
        bg = "#e9e7ff",
        highlightthickness = 0)

    inp_screen.place(
        x = 33, y = 57,
        width = 414,
        height = 79)

    # Buttons #
    img0 = PhotoImage(file = "Calculator_assets/img0.png")              # Clear Button
    delete_btn = Button(
        image = img0,
        borderwidth = 0,
        cursor = "hand2",
        activebackground = "#BFDDD4",
        highlightthickness = 0,
        command = btn_clear,
        relief = "flat")

    delete_btn.place(
        x = 31.5, y = 170,
        width = 79,
        height = 79)

    img1 = PhotoImage(file = "Calculator_assets/img1.png")              # 7 
    n5_btn = Button(
        image = img1,
        borderwidth = 0,
        cursor = "hand2",
        activebackground = "#BFDDD4",
        highlightthickness = 0,
        command = lambda: btn_click(7),
        relief = "flat")

    n5_btn.place(
        x = 31.5, y = 271,
        width = 79,
        height = 79)

    img2 = PhotoImage(file = "Calculator_assets/img2.png")              # 4
    n4_btn = Button(
        image = img2,
        borderwidth = 0,
        cursor = "hand2",
        activebackground = "#BFDDD4",
        highlightthickness = 0,
        command = lambda: btn_click(4),
        relief = "flat")

    n4_btn.place(
        x = 32, y = 372,
        width = 79,
        height = 79)

    img3 = PhotoImage(file = "Calculator_assets/img3.png")              # 1
    n1_btn = Button(
        image = img3,
        borderwidth = 0,
        cursor = "hand2",
        activebackground = "#BFDDD4",
        highlightthickness = 0,
        command = lambda: btn_click(1),
        relief = "flat")

    n1_btn.place(
        x = 32, y = 473,
        width = 79,
        height = 79)

    img4 = PhotoImage(file = "Calculator_assets/img4.png")              # Exit Button
    exit_btn = Button(
        image = img4,
        borderwidth = 0,
        cursor = "hand2",
        activebackground = "#BFDDD4",
        highlightthickness = 0,
        command = btn_home,
        relief = "flat")

    exit_btn.place(
        x = 31.5, y = 574,
        width = 79,
        height = 79)

    img5 = PhotoImage(file = "Calculator_assets/img5.png")              # Divide Button
    div_btn = Button(
        image = img5,
        borderwidth = 0,
        cursor = "hand2",
        activebackground = "#BFDDD4",
        highlightthickness = 0,
        command = btn_divide,
        relief = "flat")

    div_btn.place(
        x = 143.5, y = 170,
        width = 79,
        height = 79)

    img6 = PhotoImage(file = "Calculator_assets/img6.png")              # 8
    n8_btn = Button(
        image = img6,
        borderwidth = 0,
        cursor = "hand2",
        activebackground = "#BFDDD4",
        highlightthickness = 0,
        command = lambda: btn_click(8),
        relief = "flat")

    n8_btn.place(
        x = 144.5, y = 271,
        width = 79,
        height = 79)

    img7 = PhotoImage(file = "Calculator_assets/img7.png")              # 5
    n5_btn = Button(
        image = img7,
        borderwidth = 0,
        cursor = "hand2",
        activebackground = "#BFDDD4",
        highlightthickness = 0,
        command = lambda: btn_click(5),
        relief = "flat")

    n5_btn.place(
        x = 145, y = 372,
        width = 79,
        height = 79)

    img8 = PhotoImage(file = "Calculator_assets/img8.png")              # 2
    n2_btn = Button(
        image = img8,
        borderwidth = 0,
        cursor = "hand2",
        activebackground = "#BFDDD4",
        highlightthickness = 0,
        command = lambda: btn_click(2),
        relief = "flat")

    n2_btn.place(
        x = 146, y = 473,
        width = 79,
        height = 79)

    img9 = PhotoImage(file = "Calculator_assets/img9.png")              # 0
    n0_btn = Button(
        image = img9,
        borderwidth = 0,
        cursor = "hand2",
        activebackground = "#BFDDD4",
        highlightthickness = 0,
        command = lambda: btn_click(0),
        relief = "flat")

    n0_btn.place(
        x = 146, y = 574,
        width = 190,
        height = 79)

    img10 = PhotoImage(file = "Calculator_assets/img10.png")            # Multiply Button
    mult_btn = Button(
        image = img10,
        borderwidth = 0,
        cursor = "hand2",
        activebackground = "#BFDDD4",
        highlightthickness = 0,
        command = btn_multiply,
        relief = "flat")

    mult_btn.place(
        x = 257.5, y = 170,
        width = 79,
        height = 78)

    img11 = PhotoImage(file = "Calculator_assets/img11.png")            # 9
    n9_btn = Button(
        image = img11,
        borderwidth = 0,
        cursor = "hand2",
        activebackground = "#BFDDD4",
        highlightthickness = 0,
        command = lambda: btn_click(9),
        relief = "flat")

    n9_btn.place(
        x = 257.5, y = 271,
        width = 79,
        height = 79)

    img12 = PhotoImage(file = "Calculator_assets/img12.png")            # 6
    n6 = Button(
        image = img12,
        borderwidth = 0,
        cursor = "hand2",
        activebackground = "#BFDDD4",
        highlightthickness = 0,
        command = lambda: btn_click(6),
        relief = "flat")

    n6.place(
        x = 257.5, y = 372,
        width = 79,
        height = 79)

    img13 = PhotoImage(file = "Calculator_assets/img13.png")            # 3
    n3_btn = Button(
        image = img13,
        borderwidth = 0,
        cursor = "hand2",
        activebackground = "#BFDDD4",
        highlightthickness = 0,
        command = lambda: btn_click(3),
        relief = "flat")

    n3_btn.place(
        x = 257.5, y = 473,
        width = 79,
        height = 79)

    img14 = PhotoImage(file = "Calculator_assets/img14.png")            # Minus Button
    min_btn = Button(
        image = img14,
        borderwidth = 0,
        cursor = "hand2",
        activebackground = "#BFDDD4",
        highlightthickness = 0,
        command = btn_subtract,
        relief = "flat")

    min_btn.place(
        x = 370.5, y = 170,
        width = 79,
        height = 79)

    img15 = PhotoImage(file = "Calculator_assets/img15.png")            # Plus Button
    plus_btn = Button(
        image = img15,
        borderwidth = 0,
        cursor = "hand2",
        activebackground = "#BFDDD4",
        highlightthickness = 0,
        command = btn_add,
        relief = "flat")

    plus_btn.place(
        x = 370.5, y = 271,
        width = 79,
        height = 180)

    img16 = PhotoImage(file = "Calculator_assets/img16.png")            # Equals Button
    eq_btn = Button(
        image = img16,
        borderwidth = 0,
        cursor = "hand2",
        activebackground = "#BFDDD4",
        highlightthickness = 0,
        command = btn_equals,
        relief = "flat")

    eq_btn.place(
        x = 370.5, y = 473,
        width = 79,
        height = 180)

    home_icon = PhotoImage(file = "Homescreen_assets/home_button.png")  # Home Button
    home_btn = Button(
    image = home_icon,
    bg = "#F0F0F0",
    borderwidth = 0,
    cursor = "hand2",
    activebackground = "#F0F0F0",
    highlightthickness = 0,
    command = btn_home,
    relief = "flat"
    )

    home_btn.place(
        x = 240, y = 696,
        anchor=CENTER
        )

    # Launch Mainloop #
    window.resizable(False, False)
    window.mainloop()