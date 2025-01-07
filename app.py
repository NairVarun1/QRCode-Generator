from tkinter import messagebox, filedialog, colorchooser

import qrcode
from tkinter import *
from PIL import Image, ImageTk


def generate_qr_code():
    data = data_entry.get()
    if not data:
        messagebox.showerror("Error", "Please enter valid data")
        return

    save_path = save_path_entry.get()
    if not save_path:
        messagebox.showerror("Error", "Please enter valid save path")
        return

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=5,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img.save(save_path)

    messagebox.showinfo("QR Code Generated", f"Code Saved at {save_path}")
    show_qr_code(save_path)


def choose_save_path():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG", "*.png"), ("All Files", "*.*")],
    )
    save_path_entry.delete(0, 'end')
    save_path_entry.insert(0, file_path)


def choose_fill_color():
    global fill_color
    color = colorchooser.askcolor(title="Choose fill color")[1]
    if color:
        fill_color = color
        fill_color_label.config(bg=color)


def choose_back_color():
    global back_color
    color = colorchooser.askcolor(title="Choose back color")[1]
    if color:
        back_color = color
        back_color_label.config(bg=color)


def show_qr_code(image_path):
    # Display the generated QR code in the GUI
    qr_image = Image.open(image_path)
    qr_image = qr_image.resize((200, 200), Image.LANCZOS)  # Updated from ANTIALIAS to LANCZOS
    qr_photo = ImageTk.PhotoImage(qr_image)
    qr_label.config(image=qr_photo)
    qr_label.image = qr_photo


fill_color = "black"
back_color = "white"

root = Tk()
root.title("QR Code Generator")

Label(root, text="Enter Data:").grid(row=0, column=0, padx=10, pady=10)
data_entry = Entry(root, width=50)
data_entry.grid(row=0, column=1, padx=10, pady=10)

Label(root, text="Enter Save Path:").grid(row=1, column=0, padx=10, pady=10)
save_path_entry = Entry(root, width=50)
save_path_entry.grid(row=1, column=1, padx=10, pady=10)
Button(root, text="Browse", command=choose_save_path).grid(row=1, column=2, padx=10, pady=10)

Label(root, text="Enter Fill Color").grid(row=2, column=0, padx=10, pady=10)
fill_color_label = Label(root, text="", bg=fill_color, width=10)
fill_color_label.grid(row=2, column=1, padx=10, pady=10)
Button(root, text="Choose", command=choose_fill_color).grid(row=2, column=2, padx=10, pady=10)

Label(root, text="Background Color:").grid(row=3, column=0, padx=10, pady=10)
back_color_label = Label(root, text="", bg=back_color, width=10)
back_color_label.grid(row=3, column=1, padx=10, pady=10)
Button(root, text="Choose", command=choose_back_color).grid(row=3, column=2, padx=10, pady=10)

Button(root, text="Generate QR Code", command=generate_qr_code).grid(row=4, column=0, padx=10, pady=10)

qr_label = Label(root, text="Generated Code will appear here !")
qr_label.grid(row=5, column=0, padx=10, pady=10)

root.mainloop()
