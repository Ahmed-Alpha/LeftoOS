from tkinter import *
import tkinter as tk
from tkinter import scrolledtext
from tkinter import filedialog
import ctypes
import sys
from tkinter import ttk, colorchooser
import webbrowser
from tkinter import messagebox

print("""
██╗░░░░░███████╗███████╗████████╗░█████╗░  ░█████╗░░██████╗
██║░░░░░██╔════╝██╔════╝╚══██╔══╝██╔══██╗  ██╔══██╗██╔════╝
██║░░░░░█████╗░░█████╗░░░░░██║░░░██║░░██║  ██║░░██║╚█████╗░
██║░░░░░██╔══╝░░██╔══╝░░░░░██║░░░██║░░██║  ██║░░██║░╚═══██╗
███████╗███████╗██║░░░░░░░░██║░░░╚█████╔╝  ╚█████╔╝██████╔╝
╚══════╝╚══════╝╚═╝░░░░░░░░╚═╝░░░░╚════╝░  ░╚════╝░╚═════╝░
""")

menu = input("""
[1] Lefto Text Editor
[2] LPaint
[3] Lefto Browser
[4] Exit
""")

if menu == "1":
    # Increas Dots Per inch so it looks sharper
    ctypes.windll.shcore.SetProcessDpiAwareness(True)

    # Setup Variables
    appName = 'Simple Text Editor'
    nofileOpenedString = 'New File'
    currentFilePath = nofileOpenedString

    # Viable File Types, when opening and saving files.
    fileTypes = [("Text Files","*.txt"), ("Markdown","*.md")]

    # Tkinter Setup
    window = Tk()

    # Set the first column to occupy 100% of the width
    window.grid_columnconfigure(0, weight=1)

    window.title(appName + " - " + currentFilePath)

    # Window Dimensions in Pixel
    window.geometry('500x400')

    # Handler Functions
    def fileDropDownHandler(action):
        global currentFilePath

        # Opening a File
        if action == "open":
            file = filedialog.askopenfilename(filetypes=fileTypes)
            window.title(appName + " - " + file)
            currentFilePath = file

            with open(file, 'r') as f:
                txt.delete(1.0, END)
                txt.insert(INSERT, f.read())

        elif action == "new":
            currentFilePath = nofileOpenedString
            txt.delete(1.0, END)
            window.title(appName + " - " + currentFilePath)

        # Saving a file
        elif action == "save" or action == "saveAs":
            if currentFilePath == nofileOpenedString or action == 'saveAs':
                currentFilePath = filedialog.asksaveasfilename(filetypes=fileTypes)

            with open(currentFilePath, 'w') as f:
                f.write(txt.get('1.0', 'end'))

            window.title(appName + " - " + currentFilePath)

    def textchange(event):
        window.title(appName + " - *" + currentFilePath)

    # Widgets

    # Text Area
    txt = scrolledtext.ScrolledText(window, height=999)
    txt.grid(row=1, sticky=N + S + E + W)

    # Bind event in the widget to a function
    txt.bind('<KeyPress>', textchange)

    # Menu
    menu = Menu(window)

    # set tearoff to 0
    fileDropdown = Menu(menu, tearoff=False)

    # Add Commands and their callbacks
    fileDropdown.add_command(label='New', command=lambda: fileDropDownHandler("new"))
    fileDropdown.add_command(label='Open', command=lambda: fileDropDownHandler("open"))

    # Adding a separator between button types.
    fileDropdown.add_separator()
    fileDropdown.add_command(label='Save', command=lambda: fileDropDownHandler("save"))
    fileDropdown.add_command(label='Save as', command=lambda: fileDropDownHandler("saveAs"))

    menu.add_cascade(label='File', menu=fileDropdown)

    # Set Menu to be Main Menu
    window.config(menu=menu)

    # Enabling "open with" by looking if the second argument was passed.
    if len(sys.argv) == 2:
        currentFilePath = sys.argv[1]
        window.title(appName + " - " + currentFilePath)

        with open(currentFilePath, 'r') as f:
            txt.delete(1.0, END)
            txt.insert(INSERT, f.read())

    # Main Loop
    window.mainloop()

########################

# Function to handle mouse button press
def start_drawing(event):
    global prev_x, prev_y
    prev_x = event.x
    prev_y = event.y

# Function to handle mouse button release
def stop_drawing(event):
    global prev_x, prev_y
    prev_x = None
    prev_y = None

# Function to handle mouse motion
def draw(event):
    global prev_x, prev_y

    if prev_x is not None and prev_y is not None:
        canvas.create_line(prev_x, prev_y, event.x, event.y, fill=draw_color, width=2)
        prev_x = event.x
        prev_y = event.y

# Function to choose a drawing color
def choose_color():
    global draw_color
    color = colorchooser.askcolor()
    if color:
        draw_color = color[1]




if menu == "2":
        # Create the main window
    window = Tk()
    window.title("LPaint")

    # Create a canvas for drawing
    canvas = Canvas(window, bg="white")
    canvas.pack(fill=BOTH, expand=True)

    # Set initial values
    draw_color = "black"
    prev_x = None
    prev_y = None

    # Bind mouse events to canvas
    canvas.bind("<Button-1>", start_drawing)
    canvas.bind("<B1-Motion>", draw)
    canvas.bind("<ButtonRelease-1>", stop_drawing)

    # Create a color selection button
    color_button = Button(window, text="Choose Color", command=choose_color)
    color_button.pack()

    # Start the main loop
    window.mainloop()

if menu == "3":
    class LeftoBrowser:
        def __init__(self):
            self.window = tk.Tk()
            self.window.title("Lefto Browser")

            self.tab_control = ttk.Notebook(self.window)
            self.tab_control.pack(fill="both", expand=True)

            self.tabs = []
            self.current_tab = None

            self.create_new_tab()

            self.window.mainloop()

        def create_new_tab(self):
            new_tab = Tab(self.tab_control)
            self.tab_control.add(new_tab.frame, text="New Tab")

            new_tab.entry.bind("<Return>", self.load_url)
            new_tab.entry.focus_set()

            self.tabs.append(new_tab)
            self.current_tab = new_tab

        def load_url(self, event):
            url = self.current_tab.entry.get()
            self.current_tab.webview.load_url(url)

    class Tab:
        def __init__(self, parent):
            self.frame = tk.Frame(parent)

            self.entry = tk.Entry(self.frame)
            self.entry.pack(fill="x")

            self.webview = WebView(self.frame)
            self.webview.pack(fill="both", expand=True)

    class WebView(tk.Frame):
        def __init__(self, parent):
            tk.Frame.__init__(self, parent)

            self.webview = tk.Text(self)
            self.webview.pack(fill="both", expand=True)

        def load_url(self, url):
            self.webview.delete("1.0", "end")
            self.webview.insert("end", "Loading...")
            self.webview.update()

            try:
                response = webbrowser.open(url)
                if response:
                    self.webview.delete("1.0", "end")
                    self.webview.insert("end", response)
            except Exception as e:
                self.webview.delete("1.0", "end")
                self.webview.insert("end", str(e))

    browser = LeftoBrowser()

if menu == "4":
    def exit_application():
        answer = messagebox.askyesno("Exit", "Are you sure you want to exit the application?")
        if answer:
            root.destroy()

    root = tk.Tk()

# Add your application code here

    exit_button = tk.Button(root, text="Exit", command=exit_application)
    exit_button.pack()

    root.mainloop()