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
    password1 = str(password1)
    username1 = str(username1)
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    user_dir = ("C:/Users/achug/Desktop/Files/A Level NEA/tkinter code/Users")
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
    product1 = product_entry.get() # Assigning the value of "product_entry" to the variable "product1"
    price1 = price_entry.get() # Assigning the value of "price_entry" to the variable "price1"
    category1 = clicked.get() # Assigning the value of "clicked" to the variable "category1"
    keyword1 = keyword1_entry.get() # Assigning the value of "keyword1_entry" to "keyword1"
    keyword2 = keyword2_entry.get() # Assigning the value of "keyword2_entry" to "keyword2"
    keyword3 = keyword3_entry.get() # Assigning the value of "keyword3_entry" to "keyword3"

    global product_dir # Globalising the variable "product_dir"
    product_dir = ("C:/Users/achug/Desktop/Files/A Level NEA/tkinter code/Products")
    #Defining the variable "product_dir" with the value of the directory where all the product files would be stored
    os.chdir(product_dir) # Changing the directory to the product directory
    file=open(product1,  "w") # Creating a new file with the value of "product1" (product name) as the file name
    file.write(product1+"\n") # Writing the value of "product1" (product name) to the file
    file.write(price1+"\n") # Writing the value of "price1" (product price) to the file
    #new code-----------------------------------------------------------------------------
    file.write(username1+"\n") # Writing the value of "username1" (seller information) to the file
    #new code ends------------------------------------------------------------------------
    file.write(category1+"\n") # Writing the value of "category1" (product category) to the file
    file.write(keyword1+"\n") # Writing the value of "keyword1" (product keyword 1) to the file
    file.write(keyword2+"\n") # Writing the value of "keyword2" (product keyword 2) to the file
    file.write(keyword3+"\n") # Writing the value of "keyword3" (product keyword 3) to the file
    file.close() # Closing the file so that no more changes can be made to the file

    product_entry.delete(0, END) # Deleting the value held in the product name entry field
    price_entry.delete(0, END) # Deleting the value held in the product price entry field

    
    screen9.destroy() # Destroying the screen in which the user has entered all the product information
    variable_1 = Label(screen6, text = "Product sucessfully listed", fg = "green", font = ("Calibri", 11)).pack()
     # Displaying to the user that the product has been successfully listed
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
