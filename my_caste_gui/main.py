import tkinter

root = tkinter.Tk()
root.title("my Castle")
root.geometry("600x500")


def convert():
    if in_unit_label.grid_info().get("column") == 2:
        in_entry.delete(0, "end")
        try:
            value_in_in = float(cm_entry.get()) * 0.3937
            in_entry.insert(0, f"{value_in_in:.2f}")
            incorrect_value_error_label.grid_remove()
        except ValueError:
            incorrect_value_error_label.grid(row=2, column=0)
    else:
        cm_entry.delete(0, "end")
        try:
            value_in_cm = float(in_entry.get()) * 2.54
            cm_entry.insert(0, f"{value_in_cm:.2f}")
            incorrect_value_error_label.grid_remove()
        except ValueError:
            incorrect_value_error_label.grid(row=2, column=0)


def switch_sides():
    if in_unit_label.grid_info().get("column") == 2:
        in_unit_label.grid(row=0, column=0)
        cm_unit_label.grid(row=0, column=2)
        in_entry.grid(row=1, column=0)
        cm_entry.grid(row=1, column=2)
    else:
        in_unit_label.grid(row=0, column=2)
        cm_unit_label.grid(row=0, column=0)
        in_entry.grid(row=1, column=2)
        cm_entry.grid(row=1, column=0)


frame = tkinter.Frame()
frame.pack()

calc_frame = tkinter.LabelFrame(frame, text="Dimension Converter in/mm", pady=20)
calc_frame.grid(row=0, column=0, columnspan=2, sticky="news")

incorrect_value_error_label = tkinter.Label(calc_frame)
in_unit_label = tkinter.Label(calc_frame, text="[in]")
cm_unit_label = tkinter.Label(calc_frame, text="[cm]")
equal_label = tkinter.Label(calc_frame, text="=")
in_entry = tkinter.Entry(calc_frame, bg="#fbd808")
cm_entry = tkinter.Entry(calc_frame, bg="#c0ff00")
calc_button = tkinter.Button(calc_frame, text="convert", command=convert)
switch_sides_button = tkinter.Button(calc_frame, text="<>", command=switch_sides)

in_unit_label.grid(row=0, column=0)
cm_unit_label.grid(row=0, column=2)
in_entry.grid(row=1, column=0, padx=10)
cm_entry.grid(row=1, column=2, padx=10)
equal_label.grid(row=1, column=1)
calc_button.grid(row=2, column=1, pady=10)
switch_sides_button.grid(row=1, column=1)

popular_inch_frame = tkinter.LabelFrame(frame, text="Popular inch to mm")
popular_inch_frame.grid(row=1, column=0, pady=20, sticky="news")

one_eighth_inch_label = tkinter.Label(popular_inch_frame, text="1/8 in = 3,18 mm")
one_fourth_inch_label = tkinter.Label(popular_inch_frame, text="1/4 in = 6,35 mm")
half_inch_label = tkinter.Label(popular_inch_frame, text="1/2 in = 12,70 mm")
one_inch_label = tkinter.Label(popular_inch_frame, text="1 in = 25,40 mm")
two_inches_label = tkinter.Label(popular_inch_frame, text="2 in = 50,80 mm")
three_inches_label = tkinter.Label(popular_inch_frame, text="3 in = 76,20 mm")

one_eighth_inch_label.grid(row=0, column=3, sticky="w")
one_fourth_inch_label.grid(row=1, column=3, sticky="w")
half_inch_label.grid(row=2, column=3, sticky="w")
one_inch_label.grid(row=3, column=3, sticky="w")
two_inches_label.grid(row=4, column=3, sticky="w")
three_inches_label.grid(row=5, column=3, sticky="w")

thickness_frame = tkinter.LabelFrame(frame, text="Thickness of leather oz to mm")
thickness_frame.grid(row=1, column=1, pady=20)

one_oz_label = tkinter.Label(thickness_frame, text="1 oz = 0.4 mm")
two_oz_label = tkinter.Label(thickness_frame, text="2 oz = 0.8 mm")
three_oz_label = tkinter.Label(thickness_frame, text="3 oz = 1.2 mm")
four_oz_label = tkinter.Label(thickness_frame, text="4 oz = 1.6 mm")
five_oz_label = tkinter.Label(thickness_frame, text="5 oz = 2.0 mm")
six_oz_label = tkinter.Label(thickness_frame, text="6 oz = 2.4 mm")
seven_oz_label = tkinter.Label(thickness_frame, text="7 oz = 2.8 mm")
eight_oz_label = tkinter.Label(thickness_frame, text="8 oz = 3.2 mm")
nine_oz_label = tkinter.Label(thickness_frame, text="9 oz = 3.6 mm")
ten_oz_label = tkinter.Label(thickness_frame, text="10 oz = 4.0 mm")

one_oz_label.grid(row=0, column=3)
two_oz_label.grid(row=1, column=3)
three_oz_label.grid(row=2, column=3)
four_oz_label.grid(row=3, column=3)
five_oz_label.grid(row=4, column=3)
six_oz_label.grid(row=5, column=3)
seven_oz_label.grid(row=6, column=3)
eight_oz_label.grid(row=7, column=3)
nine_oz_label.grid(row=8, column=3)
ten_oz_label.grid(row=9, column=3)

root.mainloop()
