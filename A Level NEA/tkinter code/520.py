from tkinter import *
import os
import time
from tkinter import filedialog
import pathlib
#Next unused screen: 54

def main_screen():
    global screen
    global ORIGINAL_ROOT_DIR
    global path_for_reviews
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
    global presence_counter
    global forgotten_password_used # Was originally declared in forgotten_password_verify but the validation could not take place if user had logged in accurately
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Online Marketplace")
    Label(text = "Online Marketplace", bg = "grey", font = ("Calibri", 13)).pack()
    Label(text = " ").pack()
    Button(text = "Login", width = "30", height = "2", command = login).pack()
    Label(text = " ").pack()
    Button(text = "Register", height = "2", width = "30", command = register).pack()
    os.listdir()

    
    presence_counter = 0

    forgotten_password_used = BooleanVar()
    forgotten_password_used = False

    ORIGINAL_ROOT_DIR = StringVar()
    ORIGINAL_ROOT_DIR = os.getcwd()
    cwd = os.getcwd()
    print(cwd)
    directory_for_users = ("Users")
    directory_for_reviews = ("Reviews")
    path_for_users = os.path.join(cwd, directory_for_users)
    path_for_reviews = os.path.join(cwd, directory_for_reviews)
    is_existing_users = os.path.exists(path_for_users)
    print(is_existing_users)

    if is_existing_users == True:
        print("Doing nothing")
    else:
        print("Creating the new directory")
        os.mkdir(path_for_users)
        os.mkdir(path_for_reviews)
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


def register():
    global screen1
    screen1 = Toplevel (screen)
    screen1.title("Register")
    screen1.geometry("600x900")
    global username
    global password
    global username_entry # Would be used to delete the entry later on
    global password_entry # Would be used to delete password entry after successful
    global address_line_1
    global address_line_2
    global postcode
    global address_line_1_entry
    global address_line_2_entry
    global postcode_entry
    global memorable_word_entry
    global memorable_question_entry
    global memorable_word
    global memorable_question
    
    username = StringVar()
    password = StringVar()
    postcode = StringVar()
    address_line_1 = StringVar()
    address_line_2 = StringVar()
    memorable_word = StringVar()
    memorable_question = StringVar()

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
    Label(screen1, text = "Please enter your memorable word").pack()
    memorable_word_entry = Entry(screen1, textvariable = memorable_word)
    memorable_word_entry.pack()
    Label(screen1, text = "What is your mother's maiden name (Security question)").pack()
    memorable_question_entry = Entry(screen1, textvariable = memorable_question)
    memorable_question_entry.pack()
    Button(screen1, text = "Register", width = 10, height = 1, command = register_user).pack()

def register_user():
    global user_dir
    global ORIGINAL_ROOT_DIR
    global people_name
    global presence_counter

    presence_counter = 0
    taken_username = False
    missing_entity = False
    username_info = username.get()
    password_info = password.get()
    
    address_1_info = address_line_1.get()
    address_2_info = address_line_2.get()
    postcode_info = postcode.get()
    memorable_word_info = memorable_word.get()
    memorable_question_info = memorable_question.get()


    username_length = len(username_info)
    password_length = len(password_info)
    address1_length = len(address_1_info)
    address2_length = len(address_2_info)
    postcode_length = len(postcode_info)
    memorable_word_length = len(memorable_word_info)
    memorable_question_length = len(memorable_question_info)
    
    if username_length == 0:
        print("No username detected")
        no_username_entered = Label(screen1, text = "No username was inputted")
        no_username_entered.pack()
        screen.after(3000, no_username_entered.destroy)
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        address_line_1_entry.delete(0, END)
        address_line_2_entry.delete(0, END)
        postcode_entry.delete(0, END)
        memorable_word_entry.delete(0, END)
        memorable_question_entry.delete(0, END)
        return
    elif password_length == 0:
        print("No password detected")
        no_password_entered = Label(screen1, text = "No password detected")
        no_password_entered.pack()
        screen.after(3000, no_password_entered.destroy)
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        address_line_1_entry.delete(0, END)
        address_line_2_entry.delete(0, END)
        postcode_entry.delete(0, END)
        memorable_word_entry.delete(0, END)
        memorable_question_entry.delete(0, END)
        return
    elif address1_length == 0:
        print("No address1 detected")
        no_address1_entered = Label(screen1, text = "1st line of address has not been entered")
        no_address1_entered.pack()
        screen.after(3000, no_address1_entered.destroy)
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        address_line_1_entry.delete(0, END)
        address_line_2_entry.delete(0, END)
        postcode_entry.delete(0, END)
        memorable_word_entry.delete(0, END)
        memorable_question_entry.delete(0, END)
        return
    elif address2_length == 0:
        print("No address2 detected")
        no_address2_entered = Label(screen1, text = "2nd line of address has not been entered")
        no_address2_entered.pack()
        screen.after(3000, no_address2_entered.destroy)
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        address_line_1_entry.delete(0, END)
        address_line_2_entry.delete(0, END)
        postcode_entry.delete(0, END)
        memorable_word_entry.delete(0, END)
        memorable_question_entry.delete(0, END)
        return
    elif postcode_length == 0:
        print("No postcode detected")
        no_postcode_entered = Label(screen1, text = "Postcode has not been entered")
        no_postcode_entered.pack()
        screen.after(3000, no_postcode_entered.destroy)
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        address_line_1_entry.delete(0, END)
        address_line_2_entry.delete(0, END)
        postcode_entry.delete(0, END)
        memorable_word_entry.delete(0, END)
        memorable_question_entry.delete(0, END)
        return
    elif memorable_word_length == 0:
        print("No memorable word detected")
        no_memorable_word_entered = Label(screen1, text = "Memorable word has not been entered")
        no_memorable_word_entered.pack()
        screen.after(3000, no_memorable_word_entered.destroy)
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        address_line_1_entry.delete(0, END)
        address_line_2_entry.delete(0, END)
        postcode_entry.delete(0, END)
        memorable_word_entry.delete(0, END)
        memorable_question_entry.delete(0, END)
        return
    elif memorable_question_length == 0:
        print("No memorable question detected")
        no_memorable_question_entered = Label(screen1, text = "Memorable question has not been entered")
        no_memorable_question_entered.pack()
        screen.after(3000, no_memorable_question_entered.destroy)
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        address_line_1_entry.delete(0, END)
        address_line_2_entry.delete(0, END)
        postcode_entry.delete(0, END)
        memorable_word_entry.delete(0, END)
        memorable_question_entry.delete(0, END)
        return


    os.chdir(ORIGINAL_ROOT_DIR)
    directory_for_users = ("Users")
    user_dir = os.path.join(ORIGINAL_ROOT_DIR, directory_for_users)
    print(user_dir)

    os.chdir(user_dir)
    list_of_files = os.listdir()
    if username_info in list_of_files:
        taken_username = True
        

    if taken_username == False and missing_entity == False:
        
        os.chdir(user_dir)
        print(user_dir)
        file=open(username_info, "w")
        file.write(username_info+"\n")
        file.write(password_info+"\n")
        file.write(address_1_info+"\n")
        file.write(address_2_info+"\n")
        file.write(postcode_info+"\n")
        file.write(memorable_word_info+"\n")
        file.write(memorable_question_info+"\n")
        file.write("0"+"\n")
        file.close()

        username_entry.delete(0, END)
        password_entry.delete(0, END)
        postcode_entry.delete(0, END)
        address_line_1_entry.delete(0, END)
        address_line_2_entry.delete(0, END)
        memorable_word_entry.delete(0, END)
        memorable_question_entry.delete(0, END)

        Label(screen1, text = "Registration Success", fg = "green", font = ("Calibri", 11)).pack()
    else:
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        postcode_entry.delete(0, END)
        address_line_1_entry.delete(0, END)
        address_line_2_entry.delete(0, END)
        memorable_word_entry.delete(0, END)
        memorable_question_entry.delete(0, END)

        Label(screen1, text = "File not written", fg = "red", font = ("Calibri", 11)).pack()
        print("Username already taken")
        Label(screen46, text = "Username is taken").pack()
        Label(screen46, text = "Please register again with a different username").pack()
        screen1.destroy()



