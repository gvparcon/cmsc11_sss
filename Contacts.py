# --- MODULES --- #
from tkinter import *
import Homescreen

# --- FUNCTIONS --- #
def contacts():
    def btn_clicked(window):
        window.destroy()
        Homescreen.homescreen()

    def Store():                                                #for storing the contact data in a text file so that we will have a copy of the list even after closing 
        with open('sumsang_contacts.txt', 'w') as file:         #overwrite the previous contact list with a new list where the contact info removed is not found
            for contact in contact_data:
                for item in contact:
                    file.write(f'{item}\n')
                file.write('\n')

    def Load():                                                 #for loading the stored data from the text file as we open the tkinter
        with open("sumsang_contacts.txt", "r") as file:
            for index, line in enumerate(file):                 #reads the txt file and append each line to contact data depending on its value
                if index % 6 == 0:                              #checks each indices to get corresponding value if name, number, etc. 
                    name = line.strip()
                elif index % 6 == 1:
                    number = line.strip()
                elif index % 6 == 2:
                    sim = line.strip()
                elif index % 6 == 3:
                    group = line.strip()
                elif index % 6 == 4:
                    note = line.strip()
                    combined = (name, number, sim, group, note)
                    contact_data.append(list(combined))         #store the retrieved data from txt file to the list we have in python file

        Update_List(contact_data)                               #after retrieving, update contact list with the modified list

    def Add():  
        global contact_data                                     #global keyword allows you to modify the variable outside of the current scope
        contact_data.append([name.get(), number.get(), sim_type.get(), grouping.get(), note.get()])         #append the data we grabbed to the initialized list
        Update_List(contact_data)                               #update list to accommodate the new contact added to the list
        Clear()                                                 #clears the entry boxes to allow new input

    def View():                                                 #for viewing the data of each contact inside their respective entry boxes
        name.set(contact_data[int(contact_list.curselection()[0])][0])
        number.set(contact_data[int(contact_list.curselection()[0])][1])
        sim_type.set(contact_data[int(contact_list.curselection()[0])][2])
        grouping.set(contact_data[int(contact_list.curselection()[0])][3])
        note.set(contact_data[int(contact_list.curselection()[0])][4])

    def Delete():                                               #for deleting the contact selected
        del contact_data[int(contact_list.curselection()[0])]   
        Update_List(contact_data)                               #updates list without the removed contact

    def Clear():                                                #for clearing the entry boxes and allowing new input, sets each field to empty ('')
        name.set(''), number.set(''), sim_type.set(''), grouping.set(''), note.set('')      

    def Update_List(data):                                      #for updating the contact list each time there is a modification
        contact_list.delete(0,END)                              #clear the listbox to avoid duplications
        data.sort()                                         
        for item in data:                                       #add the items from the contact data list back to the listbox
            contact_list.insert(END, item[0])
        Store()                                                 #each time there is an update, we store these values to the text file

    def Highlight_Search(*args):                                #for searching info and highlighting it in the contact list
        typed = search_entry.get()
        lowercase = [list(map(str.casefold, x)) for x in contact_data]      #converts all items in nested list to lowercase

        for i, item in enumerate(lowercase):
            if typed.lower() in item:
                contact_list.selection_set(i)
            else:
                contact_list.selection_clear(i)
        if typed == '':
            contact_list.selection_clear(0,END)

    def temp_text(e):                                           #for the Search... temporary text, when clicked it disappears
        search_entry.delete(0,"end")

    # --- MAIN and GUI --- #
    window = Tk()

    window.geometry("480x720")                                  #dimensions of the tkinter window
    window.configure(bg = "#ffffff")

    global contact_data, contact_list,name, number, sim_type, grouping, note, search, search_entry

    canvas = Canvas(
        window,
        height = 720,
        width = 480,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = "Contacts_assets/background.png")            #for the image of the background that does not cover the widgets
    background = canvas.create_image(240, 359,image=background_img)

    name, number, sim_type, grouping, note, search = [StringVar() for i in range(6)] #StringVar helps you manage the value of a widget such as a Label or Entry more effectively.

    '''entry box for name input'''
    name_entry = Entry(                     
        bd = 0,
        bg = "#f7fff0",
        font = ("Arial Bold", 10,),
        fg = "MediumOrchid1",
        highlightthickness = 0, 
        textvariable=name)

    name_entry.place(
        x = 131, y = 89,
        width = 303,
        height = 21,)

    '''entry box for number input'''
    number_entry = Entry(
        bd = 0,
        bg = "#f7fff0",
        font = ("Arial Bold", 10,),
        fg = "MediumOrchid2", 
        highlightthickness = 0,
        textvariable=number)

    number_entry.place(
        x = 131, y = 127,
        width = 303,
        height = 21,)

    '''entry box for sim input'''
    sim_entry = Entry(
        bd = 0,
        bg = "#f7fff0",
        font = ("Arial Bold", 10,),
        fg = "MediumOrchid3", 
        highlightthickness = 0, 
        textvariable=sim_type)

    sim_entry.place(
        x = 131, y = 165,
        width = 303,
        height = 21,)

    '''entry box for grouping input'''
    grouping_entry = Entry(
        bd = 0,
        bg = "#f7fff0",
        font = ("Arial Bold", 10,),
        fg = "MediumOrchid4",
        highlightthickness = 0,
        textvariable=grouping)

    grouping_entry.place(
        x = 131, y = 203,
        width = 303,
        height = 21,)

    '''entry box for note input'''
    note_entry = Entry(
        bd = 0,
        bg = "#f7fff0",
        font = ("Arial Bold", 10,),
        fg = "DarkOrchid4",
        highlightthickness = 0,
        textvariable=note)

    note_entry.place(
        x = 131, y = 241,
        width = 303,
        height = 35,)

    '''entry box for search input'''
    search_entry = Entry(
        bd = 0,
        bg = "#dbd6f1",
        font = ("Arial Italic", 10,),
        fg = "purple4",
        highlightthickness = 0,
        textvariable= search)

    search_entry.place(
        x = 65, y = 361,
        width = 292,
        height = 26,)

    search_entry.insert(0, "Search...")                    # Insert a temporary text so when we click, it'll disappear
    search_entry.bind("<FocusIn>", temp_text)
    search_entry.bind("<KeyRelease>", Highlight_Search)    # if search input is found in contact list, then we highlight the data

    '''button for clearing fields'''
    img0 = PhotoImage(file = "Contacts_assets/img0.png")
    clr_btn = Button(
        image = img0,
        borderwidth = 0,
        cursor = "hand2",
        activebackground = "#BFFFF3",
        highlightthickness = 0,
        command = Clear,
        relief = "flat")

    clr_btn.place(
        x = 343, y = 292,
        width = 90,
        height = 23,)

    '''button for adding info'''
    img1 = PhotoImage(file = "Contacts_assets/img1.png")
    add_btn = Button(
        image = img1,
        borderwidth = 0,
        cursor = "hand2",
        activebackground = "#BFFFF3",
        highlightthickness = 0,
        command = Add,
        relief = "flat")

    add_btn.place(
        x = 288, y = 292,
        width = 38,
        height = 23,)

    '''button for viewing data'''
    img2 = PhotoImage(file = "Contacts_assets/img2.png")
    view_btn = Button(
        image = img2,
        borderwidth = 0,
        cursor = "hand2",
        activebackground = "#DBD6F1",
        highlightthickness = 0,
        command = View,
        relief = "flat")

    view_btn.place(
        x = 370, y = 362,
        width = 34,
        height = 26,)

    '''button for deleting data'''
    img3 = PhotoImage(file = "Contacts_assets/img3.png")
    del_btn = Button(
        image = img3,
        borderwidth = 0,
        cursor = "hand2",
        activebackground = "#DBD6F1",
        highlightthickness = 0,
        command = Delete,
        relief = "flat")

    del_btn.place(
        x = 417, y = 362,
        width = 34,
        height = 26,)

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

    '''creates a frame that will house the scrollbar and listbox'''
    scroll_frame = Frame(window)

    scroll_bar = Scrollbar(scroll_frame, orient=VERTICAL)
    contact_list = Listbox(scroll_frame, width = 30,  height=8, 
                yscrollcommand=scroll_bar.set, bg = "#ECE9FC", 
                font = ("Arial Bold", 18), fg = "SlateBlue4", 
                selectforeground="lightsteelblue1", selectbackground="MediumPurple1")
                
    scroll_bar.config(command= contact_list.yview)
    scroll_bar.pack(side=RIGHT, fill=Y)
    scroll_frame.place(x = 38, y = 410,)
    contact_list.pack()

    contact_data = []                       # initialize empty list where all contact datas will be stored
    Load()                                  # this function is called to load the contact list from the text file

    window.resizable(False, False)          # avoid resizing of the window
    window.mainloop()