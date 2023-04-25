from tkinter import *
import os
from tkinter import filedialog
import pathlib


#Next unused screen: 45

global productName
global product_entry

def delete2():
    screen3.destroy()
def delete3():
    screen4.destroy()
def delete4():
    screen5.destroy()
def delete5():
    screen1.destroy()

def screen_deletion():
    global detail_identifier
    if detail_identifier == 0:
         screen10.destroy()
         screen7.destroy()
    
        
        
        
        
    elif detail_identifier == 1:
        screen11.destroy()
        screen7.destroy()
        
        
    elif detail_identifier == 2:
        screen12.destroy()
        screen7.destroy()
        

    elif detail_identifier == 3:
        screen13.destroy()
        screen7.destroy()
        

    elif detail_identifier == 4:
        screen14.destroy()
        screen7.destroy()
    



def account_management():
    global screen7
    screen7 = Toplevel(screen)
    screen7.title("Account Management")
    screen7.geometry("500x500")
    Label(screen7, text="Welcome to account management").pack()
    Label(screen7, text = "Username:", font= ('Helvetica', 13, 'bold')).pack()
    Label(screen7, text=username1).pack()
    Label(screen7, text="").pack()
    Label(screen7, text = "Usernames cannot be changed").pack()
    Button(screen7, text="Change me", command=username_changes).pack()
    Label(screen7, text = "Password:", font=('Helvetica', 13, 'bold')).pack()
    Label(screen7, text =password1).pack()
    Label(screen7, text="").pack()
    Button(screen7, text="Change me", command=password_changes).pack()
   
    f= open(username1)
    content = f.readlines()

    Label(screen7, text = "Address Line 1:", font=('Helvetica', 13, 'bold')).pack()
    Label(screen7, text = content[2]).pack()
    Button(screen7, text="Change me", command=address1_changes).pack()

    Label(screen7, text = "Address Line 2:", font=('Helvetica', 13, 'bold')).pack()
    Label(screen7, text = content[3]).pack()
    Button(screen7, text="Change me", command=address2_changes).pack()

    Label(screen7, text = "Postcode", font=('Helvetica', 13, 'bold')).pack()
    Label(screen7, text = content[4]).pack()
    Button(screen7, text="Change me", command=postcode_changes).pack()

def username_changes():
    global screen10
    global new_username_entry
    global detail_identifier
    screen10 = Toplevel(screen)
    screen10.title("Changing Username")
    screen10.geometry("500x500")

    Label(screen10, text = "Currently unable to change the username")

    #data_identifier = 0
    #Label(screen10, text="Please input the new username").pack()
    #Label(screen10, text = "").pack()
    #new_username_entry = Entry(screen10)
    #new_username_entry.pack()
    #data_identifier = 0
    #Button(screen10, command = actually_changing).pack()

def password_changes():
    global screen11
    global new_password_entry
    global detail_identifier
    screen11 = Toplevel(screen)
    screen11.title("Changing Password")
    screen11.geometry("500x500")

    detail_identifier = 1
    Label(screen11, text="Please input the new password").pack()
    Label(screen11, text = "").pack()
    new_password_entry = Entry(screen11)
    new_password_entry.pack()
    Button(screen11, text = "Change password", command = actually_changing).pack()

def address1_changes():
    global screen12
    global detail_identifier
    global new_address1_entry
    screen12 = Toplevel(screen)
    screen12.title("Changing 1st line of Address")
    screen12.geometry("500x500")

    detail_identifier = 2
    Label(screen12, text = "Please enter updated 1st line of address").pack()
    Label(screen12, text = "").pack()
    new_address1_entry = Entry(screen12)
    new_address1_entry.pack()
    Button(screen12, text = "Update first line of address", command = actually_changing).pack()
    

def address2_changes():
    global screen13
    global detail_identifier
    global new_address2_entry
    screen13 = Toplevel(screen)
    screen13.title("Changing 2nd line of Address")
    screen13.geometry("500x500")

    detail_identifier = 3
    Label(screen13, text = "Please enter updated second line of address").pack()
    Label(screen13, text = "").pack()
    new_address2_entry = Entry(screen13)
    new_address2_entry.pack()
    Button(screen13, text = "Update second line of address", command = actually_changing).pack()

def postcode_changes():
    global screen14
    global detail_identifier
    global new_postcode_entry
    screen14 = Toplevel(screen)
    screen14.title("Changing Postcode")
    screen14.geometry("500x500")

    detail_identifier = 4
    Label(screen14, text = "Please enter new postcode:").pack()
    Label(screen14, text = "").pack()
    new_postcode_entry = Entry(screen14)
    new_postcode_entry.pack()
    Button(screen14, text = "Update postcode", command = actually_changing).pack()
    
    




def actually_changing():
    global username1
    global username_detail
    username_file_read = open(username1, "r")
    data = username_file_read.readlines()
    print(data)
    if detail_identifier == 0:
        username_detail = new_username_entry.get()
        print(username_detail)
        data[0] = (username_detail + "\n")
        print(data)
        username_file_write = open(username1, "w")
        username_file_write.writelines(data)
        screen_deletion()
        
        
        
        
    elif detail_identifier == 1:
        password_detail = new_password_entry.get()
        data[1] = (password_detail + "\n")
        print(data)
        password_file_write = open(username1, "w")
        password_file_write.writelines(data)
        screen_deletion()
        
    elif detail_identifier == 2:
        address1_detail = new_address1_entry.get()
        data[2] = (address1_detail + "\n")
        print(data)
        address1_file_write = open(username1, "w")
        address1_file_write.writelines(data)

    elif detail_identifier == 3:
        address2_detail = new_address2_entry.get()
        data[3] = (address2_detail + "\n")
        print(data)
        address2_file_write = open(username1, "w")
        address2_file_write.writelines(data)


    elif detail_identifier == 4:
        postcode_detail = new_postcode_entry.get()
        data[4] = (postcode_detail + "\n")
        print(data)
        postcode_file_write = open(username1, "w")
        postcode_file_wrie.writelines(data)
    
    



    
    

def buying():
    global screen8
    screen8 = Toplevel(screen)
    screen8.title("Buying Homepage")
    screen8.geometry("500x500")
    Label(screen8, text = "Welcome to the Online Marketplace").pack()

    books_button = Button(screen8, text = "Search through all available books", command = books)
    books_button.pack()

    games_button = Button(screen8, text = "Games", command = games)
    games_button.pack()

    electronics_button = Button(screen8, text = "Electronics", command = electronics)
    electronics_button.pack()

    home_garden_button = Button(screen8, text = "Home & Garden", command = home_garden)
    home_garden_button.pack()

    toys_button = Button(screen8, text = "Toys", command = toys)
    toys_button.pack()

    clothes_jewellery_button = Button(screen8, text = "Clothes & Jewellery", command = clothes_jewellery)
    clothes_jewellery_button.pack()

    sports_outdoors_button = Button(screen8, text = "Sports & Outdoors", command = sports_outdoors)
    sports_outdoors_button.pack()

    food_button = Button(screen8, text = "Food", command = food)
    food_button.pack()

    health_button = Button(screen8, text = "Health", command = health)
    health_button.pack()

    motor_vehicles_button = Button(screen8, text = "Motor Vehicles", command = motor_vehicles)
    motor_vehicles_button.pack()

    education_button = Button(screen8, text = "Education", command = education)
    education_button.pack()
    

    


def update_book(book_list_data):
    global book_list
    #Clear the listbox
    book_list.delete(0, END)

    #Add data to listbox
    for item in book_list_data:
        book_list.insert(END, item)


#Update entry box with listbox clicked
def fillout_book(event):
    global book_entry
    #Delete whatever is in the entry box
    book_entry.delete(0, END)

    #Add clicked list item to entry box
    book_entry.insert(0, book_list.get(ACTIVE))

def check_book(event):
    #Grab what was typed
    global book_entry
    global book_list_data
    typed_book = book_entry.get()

    if typed_book == " ":
        data = book_list_data
    else:
        data = []
        for item in book_list_data:
            if typed_book.lower() in item.lower():
                data.append(item)
    update_book(data)
    
def book_select():
    global screen26
    global selected_book
    global ORIGINAL_ROOT_DIR
    global path_for_books
    global book_info
    global purchasing_choice
    purchasing_choice = 1
    print(purchasing_choice)
    selected_book = StringVar()
    selected_book = book_entry.get()
    print(selected_book)
    screen26 = Toplevel(screen)
    screen26.title(selected_book)
    screen26.geometry("500x500")

    os.chdir(path_for_books)
    

    f= open(selected_book)
    book_info = f.readlines()
    print(book_info)

    Label(screen26, text = "Product name:", font=('Helvetica', 13, 'bold')).pack()
    Label(screen26, text = book_info[0]).pack()

    Label(screen26, text = "Price:", font=('Helvetica', 13, 'bold')).pack()
    Label(screen26, text = book_info[1]).pack()

    Label(screen26, text = "Description;", font=("Helvetica", 13, "bold")).pack()
    Label(screen26, text = book_info[5]).pack()

    Label(screen26, text = "Sold by:", font=("Helvetica", 13, "bold")).pack()
    Label(screen26, text = book_info[2]).pack()

    Button(screen26, text = "Purchase", command = purchase_screen).pack()



    




