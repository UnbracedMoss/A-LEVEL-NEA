from tkinter import *
import os
from tkinter import filedialog
#Next unused screen: 15

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
    global screen7 # Declaring the new screen
    screen7 = Toplevel(screen) # Making the new screen appear at the top
    screen7.title("Account Management") # Defining the header of the new screen
    screen7.geometry("500x500") # Defining the dimensions of the new screen
    Label(screen7, text="Welcome to account management").pack()
    Label(screen7, text = "Username:", font= ('Helvetica', 13, 'bold')).pack()
    Label(screen7, text=username1).pack() # Displaying the username onto the screen
    Label(screen7, text="").pack()
    #new code-----------------------------
    Button(screen7, text="Change me", command=username_changes).pack() # Directing users to the function to change their password
    #new code ends--------------------------------------------
    Label(screen7, text = "Password:", font=('Helvetica', 13, 'bold')).pack()
    Label(screen7, text =password1).pack() # Displaying the password onto the screen
    Label(screen7, text="").pack()
    #new code----------------------------------
    Button(screen7, text="Change me", command=password_changes).pack() # Directing users to the function to change their password
    #new code ends-----------------------------------------
    f= open(username1) # Opening the file under the name username1 (username of the user) and assigning its content to the variable "f"
    content = f.readlines() # Separating the contents of the file into separate lines, assigning the information to the variable "content"
    Label(screen7, text = "Address Line 1:", font=('Helvetica', 13, 'bold')).pack()
    Label(screen7, text = content[2]).pack() # Displaying to the user the first line of the address
    #new code---------------------------------------
    Button(screen7, text="Change me", command=address1_changes).pack() # Directing users to the function to change the first line of their address
    #new code ends--------------------------------------------
    Label(screen7, text = "Address Line 2:", font=('Helvetica', 13, 'bold')).pack()
    Label(screen7, text = content[3]).pack() # Displaying to the user the second line of address
    #new code-----------------------------
    Button(screen7, text="Change me", command=address2_changes).pack() # Directing user to the function to change the second line of their address
    #new code ends------------------------------
    Label(screen7, text = "Postcode", font=('Helvetica', 13, 'bold')).pack()
    Label(screen7, text = content[4]).pack() # Displaying to the user their postcode
    #new code----------------------------------
    Button(screen7, text="Change me", command=postcode_changes).pack() # Directing user to the function to change their postcode
    #new code ends--------------------------

    
def username_changes():
    global screen10 # Declaring the new screen
    global new_username_entry # Globalising the variable "new_username_entry"
    global detail_identifier # Globalising the variable "detail_identifier"
    screen10 = Toplevel(screen) # Making the new screen appear at the top
    screen10.title("Changing Username") # Defining the header of the screen
    screen10.geometry("500x500") # Defining the dimensions of the screen

    Label(screen10, text = "Currently unable to change the username")
    # Username cannot actually be changed
    # There are too many dependencies
    #If usernames are changed, the previous usernames would also not be changed so there would be seller confusion

def password_changes():
    global screen11 # Declaring the new screen
    global new_password_entry # Globalising the variable "new_password_entry"
    global detail_identifier # Globalising the variable "detail_identifier"
    screen11 = Toplevel(screen) # Making this screen appear at the top
    screen11.title("Changing Password") # Defining the header of the screen
    screen11.geometry("500x500") # Defining the dimensions of the screen

    detail_identifier = 1 # Setting the value of "detail_identifier" to 1 - to later signify that the password has been changed
    Label(screen11, text="Please input the new password").pack()
    Label(screen11, text = "").pack()
    new_password_entry = Entry(screen11) # Storing the value of the new password entry to the variable "new_password_entry"
    new_password_entry.pack()
    Button(screen11, text = "Change password", command = actually_changing).pack() # Button that would direct the code to the function actually_changing()

def address1_changes():
    global screen12 # Declaring a new screen
    global detail_identifier # Globalising the variable "detail_identifier"
    global new_address1_entry # Globalising the variable "new_address1_entry"
    screen12 = Toplevel(screen) # Making this screen appear at the top
    screen12.title("Changing 1st line of Address") # Defining the header of the screen
    screen12.geometry("500x500") # Defining the dimensions of the screen

    detail_identifier = 2 # Setting the value of "detail_identifier" to 2 - to later signify that the 1st line of address has been changed
    Label(screen12, text = "Please enter updated 1st line of address").pack()
    Label(screen12, text = "").pack()
    new_address1_entry = Entry(screen12) #  Storing the value of the new address line 1 entry to the variable "new_address1_entry"
    new_address1_entry.pack() 
    Button(screen12, text = "Update first line of address", command = actually_changing).pack() # Button that would direct the code to the function actually_changing()
    

