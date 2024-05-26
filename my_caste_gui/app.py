import tkinter

import leather_frame
import menu_frame
import merger_frame
import url_shortener_frame


class App(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("my Castle")
        self.geometry("600x500")
        self.main_frame = MainFrame(self)
        self.mainloop()


class MainFrame(tkinter.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.menu_frame = menu_frame.MenuFrame(self)
        self.leather_frame = leather_frame.LeatherFrame(self)
        self.url_shortener_frame = url_shortener_frame.UrlShortenerFrame(self)
        self.merger_frame = merger_frame.MergerFrame(self)

        self.menu_frame.tkraise()
        self.pack()


App()