def login():
    print("Login session started")
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("700x500")
    Label(screen2, text = "Please enter details below to login").pack()
    Label(screen2, text = " ").pack()

    global username_verify
    global password_verify
    global memorable_word_verify
    global memorable_question_verify

    username_verify = StringVar()
    password_verify = StringVar()
    memorable_word_verify = StringVar()
    memorable_question_verify = StringVar()

    global username_entry1
    global password_entry1
    global memorable_word_entry1
    global memorable_question_entry1
    

    Label(screen2, text = "If forgotten password, enter all other field then press forgotten password").pack()
    Label(screen2, text = "Username * ").pack()
    username_entry1 = Entry(screen2, textvariable = username_verify)
    username_entry1.pack()
    Label(screen2, text=" ").pack()
    Label(screen2, text = "Password * ").pack()
    password_entry1 = Entry(screen2, textvariable = password_verify)
    password_entry1.pack()
    Label(screen2, text=" ").pack()
    Label(screen2, text = "Memorable word").pack()
    memorable_word_entry1 = Entry(screen2, textvariable = memorable_word_verify)
    memorable_word_entry1.pack()
    Label(screen2, text = "What is your mother's maiden name").pack()
    memorable_question_entry1 = Entry(screen2, textvariable = memorable_question_verify)
    memorable_question_entry1.pack()
    Button(screen2, text="Login", width = 10, height = 1, command = login_verify).pack()
    Button (screen2, text = "Forgotten password", width = 20, height = 1, command = forgotten_password).pack()
   
def login_verify():
    global username1
    global password1
    global memorable_word1
    global memorable_question1
    global ORIGINAL_ROOT_DIR
    global username_info
    global user_dir
    global counter
    global presence_counter
    global delete_counter
    delete_counter = StringVar()
    username1 = username_verify.get()
    password1 = password_verify.get()
    memorable_word1 = memorable_word_verify.get()
    memorable_question1 = memorable_question_verify.get()
    password1 = str(password1)
    username1 = str(username1)
    memorable_word1 = str(memorable_word1)
    memorable_question1 = str(memorable_question1)
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)
    memorable_word_entry1.delete(0, END)
    memorable_question_entry1.delete(0, END)

    username1_length = len(username1)
    password1_length = len(password1)
    memorable_word1_length = len(memorable_word1)
    memorable_question1_length = len(memorable_question1)

    if username1_length == 0:
        print("Username has not been inputted")
        Label(screen46, text = "Username has not been inputted").pack()
        Label(screen46, text = "Please login again, inputting username")
        screen2.destroy()
    elif password1_length == 0:
        print("Password has not been inputted")
        Label(screen46, text = "Password has not been inputted").pack()
        Label(screen46, text = "Please login again, inputting password").pack()
        screen2.destroy()
    elif memorable_word1_length == 0:
        print("Memorable word has not been inputted")
        Label(screen46, text = "Memorable word has not been inputted").pack()
        Label(screen46, text = " Please login again, inputting your memorable word").pack()
        screen2.destroy()
    elif memorable_question1_length == 0:
        print("Memorable question has not been inputted")
        Label(screen46, text = "Memorable question has not been answered").pack()
        Label(screen46, text = "Please login again, inputting the answer to the memorable question").pack()
        screen2.destroy()
    else:
        presence_counter = 0

     
    directory_for_users = ("Users")
    user_dir = os.path.join(ORIGINAL_ROOT_DIR, directory_for_users)
    print(user_dir)

    counter = 0
    counter = int(counter)
    
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
            counter = counter + 1
            print(counter)
        else:
            password_no_recog = Label(screen2, text = "Password not recognised")
            password_no_recog.pack()
            screen.after(2000, password_no_recog.destroy)
        #their_memorable_word = verify[5]
        boolean_logic2 = (memorable_word1 == verify[5])
        print(boolean_logic2)
        if boolean_logic2 == True:
            counter = counter + 1
            print(counter)
        else:
            memWord_no_recog = Label(screen2, text = "Incorrect response to memorable word")
            memWord_no_recog.pack()
            screen.after(2000, memWord_no_recog.destroy)
        boolean_logic3 = (memorable_question1 == verify[6])
        print(boolean_logic3)
        if boolean_logic3 == True:
            counter = counter + 1
            print(counter)
        else:
            password_not_recognised()
        #their_memorable_question = verify[6]
        counter = int(counter)
        presence_counter = int(presence_counter)
        if counter == 3 and presence_counter == 0:
            os.listdir()
            print(presence_counter)
            screen2.destroy()
            session()


    else:
        user_no_fou = Label(screen2, text = "User not found")
        user_no_fou.pack()
        screen.after(2000, user_no_fou.destroy)

   
    
  