def books():
    global screen15
    global book_list
    global book_entry
    global book_list_data
    global path_for_books
    screen15 = Toplevel(screen)
    screen15.title("Books")
    screen15.geometry("500x500")

    Label(screen15, text = "BOOKS").pack()

    book_entry = Entry(screen15,)
    book_entry.pack()

    #create a list box
    book_list = Listbox(screen15)
    book_list.pack()

    #create a list
    book_list_data = os.listdir(path_for_books)
    #testing479 = os.listdir(path_for_books)
    #print(testing479)

    #Add the data to the list
    update_book(book_list_data)

    #Create a binding on the listbox onclick
    book_list.bind("<<ListboxSelect>>", fillout_book)

    #Create a binding on the entry box
    book_entry.bind("<KeyRelease>", check_book)

    #Button to select
    book_button = Button(screen15, text = "Select", command = book_select)
    book_button.pack()
    
def update_game(game_list_data):
    global game_list
    #Clear the listbox
    game_list.delete(0, END)

    #Add data to listbox
    for item in game_list_data:
        game_list.insert(END, item)


#Update entry box with listbox clicked
def fillout_game(event):
    global game_entry
    #Delete whatever is in the entry box
    game_entry.delete(0, END)

    #Add clicked list item to entry box
    game_entry.insert(0, game_list.get(ACTIVE))



def check_game(event):
    #Grab what was typed
    global game_entry
    global game_list_data
    typed_game = game_entry.get()

    if typed_game == " ":
        data = game_list_data
    else:
        data = []
        for item in game_list_data:
            if typed_game.lower() in item.lower():
                data.append(item)
    update_game(data)


def game_select():
    global screen27
    global selected_game
    global ORIGINAL_ROOT_DIR
    global path_for_games
    global game_info
    global purchasing_choice
    purchasing_choice = 2
    selected_game = StringVar()
    selected_game = game_entry.get()
    print(selected_game)
    screen27 = Toplevel(screen)
    screen27.title(selected_game)
    screen27.geometry("500x500")

    os.chdir(path_for_games)
    

    f= open(selected_game)
    game_info = f.readlines()
    print(game_info)

    Label(screen27, text = "Product name:", font=('Helvetica', 13, 'bold')).pack()
    Label(screen27, text = game_info[0]).pack()

    Label(screen27, text = "Price:", font=('Helvetica', 13, 'bold')).pack()
    Label(screen27, text = game_info[1]).pack()

    Label(screen27, text = "Description;", font=("Helvetica", 13, "bold")).pack()
    Label(screen27, text = game_info[5]).pack()

    Label(screen27, text = "Sold by:", font=("Helvetica", 13, "bold")).pack()
    Label(screen27, text = game_info[2]).pack()


    purchase = Button(screen27, text = "Purchase", command = purchase_screen)
    purchase.pack()




def games():
    global screen16
    global game_list
    global game_entry
    global game_list_data
    global path_for_games
    screen16 = Toplevel(screen)
    screen16.title("Games")
    screen16.geometry("500x500")

    Label(screen16, text = "Games").pack()

    game_entry = Entry(screen16,)
    game_entry.pack()

    #create a list box
    game_list = Listbox(screen16)
    game_list.pack()

    #create a list
    game_list_data = os.listdir(path_for_games)
    #testing479 = os.listdir(path_for_books)
    #print(testing479)

    #Add the data to the list
    update_game(game_list_data)

    #Create a binding on the listbox onclick
    game_list.bind("<<ListboxSelect>>", fillout_game)

    #Create a binding on the entry box
    game_entry.bind("<KeyRelease>", check_game)

    #Button to select
    game_button = Button(screen16, text = "Select", command = game_select)
    game_button.pack()
    
def update_electronics(electronics_list_data):
    global electronics_list
    #Clear the listbox
    electronics_list.delete(0, END)

    #Add data to listbox
    for item in electronics_list_data:
        electronics_list.insert(END, item)


#Update entry box with listbox clicked
def fillout_electronics(event):
    global electronics_entry
    #Delete whatever is in the entry box
    electronics_entry.delete(0, END)

    #Add clicked list item to entry box
    electronics_entry.insert(0, electronics_list.get(ACTIVE))



def check_electronics(event):
    #Grab what was typed
    global electronics_entry
    global electronics_list_data
    typed_electronics = electronics_entry.get()

    if typed_electronics == " ":
        data = electronics_list_data
    else:
        data = []
        for item in electronics_list_data:
            if typed_electronics.lower() in item.lower():
                data.append(item)
    update_electronics(data)    




def electronics_select():
    global screen28
    global selected_electronic
    global ORIGINAL_ROOT_DIR
    global path_for_electronics
    global electronic_info
    global purchasing_choice
    purchasing_choice = 3
    selected_electronic = StringVar()
    selected_electronic = electronics_entry.get()
    print(selected_electronic)
    screen28 = Toplevel(screen)
    screen28.title(selected_electronic)
    screen28.geometry("500x500")

    os.chdir(path_for_electronics)
    

    f= open(selected_electronic)
    electronic_info = f.readlines()
    print(electronic_info)

    Label(screen28, text = "Product name:", font=('Helvetica', 13, 'bold')).pack()
    Label(screen28, text = electronic_info[0]).pack()

    Label(screen28, text = "Price:", font=('Helvetica', 13, 'bold')).pack()
    Label(screen28, text = electronic_info[1]).pack()

    Label(screen28, text = "Description;", font=("Helvetica", 13, "bold")).pack()
    Label(screen28, text = electronic_info[8]).pack()

    Label(screen28, text = "Sold by:", font=("Helvetica", 13, "bold")).pack()
    Label(screen28, text = electronic_info[2]).pack()

    purchase = Button(screen28, text = "Purchase", command = purchase_screen)
    purchase.pack()
    purchasing_choice = selected_electronic






def electronics():
    global screen17
    global electronics_list
    global electronics_entry
    global electronics_list_data
    global path_for_electronics
    screen17 = Toplevel(screen)
    screen17.title("Electronics")
    screen17.geometry("500x500")

    Label(screen17, text = "Electronics").pack()

    electronics_entry = Entry(screen17,)
    electronics_entry.pack()

    #create a list box
    electronics_list = Listbox(screen17)
    electronics_list.pack()

    #create a list
    electronics_list_data = os.listdir(path_for_electronics)
    #testing479 = os.listdir(path_for_books)
    #print(testing479)

    #Add the data to the list
    update_electronics(electronics_list_data)

    #Create a binding on the listbox onclick
    electronics_list.bind("<<ListboxSelect>>", fillout_electronics)

    #Create a binding on the entry box
    electronics_entry.bind("<KeyRelease>", check_electronics)

    #Button to select
    electronics_button = Button(screen17, text = "Select", command = electronics_select)
    electronics_button.pack()


def update_home_garden(home_garden_list_data):
    global home_garden_list
    #Clear the listbox
    home_garden_list.delete(0, END)

    #Add data to listbox
    for item in home_garden_list_data:
        home_garden_list.insert(END, item)


#Update entry box with listbox clicked
def fillout_home_garden(event):
    global home_garden_entry
    #Delete whatever is in the entry box
    home_garden_entry.delete(0, END)

    #Add clicked list item to entry box
    home_garden_entry.insert(0, home_garden_list.get(ACTIVE))



def check_home_garden(event):
    #Grab what was typed
    global home_garden_entry
    global home_garden_list_data
    typed_home_garden = home_garden_entry.get()

    if typed_home_garden == " ":
        data = home_garden_list_data
    else:
        data = []
        for item in home_garden_list_data:
            if typed_home_garden.lower() in item.lower():
                data.append(item)
    update_home_garden(data)    


def home_garden_select():
    global screen29
    global selected_home_garden
    global ORIGINAL_ROOT_DIR
    global path_for_homegarden
    global home_garden_info
    global purchasing_choice
    purchasing_choice = 4
    selected_home_garden = StringVar()
    selected_home_garden = home_garden_entry.get()
    print(selected_home_garden)
    screen29 = Toplevel(screen)
    screen29.title(selected_home_garden)
    screen29.geometry("500x500")

    os.chdir(path_for_homegarden)
    

    f= open(selected_home_garden)
    home_garden_info = f.readlines()
    print(home_garden_info)

    Label(screen29, text = "Product name:", font=('Helvetica', 13, 'bold')).pack()
    Label(screen29, text = home_garden_info[0]).pack()

    Label(screen29, text = "Price:", font=('Helvetica', 13, 'bold')).pack()
    Label(screen29, text = home_garden_info[1]).pack()

    Label(screen29, text = "Description;", font=("Helvetica", 13, "bold")).pack()
    Label(screen29, text = home_garden_info[8]).pack()

    Label(screen29, text = "Sold by:", font=("Helvetica", 13, "bold")).pack()
    Label(screen29, text = home_garden_info[2]).pack()

    purchase = Button(screen29, text = "Purchase", command = purchase_screen)
    purchase.pack()






