from tkinter import *
from tkinter.ttk import *
from gui.login import Login
from gui.register import Register
from gui.general_gui_methods import center_window


class FirstPage:

    def __init__(self, win=None):
        if win:
            self.win = win
        else:
            self.win = Tk()
        self.win.title('VoiceChat')
        self.style = Style(self.win)
        self.frame = Frame(self.win)
        self.button_login = Button(self.frame, text='login', command=self.login)
        self.button_register = Button(self.frame, text='register', command=self.register)
        center_window(self.win)

    def main(self):
        # grid & pack
        self.button_login.grid(row=0)
        self.button_register.grid(row=1)
        self.frame.pack()

        self.win.mainloop()

    def login(self):
        self.frame.destroy()
        Login(self.win).main()

    def register(self):
        self.frame.destroy()
        Register(self.win).main()


if __name__ == '__main__':
    f = FirstPage()
    f.main()