def forgotten_password():
    global screen47
    screen47 = Toplevel(screen)
    screen47.title("Sapenzia/Isle of Sgail")
    screen47.geometry("300x500")
    Label(screen47, text = "Please enter the details below").pack()
    Label(screen47, text = "If login successful, to view password, go into account management")
    global forgotten_username_entry
    global forgotten_memorable_word_entry
    global forgotten_memorable_question_entry
    global fusername_entry
    global fword_entry
    global fquestion_entry
    forgotten_username_entry = StringVar()
    forgotten_memorable_word_entry = StringVar()
    forgotten_memorable_question_entry = StringVar()

    Label(screen47, text = "Username*").pack()
    fusername_entry = Entry(screen47, textvariable = forgotten_username_entry)
    fusername_entry.pack()
    Label(screen47, text = "Memorable word").pack()
    fword_entry = Entry(screen47, textvariable = forgotten_memorable_word_entry)
    fword_entry.pack()
    Label(screen47, text = "Memorable question").pack()
    fquestion_entry = Entry(screen47, textvariable = forgotten_memorable_question_entry)
    fquestion_entry.pack()

    Button(screen47, text = "Login", command = forgotten_password_verify).pack()


def forgotten_password_verify():
    global forgotten_username_verify
    global forgotten_memorable_word_verify
    global forgotten_memorable_question_verify
    global ORIGINAL_ROOT_DIR
    global forgotten_password_used
    
    

    forgotten_username_verify = forgotten_username_entry.get()
    forgotten_memorable_word_verify = forgotten_memorable_word_entry.get()
    forgotten_memorable_question_verify = forgotten_memorable_question_entry.get()
    # I'm having to use the get function as without using it, when calling the entry variables, it just stages PY_VAR5
    print(forgotten_username_verify)
    print(forgotten_memorable_word_verify)
    print(forgotten_memorable_question_verify)


        
    directory_for_users = ("Users")
    user_dir = os.path.join(ORIGINAL_ROOT_DIR, directory_for_users)
    print(user_dir)

    counter = IntVar()
    counter = 0
    
    os.chdir(user_dir)
    list_of_files = os.listdir()
    if forgotten_username_verify in list_of_files:
        file1 = open(forgotten_username_verify, "r")
        verify = file1.read().splitlines()
        
        #their_memorable_word = verify[5]
        boolean_logic2 = (forgotten_memorable_word_verify == verify[5])
        print(boolean_logic2)
        if boolean_logic2 == True:
            counter = counter + 1
            print(counter)
        else:
            print("Incorrect memorable word")
            incorrect_memorable_word = Label(screen47, text = "Incorrect memorable word")
            incorrect_memorable_word.pack()
            screen.after(3000, incorrect_memorable_word.destroy)
            fusername_entry.delete(0, END)
            fword_entry.delete(0, END)
            fquestion_entry.delete(0, END)
            

        boolean_logic3 = (forgotten_memorable_question_verify == verify[6])
        print(boolean_logic3)
        if boolean_logic3 == True:
            counter = counter + 1
            print(counter)
        else:
            print("Incorrect memorable question")
            incorrect_memorable_question = Label(screen47, text = "Incorrect response to memorable question")
            incorrect_memorable_question.pack()
            screen.after(2000, incorrect_memorable_question.destroy)
            fusername_entry.delete(0, END)
            fword_entry.delete(0, END)
            fquestion_entry.delete(0, END)
        #their_memorable_question = verify[6]
        counter = int(counter)
        if counter == 2:
            os.listdir()
            session()
            screen47.destroy()
            screen2.destroy()
            forgotten_password_used = True
            print(forgotten_password_used)
            
        else:
            fusername_entry.delete(0, END)
            fword_entry.delete(0, END)
            fquestion_entry.delete(0, END)
    else:
        fusername_entry.delete(0, END)
        fword_entry.delete(0, END)
        fquestion_entry.delete(0, END)



def session():
    global screen6
    print("Why even is there an else statement")
    screen6 = Toplevel(screen)
    screen6.title("Account Dashboard")
    screen6.geometry("350x500")
    Label(screen6, text= "Welcome to the Dashboard").pack()
    Button(screen6, text="Account Management", command=account_management).pack()
    Button(screen6, text= " Buying", bg = "yellow", command=buying).pack()
    Button(screen6, text="Selling", bg = "yellow", command=selling).pack()
    Button(screen6, text="Reviews", command=review_mainmenu).pack()
    Button(screen6, text="Logout", bg = "red", command=log_out).pack()








def account_management():
    global screen7
    global username1
    global forgotten_username_entry
    global forgotten_password_used
    screen7 = Toplevel(screen)
    screen7.title("Account Management")
    screen7.geometry("700x700")
    Label(screen7, text="Welcome to account management").pack()

    if forgotten_password_used == True:
        print("Forgotten password used")
        forgotten_username = forgotten_username_entry.get()
        username1 = forgotten_username

    f = open(username1)
    content = f.readlines()

    
    Label(screen7, text ="Password:", font=('Helvetica', 13, 'bold')).pack()
    Label(screen7, text=content[1]).pack()

    Label(screen7, text = "Address Line 1:", font=('Helvetica', 13, 'bold')).pack()
    Label(screen7, text = content[2]).pack()

    Label(screen7, text = "Address Line 2:", font=('Helvetica', 13, 'bold')).pack()
    Label(screen7, text = content[3]).pack()

    Label(screen7, text = "Postcode", font=('Helvetica', 13, 'bold')).pack()
    Label(screen7, text = content[4]).pack()

    Label(screen7, text = "Memorable word:", font=("Helvetica", 13, "bold")).pack()
    Label(screen7, text = content[5]).pack()

    Label(screen7, text = "Memorable Question:", font=("Helvetica", 13, "bold")).pack()
    Label(screen7, text = content[6]).pack()

    Label(screen7, text = "Funds available in account:", font=("Helvetica", 13, "bold")).pack()
    Label(screen7, text = content[7]).pack()
          


    Button(screen7, text = "Change personal details", command =changing_details).pack()
    Button(screen7, text = "View order history", command =order_history).pack()
    Button(screen7, text = "Add funds to account", command =funds).pack()



def changing_details():
    global str_out_details
    global detail_selection
    global screen50
    global clicked_details
    global new_detail_entry
    global filler
    screen50 = Toplevel(screen)
    screen50.title("Changing Account details")
    screen50.geometry("500x500")

    new_detail_entry = StringVar()

    details = [
        "Password" ,
        "1st Line of Address" ,
        "2nd Line of Address" ,
        "Postcode" ,
        "Memorable Word" ,
        "Memorable Question" 
    ]

    clicked_details = StringVar()
    clicked_details.set(details[0])

    str_out_details = StringVar()
    str_out_details.set("Output")

    drop_detail = OptionMenu(screen50, clicked_details, *details)
    drop_detail.pack(pady=20)
    b2 = Button(screen50, text = "Select category", command=lambda: my_show_details())
    b2.pack()
    Label(screen50, textvariable=str_out_details).pack()
    filler = Entry(screen50, textvariable = new_detail_entry)
    filler.pack()
    Button(screen50, text = "Make changes", command = actually_changing_details).pack()