def home_garden():
    global screen18
    global home_garden_list
    global home_garden_entry
    global home_garden_list_data
    global path_for_homegarden
    screen18 = Toplevel(screen)
    screen18.title("Home & Garden")
    screen18.geometry("500x500")

    Label(screen18, text = "Home & Garden").pack()

    home_garden_entry = Entry(screen18,)
    home_garden_entry.pack()

    #create a list box
    home_garden_list = Listbox(screen18)
    home_garden_list.pack()

    #create a list
    home_garden_list_data = os.listdir(path_for_homegarden)
    #testing479 = os.listdir(path_for_books)
    #print(testing479)

    #Add the data to the list
    update_home_garden(home_garden_list_data)

    #Create a binding on the listbox onclick
    home_garden_list.bind("<<ListboxSelect>>", fillout_home_garden)

    #Create a binding on the entry box
    home_garden_entry.bind("<KeyRelease>", check_home_garden)




    #Button to select
    home_garden_button = Button(screen18, text = "Select", command = home_garden_select)
    home_garden_button.pack()



def update_toys(toys_list_data):
    global toys_list
    #Clear the listbox
    toys_list.delete(0, END)

    #Add data to listbox
    for item in toys_list_data:
        toys_list.insert(END, item)


#Update entry box with listbox clicked
def fillout_toys(event):
    global toys_entry
    #Delete whatever is in the entry box
    toys_entry.delete(0, END)

    #Add clicked list item to entry box
    toys_entry.insert(0, toys_list.get(ACTIVE))



def check_toys(event):
    #Grab what was typed
    global toys_entry
    global toys_list_data
    typed_toys = toys_entry.get()

    if typed_toys == " ":
        data = toys_list_data
    else:
        data = []
        for item in toys_list_data:
            if typed_toys.lower() in item.lower():
                data.append(item)
    update_toys(data)    



def toys_select():
    global screen30
    global selected_toys
    global ORIGINAL_ROOT_DIR
    global path_for_toys
    global toys_info
    global purchasing_choice
    purchasing_choice = 5
    selected_toys = StringVar()
    selected_toys = toys_entry.get()
    print(selected_toys)
    screen30 = Toplevel(screen)
    screen30.title(selected_toys)
    screen30.geometry("500x500")

    os.chdir(path_for_toys)
    

    f= open(selected_toys)
    toys_info = f.readlines()
    print(toys_info)

    Label(screen30, text = "Product name:", font=('Helvetica', 13, 'bold')).pack()
    Label(screen30, text = toys_info[0]).pack()

    Label(screen30, text = "Price:", font=('Helvetica', 13, 'bold')).pack()
    Label(screen30, text = toys_info[1]).pack()

    Label(screen30, text = "Description;", font=("Helvetica", 13, "bold")).pack()
    Label(screen30, text = toys_info[8]).pack()

    Label(screen30, text = "Sold by:", font=("Helvetica", 13, "bold")).pack()
    Label(screen30, text = toys_info[2]).pack()

    purchase = Button(screen30, text = "Purchase", command = purchase_screen)
    purchase.pack()




def toys():
    global screen19
    global toys_list
    global toys_entry
    global toys_list_data
    global path_for_toys
    screen19 = Toplevel(screen)
    screen19.title("Toys")
    screen19.geometry("500x500")

    Label(screen19, text = "Toys").pack()

    toys_entry = Entry(screen19,)
    toys_entry.pack()

    #create a list box
    toys_list = Listbox(screen19)
    toys_list.pack()

    #create a list
    toys_list_data = os.listdir(path_for_toys)
    #testing479 = os.listdir(path_for_books)
    #print(testing479)

    #Add the data to the list
    update_toys(toys_list_data)

    #Create a binding on the listbox onclick
    toys_list.bind("<<ListboxSelect>>", fillout_toys)

    #Create a binding on the entry box
    toys_entry.bind("<KeyRelease>", check_toys)



    #Button to select
    toys_button = Button(screen19, text = "Select", command = toys_select)
    toys_button.pack()


def update_clothes_jewellery(clothes_jewellery_list_data):
    global clothes_jewellery_list
    #Clear the listbox
    clothes_jewellery_list.delete(0, END)

    #Add data to listbox
    for item in clothes_jewellery_list_data:
        clothes_jewellery_list.insert(END, item)


#Update entry box with listbox clicked
def fillout_clothes_jewellery(event):
    global clothes_jewellery_entry
    #Delete whatever is in the entry box
    clothes_jewellery_entry.delete(0, END)

    #Add clicked list item to entry box
    clothes_jewellery_entry.insert(0, clothes_jewellery_list.get(ACTIVE))



def check_clothes_jewellery(event):
    #Grab what was typed
    global clothes_jewellery_entry
    global clothes_jewellery_list_data
    typed_clothes_jewellery = clothes_jewellery_entry.get()

    if typed_clothes_jewellery == " ":
        data = clothes_jewellery_list_data
    else:
        data = []
        for item in clothes_jewellery_list_data:
            if typed_clothes_jewellery.lower() in item.lower():
                data.append(item)
    update_clothes_jewellery(data)    


def clothes_jewellery_select():
    global screen31
    global selected_clothes_jewellery
    global ORIGINAL_ROOT_DIR
    global path_for_clothesjewellery
    global clothes_jewellery_info
    global purchasing_choice
    purchasing_choice = 6
    selected_clothes_jewellery = StringVar()
    selected_clothes_jewellery = clothes_jewellery_entry.get()
    print(selected_clothes_jewellery)
    screen31 = Toplevel(screen)
    screen31.title(selected_clothes_jewellery)
    screen31.geometry("500x500")

    os.chdir(path_for_clothesjewellery)
    

    f= open(selected_clothes_jewellery)
    clothes_jewellery_info = f.readlines()
    print(clothes_jewellery_info)

    Label(screen31, text = "Product name:", font=('Helvetica', 13, 'bold')).pack()
    Label(screen31, text = clothes_jewellery_info[0]).pack()

    Label(screen31, text = "Price:", font=('Helvetica', 13, 'bold')).pack()
    Label(screen31, text = clothes_jewellery_info[1]).pack()

    Label(screen31, text = "Description;", font=("Helvetica", 13, "bold")).pack()
    Label(screen31, text = clothes_jewellery_info[8]).pack()

    Label(screen31, text = "Sold by:", font=("Helvetica", 13, "bold")).pack()
    Label(screen31, text = clothes_jewellery_info[2]).pack()

    purchase = Button(screen31, text = "Purchase", command = purchase_screen)
    purchase.pack()


def clothes_jewellery():
    global screen20
    global clothes_jewellery_list
    global clothes_jewellery_entry
    global clothes_jewellery_list_data
    global path_for_clothesjewellery
    screen20 = Toplevel(screen)
    screen20.title("Clothes & Jewellery")
    screen20.geometry("500x500")

    Label(screen20, text = "Clothes & Jewellery").pack()

    clothes_jewellery_entry = Entry(screen20,)
    clothes_jewellery_entry.pack()

    #create a list box
    clothes_jewellery_list = Listbox(screen20)
    clothes_jewellery_list.pack()

    #create a list
    clothes_jewellery_list_data = os.listdir(path_for_clothesjewellery)
    #testing479 = os.listdir(path_for_books)
    #print(testing479)

    #Add the data to the list
    update_clothes_jewellery(clothes_jewellery_list_data)

    #Create a binding on the listbox onclick
    clothes_jewellery_list.bind("<<ListboxSelect>>", fillout_clothes_jewellery)

    #Create a binding on the entry box
    clothes_jewellery_entry.bind("<KeyRelease>", check_clothes_jewellery)



    #Button to select
    clothes_jewellery_button = Button(screen20, text = "Select", command = clothes_jewellery_select)
    clothes_jewellery_button.pack()



def update_sports_outdoors(sports_outdoors_list_data):
    global sports_outdoors_list
    #Clear the listbox
    sports_outdoors_list.delete(0, END)

    #Add data to listbox
    for item in sports_outdoors_list_data:
        sports_outdoors_list.insert(END, item)


#Update entry box with listbox clicked
def fillout_sports_outdoors(event):
    global sports_outdoors_entry
    #Delete whatever is in the entry box
    sports_outdoors_entry.delete(0, END)

    #Add clicked list item to entry box
    sports_outdoors_entry.insert(0, sports_outdoors_list.get(ACTIVE))



