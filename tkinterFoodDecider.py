import tkinter as tk
from tkinter import ttk
import random
root = tk.Tk()
root.title('Lets Decide Dinner')

style = ttk.Style()
style.configure('chooseBtn.TButton', padding = [10], width = 20)
style.configure('radiobuttons.TRadiobuttn', font = ('arial', 20))

root.rowconfigure(0, weight = 0) #header
root.rowconfigure(0, weight = 0) #foodButtons
root.rowconfigure(0, weight = 0) #decideBtn
root.rowconfigure(0, weight = 0) #output

header = tk.Label(root, text = 'Lets Decide Dinner!')
header.grid(row = 0, column = 0, columnspan = 2)

fastFoodOptions = ['Burger King', 'Taco Bell', 'Steak n Shake', 'White Castle', 'Qudoba']
takeOutOptions = ['Siam House', 'BloomingThai', 'Amrit', 'The Owlery', 'Papa Johns', 'Buffa Louies']

def randomFastFood() :
    return random.choice(fastFoodOptions)
def randomTakeOut():
    return random.choice(takeOutOptions)
def callback():
    FF = radioBtnData.get()
    if FF == '1':
        dinnerChoice.config(text = randomFastFood())
    else:
        dinnerChoice.config(text = randomTakeOut())
# def addRemove():



radioBtnData = tk.StringVar() # gets the value from the radio button, when the radio button is selected and the callback is called, it gets radioBtnData and prints it

fastFoodBtn = ttk.Radiobutton(
    root,
    text = 'Fast Food',
    value = 1,
    variable = radioBtnData,
    style = 'radiobuttons.TRadiobutton'
)
fastFoodBtn.grid(row = 1, column = 0)

takeOutBtn = ttk.Radiobutton(
    root,
    text = 'Take-Out',
    value = 2,
    variable = radioBtnData,
    style = 'radiobuttons.TRadiobutton'
)
takeOutBtn.grid(row = 1, column = 1)

dinnerChoice = tk.Label(root, text = ' ')
dinnerChoice.grid(row = 3, column = 0, columnspan = 2)

button = ttk.Button(root, text = 'Choose!', command = lambda: callback(), style = 'chooseBtn.TButton') 
button.grid(row = 2, column = 0, columnspan = 2)

# listDisplayFF = tk.Variable(value = fastFoodOptions)
# listDisplayTO = tk.Variable(value = takeOutOptions)

# addRemoveOptions = ttk.Button(
#     root, 
#     text = 'Add/Remove Options',
#     command = lambda: addRemove()
# )

# options = tk.Listbox(
#     root,
#     listvariable = listDisplayFF,
#     height = 6,
#     selectmode = tk.EXTENDED 
# )



# header.pack()
# fastFoodBtn.pack(padx = 10, pady = 10)
# takeOutBtn.pack()
# dinnerChoice.pack()
# button.pack()

# root.geometry('500x500+500-500')
root.resizable(False, False)
# root.iconbitmap() change window icon

root.mainloop()