def my_show_details():
    str_out_details.set(clicked_details.get())
    


def actually_changing_details():
    global detail_category
    detail_category = clicked_details.get()
    print(detail_category)
    global username1
    global username_file_read
    print(username1)
    username_file_read = open(username1, "r")
    data = username_file_read.readlines()
    print(data)
    

    if detail_category == "Password":
        password_detail = new_detail_entry.get()
        data[1] = (password_detail + "\n")
        print(data)
        password_file_write = open(username1, "w")
        password_file_write.writelines(data)
        screen7.destroy()
        filler.delete(0, END)
        password_changed = Label(screen50, text = "Password has been changed")
        password_changed.pack()
        screen.after(3000, screen50.destroy)

    elif detail_category == "1st Line of Address":
        address1_detail = new_detail_entry.get()
        data[2] = (address1_detail + "\n")
        print(data)
        address1_file_write = open(username1, "w")
        address1_file_write.writelines(data)
        screen7.destroy()
        filler.delete(0, END)
        address1_changed = Label(screen50, text = "The 1st Line of address has been changed")
        address1_changed.pack()
        screen.after(3000, screen50.destroy)

    elif detail_category == "2nd Line of Address":
        address2_detail = new_detail_entry.get()
        data[3] = (address2detail + "\n")
        print(data)
        address2_file_write = open(username1, "w")
        address2_file_write.writelines(data)
        screen7.destroy()
        address2_changed = Label(screen50, text = "The 2nd Line of Address has been changed")
        address2_changed.pack()
        screen.after(3000, screen50.destroy)

    elif detail_category == "Postcode":
        postcode_detail = new_detail_entry.get()
        data[4] = (postcode_detail + "\n")
        print(data)
        postcode_file_write = open(username1, "w")
        postcode_file_write.writelines(data)
        screen7.destroy()
        postcode_changed = Label(screen50, text = "Postcode has changed")
        postcode_changed.pack()
        screen.after(3000, screen50.destroy)

    elif detail_category == "Memorable Word":
        memorable_word_detail = new_detail_entry.get()
        data[5] = (memorable_word_detail + "\n")
        print(data)
        memorable_word_write = open(username1, "w")
        memorable_word_write.writelines(data)
        screen7.destroy()
        memorable_word_changed = Label(screen50, text = "Memorable Word has changed")
        memorable_word_changed.pack()
        screen.after(3000, screen50.destroy)

    elif detail_category == "Memorable Question":
        memorable_question_detail = new_detail_entry.get()
        data[6] = (memorable_question_detail + "\n")
        print(data)
        memorable_word_write = open(username1, "w")
        memorable_question_write.writelines(data)
        screen7.destroy()
        memorable_question_changed = Label(screen50, text = "Memorable Question has changed")
        memorable_question_changed.pack()
        screen.after(3000, screen50.destroy)
    
    
def order_history():
    global screen51
    global str_out_order
    global clicked_order
    screen51 = Toplevel(screen)
    screen51.title("Order History")
    screen51.geometry("847x734")
    Label(screen51, text = "ORDER HISTORY")

    f = open(username1, "r")
    content = f.readlines()

    raw_orders = []
    y = 8
    #while len(content[i]) > 0:
        #print("Works")
        #orders.append(content[i])
        #print(orders)
        #y = y + 1
    #print("Loop has concluded")

    # had an error where because the stopping condition of the while loop could never be properly defined, it was causing issues at the end of the range, causing errors
    #exception handling may work better, utilising the IndexError that was always happening

    try:
        while len(content[y]) > 0:
            print("Works")
            raw_orders.append(content[y])
            print(raw_orders)
            y = y + 1
    except IndexError:
        print("Loop has concluded")


    orders = []
    for sub in raw_orders:
        orders.append(sub.replace("\n", ""))
        print(orders)

    for i in range (len(orders)):
        i = 0
        Label(screen51, text = orders[i]).pack()
        i = i+1




    clicked_order = StringVar()
    clicked_order.set(orders[0])

    str_out_order = StringVar()
    str_out_order.set("Output")

    drop1 = OptionMenu(screen51, clicked_order, *orders)
    drop1.pack(pady=20)
    b2 = Button(screen51, text = "Select category", command=lambda: my_show_order())
    b2.pack()
    Label(screen51, textvariable=str_out_order).pack()

    Button(screen51, text = "View specific order", command = specific_order_history).pack()


def my_show_order():
    str_out_order.set(clicked_order.get())

def specific_order_history():
    global clicked_order
    global order_name
    global list_of_files_orders
    global screen52
    screen52 = Toplevel(screen)
    screen52.title("Item details")
    screen52.geometry("800x808")
    Label(screen52, text = "Ordered item's details").pack()
    order_name = StringVar()
    order_name = clicked_order.get()
    os.chdir(path_for_products)
    print(path_for_products)
    for path, directories, files in os.walk(path_for_products):
        if order_name in files:
            order_directory = os.path.join(path, order_name)
            print(order_directory)
            fp = open(order_directory, "r")
            order_contents = fp.readlines()
            Label(screen52, text = "Item name:").pack()
            Label(screen52, text = order_contents[0]).pack()
            Label(screen52, text = "Price:").pack()
            Label(screen52, text = order_contents[1]).pack()
            Label(screen52, text = "Quantity ordered: 1").pack()
            Label(screen52, text = "Seller:").pack()
            Label(screen52, text = order_contents[3]).pack()
            Label(screen52, text = "Category:").pack()
            Label(screen52, text = order_contents[4]).pack()
            Label(screen52, text = "Description:").pack()
            Label(screen52, text = order_contents[8:-1]).pack()
        
    

def funds():
    global screen53
    global fund_amount
    global fund_amount_entry
    screen53 = Toplevel(screen)
    screen53.title("Adding funds to account")
    screen53.geometry("800x754")


    fund_amount = IntVar()
    Label(screen53, text = "How much do you want to add to your account").pack()
    fund_amount_entry = Entry(screen53, textvariable = fund_amount)
    fund_amount_entry.pack()
    Button(screen53, text = "Add funds", command = funds_addition).pack()