def check_sports_outdoors(event):
    #Grab what was typed
    global sports_outdoors_entry
    global sports_outdoors_list_data
    typed_sports_outdoors = sports_outdoors_entry.get()

    if typed_sports_outdoors == " ":
        data = sports_outdoors_list_data
    else:
        data = []
        for item in sports_outdoors_list_data:
            if typed_sports_outdoors.lower() in item.lower():
                data.append(item)
    update_sports_outdoors(data)    





def sports_outdoors_select():
    global screen32
    global selected_sports_outdoors
    global ORIGINAL_ROOT_DIR
    global path_for_sportsoutdoors
    global sports_outdoors_info
    global purchasing_choice
    purchasing_choice = 7
    selected_sports_outdoors = StringVar()
    selected_sports_outdoors = sports_outdoors_entry.get()
    print(selected_sports_outdoors)
    screen32 = Toplevel(screen)
    screen32.title(selected_sports_outdoors)
    screen32.geometry("500x500")

    os.chdir(path_for_sportsoutdoors)
    

    f= open(selected_sports_outdoors)
    sports_outdoors_info = f.readlines()
    print(sports_outdoors_info)

    Label(screen32, text = "Product name:", font=('Helvetica', 13, 'bold')).pack()
    Label(screen32, text = sports_outdoors_info[0]).pack()

    Label(screen32, text = "Price:", font=('Helvetica', 13, 'bold')).pack()
    Label(screen32, text = sports_outdoors_info[1]).pack()

    Label(screen32, text = "Description;", font=("Helvetica", 13, "bold")).pack()
    Label(screen32, text = sports_outdoors_info[8]).pack()

    Label(screen32, text = "Sold by:", font=("Helvetica", 13, "bold")).pack()
    Label(screen32, text = sports_outdoors_info[2]).pack()

    purchase = Button(screen32, text = "Purchase", command = purchase_screen)
    purchase.pack()


def sports_outdoors():
    global screen21
    global sports_outdoors_list
    global sports_outdoors_entry
    global sports_outdoors_list_data
    global path_for_sportsoutdoors
    screen21 = Toplevel(screen)
    screen21.title("Sports & Outdoors")
    screen21.geometry("500x500")

    Label(screen21, text = "Sports & Outdoors").pack()

    sports_outdoors_entry = Entry(screen21,)
    sports_outdoors_entry.pack()

    #create a list box
    sports_outdoors_list = Listbox(screen21)
    sports_outdoors_list.pack()

    #create a list
    sports_outdoors_list_data = os.listdir(path_for_sportsoutdoors)
    #testing479 = os.listdir(path_for_books)
    #print(testing479)

    #Add the data to the list
    update_sports_outdoors(sports_outdoors_list_data)

    #Create a binding on the listbox onclick
    sports_outdoors_list.bind("<<ListboxSelect>>", fillout_sports_outdoors)

    #Create a binding on the entry box
    sports_outdoors_entry.bind("<KeyRelease>", check_sports_outdoors)


    #Button to select
    sports_outdoors_button = Button(screen21, text = "Select", command = sports_outdoors_select)
    sports_outdoors_button.pack()

    


def update_food(food_list_data):
    global food_list
    #Clear the listbox
    food_list.delete(0, END)

    #Add data to listbox
    for item in food_list_data:
        food_list.insert(END, item)


#Update entry box with listbox clicked
def fillout_food(event):
    global food_entry
    #Delete whatever is in the entry box
    food_entry.delete(0, END)

    #Add clicked list item to entry box
    food_entry.insert(0, food_list.get(ACTIVE))



def check_food(event):
    #Grab what was typed
    global food_entry
    global food_list_data
    typed_food = food_entry.get()

    if typed_food == " ":
        data = food_list_data
    else:
        data = []
        for item in food_list_data:
            if typed_food.lower() in item.lower():
                data.append(item)
    update_food(data)    




def food_select():
    global screen33
    global selected_food
    global ORIGINAL_ROOT_DIR
    global path_for_food
    global food_info
    global purchasing_choice
    purchasing_choice = 8
    selected_food = StringVar()
    selected_food = food_entry.get()
    print(selected_food)
    screen33 = Toplevel(screen)
    screen33.title(selected_food)
    screen33.geometry("500x500")

    os.chdir(path_for_food)
    

    f= open(selected_food)
    food_info = f.readlines()
    print(food_info)

    Label(screen33, text = "Product name:", font=('Helvetica', 13, 'bold')).pack()
    Label(screen33, text = food_info[0]).pack()

    Label(screen33, text = "Price:", font=('Helvetica', 13, 'bold')).pack()
    Label(screen33, text = food_info[1]).pack()

    Label(screen33, text = "Description;", font=("Helvetica", 13, "bold")).pack()
    Label(screen33, text = food_info[8]).pack()

    Label(screen33, text = "Sold by:", font=("Helvetica", 13, "bold")).pack()
    Label(screen33, text = food_info[2]).pack()

    purchase = Button(screen33, text = "Purchase", command = purchase_screen)
    purchase.pack()




def food():
    global screen22
    global food_list
    global food_entry
    global food_list_data
    global path_for_food
    screen22 = Toplevel(screen)
    screen22.title("Food")
    screen22.geometry("500x500")

    Label(screen22, text = "Food").pack()

    food_entry = Entry(screen22,)
    food_entry.pack()

    #create a list box
    food_list = Listbox(screen22)
    food_list.pack()

    #create a list
    food_list_data = os.listdir(path_for_food)
    #testing479 = os.listdir(path_for_books)
    #print(testing479)

    #Add the data to the list
    update_food(food_list_data)

    #Create a binding on the listbox onclick
    food_list.bind("<<ListboxSelect>>", fillout_food)

    #Create a binding on the entry box
    food_entry.bind("<KeyRelease>", check_food)
    


    #Button to select
    food_button = Button(screen22, text = "Select", command = food_select)
    food_button.pack()


def update_health(health_list_data):
    global health_list
    #Clear the listbox
    health_list.delete(0, END)

    #Add data to listbox
    for item in health_list_data:
        health_list.insert(END, item)


#Update entry box with listbox clicked
def fillout_health(event):
    global health_entry
    #Delete whatever is in the entry box
    health_entry.delete(0, END)

    #Add clicked list item to entry box
    health_entry.insert(0, health_list.get(ACTIVE))



def check_health(event):
    #Grab what was typed
    global health_entry
    global health_list_data
    typed_health = health_entry.get()

    if typed_health == " ":
        data = health_list_data
    else:
        data = []
        for item in health_list_data:
            if typed_health.lower() in item.lower():
                data.append(item)
    update_health(data)    



def health_select():
    global screen34
    global selected_health
    global ORIGINAL_ROOT_DIR
    global path_for_health
    global health_info
    global purchasing_choice
    purchasing_choice = 9
    selected_health = StringVar()
    selected_health = health_entry.get()
    print(selected_health)
    screen34 = Toplevel(screen)
    screen34.title(selected_health)
    screen34.geometry("500x500")

    os.chdir(path_for_health)
    

    f= open(selected_health)
    health_info = f.readlines()
    print(health_info)

    Label(screen34, text = "Product name:", font=('Helvetica', 13, 'bold')).pack()
    Label(screen34, text = health_info[0]).pack()

    Label(screen34, text = "Price:", font=('Helvetica', 13, 'bold')).pack()
    Label(screen34, text = health_info[1]).pack()

    Label(screen34, text = "Description;", font=("Helvetica", 13, "bold")).pack()
    Label(screen34, text = health_info[8]).pack()

    Label(screen34, text = "Sold by:", font=("Helvetica", 13, "bold")).pack()
    Label(screen34, text = health_info[2]).pack()

    purchase = Button(screen35, text = "Purchase", command = purchase_screen)
    purchase.pack()




def health():
    global screen23
    global health_list
    global health_entry
    global health_list_data
    global path_for_health
    screen23 = Toplevel(screen)
    screen23.title("Health")
    screen23.geometry("500x500")

    Label(screen23, text = "Health").pack()

    health_entry = Entry(screen23,)
    health_entry.pack()

    #create a list box
    health_list = Listbox(screen23)
    health_list.pack()

    #create a list
    health_list_data = os.listdir(path_for_health)
    #testing479 = os.listdir(path_for_books)
    #print(testing479)

    #Add the data to the list
    update_health(health_list_data)

    #Create a binding on the listbox onclick
    health_list.bind("<<ListboxSelect>>", fillout_health)

    #Create a binding on the entry box
    health_entry.bind("<KeyRelease>", check_health)



    #Button to select
    health_button = Button(screen23, text = "Select", command = health_select)
    health_button.pack()

    




