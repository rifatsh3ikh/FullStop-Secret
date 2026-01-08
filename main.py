import customtkinter as ctk
import string
import secrets
import pyperclip

def generate():
    char_pool = ""
    if lower_switch.get(): char_pool += string.ascii_lowercase
    if upper_switch.get(): char_pool += string.ascii_uppercase
    if num_switch.get(): char_pool += string.digits
    if sym_switch.get(): char_pool += string.punctuation

    if not char_pool:
        password_entry.delete(0, 'end')
        password_entry.insert(0, "Choose Settings!")
        return

    length = int(length_slider.get())
    password = "".join(secrets.choice(char_pool) for _ in range(length))
    password_entry.delete(0, 'end')
    password_entry.insert(0, password)

def update_label(value):
    length_label.configure(text=f"Length: {int(value)}")

# UI
ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.iconbitmap("logo.ico")
app.title("FullStop Secret")
app.geometry("400x520")

# Title
title = ctk.CTkLabel(app, text="PASSWORD GENERATOR", font=("Impact", 25))
title.pack(pady=20)

# Password Display
password_entry = ctk.CTkEntry(app, width=300, height=50, font=("Consolas", 18), justify="center")
password_entry.pack(pady=10)

# Slider Length
length_label = ctk.CTkLabel(app, text="Length: 12", font=("Arial", 14, "bold"))
length_label.pack(pady=(10, 0))

length_slider = ctk.CTkSlider(app, from_=8, to=32, number_of_steps=24, command=update_label)
length_slider.set(12)
length_slider.pack(pady=10)

# Frame
settings_frame = ctk.CTkFrame(app, fg_color="transparent")
settings_frame.pack(pady=10)

lower_switch = ctk.CTkSwitch(settings_frame, text="Lowercase (abc)")
lower_switch.select()
lower_switch.pack(pady=5, anchor="w")

upper_switch = ctk.CTkSwitch(settings_frame, text="Uppercase (ABC)")
upper_switch.select()
upper_switch.pack(pady=5, anchor="w")

num_switch = ctk.CTkSwitch(settings_frame, text="Numbers (123)")
num_switch.select()
num_switch.pack(pady=5, anchor="w")

sym_switch = ctk.CTkSwitch(settings_frame, text="Symbols (!@#)")
sym_switch.pack(pady=5, anchor="w")

# Action Button
gen_button = ctk.CTkButton(app, text="GENERATE", command=generate, 
                           height=45, font=("Arial", 14, "bold"), fg_color="#0E7742")
gen_button.pack(pady=25)

app.mainloop()