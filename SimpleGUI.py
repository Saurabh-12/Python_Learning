# Simple GUI example
import tkinter as tk
# Create a root window
window= tk.Tk()
window.title('Beautiful Tool')
# Create a window of dimension 500x500. With 400 units on X-axis and 50 units on Y-axis.
window.geometry('500x500+400+50')# Add Labels to display messages on UI.

label = tk.Label(window, text = 'This is a beautiful Tool! Add your thoughts.')
label.pack()
# Add Entry to input string from users.
entry_line = tk.Entry(window)
entry_line.pack()
# Add Buttons to your UI.
button = tk.Button(window,text = 'Click', width=25)
button.pack()
#Add your logic.

window.mainloop()
