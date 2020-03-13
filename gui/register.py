from tkinter import *
from tkinter.ttk import *
from connection import handle_server

# from connection.sql import Sql
# import socket


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

    def start(self):
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

            # -----old------
            # database = Sql()
            # host_name = socket.gethostname()
            # ip = socket.gethostbyname(host_name)
            # print(host_name, ip)
            # inserted = database.insert_account(name, pas, ip)
            # database.close_conn()
            # -----old------
            if is_registered:
                pop_up_message('added to database')
                self.firstpage()
            else:
                pop_up_message('name already exist')

    def firstpage(self):
        self.frame.destroy()
        from gui.firstpage import FirstPage
        FirstPage(self.win).run()


def pop_up_message(text):
    from time import sleep
    win = Tk()
    center_window(win, height=100)
    Style(win)
    Label(win, text=text).pack()
    win.update()
    sleep(1.5)
    win.destroy()


def center_window(root, width=300, height=200):
    # get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))


if __name__ == '__main__':
    register = Register()
    register.start()
