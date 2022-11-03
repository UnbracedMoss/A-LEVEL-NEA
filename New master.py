from tkinter import *
import os
from tkinter import filedialog
#current screen 10
#make a clock

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


def account_management():
    global screen7
    screen7 = Toplevel(screen)
    screen7.title("Account Management")
    screen7.geometry("500x500")
    Label(screen7, text="Welcome to account management").pack()
    Label(screen7, text = "Username:", font= ('Helvetica', 18, 'bold')).pack()
    Label(screen7, text=username1).pack()
    Label(screen7, text="").pack()
    Label(screen7, text="").pack()
    Label(screen7, text = "Password:", font=('Helvetica', 18, 'bold')).pack()
    Label(screen7, text =password1).pack()
    Label(screen7, text="").pack()
    Label(screen7, text="").pack()
   


    f= open(username1)
    content = f.readlines()

    Label(screen7, text = "Address Line 1:", font=('Helvetica', 18, 'bold')).pack()
    Label(screen7, text = content[2]).pack()
    Label(screen7, text="").pack()
    Label(screen7, text = "Address Line 2:", font=('Helvetica', 18, 'bold')).pack()
    Label(screen7, text = content[3]).pack()
    Label(screen7, text="").pack()
    Label(screen7, text = "Postcode", font=('Helvetica', 18, 'bold')).pack()
    Label(screen7, text = content[4]).pack()
    


    
    

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
        postcode_entry.delete(0, END)
        address_line_1_entry.delete(0, END)
        address_line_2_entry.delete(0, END)

        Label(screen1, text = "Another user already has that username", fg = "green", font = ("Calibri", 11)).pack()


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
