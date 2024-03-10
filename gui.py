import json
import tkinter
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from playsound import playsound
import csv



class AccCreateWin(tkinter.Toplevel):

    def __init__(self):
        super().__init__()

        self.geometry("500x500")
        self.title("My Game 2.0")

        self.sign_up_canvas = Canvas(self, width=500, height=500)
        self.sign_up_canvas.grid(row=0, column=0)
        self.sign_up_canvas.configure(highlightthickness=0)

        self.sign_up_canvas_bg = Image.open("images/sign_up_BG.jpg")
        self.sign_up_image_resized = self.sign_up_canvas_bg.resize((500, 500))
        self.sign_up_final_bg = ImageTk.PhotoImage(self.sign_up_image_resized)
        self.sign_up_canvas.create_image(0, 0, anchor=NW, image=self.sign_up_final_bg)

        self.sign_up_canvas.create_text(250, 75, fill="white", text="Account Creation",font=("arial", 25))

        self.sign_up_canvas.create_text(140, 152, fill="white", text="Username:", font=("arial", 14))
        self.create_username = Entry(self.sign_up_canvas, fg="white", bg="black", width=35)

        self.create_username.focus()
        self.create_username.place(x=193, y=145)

        self.sign_up_canvas.create_text(160, 197, fill="white", text="Email:", font=("arial", 14))
        self.save_email = Entry(self.sign_up_canvas, fg="white", bg="black", width=35)
        self.save_email.place(x=193, y=190)

        self.sign_up_canvas.create_text(140, 243, text="Password:", fill="white",font=("arial", 14))
        self.p1 = Entry(self.sign_up_canvas, width=35, bg="black", fg="white")
        self.p1.place(x=193, y=235)

        self.sign_up_canvas.create_text(102, 290, text="Re-enter Password:", fill="white",font=("arial", 14))
        self.p2 = Entry(self.sign_up_canvas, width=35, bg="black", fg="white")
        self.p2.place(x=193, y=281)

        self.save_account_button = Button(self.sign_up_canvas, text="SAVE", fg="white", bg="black", width=42, command=self.account_creation)
        self.save_account_button.place(x=105, y=315)

        self.cancel_button = Button(self.sign_up_canvas, text="CANCEL", bg="black", fg="white", width=42)
        self.cancel_button.place(x=105, y=350)



    def return_username(self):
        return self.create_username.get()


    def account_creation(self):
        pass1 = self.p1.get()
        pass2 = self.p2.get()
        usnam = self.create_username.get()
        email = self.save_email.get()

        user_data_structure = {
            f"{usnam} log in info":{
                "Email": email,
                "Username": usnam,
                "Password": pass1
            }
        }

        if pass1 != pass2 and len(pass1) >= 4:
            messagebox.showwarning(title="Warning", message="Passwords must be longer than 3 characters and match.")
        else:
            with open(f"./User_Data/{usnam}.json", "w") as user_file:
                json.dump(user_data_structure, user_file, indent=4)
                messagebox.showinfo(title="Account created", message="Your Account was successfully created")
                AccCreateWin.destroy(self)



class StartMenu(tkinter.Toplevel):

    def __init__(self):
        super().__init__()

        self.attributes('-fullscreen', True)

        self.start_menu_canvas = Canvas(self, width=1920, height=1200)
        self.start_menu_canvas.grid(row=0, column=0)
        self.start_menu_canvas.configure(highlightthickness=0)

        self.sign_up_canvas_bg = Image.open("images/Start_menu_Background.jpg")
        self.sign_up_image_resized = self.sign_up_canvas_bg.resize((1920, 1200))
        self.sign_up_final_bg = ImageTk.PhotoImage(self.sign_up_image_resized)
        self.start_menu_canvas.create_image(0, 0, anchor=NW, image=self.sign_up_final_bg)

        self.start_menu_canvas.create_text(960, 120, text="My Game 2.0", fill="white", font=('terminal', "110"))

        self.start_button = Button(self.start_menu_canvas, text="START", fg="white", bg="black", width=35, height=2, command=self.start)
        self.start_button.place(x=830, y=390)

        self.characters_button = Button(self.start_menu_canvas, text="CHARACTERS", bg="black", fg="white", width=35, height=2)
        self.characters_button.place(x=830, y=450)

        self.tutorial_button = Button(self.start_menu_canvas, text="TUTORIAL", bg="black", fg="white", width=35, height=2)
        self.tutorial_button.place(x=830, y=510)

        self.settings_button = Button(self.start_menu_canvas, text="SETTINGS", bg="black", fg="white", width=35, height=2)
        self.settings_button.place(x=830, y=570)

        self.exit_button = Button(self.start_menu_canvas, text="EXIT", fg="white", bg="black", width=35, height=2, command=self.exit)
        self.exit_button.place(x=830, y=650)

        self.start_menu_canvas.create_text(1830, 1050, text="@Royal Games Inc.", fill="white")
        self.start_menu_canvas.create_text(100, 1050, text="Drf1331.code@gmail.com", fill="white")
        #playsound("sounds/heros-time-paulo-kalazzi-main-version-01-51-2639.mp3", block=False)

    def start(self):
        StartMenu.destroy(self)
        LogInWindow.destroy(self)
        game_menu = GameWindow()


    def exit(self):
        LogInWindow.destroy(self)




