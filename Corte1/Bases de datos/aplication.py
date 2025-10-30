import tkinter as tk

class Aplication:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Product Administrator')
        self.window.geometry('300x250')

        self.labelId = tk.Label(self.window, text='Id:')
        self.labelId.place(x=60, y=10)
        self.entryId = tk.Entry(self.window)
        self.entryId.place(x=80, y=10)

        self.buttonSearch = tk.Button(self.window, text='Search')
        self.buttonSearch.place(x=220, y=10)

        self.labelName = tk.Label(self.window, text='Name:')
        self.labelName.place(x=38, y=40)
        self.entryName = tk.Entry(self.window)
        self.entryName.place(x=80, y=40)

        self.buttonAdd = tk.Button(self.window, text='Add')
        self.buttonAdd.place(x=220, y=50)

        self.labelDescription = tk.Label(self.window, text='Description:')
        self.labelDescription.place(x=10, y=80)
        self.entryDescription = tk.Entry(self.window)
        self.entryDescription.place(x=80, y=80)

        self.buttonModify = tk.Button(self.window, text='Modify')
        self.buttonModify.place(x=220, y=90)

        self.labelPrice = tk.Label(self.window, text='Price:')
        self.labelPrice.place(x=45, y=120)
        self.entryPrice = tk.Entry(self.window)
        self.entryPrice.place(x=80, y=120)

        self.labelStock = tk.Label(self.window, text='Stock:')
        self.labelStock.place(x=45, y=160)
        self.entryStock = tk.Entry(self.window)
        self.entryStock.place(x=80, y=160)

        self.buttonDelete = tk.Button(self.window, text='Delete')
        self.buttonDelete.place(x=220, y=130)

        self.labelCategory = tk.Label(self.window, text='Category:')
        self.labelCategory.place(x=25, y=200)
        self.entryCategory = tk.Entry(self.window)
        self.entryCategory.place(x=80, y=200)

        self.buttonClear = tk.Button(self.window, text='Clear', command=self.clear)
        self.buttonClear.place(x=220, y=170)

        self.window.mainloop()

    def clear(self):
        self.entryId.delete(0,tk.END)
        self.entryName.delete(0,tk.END)
        self.entryDescription.delete(0,tk.END)
        self.entryPrice.delete(0,tk.END)
        self.entryStock.delete(0,tk.END)
        self.entryCategory.delete(0,tk.END)