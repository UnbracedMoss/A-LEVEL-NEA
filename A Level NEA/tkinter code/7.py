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
    
        
        
        
        
    elif detail_ridentifier == 1:
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
    
    




def books():
    global screen15
    screen15 = Toplevel(screen)
    screen15.title("Books")
    screen15.geometry("500x500")

    Label(screen15, text = "BOOKS").pack()
    
    
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
    global user_dir # Globalising the variable "user_dir"
    global people_name # Globalising the variable "people_name"
    taken_username = False # Assigning the value "False" to the variable "taken_username"
    username_info = username.get() # Assigning the value of "username" to the variable "username_info"
    password_info = password.get() # Assigning the value of "password" to the variable "password_info"
    address_1_info = address_line_1.get() # Assigning the value of "address_line_1" to the variable "address_1_info"
    address_2_info = address_line_2.get() # Assigning the value of "address_line_2" to the variable "address_2_info"
    postcode_info = postcode.get() # Assigning the value of "postcode" to the variable "postcode_info"

    cwd = os.getcwd() # Assigning the value of the current directory to the variable "cwd"
    directory_for_users = ("Users") # Assigning the value of "Users" to the variable "directory_for_users"
    user_dir = os.path.join(cwd, directory_for_users)
    # Using the function os.path.join, creating a directory for the users by concancenating the variable "cwd" and the variable "directory_for_users".
    #Storing the result of this to the variable "user_dir"
    os.chdir(user_dir) # Changing the current directory to the directory where all user files are stored
    list_of_files = os.listdir() # Creating an array "list_of_files" that would store all the file names of all the files that are located in the current directory
    if username_info in list_of_files: # Creating a conditional statement based on whether "username_info" (user-entered username) is in the "list_of_files"
        # If it is already there, it means that another user has already registered with that username
        taken_username = True # Assigning the value "True" to the variable "taken_username"
        

    if taken_username == False: # Initialising a conditional statement based on the state of the variable "taken_username"
      #If the value of "taken_username" == False (If the username is not taken by a different user)  
        os.chdir(user_dir) # Change the directory to the user directory where all the user files would be stored
        file=open(username_info, "w") # Creating a file with the value of "username_info" as the file name
        file.write(username_info+"\n") # Writing the value of the variable "username_info" (username) into the file
        file.write(password_info+"\n") # Writing the value of the variable "password_info" (password) into the file
        file.write(address_1_info+"\n") # Writing the value of the variable "address_1_info" (1st line of address) into the file
        file.write(address_2_info+"\n") # Writing the value of the variable "address_2_info" (2nd line of address) into the file
        file.write(postcode_info+"\n") # Writing the value of the variable "postcode_info" (postcode) into the file
        file.close() # Closing the file so that no more changes can be made to the file

        username_entry.delete(0, END) # Deleting the value held in the username entry field
        password_entry.delete(0, END) # Deleting the value held in the password entry field
        postcode_entry.delete(0, END) # Deleting the value held in the postcode entry field
        address_line_1_entry.delete(0, END) # Deleting the value held in the 1st line of address field
        address_line_2_entry.delete(0, END) # Deleting the value held in the 2nd line of address field

        Label(screen1, text = "Registration Success", fg = "green", font = ("Calibri", 11)).pack()
    else:
        username_entry.delete(0, END) # Deleting the value held in the username entry field
        password_entry.delete(0, END) # Deleting the value held in the password entry field

        Label(screen1, text = "Username taken", fg = "green", font = ("Calibri", 11)).pack()


