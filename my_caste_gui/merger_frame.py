import re
import tkinter
from tkinter import filedialog

from PyPDF2 import PdfMerger


class MergerFrame(tkinter.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.pdf_merger_frame = tkinter.LabelFrame(self, text="PDF Files to merge", pady=20, width=300, height=300)
        self.pdf_merger_frame.grid(row=0, column=0, columnspan=3, sticky="news")

        home_button = tkinter.Button(self, text="<-- Go home",
                                     command=lambda: [parent.menu_frame.tkraise(), self.delete_all()])
        home_button.grid(row=2, column=0, sticky="news", pady=30)

        open_pdf_button = tkinter.Button(self, text="Open PDF Files", command=lambda: self.open_pdfs())
        open_pdf_button.grid(row=1, column=0, sticky="news", pady=30, padx=15)
        self.grid(row=0, column=0, sticky="news")

        delete_all_button = tkinter.Button(self, text="Delete all", command=self.delete_all)
        delete_all_button.grid(row=1, column=1, padx=15)

        merge_and_save_button = tkinter.Button(self, text="Merge and save at...", command=self.merge_and_save)
        merge_and_save_button.grid(row=1, column=2, padx=15)

        self.list_of_pdfs = []
        self.list_of_paths = []
        self.list_of_row_frame = []

        self.pdf_index = 0

    def open_pdfs(self):
        filename = filedialog.askopenfilenames(title="Open files", filetypes=[("PDF files", ".pdf")])
        file_list = list(filename)

        for file in file_list:
            if file not in self.list_of_paths:
                self.list_of_paths.append(file)

        self.pdf_index = 0
        self.assign_buttons()

    def assign_buttons(self):

        for path in self.list_of_paths:
            pdf_file = re.search(r"/([^/]+)$", path)
            pdf_file = pdf_file.group(1)
            if pdf_file not in self.list_of_pdfs:
                self.list_of_pdfs.append(pdf_file)

        for pdf_index in range(self.pdf_index, len(self.list_of_pdfs)):
            row_frame = tkinter.Frame(self.pdf_merger_frame)
            row_frame.grid(row=pdf_index, column=0)
            name_label = tkinter.Label(row_frame, text=self.list_of_pdfs[pdf_index], width=20)
            name_label.grid(row=0, column=0)

            delete_button = tkinter.Button(row_frame, text="Delete",
                                           command=lambda index=pdf_index: self.delete_row(index))

            up_button = tkinter.Button(row_frame, text="Up", command=lambda index=pdf_index: self.move_up(index))
            down_button = tkinter.Button(row_frame, text="Down", command=lambda index=pdf_index: self.move_down(index))

            if pdf_index == 0:
                up_button["state"] = "disabled"
            if pdf_index == len(self.list_of_pdfs) - 1:
                down_button["state"] = "disabled"

            delete_button.grid(row=0, column=1)
            up_button.grid(row=0, column=2)
            down_button.grid(row=0, column=3)

            self.list_of_row_frame.append(row_frame)
            self.pdf_index = pdf_index + 1

    def delete_row(self, index):

        del self.list_of_paths[index]

        for frame in self.list_of_row_frame:
            frame.grid_remove()
        self.list_of_row_frame.clear()
        self.list_of_pdfs.clear()

        self.pdf_index = 0
        self.assign_buttons()

    def delete_all(self):
        for frame in self.list_of_row_frame:
            frame.grid_remove()

        self.list_of_row_frame.clear()
        self.list_of_pdfs.clear()
        self.list_of_paths.clear()
        self.pdf_index = 0

    def move_up(self, index):

        self.list_of_paths[index], self.list_of_paths[index - 1] = self.list_of_paths[index - 1], self.list_of_paths[
            index]

        for frame in self.list_of_row_frame:
            frame.grid_remove()
        self.list_of_row_frame.clear()
        self.list_of_pdfs.clear()

        self.pdf_index = 0
        self.assign_buttons()

    def move_down(self, index):
        self.list_of_paths[index], self.list_of_paths[index + 1] = self.list_of_paths[index + 1], self.list_of_paths[
            index]
        for frame in self.list_of_row_frame:
            frame.grid_remove()
        self.list_of_row_frame.clear()
        self.list_of_pdfs.clear()
        self.pdf_index = 0
        self.assign_buttons()

    def merge_and_save(self):

        save_path = filedialog.asksaveasfilename(filetypes=[("PDF files", ".pdf")])

        merger = PdfMerger()

        for pdf_file in self.list_of_paths:
            merger.append(pdf_file)

        merger.write(f"{save_path}.pdf")
        merger.close()
