#GUI CALCULATOR ASSIGNMENT

import tkinter as tk

expression = ""

def btn_click(num):
    global expression
    expression += str(num)
    text_input.delete(0, tk.END)
    text_input.insert(0, expression)

def btn_clear():
    global expression
    expression = ""
    text_input.delete(0, tk.END)


def btn_equal():
    global expression
    try:
        result = eval(expression)
        text_input.delete(0, tk.END)
        text_input.insert(0, result)

    except:
        text_input.delete(0, tk.END)
        text_input.insert(0, "Invalid operation")

root = tk.Tk()
root.title("Devote Boniface calculator")

text_input = tk.Entry(root, width=25)
text_input.grid(row=0, column=0, columnspan=5)
text_input.configure(font=("Arial Black", 15, "bold"), borderwidth=5)


#buttons
btn1 = tk.Button(root, text="1", command=lambda: btn_click(1))
btn1.grid(row=2, column=0)
btn1.configure(bg="blue", height=4, width=6)


btn2 = tk.Button(root, text="2", command=lambda: btn_click(2))
btn2.grid(row=2, column=1)
btn2.configure(bg="blue", height=4, width=6)

btn3 = tk.Button(root, text="3", command=lambda: btn_click(3))
btn3.grid(row=2, column=2)
btn3.configure(bg="blue", height=4, width=6)

btn4 = tk.Button(root, text="4", command=lambda: btn_click(4))
btn4.grid(row=3, column=0)
btn4.configure(bg="blue", height=4, width=6)

btn5 = tk.Button(root, text="5", command=lambda: btn_click(5))
btn5.grid(row=3, column=1)
btn5.configure(bg="blue", height=4, width=6)

btn6 = tk.Button(root, text="6", command=lambda: btn_click(6))
btn6.grid(row=3, column=2)
btn6.configure(bg="blue", height=4, width=6)

btn7 = tk.Button(root, text="7", command=lambda: btn_click(7))
btn7.grid(row=4, column=0)
btn7.configure(bg="blue", height=4, width=6)

btn8 = tk.Button(root, text="8", command=lambda: btn_click(8))
btn8.grid(row=4, column=1)
btn8.configure(bg="blue", height=4, width=6)

btn9 = tk.Button(root, text="9", command=lambda: btn_click(9))
btn9.grid(row=4, column=2)
btn9.configure(bg="blue", height=4, width=6)

btnClr = tk.Button(root, text="clr", command=lambda: btn_clear())
btnClr.grid(row=5, column=0)
btnClr.configure(bg="yellow", height=4, width=6)

btn0 = tk.Button(root, text="0" , command=lambda: btn_click(0))
btn0.grid(row=5, column=1)
btn0.configure(bg="blue", height=4, width=6)


btnEq = tk.Button(root, text="=", command=lambda: btn_equal())
btnEq.grid(row=5, column=2)
btnEq.configure(bg="yellow", height=4, width=6)


btnAdd = tk.Button(root, text="+", command=lambda: btn_click("+"))
btnAdd.grid(row=2, column=3)
btnAdd.configure(bg="red", height=4, width=6)

btnSub = tk.Button(root, text="-", command=lambda: btn_click("-"))
btnSub.grid(row=3, column=3)
btnSub.configure(bg="red", height=4, width=6)

btnMul = tk.Button(root, text="*", command=lambda: btn_click("*"))
btnMul.grid(row=4, column=3)
btnMul.configure(bg="red", height=4, width=6)

btnDiv = tk.Button(root, text="/", command=lambda: btn_click("/"))
btnDiv.grid(row=5, column=3)
btnDiv.configure(bg="red", height=4, width=6)

root.mainloop()

