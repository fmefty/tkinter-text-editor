# Importing required modules from tkinter
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to clear the text editor for a new file
def new_file():
    text.delete(1.0, tk.END)  # Deletes all content from the text widget

# Function to open a file and display its content in the text editor
def open_file():
    file_path = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )
    if file_path:
        with open(file_path, 'r') as file:
            text.delete(1.0, tk.END)      # Clear current text
            text.insert(tk.END, file.read())  # Load file content

# Function to save the content of the text editor to a file
def save_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text.get(1.0, tk.END))  # Get all text and write to file
            messagebox.showinfo("Info", "File saved successfully!")  # Success message

# Main application window
root = tk.Tk()
root.title("Simple Text Editor")     # Set window title
root.geometry("800x600")             # Set default window size

# Create the menu bar
menu = tk.Menu(root)
root.config(menu=menu)               # Attach the menu to the root window

# Add 'File' dropdown menu
file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)      # New file
file_menu.add_command(label="Open", command=open_file)    # Open file
file_menu.add_command(label="Save", command=save_file)    # Save file
file_menu.add_separator()                                 # Adds a separator line
file_menu.add_command(label="Exit", command=root.quit)    # Exit application

# Create the main text editor area
text = tk.Text(
    root,
    wrap=tk.WORD,                    # Wrap lines at word boundaries
    font=("Helvetica", 12),          # Set font style and size
    fg="blue"                        # Set text color
)
text.pack(expand=tk.YES, fill=tk.BOTH)  # Fill available space

# Start the GUI event loop
root.mainloop()
