from tkinter import *
import os
from tkinter import filedialog
import pathlib

#Next unused screen: 16

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
def fillout(event):
    global book_entry
    #Delete whatever is in the entry box
    book_entry.delete(0, END)

    #Add clicked list item to entry box
    book_entry.insert(0, book_list.get(ACTIVE))

def check(event):
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
    

def books():
    global screen15
    global book_list
    global book_entry
    global book_list_data
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
    book_list_data = ["A", "b", "c", "d", "e"]

    #Add the data to the list
    update_book(book_list_data)

    #Create a binding on the listbox onclick
    book_list.bind("<<ListboxSelect>>", fillout)

    #Create a binding on the entry box
    book_entry.bind("<KeyRelease>", check)
    
def games():
    print("Games works")


def electronics():
    print("electronics works")

def home_garden():
    print("Home & Garden works")


def toys():
    print("Toys works")


def clothes_jewellery():
    print("Clothes and Jewellery works")


def sports_outdoors():
    print("Sports & Outdoors works")


def food():
    print("Food works")



def health():
    print("Health works")



def motor_vehicles():
    print("Motor vehicles works")



def education():
    print("Education works")



    
    



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
    global str_out
    global options

    screen9 = Toplevel(screen)
    screen9.title("Generate a post")
    screen9.geometry("500x500")

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


    
    Label(screen9, text = "").pack()
    Label(screen9, text = "").pack()
    Button(screen9, text = "List item for sale", width = 15, height = 2, command = store_products).pack()

def my_show():
    str_out.set(clicked.get())

    #special_button = Button(screen9, text = "Select from list", command=selected)
    #special_button.pack()





def store_products():
    global ORIGINAL_ROOT_DIR # Globalising the variable "ORIGINAL_ROOT_DIR"
    global path_for_products # Globalising the variable "path_for_products"
    global path_for_books # Globalising the variable "path_for_books"
    global path_for_games # Globalising the variable "path_for_games"
    global path_for_electronics # Globalising the variable "path_for_electronics"
    global path_for_homegarden # Globalising the variable "path_for_homegarden"
    global path_for_toys # Globalising the variable "path_for_toys"
    global path_for_clothesjewellery # Globalising the variable "path_for_clothesjewellery"
    global path_for_sportsoutdoors # Globalising the variable "path_for_sportsoutdoors"
    global path_for_food # Globalising the variable "path_for_food"
    global path_for_health # Globalising the variable "path_for_health"
    global path_for_motorvehicles # Globalising the variable "path_for_motorvehicles"
    global path_for_education # Globalising the variable "path_for_education"
    product1 = product_entry.get() # Assigning the value of the variable "product_entry" to the variable "product1"
    price1 = price_entry.get() # Assigning the value of the variable "price_entry" to the variable "price1"
    category1 = clicked.get() # Assigning the value of the variable "clicked" to the variable "category1"
    keyword1 = keyword1_entry.get() # Assigning the value of the variable "keyword1_entry" to the variable "keyword1"
    keyword2 = keyword2_entry.get() # Assigning the value of the variable "keyword2_entry" to the variable "keyword2"
    keyword3 = keyword3_entry.get() # Assigning the value of the variable "keyword3_entry" to the variable "keyword3"
    if category1 == "Books": # Intialising a conditional statement based on the value of the variable "category1"
        # If the value of "category1" equals "Books", it means it would have to be stored in the book directory
        print(path_for_books)
        os.chdir(path_for_books) # Changing the directory to the value of the variable "path_for_books" (book directory)
    elif category1 == "Games":
        # If the value of "category1" equals "Games", it means it would have to be stored in the games directory
        os.chdir(path_for_games) # Changing the directory to the value of the variable "path_for_games" (games directory)
    elif category1 == "Electronics":
        # If the value of "category1" equals "Electronics", it means it would have to be stored in the electronics directory
        os.chdir(path_for_electronics) # Changing the directory to the value of the variable "path_for_electronics" (electronics category)
    elif category1 == "Home & Garden":
        # If the value of "category1" equals "Home & Garden", it means it would have to be stored in the home & garden directory
        os.chdir(path_for_homegarden) # Changing the directory to the value of the variable "path_for_homegarden" (home & garden directory)
    elif category1 == "Toys":
        # If the value of "category1" equals "Toys", it means it would have to be stored in the toys directory
        os.chdir(path_for_toys) # Changing the directory to the value of the variable "path_for_toys" (toys directory)
    elif category1 == "Clothes & Jewellery":
        # If the value of "category1" equals "Clothes & Jewellery", it means it would have to be stored in the clothes & jewellery directory
        os.chdir(path_for_clothesjewellery) # Changing the directory to the value of the variable "path_for_clothesjewellery" (clothes & jewellery directory)
    elif category1 == "Sports & Outdoors":
        # If the value of "category1" equals "Sports & Outdoors", it means it would have to be stored in the sports & outdoors directory
        os.chdir(path_for_sportsoutdoors) # Changing the directory to the value of the variable "path_for_sportsoutdoors" (sports & outdoors directory)
    elif category1 == "Food":
        # If the value of "category1" equals "Food", it means it would have to be stored in the food directory
        os.chdir(path_for_food) # Changing the directory to the value of the variable "path_for_food" (food directory)
    elif category1 == "Health":
        # If the value of "category1" equals "Health", it means it would have to be stored in the health directory
        os.chdir(path_for_health) # Changing the directory to the value of the variable "path_for_health" (health directory)
    elif category1 == "Motor Vehicles":
        # If the value of "category1" equals "Motor Vehicles", it means it would have to be stored in the motor vehicles directory
        os.chdir(path_for_motorvehicles) # Changing the directory to the value of the variable "path_for_motorvehicles" (motor vehicles directory)
    elif category1 == "Education":
        # If the value of "category1" equals "Education", it means it would have to be stored in the education directory
        os.chdir(path_for_education) # Changing the directory to the value of the variable "path_for_education" (education directory)



    file=open(product1,  "w") # Creating a new file under the name of the value of the variable "product1"
    file.write(product1+"\n") # Writing the value of the variable "product1" (product name) to the file
    file.write(price1+"\n") # Writing the value of the variable "price1" (product price) to the file
    file.write(username1+"\n") # Writing the value of the variable "username1" (username of seller) to the file
    file.write(category1+"\n") # Writing the value of the variable "category1" (category of product) to the file
    file.write(keyword1+"\n") # Writing the value of the variable "keyword1" (keyword) to the file
    file.write(keyword2+"\n") # Writing the value of the variable "keyword2" (keyword) to the file
    file.write(keyword3+"\n") # Writing the value of the variable "keyword3" (keyword) to the file
    file.close() # Closing the file so that no more changes can be made to it
    product_entry.delete(0, END) # Deleting the value held in the product name entry field
    price_entry.delete(0, END) # Deleting the value held in the product price entry field
    screen9.destroy() # Deleting the screen in which the user had entered all information about the product
    variable_1 = Label(screen6, text = "Product sucessfully listed", fg = "green", font = ("Calibri", 11)).pack()





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
