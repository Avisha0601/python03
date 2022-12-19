from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

root = Tk()
root.title("Planet Encyclopedia")
root.geometry("500x500")
root.configure(background="cyan")

Mercury = ImageTk.PhotoImage(Image.open ("mercury.jpg"))
Venus = ImageTk.PhotoImage(Image.open ("venus.jpg"))
Earth = ImageTk.PhotoImage(Image.open ("earth.jpg"))

label_planet = Label(root, text="Planet : ", bg="cyan")
label_planet_name = Label(root,font=("courier",18,"bold"), bg="cyan")
label_planet_image = Label(root,bg="DarkSlateGray3", highlightthickness=5, borderwidth=2, relief=SOLID)
label_planet_gravity_radius = Label(root,font=("Comic Sans MS"), bg="cyan")
label_planet_info = Label(root,font=("Broadway",10,"bold"), bg="cyan", wrap=500)

planets = ["Mercury","Venus","Earth"]
selectedval = StringVar()
dropdown = ttk.Combobox(root, values = planets, textvariable=selectedval)

root.mainloop()

 
