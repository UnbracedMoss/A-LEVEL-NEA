from tkinter import *
import os
from tkinter import filedialog
import pathlib


#Next unused screen: 27

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
    selected_book = book_entry.get()
    print(selected_book)
    screen26 = Toplevel(screen)
    screen26.title(selected_book)
    screen26.geometry("500x500")


    os.chdir(path_for_books)
    

    f= open(selected_book)
    book_info = f.readlines()
    print(book_info)



    




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
    


    
    



def log_out():
    
    screen6.destroy()
  
    
    
    
    


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
    screen=Tk()
    screen.geometry("300x250")
    screen.title("Online Marketplace")
    Label(text = "Online Marketplace", bg = "grey", font = ("Calibri", 13)).pack()
    Label(text = " ").pack()
    Button(text = "Login", width = "30", height = "2", command = login).pack()
    Label(text = " ").pack()
    Button(text = "Register", height = "2", width = "30", command = register).pack()
    os.listdir()


    ORIGINAL_ROOT_DIR = StringVar()
    ORIGINAL_ROOT_DIR = os.getcwd()
    cwd = os.getcwd()
    print(cwd)
    directory_for_users = ("Users")
    path_for_users = os.path.join(cwd, directory_for_users)
    is_existing_users = os.path.exists(path_for_users)
    print(is_existing_users)

    if is_existing_users == True:
        print("Doing nothing")
    else:
        print("Creating the new directory")
        os.mkdir(path_for_users)
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
