import tkinter

import pyshorteners


# idea for later - create "copy to clipboard button"
# refactor from pack to grid

class UrlShortenerFrame(tkinter.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        long_url_label = tkinter.Label(self, text="Provide url to be shortened")
        self.long_url_entry = tkinter.Entry(self)

        short_url_label = tkinter.Label(self, text="Here's your URL in shortened form")
        self.short_url_entry = tkinter.Entry(self)

        shorten_url_button = tkinter.Button(self, text="Shorten!", command=lambda: self.shorten_url())
        go_back_button = tkinter.Button(self, text="<-- Go home", command=lambda: parent.menu_frame.tkraise())

        self.incorrect_url_label = tkinter.Label(self, text="Please provide correct URL")

        long_url_label.grid(row=0, column=0, pady=15)
        self.long_url_entry.grid(row=1, column=0)

        short_url_label.grid(row=0, column=2, pady=15)
        self.short_url_entry.grid(row=1, column=2)

        shorten_url_button.grid(row=1, column=1)
        go_back_button.grid(row=2, column=1, pady=15)
        self.grid(row=0, column=0, sticky="news")

    def shorten_url(self):
        shortener = pyshorteners.Shortener()
        try:
            short_url = shortener.tinyurl.short(self.long_url_entry.get())
            self.short_url_entry.insert(0, short_url)
            self.incorrect_url_label.grid_remove()
        except Exception as e:
            if type(e).__name__ == "BadURLException" or type(e).__name__ == "ShorteningErrorException":
                self.incorrect_url_label.grid(row=2, column=0)
            if type(e).__name__ == "ReadTimeout":
                self.incorrect_url_label.pack()
