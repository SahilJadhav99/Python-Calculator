import tkinter as tk
import math

# Function to handle button clicks


def on_click(btn_text):
    current_text = display_var.get()
    if btn_text == "=":
        try:
            # Evaluate the expression and set the result to the display
            result = eval(current_text)
            display_var.set(result)
        except Exception as e:
            # If an error occurs during evaluation, set the display to "Error"
            display_var.set("Error")
    elif btn_text == "C":
        # Clear the display
        display_var.set("")
    elif btn_text == "√":
        try:
            # Calculate square root and set result to the display
            result = math.sqrt(float(current_text))
            display_var.set(result)
        except ValueError:
            # If input is invalid for square root, set display to "Error"
            display_var.set("Error")
    elif btn_text == "x²":
        try:
            # Square the current value and set result to the display
            result = eval(current_text + "**2")
            display_var.set(result)
        except Exception as e:
            # If an error occurs, set the display to "Error"
            display_var.set("Error")
    elif btn_text == "sin":
        try:
            # Calculate sine and set result to the display
            result = math.sin(math.radians(float(current_text)))
            display_var.set(result)
        except ValueError:
            # If input is invalid for sine, set display to "Error"
            display_var.set("Error")
    elif btn_text == "cos":
        try:
            # Calculate cosine and set result to the display
            result = math.cos(math.radians(float(current_text)))
            display_var.set(result)
        except ValueError:
            # If input is invalid for cosine, set display to "Error"
            display_var.set("Error")
    elif btn_text == "tan":
        try:
            # Calculate tangent and set result to the display
            result = math.tan(math.radians(float(current_text)))
            display_var.set(result)
        except ValueError:
            # If input is invalid for tangent, set display to "Error"
            display_var.set("Error")
    elif btn_text == "ln":
        try:
            # Calculate natural logarithm and set result to the display
            result = math.log(float(current_text))
            display_var.set(result)
        except ValueError:
            # If input is invalid for logarithm, set display to "Error"
            display_var.set("Error")
    elif btn_text == "log":
        try:
            # Calculate base 10 logarithm and set result to the display
            result = math.log10(float(current_text))
            display_var.set(result)
        except ValueError:
            # If input is invalid for logarithm, set display to "Error"
            display_var.set("Error")
    elif btn_text == "!":
        try:
            # Calculate factorial and set result to the display
            result = math.factorial(int(current_text))
            display_var.set(result)
        except ValueError:
            # If input is invalid for factorial, set display to "Error"
            display_var.set("Error")
        except Exception as e:
            # If an error occurs, set the display to "Error"
            display_var.set("Error")
    elif btn_text == "M+":
        # Store current value to memory
        memory_var.set(float(current_text))
    elif btn_text == "MR":
        # Recall value from memory and set to the display
        display_var.set(memory_var.get())
    elif btn_text == "MC":
        # Clear memory
        memory_var.set(0)
    elif btn_text == "%":
        try:
            # Calculate percentage and set result to the display
            result = eval(current_text) / 100
            display_var.set(result)
        except Exception as e:
            # If an error occurs, set the display to "Error"
            display_var.set("Error")
    elif btn_text == "π":
        # Set Pi constant to the display
        display_var.set(math.pi)
    elif btn_text == "⌫":
        # Remove the last character from the display
        display_var.set(current_text[:-1])
    else:
        # Append the clicked button text to the display
        display_var.set(current_text + btn_text)


# Create the Tkinter root window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")
root.configure(bg="#333")

# Variable to hold display text
display_var = tk.StringVar()
display = tk.Entry(root, textvariable=display_var, font=(
    "Arial", 24), bd=5, justify="right", bg="#444", fg="white")
display.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")

# Memory variable
memory_var = tk.DoubleVar()

# Styling for buttons
button_bg = "#555"
button_fg = "white"
button_active_bg = "#666"
button_active_fg = "white"
button_width = 6
button_height = 2
button_font = ("Arial", 18)

# Buttons
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+",
    "√", "x²", "sin", "cos", "tan",
    "ln", "log", "!", "M+", "MR",
    "MC", "%", "π", "⌫"  # Added backspace button
]

row_num = 1
col_num = 0
for button in buttons:
    tk.Button(root, text=button, font=button_font, width=button_width, height=button_height,
              bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg,
              command=lambda btn_text=button: on_click(btn_text)).grid(row=row_num, column=col_num, padx=5, pady=5, sticky="nsew")
    col_num += 1
    if col_num > 4:
        col_num = 0
        row_num += 1

# Configure row and column weights
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(5):
    root.grid_columnconfigure(i, weight=1)

root.mainloop() 
