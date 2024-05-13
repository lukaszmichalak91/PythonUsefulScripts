import re
import tkinter
from tkinter import filedialog


class MergerFrame(tkinter.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.pdf_merger_frame = tkinter.LabelFrame(self, text="PDF Merger", pady=20)
        self.pdf_merger_frame.grid(row=0, column=1, columnspan=2, sticky="news")

        header_for_list = tkinter.Label(self.pdf_merger_frame, text="List of pdfs to merge:")
        header_for_list.grid(row=0, column=0)

        home_button = tkinter.Button(self, text="<-- Go home",
                                     command=lambda: [parent.menu_frame.tkraise(), self.delete_all()])
        home_button.grid(row=1, column=0, sticky="news", pady=30)

        open_pdf_button = tkinter.Button(self, text="Open PDF Files", command=lambda: self.open_pdfs())
        open_pdf_button.grid(row=2, column=0, sticky="news", pady=30)
        self.grid(row=0, column=0, sticky="news")

        delete_all_button = tkinter.Button(self, text="Delete all", command=self.delete_all)
        delete_all_button.grid(row=0, column=0)

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

        for path in self.list_of_paths:
            pdf_file = re.search(r"/([^/]+)$", path)
            pdf_file = pdf_file.group(1)
            if pdf_file not in self.list_of_pdfs:
                self.list_of_pdfs.append(pdf_file)

        for pdf_index in range(self.pdf_index, len(self.list_of_pdfs)):
            row_frame = tkinter.Frame(self.pdf_merger_frame, name=f"widget_frame_{pdf_index}")
            row_frame.grid(row=pdf_index, column=0)
            name_label = tkinter.Label(row_frame, text=self.list_of_pdfs[pdf_index])
            name_label.grid(row=0, column=0)

            delete_button = tkinter.Button(row_frame, text="Delete",
                                           command=lambda index=pdf_index: self.delete_row(index))

            up_button = tkinter.Button(row_frame, text="Up")
            down_button = tkinter.Button(row_frame, text="Down")

            delete_button.grid(row=0, column=1)
            up_button.grid(row=0, column=2)
            down_button.grid(row=0, column=3)

            self.list_of_row_frame.append(row_frame)
            self.pdf_index = pdf_index + 1

        self.test_lists()

    def delete_row(self, index):
        widget = self.pdf_merger_frame.nametowidget(f"widget_frame_{index}")
        widget.grid_remove()

        widget_children_list = list(widget.children.values())
        label_child = widget_children_list[0]
        label_child_text = label_child.cget("text")
        self.list_of_pdfs.remove(label_child_text)

        for path in self.list_of_paths:
            if label_child_text in path:
                self.list_of_paths.remove(path)

        self.list_of_row_frame.remove(widget)
        self.pdf_index -= 1

        self.test_lists()

    def delete_all(self):
        for frame in self.list_of_row_frame:
            frame.grid_remove()

        self.list_of_row_frame.clear()
        self.list_of_pdfs.clear()
        self.list_of_paths.clear()
        self.pdf_index = 0

        self.test_lists()

    def test_lists(self):
        print("### test ###")
        print(len(self.list_of_paths))
        print(len(self.list_of_pdfs))
        print(len(self.list_of_row_frame))
