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


def account_management():
    global screen7
    screen7 = Toplevel(screen)
    screen7.title("Account Management")
    screen7.geometry("500x500")
    Label(screen7, text="Welcome to account management").pack()
    label47=Label(screen7, text = "Username:")
    label47.pack(side=LEFT)
    label48=Label(screen7, text=username1)
    label48.pack(side=LEFT, pady=0)

    print(username1)
    print(password1)
    

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
    username_info = username.get()
    password_info = password.get()

    user_dir = filedialog.askdirectory()
    os.chdir(user_dir)
    print(user_dir)
    file=open(username_info, "w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text = "Registration Success", fg = "green", font = ("Calibri", 11)).pack()


def login_verify():
    global username1
    global password1
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

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
    screen1.geometry("300x250")
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(screen1, text = "Please enter details below").pack()
    Label(screen1, text = " ").pack()
    Label(screen1, text= "Username * ").pack()

    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    Label(screen1, text = "Password * ").pack()
    password_entry = Entry(screen1, textvariable = password)
    password_entry.pack()
    Label(screen1, text = "").pack()
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
    Button(screen9, text = "List item for sale", width = 15, height = 2, command = store_products).pack()



def store_products():
    print("Works")
    product1 = product_entry.get()
    price1 = price_entry.get()
    print(product1)
    print(price1)

    file=open(product1,  "w")
    file.write(product1+"\n")
    file.write(price1)
    file.close()

    product_entry.delete(0, END)
    price_entry.delete(0, END)

    
    screen9.destroy()
    variable_1 = Label(screen6, text = "Product sucessfully listed", fg = "green", font = ("Calibri", 11)).pack()
    variable_1 = label.after(1000, Label.destroy())
     
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
