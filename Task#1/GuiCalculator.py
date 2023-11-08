import tkinter as tk

def click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def c_button(): 
    global expression
    expression = "" 
    input_text.set("")
    
def equal_button():
    global expression
    try:         
            result = str(eval(expression)) # 'eval':This function is used to evaluates the string expression directly
            input_text.set(result)
            expression = result
    
    except ZeroDivisionError:
        input_text.set("Math Error: Division by zero is not allowed.")
        expression = ""
    
    except:
            input_text.set("Syntax Error")
            expression = ""


def create_Calculator_Interface(root):
    buttonframe = tk.Frame(root)
    buttonframe.config(bg = 'black')
    for z in range(4):
        buttonframe.columnconfigure(z, weight = 5)
    x = 1
    for rowNum in range(3):
        for colNum in range(3):
            tk.Button(buttonframe, text=str(x), bg='purple',font=('Arial', 19), command = lambda x=x: click(x)).grid(row=2-rowNum, column=colNum,padx=5, pady=5, sticky=tk.W+tk.E)
            x += 1
        tk.Button(buttonframe, text='0', bg='purple', font=('Arial', 19), command = lambda: click("0")).grid(row=3, column=1, sticky=tk.W+tk.E,padx=5, pady=5)
        tk.Button(buttonframe, text='/', bg = '#7092BE', font=('Arial', 19), command = lambda: click("/")).grid(row=0, column=3, sticky=tk.W+tk.E,padx=5, pady=5)
        tk.Button(buttonframe, text='*', bg = '#7092BE', font=('Arial', 19), command = lambda: click("*")).grid(row=1, column=3, sticky=tk.W+tk.E,padx=5, pady=5)
        tk.Button(buttonframe, text='-', bg = '#7092BE', font=('Arial', 19), command = lambda: click("-")).grid(row=2, column=3, sticky=tk.W+tk.E,padx=5, pady=5)
        tk.Button(buttonframe, text='+', bg = '#7092BE', font=('Arial', 19), command = lambda: click("+")).grid(row=3, column=3, sticky=tk.W+tk.E,padx=5, pady=5)
        tk.Button(buttonframe, text=')', bg='green', font=('Arial', 19), command = lambda: click(")")).grid(row=3, column=2, sticky=tk.W+tk.E,padx=5, pady=5)
        tk.Button(buttonframe, text='(', bg='green', font=('Arial', 19), command = lambda: click("(")).grid(row=3, column=0, sticky=tk.W+tk.E,padx=5, pady=5)
        tk.Button(buttonframe, text='C', bg = 'yellow',font=('Arial', 19), command = lambda: c_button()).grid(row=4, column=0, columnspan=2, sticky=tk.W+tk.E,padx=5, pady=5)
        tk.Button(buttonframe, text='=', bg='orange',font=('Arial', 19), command = lambda: equal_button()).grid(row=4, column=2, columnspan=2, sticky=tk.W+tk.E,padx=5, pady=5)
    buttonframe.pack(fill='both', pady = 5, padx = 5)

expression = ""

root = tk.Tk()
root.config(bg = '#808080')
root.geometry("400x360")
root.title("Caclulator")
root.resizable(0, 0)

 
expression = ""
 
# 'StringVar()' :It is used to get the instance of input field
 
input_text = tk.StringVar()
 
# Let us creating a frame for the input field
 
input_frame = tk.Frame(root, bg = 'grey', pady = 5)
 
input_frame.pack(side='top')
 
#Let us create a input field inside the 'Frame'
 
input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify='right')
 
input_field.grid(row=0, column=0)
 
input_field.pack(pady=10) # 'ipady' is internal padding to increase the height of input field
 

create_Calculator_Interface(root)

root.mainloop()
