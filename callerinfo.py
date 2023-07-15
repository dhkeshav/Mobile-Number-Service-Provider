import phonenumbers
from phonenumbers import geocoder, carrier
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter.font import Font

root = tk.Tk()
root.title("Mobile Number Info")

background_image = Image.open("Assets/background_image.jpg")
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

window_width = 400
window_height = 250
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width / 2) - (window_width / 2)
y_coordinate = (screen_height / 2) - (window_height / 2)
root.geometry(f"{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}")


root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(2, weight=1)

label_font = Font(weight="bold")
label = tk.Label(root, text="Enter Mobile Number with country code:", font=label_font)
label.grid(row=2, column=1, pady=(50, 10))

mobile_entry = tk.Entry(root)
mobile_entry.grid(row=3, column=1, pady=10)

def get_mobile_info():
    mobile_no = mobile_entry.get()

    try:
        parsed_number = phonenumbers.parse(mobile_no)

        is_possible = phonenumbers.is_possible_number(parsed_number)
        is_valid = phonenumbers.is_valid_number(parsed_number)
        service_provider = carrier.name_for_number(parsed_number, "en")
        country = geocoder.description_for_number(parsed_number, "en")

        message = f"Checking possibility of a Number: {is_possible}\n"
        message += f"Valid Mobile Number: {is_valid}\n"
        message += f"Service Provider: {service_provider}\n"
        message += f"Country: {country}"

        messagebox.showinfo("Mobile Number Info", message)

    except phonenumbers.phonenumberutil.NumberParseException:
        messagebox.showerror("Error", "Invalid phone number. Please enter a valid number.")

button = tk.Button(root, text="Get Info", font=label_font, command=get_mobile_info)
button.grid(row=4, column=1, pady=(10, 50))

root.mainloop()