def login_verify():
    global username1 # Globalising the variable "username1"
    global password1 # Globalising the variable "password1"
    global ORIGINAL_ROOT_DIR # Globalising the variable "ORIGINAL_ROOT_DIR"
    global username_info # Globalising the variable "username_info"
    username1 = username_verify.get() # Assigning the value of "username_verify" to the variable "username1"
    password1 = password_verify.get() # Assigning the value of "password_verify" to the variable "password1"
    password1 = str(password1) # Assigning the string value of  "password1" to the variable "password1"
    username1 = str(username1) # Assigning the string value of "username1" to the variable "username1"
    username_entry1.delete(0, END) # Deleting the value held in the username entry field
    password_entry1.delete(0, END) # Deleting the value held in the password entry field


    
    directory_for_users = ("Users") # Declaring the variable "directory_for_users" with the value of "Users"
    user_dir = os.path.join(ORIGINAL_ROOT_DIR, directory_for_users)
    # Through the function os.path.join, it would concancenate the "ORIGINAL_ROOT_DIR" value and the "directory_for_users" value
    # Creating a new directory for the users
    #Assigning this value to the variable "user_dir"
    os.chdir(user_dir) # Changing the current directory to the user directory, where all the user files would be stored
    list_of_files = os.listdir() # Creating an array under the name "list_of_files" which would store the file names of all the files within the current directory
    if username1 in list_of_files: # Creating a conditional statement based on whether "username1" (user entered username) would be within the current directory
        # If it is in the directory, it means that it is a valid username and someone has registered with it
        file1 = open(username1, "r") # Opening the file with the file name as the value of "username1" and storing its contents into the variable "file1"
        verify = file1.read().splitlines() # Separating the contents of the file and removing the newline comments, then assigning the remaining contents to the variable "verify"
        their_password = verify[1] # Assigning the value of "verify[1]" to the variable "their_password"
        boolean_login = (password1 == verify[1]) # Initialising a boolean variable with the value of the condition "password1==verify[1]" (testing whether the user inputted password is the same as the stored password)
        if boolean_login == True:
            #Means that the user inputted password and the stored password was the same
            login_success() # Redirects the code to the login_success() function
        else:
            #Mean that the user has entered a password that does not match with the stored password
            password_not_recognised() # Redirects the code to the password_not_recognised() function
    else:
        # Means that the value of "username1" was not found within the user directory
        # Meaning that that is not a registered user.
        user_not_found() # Redirects the code to the user_not_found() function.


    

    

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
        "Sports & Outdoors ",
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
    product1 = product_entry.get() # Assigning the value of "product_entry" to the variable "product1"
    price1 = price_entry.get() # Assigning the value of "price_entry" to the variable "price1"
    category1 = clicked.get() # Assigning the value of "clicked" to the variable "category1"
    keyword1 = keyword1_entry.get() # Assigning the value of "keyword1_entry" to the variable "keyword1"
    keyword2 = keyword2_entry.get() # Assigning the value of "keyword2_entry" to the variable "keyword2"
    keyword3 = keyword3_entry.get() # Assigning the value of "keyword3_entry" to the variable "keyword3"

    os.chdir(ORIGINAL_ROOT_DIR) # Changing the directory to the value held in "ORIGINAL_ROOT_DIR"
    cwd = os.getcwd() # Assigning the value of the current directory to the variable "cwd"
    directory_for_products = ("Products") # Assigning the value "Products" to the variable "directory_for_products"
    path_for_products = os.path.join(cwd, directory_for_products)
    # Through the os.path.join function, it creates the directory for products by concancenating the values of the variable "cwd" and "directory_for_products"
    # The new products directory is assigned to the variable "path_for_products"
    is_existing_products = os.path.exists(path_for_products)
    #Creating a boolean variable depending on whether or not the directory value held in "path_for_products" already exists
    if is_existing_products == True: # Creating a conditional statement depending on the value of the variable "is_existing_products"
        # If "True", it means that the directory for products already exists, so there is no need to create the products directory
        print("Doing nothing")
    else:
        # If "False", it means that the directory for products does not exist
        print("Creating the new directory")
        os.mkdir(path_for_products) # Making a directory with the value of the variable "path_for_products"
        print("Made new directory")
        

    os.chdir(path_for_products) # Changing the current directory to the directory for products
    file=open(product1,  "w") # Opening a file with the filename as the value of the variable "product1"
    file.write(product1+"\n") # Writing the value of the variable "product1" (product name) to the file
    file.write(price1+"\n") # Writing the value of the variable "price1" (product price) to the file
    file.write(username1+"\n") # Writing the value of the variable "username1" (username of the seller) to the file
    file.write(category1+"\n") # Writing the value of the variable "category1" (category of product) to the file
    file.write(keyword1+"\n") # Writing the value of the variable "keyword1" (1st keyword) to the file
    file.write(keyword2+"\n") # Writing the value of the variable "keyword2" (2nd keyword) to the file
    file.write(keyword3+"\n") # Writing the value of the variable "keyword3" (3rd keyword) to the file
    file.close() # Closing the file so that no more changes can be made to the file

    product_entry.delete(0, END) # Deleting the value held in the product name entry field
    price_entry.delete(0, END) # Deleting the value held in the product price entry field

    
    screen9.destroy() # Destroying the screen in which the user had entered all the information regarding the product
    variable_1 = Label(screen6, text = "Product sucessfully listed", fg = "green", font = ("Calibri", 11)).pack()
     
    #label.after(1000, label.master.destroy)





def main_screen():
    global screen # Declaring a new screen
    global ORIGINAL_ROOT_DIR # Globalising the variable "ORIGINAL_ROOT_DIR"
    screen=Tk()
    screen.geometry("300x250") # Defining the dimensions of the screen
    screen.title("Online Marketplace") # Defining the header of the screen
    Label(text = "Online Marketplace", bg = "grey", font = ("Calibri", 13)).pack()
    Label(text = " ").pack()
    Button(text = "Login", width = "30", height = "2", command = login).pack() # Button to direct the user to the login page
    Label(text = " ").pack()
    Button(text = "Register", height = "2", width = "30", command = register).pack() # Button to direct the user to the register page


    ORIGINAL_ROOT_DIR = StringVar() # Defining the variable "ORIGINAL_ROOT_DIR" as a string variable
    ORIGINAL_ROOT_DIR = os.getcwd() # Assigning the variable "ORIGINAL_ROOT_DIR" with the current directory
    cwd = os.getcwd() # Assigning the variable "cwd" with the value of the current directory
    directory_for_users = ("Users") # Assigning the variable "directory_for_users" with the value "Users"
    path_for_users = os.path.join(cwd, directory_for_users)
    # Through the os.path.join function, it concancentates the values of the variables "cwd" and "directory_for_users"
    # This creates the directory for users
    # This value is assigned to the variable "path_for_users"
    is_existing_users = os.path.exists(path_for_users)
    # Creating a boolean variable depending on whether the value of "path_for_users" (user directory) already exists
    if is_existing_users == True:
        # If true, it means that the user directory already exists, so it does not need to be generated
        pass
    else:
        # If not true, it means that the user directory does not exist, so it would need to be generated
        os.mkdir(path_for_users) # Making the user directory
        print("Made new directory")
        
    

    screen.mainloop()



main_screen()