def update_motor_vehicles(motor_vehicles_list_data):
    global motor_vehicles_list
    #Clear the listbox
    motor_vehicles_list.delete(0, END)

    #Add data to listbox
    for item in motor_vehicles_list_data:
        motor_vehicles_list.insert(END, item)


#Update entry box with listbox clicked
def fillout_motor_vehicles(event):
    global motor_vehicles_entry
    #Delete whatever is in the entry box
    motor_vehicles_entry.delete(0, END)

    #Add clicked list item to entry box
    motor_vehicles_entry.insert(0, motor_vehicles_list.get(ACTIVE))



def check_motor_vehicles(event):
    #Grab what was typed
    global motor_vehicles_entry
    global motor_vehicles_list_data
    typed_motor_vehicles = motor_vehicles_entry.get()

    if typed_motor_vehicles == " ":
        data = motor_vehicles_list_data
    else:
        data = []
        for item in motor_vehicles_list_data:
            if typed_motor_vehicles.lower() in item.lower():
                data.append(item)
    update_motor_vehicles(data)    


def motor_vehicles_select():
    global screen35
    global selected_motor_vehicles
    global ORIGINAL_ROOT_DIR
    global path_for_motorvehicles
    global motor_vehicles_info
    global purchasing_choice
    purchasing_choice = 10
    selected_motor_vehicles = StringVar()
    selected_motor_vehicles = motor_vehicles_entry.get()
    print(selected_motor_vehicles)
    screen35 = Toplevel(screen)
    screen35.title(selected_motor_vehicles)
    screen35.geometry("500x500")

    os.chdir(path_for_motorvehicles)
    

    f= open(selected_motor_vehicles)
    motor_vehicles_info = f.readlines()
    print(motor_vehicles_info)
    

    Label(screen35, text = "Product name:", font=('Helvetica', 13, 'bold')).pack()
    Label(screen35, text = motor_vehicles_info[0]).pack()

    Label(screen35, text = "Price:", font=('Helvetica', 13, 'bold')).pack()
    Label(screen35, text = motor_vehicles_info[1]).pack()

    Label(screen35, text = "Description;", font=("Helvetica", 13, "bold")).pack()
    Label(screen35, text = motor_vehicles_info[8]).pack()

    Label(screen35, text = "Sold by:", font=("Helvetica", 13, "bold")).pack()
    Label(screen35, text = motor_vehicles_info[2]).pack()

    purchase = Button(screen35, text = "Purchase", command = purchase_screen)
    purchase.pack()



def motor_vehicles():
    global screen24
    global motor_vehicles_list
    global motor_vehicles_entry
    global motor_vehicles_list_data
    global path_for_motorvehicles
    screen24 = Toplevel(screen)
    screen24.title("Motor Vehicles")
    screen24.geometry("500x500")

    Label(screen24, text = "Motor vehicles").pack()

    motor_vehicles_entry = Entry(screen24,)
    motor_vehicles_entry.pack()

    #create a list box
    motor_vehicles_list = Listbox(screen24)
    motor_vehicles_list.pack()

    #create a list
    motor_vehicles_list_data = os.listdir(path_for_motorvehicles)
    #testing479 = os.listdir(path_for_books)
    #print(testing479)

    #Add the data to the list
    update_motor_vehicles(motor_vehicles_list_data)

    #Create a binding on the listbox onclick
    motor_vehicles_list.bind("<<ListboxSelect>>", fillout_motor_vehicles)

    #Create a binding on the entry box
    motor_vehicles_entry.bind("<KeyRelease>", check_motor_vehicles)


    #Button to select
    motor_vehicles_button = Button(screen24, text = "Select", command = motor_vehicles_select)
    motor_vehicles_button.pack()

    









def update_education(education_list_data):
    global education_list
    #Clear the listbox
    education_list.delete(0, END)

    #Add data to listbox
    for item in education_list_data:
        education_list.insert(END, item)


#Update entry box with listbox clicked
def fillout_education(event):
    global education_entry
    #Delete whatever is in the entry box
    education_entry.delete(0, END)

    #Add clicked list item to entry box
    education_entry.insert(0, education_list.get(ACTIVE))



def check_education(event):
    #Grab what was typed
    global education_entry
    global education_list_data
    typed_education = education_entry.get()

    if typed_education == " ":
        data =education_list_data
    else:
        data = []
        for item in education_list_data:
            if typed_education.lower() in item.lower():
                data.append(item)
    update_education(data)    



def education_select():
    global screen36
    global selected_education
    global ORIGINAL_ROOT_DIR
    global path_for_education
    global education_info
    global purchasing_choice
    purchasing_choice = 11
    selected_education = StringVar()
    selected_education = education_entry.get()
    print(selected_education)
    screen36 = Toplevel(screen)
    screen36.title(selected_education)
    screen36.geometry("500x500")

    os.chdir(path_for_education)
    

    f= open(selected_education)
    education_info = f.readlines()
    print(education_info)

    Label(screen36, text = "Product name:", font=('Helvetica', 13, 'bold')).pack()
    Label(screen36, text = education_info[0]).pack()

    Label(screen36, text = "Price:", font=('Helvetica', 13, 'bold')).pack()
    Label(screen36, text = education_info[1]).pack()

    Label(screen36, text = "Description;", font=("Helvetica", 13, "bold")).pack()
    Label(screen36, text = education_info[8]).pack()

    Label(screen36, text = "Sold by:", font=("Helvetica", 13, "bold")).pack()
    Label(screen36, text = education_info[2]).pack()

    education_select_button = Button(screen36, text = "Purchase", command = purchase_screen)
    education_select_button.pack()

    





def education():
    global screen25
    global education_list
    global education_entry
    global education_list_data
    global path_for_education
    screen25 = Toplevel(screen)
    screen25.title("Education")
    screen25.geometry("500x500")

    Label(screen25, text = "Education").pack()

    education_entry = Entry(screen25,)
    education_entry.pack()

    #create a list box
    education_list = Listbox(screen25)
    education_list.pack()

    #create a list
    education_list_data = os.listdir(path_for_education)
    #testing479 = os.listdir(path_for_books)
    #print(testing479)

    #Add the data to the list
    update_education(education_list_data)

    #Create a binding on the listbox onclick
    education_list.bind("<<ListboxSelect>>", fillout_education)

    #Create a binding on the entry box
    education_entry.bind("<KeyRelease>", check_education)





    #Button to select
    education_button = Button(screen25, text = "Select", command = education_select)
    education_button.pack()

    

def purchase_screen():
    global screen37
    global ORIGINAL_ROOT_DIR
    global purchasing_directory
    global purchasing_choice
    global purchasing_product
    global selected_book
    global selected_game
    global selected_electronic
    global selected_home_garden
    global selected_toys
    global selected_clothes_jewellery
    global selected_sports_outdoors
    global selected_food
    global selected_health
    global selected_motor_vehicles
    global selected_education
    global path_for_products
    global path_for_books
    global path_for_games
    global path_for_electronics
    global path_for_homegarden
    global path_for_toys
    global path_for_clothesjewellery
    global path_for_sportsoutdoors
    global path_for_food
    global path_for_health
    global path_for_motorvehicles
    global path_for_education
    global user_dir



    print(path_for_health)

    
    if purchasing_choice == 1:
        purchasing_product = selected_book
        purchasing_directory = path_for_books
    elif purchasing_choice == 2:
        purchasing_product = selected_game
        purchasing_directory = path_for_games
    elif purchasing_choice == 3:
        purchasing_product = selected_electronic
        purchasing_directory = path_for_electronics
    elif purchasing_choice == 4:
        purchasing_product = selected_home_garden
        purchasing_directory = path_for_homegarden
    elif purchasing_choice == 5:
        purchasing_product = selected_toys
        purchasing_directory = path_for_toys
    elif purchasing_choice == 6:
        purchasing_product = selected_clothes_jewellery
        purchasing_directory = path_for_clothesjewellery
    elif purchasing_choice == 7:
        purchasing_product = selected_sports_outdoors
        purchasing_directory = path_for_sportsoutdoors
    elif purchasing_choice == 8:
        purchasing_product = selected_food
        purchasing_directory = path_for_food
    elif purchasing_choice == 9:
        purchasing_product = selected_health
        purchasing_directory = path_for_health
    elif purchasing_choice == 10:
        purchasing_product = selected_motor_vehicles
        purchasing_directory = path_for_motorvehicles
    elif purchasing_choice == 11:
        purchasing_product = selected_education.get()
        purchasing_directory = path_for_education.get()
    else:
        print("I really can't be asked to fix this issue")



    screen37 = Toplevel(screen)
    screen37.title("Purchasing Screen")
    screen37.geometry("500x500")

    Label(screen37, text = "Item:", font=('Helvetica', 13, 'bold')).pack()
    print(purchasing_product)
    print(purchasing_directory)
    os.chdir(purchasing_directory)
    f= open(purchasing_product)
    purchasing_info = f.readlines()
    print(purchasing_info)
    print(username1)

    Label(screen37, text = "Product name:", font=('Helvetica', 13, 'bold')).pack()
    Label(screen37, text = purchasing_info[0]).pack()

    Label(screen37, text = "Price:", font=('Helvetica', 13, 'bold')).pack()
    Label(screen37, text = purchasing_info[1]).pack()


    os.chdir(user_dir)
    f= open(username1)
    content = f.readlines()

    Label(screen37, text = "Address Line 2:", font=('Helvetica', 13, 'bold')).pack()
    Label(screen37, text = content[3]).pack()


    Button(screen37, text = "Purchase", command = final_screen).pack()

    
    