def address2_changes():
    global screen13 # Declaring a new screen
    global detail_identifier # Globalising the variable "detail_identifier"
    global new_address2_entry # Globalising the variable "new_address2_entry"
    screen13 = Toplevel(screen) # Making this screen appear at the top
    screen13.title("Changing 2nd line of Address") # Defining the header of the screen
    screen13.geometry("500x500") # Defining the dimensions of the screen

    detail_identifier = 3 # Setting the value of "detail_identifier" to 3 - to later signify that the 2nd line of address has been changed
    Label(screen13, text = "Please enter updated second line of address").pack()
    Label(screen13, text = "").pack()
    new_address2_entry = Entry(screen13) # Storing the value of the new address line 2 entry to the variable "new_address2_entry"
    new_address2_entry.pack()
    Button(screen13, text = "Update second line of address", command = actually_changing).pack() # Button that would direct the code to the function actually_changing()

def postcode_changes():
    global screen14 # Declaring a new screen
    global detail_identifier # Globalising the variable "detail_identifier"
    global new_postcode_entry # Globalising the variable "new_postcode_entry"
    screen14 = Toplevel(screen) # Making this screen appear at the top
    screen14.title("Changing Postcode") # Defining the header of the screen
    screen14.geometry("500x500") # Defining the dimenions of the screen

    detail_identifier = 4 # Setting the value of "detail_identifier" to 4 - to later signify that the postcode has been changed
    Label(screen14, text = "Please enter new postcode:").pack()
    Label(screen14, text = "").pack()
    new_postcode_entry = Entry(screen14) # Storing the value of the new postcode entry to the variable "new_postcode_entry"
    new_postcode_entry.pack()
    Button(screen14, text = "Update postcode", command = actually_changing).pack() # Button that would direct the code to the function actually_changing()
    
    

def actually_changing():
    global username1 # Globalising the variable "username1"
    global username_detail # Globalising the variable "username_detail"
    username_file_read = open(username1, "r") # Opening the file under the name of username1 and assigning its content to the variable "username_file_read", in read mode
    data = username_file_read.readlines() # Separating the contents of the file and assigning all the values to the variable "data"
    if detail_identifier == 0: # Conditional statement based if the value of the variable "detail_identifier" equals 0 / signifying that there are usernames changes
        username_detail = new_username_entry.get() # Assigning the value of "new_username_entry" to the variable "username_detail"
        data[0] = (username_detail + "\n") # Overwriting the previous username value (first line of the file/first entry on the array) with the new username value held in "username_detail"
        username_file_write = open(username1, "w") # Opening the file under the name of username 1, in write mode, and assigning its contents to the variable "username_file_write"
        username_file_write.writelines(data) # Overwriting the file with the contents of the array "data", which would now have the updated username
        screen_deletion() # Deleting this screen        
        
    elif detail_identifier == 1: # Conditional statement based on if the value of the variable "detail_identifier" equals 1 - signifying that there are password changes
        password_detail = new_password_entry.get() # Assigning the value of the new password entry "new_password_entry" to the variable "password_detail"
        data[1] = (password_detail + "\n") # Overwriting the previous password value (second line of the file / second entry on the array) with the new password value held in "password_detail"
        password_file_write = open(username1, "w") # Opening the file under the name of username1, in write mode, and assigning its content to the variable "password_file_write"
        password_file_write.writelines(data) # Overwriting the file with the contents of the array "data", which would now have the updated password
        screen_deletion() # Deleting this screen
        
    elif detail_identifier == 2: # Conditional statement based on if the value of the variable "detail_identifier" equals 2 - signifiying that there are first line of address changes
        address1_detail = new_address1_entry.get() # Assigning the value of the new address 1 entry "new_address1_entry" to the variable "address1_detail"
        data[2] = (address1_detail + "\n") # Overwriting the previous 1st line of address value (third line of file / third entry on the array) with the new first line of address held in "address1_detail"
        address1_file_write = open(username1, "w") # Opening the file under the name of username1, in write mode, and assigning its content to the variable "address1_file_write"
        address1_file_write.writelines(data) # Overwriting the file with the contents of the array "data", which would now have the updated first line of address

    elif detail_identifier == 3: # Conditional statement based on if the value of the variable "detail_identifier" equals 3 - signifying that there are second line of address changes
        address2_detail = new_address2_entry.get() # Assigning the value of the new second line of address entry "new_address2_entry" to the varaible "address2_detail"
        data[3] = (address2_detail + "\n") # Overwriting the previous 2nd line of address value (fourth line of file / fourth entry on the array) with the new second line of address held in "address2_detail"
        address2_file_write = open(username1, "w") # Opening the file under the name of username1, in write mode, and assigning its content to the variable "address2_file_write"
        address2_file_write.writelines(data) # Overwriting the file with the contents of the array "data", which would now have the updated second line of address

    elif detail_identifier == 4: # Conditional statement based on if the value of the variable "detail_identifier" equals 4 - signifying that there are postcode changes
        postcode_detail = new_postcode_entry.get() # Assigning the value of the new postcode entry "new_postcode_entry" to the variable "postcode_detail"
        data[4] = (postcode_detail + "\n") # Overwriting the previous postcode value (fifth line of file / fifth entry on the array) with the new postcode value held in "postcode_detail"
        postcode_file_write = open(username1, "w") # Opening the file under the name of username1, in write mode, and assigning its contents to the variable "postcode_file_write"
        postcode_file_wrie.writelines(data) # Overwriting the file with the contents of the array "data", which would now have the updated postcode.
    
    


