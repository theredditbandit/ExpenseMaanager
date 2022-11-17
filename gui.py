import tkinter as tk

root = tk.Tk()
root.title("Expanse manager")

root.geometry("1920x1080")

nav_barBG = tk.Label(root, bg = "dodgerblue2", height = 100, width = 1000)
nav_barBG.pack()

projName = tk.Label(root, text = "Whatever name we decide", height = 2, width = 20, font = ("arial", 30, "bold"), bg = "dodgerblue2")
projName.place(x = 15, y = 0)

content_label = tk.Label(root, height = 100, width = 250, borderwidth= 2, bg = "floral white")
content_label.place(x = 325, y = 75)

exp_tracking = tk.Button(root, height = 3, width = 45, text = "Track expenses", bg = "dodgerblue2", fg = "white")
exp_tracking.place(x = 0, y = 75)

button2 = tk.Button(root, height = 3, width = 45, text = "button2", bg = "dodgerblue2", fg = "white")
button2.place(x = 0, y = 125)

button3 = tk.Button(root,height = 3, width = 45, text = "button3", bg = "dodgerblue2", fg = "white")
button3.place(x = 0, y = 175)

button4 = tk.Button(root,height = 3, width = 45, text = "button4", bg = "dodgerblue2", fg = "white")
button4.place(x = 0, y = 225)

button5 = tk.Button(root,height = 3, width = 45, text = "button5", bg = "dodgerblue2", fg = "white")
button5.place(x = 0, y = 275)

button6 = tk.Button(root,height = 3, width = 45, text = "button6", bg = "dodgerblue2", fg = "white")
button6.place(x = 0, y = 325)

exptrack_label = tk.Label(root, text = "Track your expenses", height = 2, width = 20, font=("arial", 20, "bold"), bg = "floral white", fg = "blue")
exptrack_label.place(x = 410, y = 85)

add_expense_btn = tk.Button(root, height = 2, width = 20, text = "Add expense", bg = "dodgerblue1", fg = "white")
add_expense_btn.place(x = 450, y = 150)

hist_btn = tk.Button(root, height = 2, width = 20, text = "History", bg = "dodgerblue1", fg = "white")
hist_btn.place(x = 1300, y = 150)

logo_label = tk.Label(root, height = 20, width = 46, text = "LOGO")
logo_label.place(x = 0, y = 500)

bal_disp = tk.Label(root, text = "$3000", height = 6, width = 100, borderwidth= 2, relief="solid")
bal_disp.place(x = 600, y = 250)

graph_disp = tk.Label(root, text = "Graphs will be printed here", height = 25, width = 150, borderwidth= 2, relief="solid")
graph_disp.place(x = 450, y = 400)



root.mainloop()