def final_screen():
    global screen38
    global screen8
    global purchasing_choice
    
    screen38 = Toplevel(screen)
    screen38.title("Congratualtions")
    screen38.geometry("500x500")

    Label(screen38, text = "Can't even spell congratulations").pack()
    Label(screen38, text = "Product purchased").pack()
    screen37.destroy()
    screen8.destroy()


    if purchasing_choice == 1:
        screen26.destroy()
        screen15.destroy()
    elif purchasing_choice == 2:
        screen27.destroy()
        screen16.destroy()
    elif purchasing_choice == 3:
        screen28.destroy()
        screen17.destroy()
    elif purchasing_choice == 4:
        screen29.destroy()
        screen18.destroy()
    elif purchasing_choice == 5:
        screen30.destroy()
        screen19.destroy()
    elif purchasing_choice == 6:
        screen31.destroy()
        screen20.destroy()
    elif purchasing_choice == 7:
        screen32.destroy()
        screen21.destroy()
    elif purchasing_choice == 8:
        screen33.destroy()
        screen22.destroy()
    elif purchasing_choice == 9:
        screen34.destroy()
        screen23.destroy()
    elif purchasing_choice == 10:
        screen35.destroy()
        screen24.destroy()
    elif purchasing_choice == 11:
        screen36.destroy()
        screen25.destroy()
    

    

    
    


    
    
    



def log_out():
    
    screen6.destroy()
  

    
 
def review_mainmenu():
    global screen39
    screen39 = Toplevel(screen)
    screen39.title("Reviews")
    screen39.geometry("350x500")
    Label(screen39, text = "Review Main Menu").pack()

    Button(screen39, text = "Leave a review", command=review_write_select_user).pack()
    Button(screen39, text = "Look at seller's rating", command = review_read_select_user).pack()


def update_user_list_read(user_list_data_read):
    global user_list_read
    #Clear the listbox
    user_list_read.delete(0, END)

    #Add data to listbox
    for item in user_list_data_read:
        user_list_read.insert(END, item)
      
#Update entry box with listbox clicked
def fillout_user_list_read(event):
    global review_read_user_entry
    #Delete whatever is in the entry box
    review_read_user_entry.delete(0, END)
    #Add clicked list item to entry box
    review_read_user_entry.insert(0, user_list_read.get(ACTIVE))

def check_user_list_read(event):
    #Grab what was typed
    global review_read_user_entry
    global user_list_data_read
    typed_user_read = review_read_user_entry.get()
    if typed_user_read == " ":
        data = user_list_data_read
    else:
        data = []
        for item in user_list_data_read:
            if typed_user_read.lower() in item.lower():
                data.append(item)
    update_user_list_read(data)




def review_read_select_user():
    global screen43 # Defiing a new screen
    global review_read_user_entry # Globalising the variable "review_read_user_entry"
    global user_list_read # Globalising the variable "user_list_read" (List of all users)
    global path_for_users # Globalising the variable "path_for_users" (User directory)
    global user_list_data_read # Globalising the variable "user_list_data_read"
    screen43 = Toplevel(screen) # Making this screen appear at the top
    screen43.title("Selecting the User") # Defining the header of the screen
    screen43.geometry("350x500") # Defining the dimensions of the screen
    review_read_user_entry = Entry(screen43,)
    review_read_user_entry.pack()
    #create a list box
    user_list_read = Listbox(screen43)
    user_list_read.pack()
    #create a list
    user_list_data_read = os.listdir(path_for_users)
    # Creating an array "user_list_data_read"
    # Through the os.listdir function, going through the directory with the path as the value of the variable "path_for_users" (User directory)
    # Storing the contents of each file name (which would also be the username for each user) into the array "user_list_data_read"

    #Add the data to the list
    update_user_list_read(user_list_data_read)
    #Create a binding on the listbox onclick
    user_list_read.bind("<<ListboxSelect>>", fillout_user_list_read)
    #Create a binding on the entry box
    review_read_user_entry.bind("<KeyRelease>", check_user_list_read)
    #Button to select
    review_read_button = Button(screen43, text = "Select", command = review_read)
    review_read_button.pack()  
    
    #use this to separate the users name and the review header, use this to search through the reviews
    #user would input a name, the function would implement this to the data
    #x = filename.split(selected_user)
    #print(x)





def review_read():
    global screen44
    global path_for_reviews
    global selected_user
    global review_read_user_entry

    screen44 = Toplevel(screen)
    screen44.title("Select review")
    screen44.geometry("350x500")
    Label(screen44, text = "Select a review").pack()

def review_write():
    global screen41 # Defining a new screen
    global path_for_reviews # Globalising the variable "path_for_reviews" (Review directory)
    global header_entry # Globalising the variable "header_entry" (Variable to store review header)
    global review_entry # Globalising the variable "review_entry" (Varaible to store main body of review)
    global selected_user # Globalising the variable "selected_user" (Variable to store the seller username)
    global review_write_user_entry # Globalising the variable "review_write_user_entry"
    screen41 = Toplevel(screen) # Making this screen appear at the top
    screen41.title("Leave a review") # Defining the header of this screen
    screen41.geometry("350x500") # Defining the dimensions of this screen
    Label(screen40, text = "Leaving a review").pack()

    review_entry = StringVar() # Declaring the variable "review_entry" as a string variable
    header_entry = StringVar() # Declaring the variable "header_entry" as a string variable
    os.chdir(path_for_reviews) # Changing the directory to the value of the variable "path_for_review" (Review directory)
    Label(screen41, text = "Header").pack()
    header_entry= Entry(screen41) # Storing the value of the user input for the review header to the variable "header_entry"
    header_entry.pack()

    Label(screen41, text = "Description of review").pack()
    review_entry = Text(screen41, height = 8, width = 60)
    # Storing the value of the user input for the description of the review to the variable "review_entry"
    review_entry.pack()

    selected_user = StringVar() # Declaring the variable "selected_user" as a string variable
    selected_user = review_write_user_entry.get() # Assigning the value of "review_write_user_entry" to the variable "selected_user"
    print(selected_user)
    Button(screen41, text = "Store values", command=review_write_store).pack()

 




def review_write_store():
    global screen42 # Defining a new screen
    global header # Globalising the variable "header" (variable to store user header)
    global review # Globalising the variable "review" (variable to store main body of review)
    global selected_user # Globalising the variable "selected_user" (variable to store the seller that the review is in regards with)
    header = header_entry.get() # Assigning the value of the variable "header_entry" to the variable "header"
    review = review_entry.get(1.0 , END) # Assigning the value of the variable "review_entry" to the variable "review"
    print(header)
    print(review)
    print(selected_user)
    filename = selected_user + header
    # Concatenates the values of the variables "selected_user" and "header"
    # Assigning this value to the variable "filename"
    # This is done for easier searching of reviews by seller
    print(filename)


    os.chdir(path_for_reviews) # Changing the directory to the value of the variable "path_for_reviews"
    file=open(filename, "w") # Creating a new file with the value of the variable "filename" as the name for the file
    file.write(header+"\n") # Writing the value of the variable "header" to the file
    file.write(review+"\n") # Writing the value of the variable "review" to the file
    file.close() # Closing the file so that no more changes can be made to it

    Label(screen41, text = "Review submitted").pack()
    screen41.destroy() # Deleting the screen
    

 
def update_user_list_write(user_list_data_write):
    global user_list_write
    #Clear the listbox
    user_list_write.delete(0, END)
    #Add data to listbox
    for item in user_list_data_write:
        user_list_write.insert(END, item)

#Update entry box with listbox clicked
def fillout_user_list_write(event):
    global review_write_user_entry
    #Delete whatever is in the entry box
    review_write_user_entry.delete(0, END)
    #Add clicked list item to entry box
    review_write_user_entry.insert(0, user_list_write.get(ACTIVE))

def check_user_list_write(event):
    #Grab what was typed
    global review_write_user_entry
    global user_list_data_write
    typed_user_write = review_write_user_entry.get()
    if typed_user_write == " ":
        data = user_list_data_write
    else:
        data = []
        for item in user_list_data_write:
            if typed_user_write.lower() in item.lower():
                data.append(item)
    update_user_list_write(data)




