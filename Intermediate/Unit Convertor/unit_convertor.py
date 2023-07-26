import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width = 500, height = 200)
window.config(padx=20, pady=20)

#3 constant label
label_1 = tkinter.Label(text = "Miles",font= ("Arial",24,"normal"))
label_1.grid(row=0,column=2)

label_2 = tkinter.Label(text = "is equal to",font= ("Arial",24,"normal"))
label_2.grid(row=1, column=0)

label_3 = tkinter.Label(text = "Km",font= ("Arial",24,"normal"))
label_3.grid(row=1,column=2)

#1 dynamic label

label_4 = tkinter.Label(text= "0")
label_4.grid(row=1, column = 1)

#1 button
def button_clicked():
    km = int(input.get())*1.61
    label_4.config(text = km)

button_1 = tkinter.Button(text = "Calculate", command = button_clicked)
button_1.grid(row=2, column=1)

#1 text box
input = tkinter.Entry(width=10)
input.grid(row= 0, column= 1)



window.mainloop()