def funds_addition():
    global fund
    global old_fund
    global fund_amount

    fund = IntVar()
    old_fund = IntVar()
    new_fund = IntVar()
    fund = fund_amount.get()
    print(fund)
    fund_read = open(username1, "r")
    data = fund_read.readlines()
    old_fund = int(data[7]) # Make it an integer to perform numerical calculations on the data
    new_fund = old_fund + fund
    new_fund = str(new_fund) # Have to make it a string before writing
    data[7] = new_fund
    print(new_fund)
    fund_write = open(username1, "w")
    fund_write.writelines(data)
    print(data)

    if len(str(fund))> 0:
        fund_amount_entry.delete(0, END)
        Label(screen53, text = "Funds have been added to the account").pack()
        Label(screen53, text = "Please refresh the account management screen").pack()
        screen.after(3000, screen53.destroy)
    
    



    


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
    global book_list
    global book_entry
    global book_list_data
    global path_for_books
    global purchasing_choice
    purchasing_choice = 1
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
    book_button = Button(screen15, text = "Select", command = selection_screen)
    book_button.pack()

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
    

def games():
    global screen16
    global game_list
    global game_entry
    global game_list_data
    global path_for_games
    global purchasing_choice
    purchasing_choice = 2
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
    game_button = Button(screen16, text = "Select", command = selection_screen)
    game_button.pack()
    
  




    
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


def electronics():
    global screen17
    global electronics_list
    global electronics_entry
    global electronics_list_data
    global path_for_electronics
    global purchasing_choice
    purchasing_choice = 3
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
    electronics_button = Button(screen17, text = "Select", command = selection_screen)
    electronics_button.pack()



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


def home_garden():
    global screen18
    global home_garden_list
    global home_garden_entry
    global home_garden_list_data
    global path_for_homegarden
    global purchasing_choice
    purchasing_choice = 4
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
    home_garden_button = Button(screen18, text = "Select", command = selection_screen)
    home_garden_button.pack()







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



def toys():
    global screen19
    global toys_list
    global toys_entry
    global toys_list_data
    global path_for_toys
    global purchasing_choice
    purchasing_choice = 5
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
    toys_button = Button(screen19, text = "Select", command = selection_screen)
    toys_button.pack()

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



def clothes_jewellery():
    global screen20
    global clothes_jewellery_list
    global clothes_jewellery_entry
    global clothes_jewellery_list_data
    global path_for_clothesjewellery
    global purchasing_choice
    purchasing_choice = 6
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
    clothes_jewellery_button = Button(screen20, text = "Select", command = selection_screen)
    clothes_jewellery_button.pack()





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



def sports_outdoors():
    global screen21
    global sports_outdoors_list
    global sports_outdoors_entry
    global sports_outdoors_list_data
    global path_for_sportsoutdoors
    global purchasing_choice
    purchasing_choice = 7
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
    sports_outdoors_button = Button(screen21, text = "Select", command = selection_screen)
    sports_outdoors_button.pack()

    


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





def food():
    global screen22
    global food_list
    global food_entry
    global food_list_data
    global path_for_food
    global purchasing_choice
    purchasing_choice = 8
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
    food_button = Button(screen22, text = "Select", command = selection_screen)
    food_button.pack()




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



def health():
    global screen23
    global health_list
    global health_entry
    global health_list_data
    global path_for_health
    global purchasing_choice
    purchasing_choice = 9
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
    health_button = Button(screen23, text = "Select", command = selection_screen)
    health_button.pack()

    


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


def motor_vehicles():
    global screen24
    global motor_vehicles_list
    global motor_vehicles_entry
    global motor_vehicles_list_data
    global path_for_motorvehicles
    global purchasing_choice
    purchasing_choice = 10
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
    motor_vehicles_button = Button(screen24, text = "Select", command = selection_screen)
    motor_vehicles_button.pack()

    
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


def education():
    global screen25
    global education_list
    global education_entry
    global education_list_data
    global path_for_education
    global purchasing_choice
    purchasing_choice = 11
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
    education_button = Button(screen25, text = "Select", command = selection_screen)
    education_button.pack()

    
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



    
def selection_screen():
    global screen51    
    global ORIGINAL_ROOT_DIR
    global selected_directory
    global purchasing_choice
    global selected_product
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
    global education_entry
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
    global selected_category

    selected_product = StringVar()
    selected_category = StringVar()

    if purchasing_choice == 1:
        selected_book = book_entry.get()
        selected_product = selected_book
        selected_directory = path_for_books
    elif purchasing_choice == 2:
        selected_game = game_entry.get()
        selected_product = selected_game
        selected_directory = path_for_games
    elif purchasing_choice == 3:
        selected_electronic = electronics_entry.get()
        selected_product = selected_electronic
        selected_directory = path_for_electronics
    elif purchasing_choice == 4:
        selected_home_garden = home_garden_entry.get()
        selected_product = selected_home_garden
        selected_directory = path_for_homegarden
    elif purchasing_choice == 5:
        selected_toys = toys_entry.get()
        selected_product = selected_toys
        selected_directory = path_for_toys
    elif purchasing_choice == 6:
        selected_clothes_jewellery = clothes_jewellery_entry.get()
        selected_product = selected_clothes_jewellery
        selected_directory = path_for_clothesjewellery
    elif purchasing_choice == 7:
        selected_sports_outdoors = sports_outdoors_entry.get()
        selected_product = selected_sports_outdoors
        selected_directory = path_for_sportsoutdoors
    elif purchasing_choice == 8:
        selected_food = food_entry.get()
        selected_product = selected_food
        selected_directory = path_for_food
    elif purchasing_choice == 9:
        selected_health = health_entry.get()
        selected_product = selected_health
        selected_directory = path_for_health
    elif purchasing_choice == 10:
        selected_motor_vehicles = motor_vehicles_entry.get()
        selected_product = selected_motor_vehicles
        selected_directory = path_for_motorvehicles
    elif purchasing_choice == 11:
        selected_education = education_entry.get()
        selected_product = selected_education
        selected_directory = path_for_education
    else:
        print("I really can't be asked to fix this issue")


    print(selected_product)
    print(selected_directory)
    screen51 = Toplevel(screen)
    screen51.title(selected_product)
    screen51.geometry("800x900")

    os.chdir(selected_directory)
    f = open(selected_product)
    content = f.readlines()

    Label(screen51, text = "Product Name:").pack()
    Label(screen51, text = content[0]).pack()
    Label(screen51, text = "Price:").pack()
    Label(screen51, text = content[1]).pack()
    Label(screen51, text = "Quantity").pack()
    Label(screen51, text = content[2]).pack()
    Label(screen51, text = "Seller:").pack()
    Label(screen51, text = content[3]).pack()
    Label(screen51, text = "Category:").pack()
    Label(screen51, text = content[4]).pack()
    Label(screen51, text = "Keyword 1:").pack()
    Label(screen51, text = content[5]).pack()
    Label(screen51, text = "Keyword 2:").pack()
    Label(screen51, text = content[6]).pack()
    Label(screen51, text = "Keyword 3:").pack()
    Label(screen51, text = content[7]).pack()
    Label(screen51, text = "Description:").pack()
    Label(screen51, text = content[8:-1]).pack() # Cannot remove the brace brackets, no clue how, simply going to leave it there

    Button(screen51, text = "Purchase", command = purchase_screen).pack()




    

    

    