def review_write_select_user():
    global screen40 # Defining a new screen
    global review_write_user_entry # Globalising the variable "review_write_user_entry"
    global user_list_write # Globalising the variable "user_list_write"
    global path_for_users # Globalising the variable "path_for_users"
    global user_list_data_write # Globalising the variable "user_list_data_write"
    screen40 = Toplevel(screen) # Making this screen appear at the top
    screen40.title("Selecting the User") # Defining the header of the screen
    screen40.geometry("350x500") # Defining the dimensions of the screen
    review_write_user_entry = Entry(screen40,)
    review_write_user_entry.pack() # Creating an entry box, within which the user would enter the seller name for who they want to write a review
    #create a list box
    user_list_write = Listbox(screen40)
    user_list_write.pack()
    #create a list
    user_list_data_write = os.listdir(path_for_users)
    # Creating an array "user_list_write_data"
    # Would open the directory under the value of the variable "path_for_users" (user directory)
    # File names would be all the usernames registered within the online marketplace
    # Assign the value of all the filenames to the array "user_list_write_data"
    #Add the data to the list
    update_user_list_write(user_list_data_write)
    #Create a binding on the listbox onclick
    user_list_write.bind("<<ListboxSelect>>", fillout_user_list_write)
    #Create a binding on the entry box
    review_write_user_entry.bind("<KeyRelease>", check_user_list_write)
    #Button to select
    review_write_button = Button(screen40, text = "Select", command = review_write)
    review_write_button.pack()  
    
    


def session():
    global screen6
    screen6 = Toplevel(screen)
    screen6.title("Account Dashboard")
    screen6.geometry("350x500")
    Label(screen6, text= "Welcome to the Dashboard").pack()
    Button(screen6, text="Account Management", command=account_management).pack()
    Button(screen6, text= " Buying", command=buying).pack()
    Button(screen6, text="Selling", command=selling).pack()
    Button(screen6, text="Logout", command=log_out).pack()
    Button(screen6, text="Reviews", command=review_mainmenu).pack()

    


def login_success():
    screen2.destroy()
    session()
    
def password_not_recognised():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Password Error")
    screen4.geometry("150x100")
    Label(screen4, text = "Password not recognised").pack()
    Button(screen4, text = "Ok", command = delete3).pack()

def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Error")
    screen5.geometry("150x100")
    Label(screen5, text = "User not found").pack()
    Button(screen5, text = "Ok", command = delete4).pack()


def register_user():
    global user_dir
    global ORIGINAL_ROOT_DIR
    global people_name
    taken_username = False
    username_info = username.get()
    password_info = password.get()
    address_1_info = address_line_1.get()
    address_2_info = address_line_2.get()
    postcode_info = postcode.get()



    os.chdir(ORIGINAL_ROOT_DIR)
    directory_for_users = ("Users")
    user_dir = os.path.join(ORIGINAL_ROOT_DIR, directory_for_users)
    print(user_dir)

    os.chdir(user_dir)
    list_of_files = os.listdir()
    if username_info in list_of_files:
        taken_username = True
        

    if taken_username == False:
        
        os.chdir(user_dir)
        print(user_dir)
        file=open(username_info, "w")
        file.write(username_info+"\n")
        file.write(password_info+"\n")
        file.write(address_1_info+"\n")
        file.write(address_2_info+"\n")
        file.write(postcode_info+"\n")
        file.close()

        username_entry.delete(0, END)
        password_entry.delete(0, END)
        postcode_entry.delete(0, END)
        address_line_1_entry.delete(0, END)
        address_line_2_entry.delete(0, END)

        Label(screen1, text = "Registration Success", fg = "green", font = ("Calibri", 11)).pack()
    else:
        username_entry.delete(0, END)
        password_entry.delete(0, END)

        Label(screen1, text = "Username taken", fg = "green", font = ("Calibri", 11)).pack()


def login_verify():
    global username1
    global password1
    global ORIGINAL_ROOT_DIR
    global username_info
    global user_dir
    print(ORIGINAL_ROOT_DIR)
    username1 = username_verify.get()
    password1 = password_verify.get()
    password1 = str(password1)
    username1 = str(username1)
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)


    
    directory_for_users = ("Users")
    user_dir = os.path.join(ORIGINAL_ROOT_DIR, directory_for_users)
    print(user_dir)

    os.chdir(user_dir)
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        their_password = verify[1]
        print(their_password)
        print(password1)
        print(password1 == verify[1])
        boolean_login = (password1 == verify[1])
        print(boolean_login)
        if boolean_login == True:
            os.listdir()
            login_success()
        else:
            password_not_recognised()
    else:
        user_not_found()
        


    

    

def register():
    global screen1
    screen1 = Toplevel (screen)
    screen1.title("Register")
    screen1.geometry("600x900")
    global username
    global password
    global username_entry
    global password_entry
    global address_line_1
    global address_line_2
    global postcode
    global address_line_1_entry
    global address_line_2_entry
    global postcode_entry
    
    username = StringVar()
    password = StringVar()
    postcode = StringVar()
    address_line_1 = StringVar()
    address_line_2 = StringVar()

    Label(screen1, text = "Please enter details below").pack()
    Label(screen1, text = " ").pack()
    Label(screen1, text= "Username * ").pack()

    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    Label(screen1, text = "Password * ").pack()
    password_entry = Entry(screen1, textvariable = password)
    password_entry.pack()
    Label(screen1, text = "").pack()
    Label(screen1, text="1st address line").pack()
    address_line_1_entry = Entry(screen1, textvariable = address_line_1)
    address_line_1_entry.pack()
    Label(screen1, text="2nd line of address/town").pack()
    address_line_2_entry = Entry(screen1, textvariable = address_line_2)
    address_line_2_entry.pack()
    Label(screen1, text = "Postcode*").pack()
    postcode_entry = Entry(screen1, textvariable = postcode)
    postcode_entry.pack()
    Button(screen1, text = "Register", width = 10, height = 1, command = register_user).pack()


def login():
    print("Login session started")
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")
    Label(screen2, text = "Please enter details below to login").pack()
    Label(screen2, text = " ").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1

    Label(screen2, text = "Username * ").pack()
    username_entry1 = Entry(screen2, textvariable = username_verify)
    username_entry1.pack()
    Label(screen2, text=" ").pack()
    Label(screen2, text = "Password * ").pack()
    password_entry1 = Entry(screen2, textvariable = password_verify)
    password_entry1.pack()
    Label(screen2, text=" ").pack()
    Button(screen2, text="Login", width = 10, height = 1, command = login_verify).pack()
    
    
def selling():
    global screen9
    global product_entry
    global price_entry
    global clicked
    global keyword1_entry
    global keyword2_entry
    global keyword3_entry
    global description_entry
    global str_out
    global options

    screen9 = Toplevel(screen)
    screen9.title("Generate a post")
    screen9.geometry("1000x1000")

    product_entry = StringVar()
    price_entry = IntVar()
    
    Label(screen9, text = "Product name*").pack()
    product_entry = Entry(screen9)
    product_entry.pack()
    Label(screen9, text = "").pack()
    Label(screen9, text = "Price * ").pack()
    price_entry = Entry(screen9)
    price_entry.pack()
    Label(screen9, text = "").pack()
    Label(screen9, text = "Keyword 1:").pack()
    keyword1_entry = Entry(screen9)
    keyword1_entry.pack()
    Label(screen9, text = "").pack()
    Label(screen9, text = "Keyword 2:").pack()
    keyword2_entry = Entry(screen9)
    keyword2_entry.pack()
    Label(screen9, text = "").pack()
    Label(screen9, text = "Keyword 3:").pack()
    keyword3_entry = Entry(screen9)
    keyword3_entry.pack()
    Label(screen9, text = "").pack()
    Label(screen9, text = "Description:").pack()
    description_entry = Text(screen9, height = 8, width = 60)
    description_entry.pack()

    options = [
        "Books" ,
        "Games" ,
        "Electronics" ,
        "Home & Garden" ,
        "Toys" ,
        "Clothes & Jewellery" ,
        "Sports & Outdoors",
        "Food",
        "Health",
        "Motor Vehicles",
        "Education"
    ]

    clicked = StringVar()
    clicked.set(options[0])

    str_out = StringVar()
    str_out.set("Output")

    drop = OptionMenu(screen9, clicked, *options)
    drop.pack(pady=20)
    b1 = Button(screen9, text = "Select category", command=lambda: my_show())
    b1.pack()
    Label(screen9, textvariable=str_out).pack()


    Button(screen9, text = "List item for sale", width = 15, height = 2, command = store_products).pack()

def my_show():
    str_out.set(clicked.get())

    #special_button = Button(screen9, text = "Select from list", command=selected)
    #special_button.pack()





