from tkinter import Tk, Button, PhotoImage
from tkinter.messagebox import showinfo

window = Tk()
window.geometry("300x300+760+340")

cross = PhotoImage(file="./cross.png")
circle = PhotoImage(file="./circle.png")

hod = 0


def click(button: Button, y, x):
    if (field[y][x] != ""):
        return
    global hod
    znack = ""
    if (hod % 2 == 0):
        znack = 'X'
    else:
        znack = "O"
    button["text"] = znack
    field[y][x] = znack
    hod += 1
    if win(znack):
        showinfo("Победитель", f"Победил {znack}")
        print(f"{znack} win")
        window.destroy()
    if hod == 9:
        showinfo("","Ничья")
        window.destroy()

field = [["", "", ""],
         ["", "", ""],
         ["", "", ""]]


def win(znack):
    for i in range(3):
        if field[i][0] == znack and field[i][1] == znack and field[i][2] == znack:
            return True
        if field[0][i] == znack and field[1][i] == znack and field[2][i] == znack:
            return True
    if field[0][0] == znack and field[1][1] == znack and field[2][2] == znack:
        return True
    if field[0][2] == znack and field[1][1] == znack and field[2][2] == znack:
        return True


for y in range(3):
    for x in range(3):
        button = Button(text="", width=13, height=6)
        button["command"] = lambda but=button, but_y=y, but_x=x: click(but, but_y, but_x)
        button.place(x=x * 100, y=y * 100)

window.mainloop()
