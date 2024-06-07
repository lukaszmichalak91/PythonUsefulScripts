import tkinter


class MenuFrame(tkinter.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        welcome_label = tkinter.Label(self, text="Welcome to myCastle App", font=("Arial", 20))

        go_leather_button = tkinter.Button(self, text="Leather Assistance",
                                           command=lambda: parent.leather_frame.tkraise())
        go_url_shortener_button = tkinter.Button(self, text="Url Shortener",
                                                 command=lambda: parent.url_shortener_frame.tkraise())
        go_merger_button = tkinter.Button(self, text="PDF Merger", command=lambda: parent.merger_frame.tkraise())
        go_invoicer_button = tkinter.Button(self, text="Invoicer", command=lambda: parent.invoicer_frame.tkraise())

        welcome_label.grid(row=0, column=0, pady=10, padx=30)

        go_leather_button.grid(row=1, column=0, pady=10)
        go_url_shortener_button.grid(row=2, column=0, pady=10)
        go_merger_button.grid(row=3, column=0, pady=10)
        go_invoicer_button.grid(row=4, column=0, pady=10)

        self.grid(row=0, column=0, sticky="news")
