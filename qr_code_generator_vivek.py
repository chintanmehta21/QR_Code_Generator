import tkinter as tk
from tkinter import ttk
import qrcode
from PIL import Image, ImageTk
import os

# Function to generate QR code
def generate_qr_code():
    # Retrieve values from entries
    data = ""
    fields = {
        "Job No": entry_job_no.get(),
        "Serial No": entry_serial_no.get(),
        "Man Year": entry_man_year.get(),
        "Pressure": entry_pressure.get(),
        "Batch": entry_batch.get(),
        "Weight": entry_weight.get(),
        "Model": entry_model.get(),
        "Part Code": entry_part_code.get(),
    }
    for label, value in fields.items():
        if value:  # Check if the field has a value
            data += f"{label}: {value}\n"
    
    # Generate QR code
    if data:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save("qr_code.png")

        # Display QR code
        img = Image.open("qr_code.png")
        img = img.resize((250, 250))  # Corrected line
        img = ImageTk.PhotoImage(img)
        label_image.config(image=img)
        label_image.photo = img  # keep a reference!
    else:
        label_image.config(image='')
		
# Create the main window
root = tk.Tk()
root.title("QR Code Generator")

# Variables for checkboxes
var_serial = tk.BooleanVar()
var_order = tk.BooleanVar()
var_chart = tk.BooleanVar()

# Create widgets for new fields
entry_job_no = ttk.Entry(root)
entry_job_no.grid(row=0, column=1)
ttk.Label(root, text="Job No").grid(row=0, column=0, sticky=tk.W)

entry_serial_no = ttk.Entry(root)
entry_serial_no.grid(row=1, column=1)
ttk.Label(root, text="Serial No").grid(row=1, column=0, sticky=tk.W)

entry_man_year = ttk.Entry(root)
entry_man_year.grid(row=2, column=1)
ttk.Label(root, text="Man Year").grid(row=2, column=0, sticky=tk.W)

entry_pressure = ttk.Entry(root)
entry_pressure.grid(row=3, column=1)
ttk.Label(root, text="Pressure").grid(row=3, column=0, sticky=tk.W)

entry_batch = ttk.Entry(root)
entry_batch.grid(row=4, column=1)
ttk.Label(root, text="Batch").grid(row=4, column=0, sticky=tk.W)

entry_weight = ttk.Entry(root)
entry_weight.grid(row=5, column=1)
ttk.Label(root, text="Weight").grid(row=5, column=0, sticky=tk.W)

entry_model = ttk.Entry(root)
entry_model.grid(row=6, column=1)
ttk.Label(root, text="Model").grid(row=6, column=0, sticky=tk.W)

entry_part_code = ttk.Entry(root)
entry_part_code.grid(row=7, column=1)
ttk.Label(root, text="Part Code").grid(row=7, column=0, sticky=tk.W)

# Adjust the button and label_image grid row accordingly
ttk.Button(root, text="Generate QR Code", command=generate_qr_code).grid(row=8, columnspan=2)
label_image = ttk.Label(root)
label_image.grid(row=9, columnspan=2)

# Run the application
root.mainloop()