import tkinter


class LeatherFrame(tkinter.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        calc_frame = tkinter.LabelFrame(self, text="Dimension Converter in/mm", pady=20)
        calc_frame.grid(row=0, column=0, columnspan=2, sticky="news")

        self.incorrect_value_error_label = tkinter.Label(calc_frame, text="Provide correct value")
        self.in_unit_label = tkinter.Label(calc_frame, text="[in]")
        self.cm_unit_label = tkinter.Label(calc_frame, text="[cm]")

        equal_label = tkinter.Label(calc_frame, text="=")
        self.in_entry = tkinter.Entry(calc_frame, bg="#fbd808")
        self.cm_entry = tkinter.Entry(calc_frame, bg="#c0ff00")

        calc_button = tkinter.Button(calc_frame, text="convert", command=self.convert)
        switch_sides_button = tkinter.Button(calc_frame, text="<>", command=self.switch_sides)

        self.in_unit_label.grid(row=0, column=0)
        self.cm_unit_label.grid(row=0, column=2)
        self.in_entry.grid(row=1, column=0, padx=10)
        self.cm_entry.grid(row=1, column=2, padx=10)

        equal_label.grid(row=1, column=1)
        calc_button.grid(row=2, column=1, pady=10)
        switch_sides_button.grid(row=1, column=1)

        # Frames for popular inch and oz to mm for leather(children of 'leather_frame')

        popular_inch_frame = tkinter.LabelFrame(self, text="Popular inch to mm")
        popular_inch_frame.grid(row=1, column=0, sticky="w")

        popular_inch_tuple = ("1/8 in = 3,18 mm", "1/4 in = 6,35 mm", "1/2 in = 12,70 mm",
                              "1 in = 25,40 mm", "2 in = 50,80 mm", "3 in = 76,20 mm")

        for inch_label_index in range(0, len(popular_inch_tuple)):
            inch_label = tkinter.Label(popular_inch_frame, text=popular_inch_tuple[inch_label_index])
            inch_label.grid(row=inch_label_index, column=3, padx=30)
        thickness_frame = tkinter.LabelFrame(self, text="Thickness of leather oz to mm")
        thickness_frame.grid(row=1, column=1)

        oz_label_tuple = (
            "1 oz = 0.4 mm", "2 oz = 0.8 mm", "3 oz = 1.2 mm", "4 oz = 1.6 mm", "5 oz = 2.0 mm", "6 oz = 2.4 mm",
            "7 oz = 2.8 mm", "8 oz = 3.2 mm", "9 oz = 3.6 mm", "10 oz = 4.0 mm")

        for oz_label_index in range(0, len(oz_label_tuple)):
            oz_label = tkinter.Label(thickness_frame, text=oz_label_tuple[oz_label_index])
            oz_label.grid(row=oz_label_index, column=3, padx=30)

        home_button = tkinter.Button(self, text="<-- Go home", command=lambda: parent.menu_frame.tkraise())
        home_button.grid(row=2, column=0, sticky="news", pady=30)

        self.grid(row=0, column=0, sticky="news")

    def convert(self):
        if self.in_unit_label.grid_info().get("column") == 2:
            self.in_entry.delete(0, "end")
            try:
                value_in_in = float(self.cm_entry.get()) * 0.3937
                self.in_entry.insert(0, f"{value_in_in:.2f}")
                self.incorrect_value_error_label.grid_remove()
            except ValueError:
                self.incorrect_value_error_label.grid(row=2, column=0)
        else:
            self.cm_entry.delete(0, "end")
            try:
                value_in_cm = float(self.in_entry.get()) * 2.54
                self.cm_entry.insert(0, f"{value_in_cm:.2f}")
                self.incorrect_value_error_label.grid_remove()
            except ValueError:
                self.incorrect_value_error_label.grid(row=2, column=0)

    def switch_sides(self):
        if self.in_unit_label.grid_info().get("column") == 2:
            self.in_unit_label.grid(row=0, column=0)
            self.cm_unit_label.grid(row=0, column=2)
            self.in_entry.grid(row=1, column=0)
            self.cm_entry.grid(row=1, column=2)
        else:
            self.in_unit_label.grid(row=0, column=2)
            self.cm_unit_label.grid(row=0, column=0)
            self.in_entry.grid(row=1, column=2)
            self.cm_entry.grid(row=1, column=0)
