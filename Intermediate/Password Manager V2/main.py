from tkinter import *
from tkinter import messagebox #this is not a class
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():

    password_entry.delete(0,END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for item in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for item in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for item in range(random.randint(2, 4))]

    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():

    website = website_entry.get().lower()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email" : email,
            "password" : password,
        }
    }


    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title = "Warning !", message = "Please do not leave any field empty.")

    else:
        is_ok = messagebox.askokcancel(title = website, message= f"These are the details entered : \n"
                                                                             f"Email: {email}\n"
                                                                             f"Password: {password}\n"
                                                                             f"Is it okay to save ? " )

        if is_ok:
            try:
                with open("data.json", "r") as new_file:
                    #returning old data
                    data = json.load(new_file)
                    #update old data with new data
            except FileNotFoundError:
                with open("data.json","w") as new_file:
                    json.dump(new_data,new_file,indent=4)
            else:
                data.update(new_data)
                with open("data.json","w") as new_file:
                    #write new data into json
                    json.dump(data, new_file ,indent=4)
            finally:
                website_entry.delete(0,END)
                password_entry.delete(0,END)
# ---------------------------- search data ------------------------------- #

def search_data():
    try:
        with open("data.json", "r") as new_file:
            data = json.load(new_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error",message="No file is found")
    else:
        query = website_entry.get().lower()
        if len(query) == 0:
            messagebox.showerror(title= "Empty", message="Website Entry is empty, nothing to search !")
        else:
            if query in data:
                email = data[query]["email"]
                password = data[query]["password"]
                messagebox.showinfo(title=query, message=f"Email = {email} \n Password = {password}")
            else:
                messagebox.showerror(title="Error",message="No such website found in data.")



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file= "logo.png")
canvas.create_image(50,100, image=lock_img)
canvas.grid(row=0,column=1)

#Label
website_label = Label(text="Website: ")
website_label.grid(row=1,column=0)
email_label = Label(text = "Email/Username: ")
email_label.grid(row=2,column=0)
password_label = Label(text = "Password: ")
password_label.grid(row=3,column=0)

#Entry
website_entry = Entry(width=20)
website_entry.insert(END, string="")
website_entry.focus()
website_entry.grid(row=1,column=1, sticky="w") #can use columnspan as well

email_entry = Entry(width=40)
email_entry.insert(END, string="")
email_entry.grid(row=2,column=1)
email_entry.insert(0,"kyuan0853@gmail.com")

password_entry = Entry(width=20)
password_entry.insert(END, string="")
password_entry.grid(row=3,column=1, sticky="w")

#Button
generate_button = Button(text= "Generate Password", width = 15,command=generate_password)
generate_button.grid(row=3,column=1,sticky="e")

add_button = Button(text= "Add", width=37,command=save_password)
add_button.grid(row=4, column=1)

search_button = Button(text= "Search",width=15, command=search_data)
search_button.grid(row=1, column=1,sticky="e")





window.mainloop()