def buying():
    global screen8
    screen8 = Toplevel(screen)
    screen8.title("Buying Homepage")
    screen8.geometry("500x500")
    Label(screen8, text = "Welcome to the Online Marketplace").pack()
    



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
    taken_username = False
    username_info = username.get()
    password_info = password.get()
    address_1_info = address_line_1.get()
    address_2_info = address_line_2.get()
    postcode_info = postcode.get()

    user_dir = ("C:/Users/achug/Desktop/Files/A Level NEA/tkinter code/Users")
    os.chdir(user_dir)
    list_of_files = os.listdir()
    if username_info in list_of_files:
        taken_username = True
        

    if taken_username == False:
        
        user_dir = ("C:/Users/achug/Desktop/Files/A Level NEA/tkinter code/Users")
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
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    user_dir = ("C:/Users/achug/Desktop/Files/A Level NEA/tkinter code/Users")
    os.chdir(user_dir)
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
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
    
    

def selected_searching_selling(event):
    myLabel = Label(screen9, text=clicked.get()).pack()

def selling():
    global screen9
    global product_entry
    global price_entry
    global clicked
    global keyword1_entry
    global keyword2_entry
    global keyword3_entry

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

    drop = OptionMenu(screen9, clicked, *options, command=selected_searching_selling)
    drop.pack(pady=20)
    print(clicked)

    #special_button = Button(screen9, text = "Select from list", command=selected)
    #special_button.pack()


    Label(screen9, text = "").pack()
    Label(screen9, text = "").pack()
    Button(screen9, text = "List item for sale", width = 15, height = 2, command = store_products).pack()



def store_products():
    print("Works")
    product1 = product_entry.get()
    price1 = price_entry.get()
    category1 = clicked.get()
    keyword1 = keyword1_entry.get()
    keyword2 = keyword2_entry.get()
    keyword3 = keyword3_entry.get()
    print(product1)
    print(category1)
    print(price1)
    print(keyword1)
    print(keyword2)
    print(keyword3)


    global product_dir
    product_dir = ("C:/Users/achug/Desktop/Files/A Level NEA/tkinter code/Products")
    os.chdir(product_dir)
    file=open(product1,  "w")
    file.write(product1+"\n")
    file.write(price1+"\n")
    file.write(category1+"\n")
    file.write(keyword1+"\n")
    file.write(keyword2+"\n")
    file.write(keyword3+"\n")
    file.close()

    product_entry.delete(0, END)
    price_entry.delete(0, END)

    
    screen9.destroy()
    variable_1 = Label(screen6, text = "Product sucessfully listed", fg = "green", font = ("Calibri", 11)).pack()
     
    #label.after(1000, label.master.destroy)





def main_screen():
    global screen
    screen=Tk()
    screen.geometry("300x250")
    screen.title("Online Marketplace")
    Label(text = "Online Marketplace", bg = "grey", font = ("Calibri", 13)).pack()
    Label(text = " ").pack()
    Button(text = "Login", width = "30", height = "2", command = login).pack()
    Label(text = " ").pack()
    Button(text = "Register", height = "2", width = "30", command = register).pack()

    screen.mainloop()



main_screen()
