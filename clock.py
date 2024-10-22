import tkinter as tk
from tkinter import ttk
from datetime import datetime
import pytz

# List of time zones
timezones = pytz.all_timezones

def update_clock():
    # Get the selected time zones
    selected_timezone1 = timezone_var1.get()
    selected_timezone2 = timezone_var2.get()
    
    # Get the current time in the selected time zones
    timezone1 = pytz.timezone(selected_timezone1)
    timezone2 = pytz.timezone(selected_timezone2)
    current_time_str1 = datetime.now(timezone1).strftime('%H:%M:%S %p')
    current_time_str2 = datetime.now(timezone2).strftime('%H:%M:%S %p')
    
    # Update the labels with the current time
    time_label1.config(text=f"{current_time_str1}")
    time_label2.config(text=f"{current_time_str2}")
    
    # Call the update function every second
    root.after(1000, update_clock)

# Set up the main window
root = tk.Tk()
# root.configure(width=300, height=300)
root.title("Dual Time Zone Clock")
root.configure(bg='darkgrey',)  # Set the background color to dark grey

# Create a heading label
heading_label = tk.Label(root, text="Dual Time Zone Clock", font=('calibri', 24, 'bold'), bg='darkgrey', fg='purple')
heading_label.pack(pady=20)  # Add padding above and below

# Create variables for the selected timezones
timezone_var1 = tk.StringVar(value=timezones[0])  # Default to first timezone
timezone_var2 = tk.StringVar(value=timezones[0])  # Default to UTC timezone

# Create Comboboxes for selecting time zones
timezone_combobox1 = ttk.Combobox(root, textvariable=timezone_var1, values=timezones, state="readonly", font=('calibri', 16))
timezone_combobox1.pack(pady=3)
timezone_combobox1.current(timezones.index("Asia/Karachi"))  # Set the default selection

# Create labels to display the time
time_label1 = tk.Label(root, font=('calibri', 40, 'bold'), bg='darkgrey', fg='black')
time_label1.pack(pady=0)

heading_label1 = tk.Label(root, text="---------------⏱--------------", font=('calibri', 24, 'bold'), bg='darkgrey', fg='purple')
heading_label1.pack(pady=20)  # Add padding above and below

timezone_combobox2 = ttk.Combobox(root, textvariable=timezone_var2, values=timezones, state="readonly", font=('calibri', 16))
timezone_combobox2.pack(pady=3)
timezone_combobox2.current(timezones.index("UTC"))  # Set the default selection

time_label2 = tk.Label(root, font=('calibri', 40, 'bold'), bg='darkgrey', fg='black')
time_label2.pack(pady=20)


footer_label = tk.Label(root, text="Muhammad Salman: linkedin.com/in/msalmanai62", font=('calibri', 10), bg='darkgrey', fg='black')
footer_label.pack(side=tk.BOTTOM, anchor='se', padx=10, pady=10)  # Position it to the bottom right

update_clock()  # Initialize the clock update function

# Run the Tkinter event loop
root.mainloop()