def store_products():
    global ORIGINAL_ROOT_DIR
    global path_for_products
    global path_for_books
    global path_for_games
    global path_for_electronics
    global path_for_homegarden
    global path_for_toys
    global path_for_clothesjewellery
    global path_for_sportsoutdoors
    global path_for_food
    global path_for_health
    global path_for_motorvehicles
    global path_for_education
    print(ORIGINAL_ROOT_DIR)
    print("Works")
    product1 = product_entry.get()
    price1 = price_entry.get()
    category1 = clicked.get()
    keyword1 = keyword1_entry.get()
    keyword2 = keyword2_entry.get()
    keyword3 = keyword3_entry.get()
    description = description_entry.get(1.0 , END)
    print(username1)
    print(product1)
    print(category1)
    print(price1)
    print(keyword1)
    print(keyword2)
    print(keyword3)
    print(description)

    if category1 == "Books":
        print(path_for_books)
        os.chdir(path_for_books)
        
    elif category1 == "Games":
        os.chdir(path_for_games)
    elif category1 == "Electronics":
        os.chdir(path_for_electronics)
    elif category1 == "Home & Garden":
        os.chdir(path_for_homegarden)
    elif category1 == "Toys":
        os.chdir(path_for_toys)
    elif category1 == "Clothes & Jewellery":
        print(path_for_clothesjewellery)
        os.chdir(path_for_clothesjewellery)
    elif category1 == "Sports & Outdoors":
        print(path_for_sportsoutdoors)
        os.chdir(path_for_sportsoutdoors)
    elif category1 == "Food":
        os.chdir(path_for_food)
    elif category1 == "Health":
        os.chdir(path_for_health)
    elif category1 == "Motor Vehicles":
        os.chdir(path_for_motorvehicles)
    elif category1 == "Education":
        os.chdir(path_for_education)
    

    





    file=open(product1,  "w")
    file.write(product1+"\n")
    file.write(price1+"\n")
    file.write(username1+"\n")
    file.write(category1+"\n")
    file.write(keyword1+"\n")
    file.write(keyword2+"\n")
    file.write(keyword3+"\n")
    file.write(description+"\n")
    file.close()

    product_entry.delete(0, END)
    price_entry.delete(0, END)

    
    screen9.destroy()
    variable_1 = Label(screen6, text = "Product sucessfully listed", fg = "green", font = ("Calibri", 11)).pack()
     
    #label.after(1000, label.master.destroy)





def main_screen():
    global screen
    global ORIGINAL_ROOT_DIR
    global path_for_reviews # Globalising the variable "path_for_reviews"
    global path_for_products
    global path_for_books
    global path_for_games
    global path_for_electronics
    global path_for_homegarden
    global path_for_toys
    global path_for_clothesjewellery
    global path_for_sportsoutdoors
    global path_for_food
    global path_for_health
    global path_for_motorvehicles
    global path_for_education
    global path_for_users
    screen=Tk()
    screen.geometry("300x250")
    screen.title("Online Marketplace")
    Label(text = "Online Marketplace", bg = "grey", font = ("Calibri", 13)).pack()
    Label(text = " ").pack()
    Button(text = "Login", width = "30", height = "2", command = login).pack()
    Label(text = " ").pack()
    Button(text = "Register", height = "2", width = "30", command = register).pack()
    os.listdir()


    ORIGINAL_ROOT_DIR = StringVar() # Declaring the variable "ORIGINAL_ROOT_DIR" as string
    ORIGINAL_ROOT_DIR = os.getcwd() # Assigning the value of the current directory to the variable "ORIGINAL_ROOT_DIR"
    cwd = os.getcwd() # Assigning the value of the current directory to the variable "cwd"
    print(cwd)
    directory_for_users = ("Users") # Assigning the value "Users" to the variable "directory_for_users"
    path_for_users = os.path.join(cwd, directory_for_users)
    # Through the os.path.join function, it concatenates the values of the variables "cwd" and "directory_for_users"
    # Creating a new directory (where all user files will be stored)
    # Assigning the value of the directory to the variable "path_for_users"
    directory_for_reviews = ("Reviews") # Assigning the value "Reviews" to the variable "directory_for_reviews"
    path_for_reviews = os.path.join(cwd, directory_for_reviews)
    # Through the os.path.join function, it concatenates the values of the variables "cwd" and "directory_for_reviews"
    # Creating a new directory (where all review files would be stored)
    # Assigning the value of the directory to the variable "path_for_reviews"
    is_existing_users = os.path.exists(path_for_users)
  # Checking if the value of the variable "path_for_users" exists as a directory path
  # If it does, the value "True" would be assignined to the variable "is_existing_users"
  # If it does not exist, the value "False" would be assigned to the variable
    print(is_existing_users)
    if is_existing_users == True: # Intialising a conditional statement based on the value of the variable "is_existing_users"
      # If "True", it means that the user directory already exists
      # This means that the review directory would have already be generated
        print("Doing nothing")
    else:
      # If "False", it means that the user directory does not exist
      # This means that the review directory would have also not have been generated
      # Those directories would have to be made
        print("Creating the new directory")
        os.mkdir(path_for_users) # Making a directory path with the value of the variable "path_for_users"
        os.mkdir(path_for_reviews) # Making a directory path with the value of the variable "path_for_reviews"
        print("Made new directory")


    os.chdir(ORIGINAL_ROOT_DIR)
    cwd = os.getcwd()
    print(cwd)
    directory_for_products = ("Products")
    path_for_products = os.path.join(cwd, directory_for_products)

    is_existing_products = os.path.exists(path_for_products)
    print(is_existing_products)
    if is_existing_products == True:
        print("Doing nothing")
    else:
        print("Creating the new directory")
        os.mkdir(path_for_products)

    
    os.chdir(path_for_products)
    cwd = os.getcwd()
    print(cwd)
    directory_for_books = ("Books")
    path_for_books = os.path.join(cwd, directory_for_books)
    print(path_for_books)

    os.chdir(path_for_products)
    cwd = os.getcwd()
    print(cwd)
    directory_for_games = ("Games")
    path_for_games = os.path.join(cwd, directory_for_games)
    print(path_for_games)

    os.chdir(path_for_products)
    cwd = os.getcwd()
    print(cwd)
    directory_for_electronics = ("Electronics")
    path_for_electronics = os.path.join(cwd, directory_for_electronics)
    print(path_for_electronics)

    os.chdir(path_for_products)
    cwd = os.getcwd()
    print(cwd)
    directory_for_homegarden = ("Home")
    path_for_homegarden = os.path.join(cwd, directory_for_homegarden)
    print(path_for_homegarden)

    os.chdir(path_for_products)
    cwd = os.getcwd()
    print(cwd)
    directory_for_toys = ("Toys")
    path_for_toys = os.path.join(cwd, directory_for_toys)
    print(path_for_toys)

    os.chdir(path_for_products)
    cwd = os.getcwd()
    print(cwd)
    directory_for_clothesjewellery = ("Clothes")
    path_for_clothesjewellery = os.path.join(cwd, directory_for_clothesjewellery)
    print(path_for_clothesjewellery)

    os.chdir(path_for_products)
    cwd = os.getcwd()
    print(cwd)
    directory_for_sportsoutdoors = ("Sports")
    path_for_sportsoutdoors = os.path.join(cwd, directory_for_sportsoutdoors)
    print(path_for_sportsoutdoors)

    os.chdir(path_for_products)
    cwd = os.getcwd()
    print(cwd)
    directory_for_food = ("Food")
    path_for_food = os.path.join(cwd, directory_for_food)
    print(path_for_food)

    os.chdir(path_for_products)
    cwd = os.getcwd()
    directory_for_health = ("Health")
    path_for_health = os.path.join(cwd, directory_for_health)

    os.chdir(path_for_products)
    cwd = os.getcwd()
    directory_for_motorvehicles = ("MotorVehicles")
    path_for_motorvehicles = os.path.join(cwd, directory_for_motorvehicles)
    print(path_for_motorvehicles)

    os.chdir(path_for_products)
    cwd = os.getcwd()
    directory_for_education = ("Education")
    path_for_education = os.path.join(cwd, directory_for_education)
    print(path_for_education)
    
    
    is_existing_education = os.path.exists(path_for_education)
    print(is_existing_education)
    

    if is_existing_education == True:
        print("Doing nothing")
    else:
        print("Creating the new directory")
        os.mkdir(path_for_books)
        os.mkdir(path_for_games)
        os.mkdir(path_for_electronics)
        os.mkdir(path_for_homegarden)
        os.mkdir(path_for_toys)
        os.mkdir(path_for_clothesjewellery)
        os.mkdir(path_for_sportsoutdoors)
        os.mkdir(path_for_food)
        os.mkdir(path_for_health)
        os.mkdir(path_for_motorvehicles)
        os.mkdir(path_for_education)
        print("Made new directory")
        
        
    

    screen.mainloop()



main_screen()