class LogInWindow(tkinter.Tk):

    def __init__(self):
        super().__init__()

        self.geometry("700x400")
        self.title("My Game 2.0")

        self.canvas = Canvas(self, width=700, height=400)
        self.canvas.grid(row=0, column=0)
        self.canvas.configure(highlightthickness=0)
        self.canvas_bg = Image.open("images/log_in_image.jpg")
        self.canvas_bg_resized = self.canvas_bg.resize((700, 400))
        self.final_bg = ImageTk.PhotoImage(self.canvas_bg_resized)

        self.canvas.create_image(0, 0, anchor=NW, image=self.final_bg)

        self.canvas.create_text(180, 160, text='Username:', fill="white", font=('Helvetica','12'))
        self.username = self.username_entry = Entry(width=40, bg="black", fg="white")
        self.username_entry.place(x=220, y=150)
        self.username_entry.focus()

        self.canvas.create_text(335, 90, text="My Game 2.0", fill="white", font=('terminal', "30"))

        self.canvas.create_text(180, 200, text="Password:", fill="white", font=('Helvetica','12'))
        self.password_entry = Entry(width=40, bg="black", fg="white")
        self.password_entry.place(x=220, y=190)

        self.log_in_button = Button(text="Log In", bg="black", fg="white", width=16, command=self.log_in)
        self.log_in_button.place(x=220, y=230)

        self.sign_up_button = Button(text="Sign Up", bg="black", fg="white", width=16, command=self.open_acc_create_win)
        self.sign_up_button.place(x=345, y=230)



    def open_acc_create_win(self):
        ac_win = AccCreateWin()
        ac_win.grab_set()


    def open_start_menu(self):
        start_win = StartMenu()
        start_win.start_menu_canvas.create_text(960, 230, text=f"Signed in as: {main_window.username_entry.get()}",
                                                fill="white", font=('Helvetica','18'))
        start_win.grab_set()

    def log_in(self):
        usnam = self.username_entry.get()
        v_password = self.password_entry.get()

        try:
            with open(f"./User_Data/{usnam}.json", "r") as user_data:
                loaded_data = json.load(user_data)
        except FileNotFoundError:
            messagebox.showwarning(title="No file error.", message="There was no file under that UserName.\nPlease check spelling or create an account.")
        else:
            try:
                if loaded_data[f"{usnam} log in info"]["Password"] == v_password:
                    self.open_start_menu()
                    self.password_entry.delete(0, END)
            except KeyError:
                messagebox.showwarning(title="No file error.",
                                       message="There was no file under that Username.\nPlease check spelling or create an account.")



class GameWindow(tkinter.Tk):

    def __init__(self):
        super().__init__()

        self.attributes('-fullscreen', True)

        self.game_canvas = Canvas(self, width=1920, height=1200)
        self.game_canvas.grid(row=0, column=0)
        self.game_canvas.configure(highlightthickness=0)

        self.sign_up_canvas_bg = Image.open("images/game_board_image.jpg")
        self.sign_up_image_resized = self.sign_up_canvas_bg.resize((1920, 1200))
        self.sign_up_final_bg = ImageTk.PhotoImage(self.sign_up_image_resized)
        self.game_canvas.create_image(0, 0, anchor=NW, image=self.sign_up_final_bg)






if __name__ == "__main__":
    main_window = LogInWindow()

    main_window.mainloop()













