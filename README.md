# tkinter-text-editor
Simple Text Editor built with Python and Tkinter, supporting basic file operations like New, Open, and Save with an easy-to-use graphical interface.


# Tkinter Text Editor 📝

A simple and lightweight text editor application developed in Python using the Tkinter library. This project demonstrates how to build a graphical user interface (GUI) for basic text editing tasks such as creating new files, opening existing text files, and saving changes. It's a great starting point for beginners learning Python GUI development.

---

## Features

- **New File:** Clear the editor to start writing fresh content.
- **Open File:** Browse and open `.txt` files from your computer.
- **Save File:** Save your current work to a `.txt` file.
- **User-friendly Interface:** Clean and intuitive layout using Tkinter widgets.
- **Text Formatting:** Basic text input with word wrapping and font styling.
- **Cross-platform:** Runs on Windows, macOS, and Linux with Python installed.

---

## Getting Started

### Prerequisites

- Python 3.x installed on your system.
- Tkinter comes pre-installed with most Python distributions. If you don't have it, install it via your package manager or Python installer.

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/tkinter-text-editor.git
   cd tkinter-text-editor





### Usage
- Use the File menu to create a new document, open an existing file, or save your work.
- The text area supports typing and editing with word wrap enabled.
- When opening or saving files, only .txt files are supported.
- You will receive confirmation messages when files are saved successfully.

### Code Overview
- new_file(): Clears all text from the editor.
- open_file(): Opens a file dialog to select a text file and loads its content into the editor.
- save_file(): Opens a save dialog to save the current text content to a file.

The GUI uses Tkinter’s Menu widget to build the File menu and a Text widget for the editing area.
The application window is configured with a default size of 800x600 pixels and a simple blue-colored text style.

