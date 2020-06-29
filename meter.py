import tkinter as tk
import tkinter.font as font
from tkinter import ttk
from windows import set_dpi_awareness
set_dpi_awareness()


def calculate_feet():
    try:
        metres = float(metres_value.get())
        feet = (metres * 3.28084)
        feet_value.set("{:.3f}".format(float(feet)))
        # print("{} metres is equal to {:.3f} feet".format(metres, feet))
    except ValueError:
        pass


# the main window code
root = tk.Tk()
root.title("Distance Converter")
root.resizable(0, 0)


# setting the font of the GUI
font.nametofont("TkDefaultFont").configure(size=12)     # the drawback of this is that the entry widget text remains
# unchanged

# this is a variable that will be used to get the the value from the entry widget
metres_value = tk.StringVar()
feet_value = tk.StringVar(value='Feet shown here')

# the frame that hold the rest of the GUI components
main = ttk.Frame(root, padding=(30, 15))
main.grid()     # default is column=0, row=0, hence we write just grid()


# GUI components Define below
metres_label = ttk.Label(main, text='Metres:')
metres_entry = ttk.Entry(main, width=10, textvariable=metres_value, font=("Segoe UI", 12))
feet_label = ttk.Label(main, text='Feet')
feet_display = ttk.Label(main, textvariable=feet_value)
calc_button = ttk.Button(main, text='Calculate', command=calculate_feet)

# GUI components will be place below using Grid Manager
metres_label.grid(row=0, column=0, sticky='w')       # padx=5, pady=5
metres_entry.grid(row=0, column=1, sticky='ew')      # padx=5, pady=5
metres_entry.focus()
feet_label.grid(row=1, column=0, stick='w')          # padx=5, pady=5
feet_display.grid(row=1, column=1)                   # padx=5, pady=5
calc_button.grid(row=2, column=0, columnspan=2, sticky='ew')        # padx=5, pady=5

# binding shortcut keys from the keyboard to the components of the GUI
root.bind("<Return>", calculate_feet)
root.bind("<KP_Enter>", calculate_feet)

# we will remove the redundant padx and pady that we have in almost all the GUI components by using
# the winfo_children() method which will allow us to set the padding of the components at one go rather
# than individually like we did before
for child in main.winfo_children():
    child.grid_configure(padx=15, pady=15)

root.mainloop()