def purchase_screen():
    global screen37
    global ORIGINAL_ROOT_DIR
    global purchasing_product
    global purchasing_directory
    purchasing_product = selected_product
    purchasing_directory = selected_directory

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
    global screen6 # Defining a new screen
    global purchasing_choice # Globalising the variable "purchasing_choice"
    global purchasing_product # Globalising the variable "purchasing_product"
    global purchasing_directory # Globalising the variable "purchasing_directory"
    os.chdir(purchasing_directory) # Changing the directory to the value of the variable "purchasing_directory"
    f = open(purchasing_product, "r") # Opening the file with the value of the variable "purchasing_product" as the file name, assigning the contents to the variable "f"
    content = f.readlines() # Separating the cotents & removing the newline comments of "f", assigning the updated content to the variable "content"
    quantity = IntVar() # Declaring the variable "quantity" as an integer variable
    quantity = int(content[2]) # Assigning the integer value of the third value within "content" to the variable "quantity"
    print(quantity)

    
    # DELETING SCREENS DEPENDING ON WHAT PRODUCT THE USER IS PURCHASING
    screen37.destroy() 
    screen8.destroy()
    screen51.destroy()
    if purchasing_choice == 1:
        screen15.destroy()
    elif purchasing_choice == 2:
        screen16.destroy()
    elif purchasing_choice == 3:
        screen17.destroy()
    elif purchasing_choice == 4:
        screen18.destroy()
    elif purchasing_choice == 5:
        screen19.destroy()
    elif purchasing_choice == 6:
        screen20.destroy()
    elif purchasing_choice == 7:
        screen21.destroy()
    elif purchasing_choice == 8:
        screen22.destroy()
    elif purchasing_choice == 9:
        screen23.destroy()
    elif purchasing_choice == 10:
        screen24.destroy()
    elif purchasing_choice == 11:
        screen25.destroy()
    
    if quantity == 0: # Initalising a conditional statement based on the value of the variable "quantity"
      # If the value of "quantity" equals 0 , it means that there is no more of the product available for purchase
      # Meaning that the user should not be able to purchase the product
        unlucky = Label(screen6, text = "None left, cannot purchase")
        unlucky.pack() # Displaying to the user that they are unable to purchase the product
        screen.after(3000, unlucky.destroy)

    
    
    else:
      # If the value of "quantity" does not equal 0, it means that there is an amount of the product available for purchase
      # Meaning that the user should be able to purchase the product
        quantity = quantity - 1 # Reducing the value of the variable "quantity" by 1
        os.chdir(path_for_users) # Changing directory to the value of the variable "path_for_users" (User directory)
        money_check = open(username1, "r") # Opening the file with the value of the variable "username1" (user file), assigning the contents to "money_check"
        buyer_content = money_check.readlines() # Separating the content & removing the newline comments of "money_check", assigning the content to the variable "buyer_content"
        money_available = IntVar() # Declaring the variable "money_available" as an integer variable
        money_available = int(buyer_content[7]) # Assigning the integer value of the 8th value within "buyer_content" to the variable "money_available"

        os.chdir(purchasing_directory) # Changing the directory to the value of the variable "purchasing_directory" (Directory of the purchasing product)
        price_check = open(purchasing_product, "r") # Opening the file with the value of the variable "purchasing_product", assigning the content to the variable "price_check"
        price_content = price_check.readlines() # Separating the content & removing the newline comments of "price_check", assigning the content to the variable "price_content"
        price = IntVar() # Declaring the variable "price" as an integer variable
        price = int(price_content[1]) # Assigning the integer value of the 2nd value within "price_content" to the variable "price"
        seller = StringVar() # Declaring the variable "seller" as a string variable
        seller = str(price_content[3]) # Have an issue where im getting the newline character
        seller = seller.strip() # Removing the newline comments & unnecessary whitespaces within the variable "seller"
        print(seller)
      
        

        os.chdir(path_for_users) # Changing the directory to the value of the variable "path_for_users" (User directory)
        seller_details = open(seller, "r") # Opening the file with the value of the variable "seller" as the file name, assigning the contents to the variable "seller_details"
        seller_content = seller_details.readlines() # Separating the contents & removing the newline comments of "seller_details", assigning the contents to the variable "seller_content"
        seller_money = int(seller_content[7]) # Assigning the integer value of the 8th value within "seller_content" to the variable "seller_money"
        

        if money_available > price: # Initialising a conditional statement based on whether the value of "money_available" is greater than "price"
          # If the value of "money_available" is greater than "price", it means that the user is able to afford the product
          # Meaning the purchase should be carried out
            money_available = money_available - price # Subtracting the values of the variable "price" from "money_available", assigning the result to the variable "money_available" (How much money the user would have remaining after the transactions)
            buyer_content[7] = str(money_available) # Assigning the string value of the variable "money_available" to the 8th element within the variable "buyer_content" (Updating the funds amount stored within the user account)
            seller_money = seller_money + price # Adding the values of the variables "seller_money" and "price", assigning the result to the variable "seller_money" (How much money the seller would have gained after the transaction)
            seller_content[7] = str(seller_money) # Assigning the string value of the variable "seller_money" to the 8th element within the variable "seller_content" (Updating the funds amount stored within the seller account)
            buyer_write = open(username1, "w") # Opening the file with the value of the variable "username1" (buyer), assigning the contents to the variable "buyer_write"
            buyer_write.writelines(buyer_content) # Separating the content & removing the newline comments within "buyer_content", assigning the contents to the variable "buyer_write"
            seller_write = open(seller, "w") # Opening the file with the value of the variable "seller" (seller), assigning the contents to the variable "seller_write"
            seller_write.writelines(seller_content) # Separating the content & removing the newline comments within "seller_content", assinging the contents to the variable "seller_write"
            q_data = StringVar() # Declaring the variable "q_data" as a string variable
            q_data = str(quantity) # Assigning the string value of the variable "quantity" to the variable "q_data"
            content[2] = (q_data + "\n")# Had an issue where funds were going up and down in the right places, but quantity wasnt going dowb
            print(content)
            os.chdir(purchasing_directory) # Changing the directory to the value of the variable "purchasing_directory"
            quantity_write = open(purchasing_product, "w") # Opening the file with the value of the variable "purchasing_product" as the file name, assigning the content to the variable "quantity_write"
            quantity_write.writelines(content) # Writing the value of "content" within the open file (With the updated quantity)
            lucky = Label(screen6, text = "Item purchased, delivery is who knows when")
            lucky.pack()
            screen.after(3000, lucky.destroy)
            print(username1)
            os.chdir(path_for_users) # Changing the directory to the value of the variable
            # Basically, I need to open the file with "a" as that is append, allowing for me to add info to the file (previous issue) opening the file with "w" destroys everyting within the file
            q = open(username1, "a") # Opening the file with the value of the variable "username1" as the file name, assigning the contents to the variable "q"
            print(q)
            q.write(purchasing_product + "\n") # Writing the value of the variable "purchasing_product" (purchased product) to the user file
            q.close()
        
            
        else:
            print("Purchase cancelled")
            
        
        

