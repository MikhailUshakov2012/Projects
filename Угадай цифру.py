import tkinter as tk
import random
from tkinter.messagebox import showinfo

number = random.randint(1,100)
print(number)


def check():
    number1 = int(entry.get())
    entry.delete(0, tk.END)
    print(number1)
    if number1 ==number:
        showinfo("Победителю", f"Вы выйграли!")
        window.destroy()
    else:
        if number1 <number:
            label = tk.Label(text="Больше", font=("Open Sans", 15))
            label.place(x=88, y=45)
        else:
            label = tk.Label(text="Меньше", font=("Open Sans", 15))
            label.place(x=88, y=45)

window = tk.Tk()
window.geometry("300x200")
window.title("Угадай число 1-100.")
window.resizable(False, False)

button = tk.Button(text="Проверить цифру", command=check)
button.place(x=100, y=120)

entry = tk.Entry(width=3)
entry.place(x=145, y=95)

window.mainloop()
