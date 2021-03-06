from tkinter import *
from tkinter.ttk import *
from connection import handle_server
from gui.general_gui_methods import pop_up_message, center_window


class Register:

    def __init__(self, win=None):
        if win:
            self.win = win
        else:
            self.win = Tk()
        self.win.title('Register')
        self.style = Style(self.win)
        self.frame = Frame(self.win)
        self.entry_name = Entry(self.frame)
        self.entry_pas = Entry(self.frame)
        center_window(self.win)

    def main(self):
        # self.win.geometry('500x500')
        name = Label(self.frame, text='Name')
        pas = Label(self.frame, text='Password')
        enter = Button(self.frame, text='Register', command=self.handle)
        self.frame.bind_all('<Return>', self.handle)
        self.entry_name.focus_set()

        # grid & pack
        name.grid(row=0, sticky=E)
        pas.grid(row=1, sticky=E)
        self.entry_name.grid(row=0, column=1)
        self.entry_pas.grid(row=1, column=1)
        enter.grid()
        self.frame.pack()
        self.win.mainloop()

    def handle(self, event=None):
        # acquire args
        name = self.entry_name.get()
        pas = self.entry_pas.get()

        self.entry_name.delete(0, len(name))
        self.entry_pas.delete(0, len(pas))
        # checks if valid
        if len(name) < 3 or len(pas) < 3:
            pop_up_message('name and password must be at least 3 characters')
        # add to database unless name is already used
        else:
            is_registered = handle_server.register(name, pas)
            if is_registered:
                pop_up_message('added to database')
                self.firstpage()
            else:
                pop_up_message('name already exist')

    def firstpage(self):
        self.frame.destroy()
        from gui.firstpage import FirstPage
        FirstPage(self.win).main()


if __name__ == '__main__':
    register = Register()
    register.main()