def selling():
    global screen9
    global product_entry
    global price_entry
    global quantity_entry
    global clicked
    global keyword1_entry
    global keyword2_entry
    global keyword3_entry
    global description_entry
    global str_out
    global options

    screen9 = Toplevel(screen)
    screen9.title("Generate a post")
    screen9.geometry("1920x1080")

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
    Label(screen9, text = "Quantity").pack()
    quantity_entry = Entry(screen9)
    quantity_entry.pack()
    Label(screen, text ="").pack() 
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
    global username1
    global forgotten_username_entry
    global forgotten_password_used
    global presence_counter
    print(ORIGINAL_ROOT_DIR)
    print("Works")

    product1 = StringVar()
    price1 = StringVar()
    quantity1 = StringVar()
    category1 = StringVar()
    keyword1 = StringVar()
    keyword2 = StringVar()
    keyword3 = StringVar()
    description = StringVar()
    product1 = product_entry.get()
    price1 = price_entry.get()
    quantity1 = quantity_entry.get()
    category1 = clicked.get()
    keyword1 = keyword1_entry.get()
    keyword2 = keyword2_entry.get()
    keyword3 = keyword3_entry.get()
    description = description_entry.get(1.0 , END)

    price_not_number = BooleanVar()
    price_not_number = False

    quantity_not_number = BooleanVar()
    quantity_not_number = False

    not_number = BooleanVar()
    not_number = False
    
    x = price_entry.get()
    try:
        int(x)
    except ValueError:
        price_not_number = True
        print(price_not_number)

    y = quantity_entry.get()
    try:
        int(y)
    except ValueError:
        quantity_not_number = True
        print(quantity_not_number)


    if (quantity_not_number == True) or (price_not_number == True):
        not_number = True
        print(not_number)
    else:
        not_number = False
        print(not_number)
        


    

    if not_number == False:
        if forgotten_password_used == True:
            print(forgotten_username_entry)
        else:
            print(username1)
            print(product1)
            print(category1)
            print(price1)
            print(quantity1)
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
        else:
            print("Category not selected")
            selling()

        if len(product1) == 0:
            print("WORKS")
            screen9.destroy()
            no_product1_entry = Label(screen6, text = "Product name has not been entered, please enter again")
            no_product1_entry.pack()
            screen.after(3000, no_product1_entry.destroy)
            return
        if len(price1) == 0:
            screen9.destroy()
            no_price1_entry = Label(screen6, text = "Price has not been entered, please enter all information again")
            no_price1_entry.pack()
            screen.after(3000, no_price1_entry.destroy)
            return
        if len(quantity1) == 0:
            screen9.destroy()
            no_quantity1_entry = Label(screen6, text = "Quantity has not been entered, please enter all information again")
            no_quantity1_entry.pack()
            screen.after(3000, no_quantity1_entry.destroy)
            return
        if len(keyword1) == 0:
            screen9.destroy()
            no_keyword_1_entry = Label(screen6, text = "Keyword 1 has not been entered, please enter all information again")
            no_keyword1_entry.pack()
            screen.after(3000, no_keyword1_entry.destroy)
            return
        if len(keyword2) == 0:
            screen9.destroy()
            no_keyword2_entry = Label(screen6, text = "Keyword 2 has not been entered, please enter all information again")
            no_keyword2_entry.pack()
            screen.after(3000, no_keyword2_entry.destroy)
            return
        if len(keyword3) == 0:
            screen9.destroy()
            no_keyword3_entry = Label(screen6, text = "Keyword 3 has not been entered, please enter all information again")
            no_keyword3_entry.pack()
            screen.after(3000, no_keyword3_entry.destroy)
            return
        if len(description) == 0:
            screen9.destroy()
            no_description_entry = Label(screen6, text = "Nothing has been entered for description, please add more")
            no_description_entry.pack()
            screen.after(3000, no_description_entry.destroy)
            return
            
            
            
    

  

        file=open(product1,  "w")
        file.write(product1+"\n")
        file.write(price1+"\n")
        file.write(quantity1+"\n")
    
        if forgotten_password_used == True:
            username = forgotten_username_entry.get()
            file.write(username+"\n")
        else:
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
        successful_listing = Label(screen6, text = "Product sucessfully listed", fg = "green", font = ("Calibri", 11))
        successful_listing.pack()
        screen.after(3000, successful_listing.destroy)
    else:
        if price_not_number == True:
            price_entry.delete(0, END)
            price_no_num = Label(screen9, text = "Only integer value accepted for Price, please correct")
            price_no_num.pack()
            screen.after(3000, price_no_num.destroy)
        elif quantity_not_number == True:
            quantity_entry.delete(0, END)
            quantity_no_num = Label(screen9, text = "Only an integer value can be accepted for quantity, please correct")
            quantity_no_num.pack()
            screen.after(3000, quantity_no_num.destroy)

 
def review_mainmenu():
    global screen39
    screen39 = Toplevel(screen)
    screen39.title("Reviews")
    screen39.geometry("350x500")
    Label(screen39, text = "Review Main Menu").pack()

    Button(screen39, text = "Leave a review", command=review_write_select_user).pack()
    Button(screen39, text = "Look at seller's rating", command = review_read_select_user).pack()



def review_write_select_user():
    global screen40
    global review_write_user_entry
    global user_list_write
    global path_for_users
    global user_list_data_write
    screen40 = Toplevel(screen)
    screen40.title("Selecting the User")
    screen40.geometry("350x500")

    review_write_user_entry = Entry(screen40,)
    review_write_user_entry.pack()

    #create a list box
    user_list_write = Listbox(screen40)
    user_list_write.pack()

    #create a list
    user_list_data_write = os.listdir(path_for_users)
    #Add the data to the list
    update_user_list_write(user_list_data_write)
    #Create a binding on the listbox onclick
    user_list_write.bind("<<ListboxSelect>>", fillout_user_list_write)
    #Create a binding on the entry box
    review_write_user_entry.bind("<KeyRelease>", check_user_list_write)
    #Button to select
    review_write_button = Button(screen40, text = "Select", command = review_write)
    review_write_button.pack()  


