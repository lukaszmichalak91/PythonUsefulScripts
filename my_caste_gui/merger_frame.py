import re
import tkinter
from tkinter import filedialog
import logging


class MergerFrame(tkinter.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        pdf_merger_frame = tkinter.LabelFrame(self, text="PDF Merger", pady=20)
        pdf_merger_frame.grid(row=0, column=0, columnspan=2, sticky="news")

        header_for_list = tkinter.Label(pdf_merger_frame, text="List of pdfs to merge:")
        header_for_list.grid(row=0, column=0)

        home_button = tkinter.Button(self, text="<-- Go home", command=lambda: parent.menu_frame.tkraise())
        home_button.grid(row=1, column=0, sticky="news", pady=30)

        open_pdf_button = tkinter.Button(self, text="Open PDF Files", command=lambda: self.open_pdfs())
        open_pdf_button.grid(row=2, column=0, sticky="news", pady=30)
        self.grid(row=0, column=0, sticky="news")

        self.list_of_pdfs = []
        self.list_of_paths = []

    def open_pdfs(self):
        filename = filedialog.askopenfilenames(title="Open files", filetypes=[("PDF files", ".pdf")], )

        self.list_of_paths = list(filename)

        for path in self.list_of_paths:
            pdf_file = re.search(r"/([^/]+)$", path)
            self.list_of_pdfs.append(pdf_file.group(1))

        print(self.list_of_paths)
        print(self.list_of_pdfs)