def review_write():
    global screen41
    global path_for_reviews
    global header_entry
    global review_entry
    global selected_user
    global review_write_user_entry
    screen41 = Toplevel(screen)
    screen41.title("Leave a review")
    screen41.geometry("350x500")
    Label(screen40, text = "Leaving a review").pack()
    
    review_entry = StringVar()
    header_entry = StringVar()
    os.chdir(path_for_reviews)
    Label(screen41, text = "Header").pack()
    header_entry= Entry(screen41)
    header_entry.pack()
    Label(screen41, text = "Description of review").pack()
    review_entry = Text(screen41, height = 8, width = 60)
    review_entry.pack()
    selected_user = StringVar()
    selected_user = review_write_user_entry.get()
    print(selected_user)
    Button(screen41, text = "Store values", command=review_write_store).pack()


def review_write_store():
    global screen42
    global header
    global review
    global selected_user
    header = header_entry.get()
    review = review_entry.get(1.0 , END)
    print(header)
    print(review)
    print(selected_user)
    filename = selected_user + header
    print(filename)

    if len(header) == 0:
        screen41.destroy()
        no_header_entry = Label(screen40, text = "No header has been inputted")
        no_header_entry.pack()
        screen.after(3000, no_header_entry.destroy)
        return
    if len(review) == 0:
        screen41.destroy()
        no_review_entry = Label(screen40, text = "Nothing has been entered for the review")
        no_review_entry.pack()
        screen.after(3000, no_review_entry.destroy)
        return
    
    os.chdir(path_for_reviews)
    file=open(filename, "w")
    file.write(header+"\n")
    file.write(review+"\n")
    file.close()
    Label(screen41, text = "Review submitted").pack()
    screen41.destroy()

    
def review_read_select_user():
    global screen43
    global review_read_user_entry
    global user_list_read
    global path_for_users
    global user_list_data_read
    screen43 = Toplevel(screen)
    screen43.title("Selecting the User")
    screen43.geometry("350x500")
    review_read_user_entry = Entry(screen43,)
    review_read_user_entry.pack()
    #create a list box
    user_list_read = Listbox(screen43)
    user_list_read.pack()
    #create a list
    user_list_data_read = os.listdir(path_for_users)
    #Add the data to the list
    update_user_list_read(user_list_data_read)
    #Create a binding on the listbox onclick
    user_list_read.bind("<<ListboxSelect>>", fillout_user_list_read)
    #Create a binding on the entry box
    review_read_user_entry.bind("<KeyRelease>", check_user_list_read)
    #Button to select
    review_read_button = Button(screen43, text = "Select", command = review_read_selection)
    review_read_button.pack()  

    #use this to separate the users name and the review header, use this to search through the reviews
    #user would input a name, the function would implement this to the data
    #x = filename.split(selected_user)
    #print(x)


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


def update_review_list_read(review_list_data_read):
    global review_list_read
    #Clear the listbox
    review_list_read.delete(0, END)
    #Add data to listbox
    for item in review_list_data_read:
        review_list_read.insert(END, item)


#Update entry box with listbox clicked
def fillout_review_list_read(event):
    global review_read_selection_entry
    #Delete whatever is in the entry box
    review_read_selection_entry.delete(0, END)
    #Add clicked list item to entry box
    review_read_selection_entry.insert(0, review_list_read.get(ACTIVE))

def check_review_list_read(event):
    #Grab what was typed
    global review_read_selection_entry
    global review_list_data_read
    typed_review_read = review_read_selection_entry.get()
    
    if typed_review_read == " ":
        data = review_list_data_read
    else:
        data = []
        for item in review_list_data_read:
            if typed_review_read.lower() in item.lower():
                data.append(item)
    update_review_list_read(data)


def review_read_selection():
    global screen44
    global path_for_reviews
    global selected_user
    global review_read_user_entry
    global review_read_selection_entry
    global review_list
    global review_list_read

    screen44 = Toplevel(screen)
    screen44.title("Select review")
    screen44.geometry("350x500")
    Label(screen44, text = "Select a review").pack()
    selected_user = StringVar()
    selected_user = review_read_user_entry.get()
    print(selected_user)
    review_data_structure = []
    for file in os.listdir(path_for_reviews):
        if file.startswith(selected_user):
            file = file.replace(selected_user, '')
            print(file)
            review_data_structure.append(file)
            print(review_data_structure)
        else:
            print("It doesn't work")

    review_read_selection_entry = Entry(screen44,)
    review_read_selection_entry.pack()
    #create a list box
    review_list_read = Listbox(screen44)
    review_list_read.pack()
    #create a list
    review_list_data_read = review_data_structure
    #Add the data to the list
    update_review_list_read(review_list_data_read)
    #Create a binding on the listbox onclick
    review_list_read.bind("<<ListboxSelect>>", fillout_review_list_read)
    #Create a binding on the entry box
    review_read_selection_entry.bind("<KeyRelease>", check_review_list_read)
    #Button to select
    review_read_button = Button(screen44, text = "Select", command = review_read)
    review_read_button.pack()  
    

def review_read():
    global screen45
    global actual_review_header
    global review_read_selection_entry
    global path_for_reviews
    global selected_user
    global review_header
    global review_description
    global selected_user
    screen45 = Toplevel(screen)
    screen45.title("Reviews")
    screen45.geometry("350x500")
    Label(screen45, text = "Review").pack()
    actual_review_header = StringVar()
    actual_review_header = review_read_selection_entry.get()
    print(actual_review_header)
    print(path_for_reviews)
    review_file = StringVar()
    review_file = " "
    review_file = selected_user + actual_review_header
    print(review_file)
    os.chdir(path_for_reviews)
    list_of_files = os.listdir()
    if review_file in list_of_files:
        review_file1 = open(review_file, "r")
        review_file = review_file1.read().splitlines()
        print(review_file[1])
    else:
        pass

    review_header = StringVar()
    review_description = StringVar()
    review_header = review_file[0]
    review_description = review_file[1:-1]
    Label(screen45, text = "Header:").pack()
    Label(screen45, text = review_header).pack()
    Label(screen45, text = "").pack()
    Label(screen45, text = "Description:").pack()
    Label(screen45, text = review_description).pack()

 
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


def screen_deletion():
    global delete_counter
    if delete_counter == 4:
        screen5.destroy()
    elif delete_counter == 48:
        screen48.destroy()


def log_out(): 
    screen6.destroy()

  
main_screen()
