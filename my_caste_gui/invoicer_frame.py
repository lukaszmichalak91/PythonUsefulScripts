import datetime
import tkinter

from work_predicter.hours_per_month import count_working_hour_per_month


class InvoicerFrame(tkinter.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.today_date = datetime.date.today()

        self.salary_per_hour_label = tkinter.Label(self, text="Provide amount per hour")
        self.salary_per_hour_entry = tkinter.Entry(self)
        self.months_hours_frame = tkinter.LabelFrame(self, text="Working hours per month", pady=20, width=300,
                                                     height=300)
        self.current_working_hours_frame = tkinter.LabelFrame(self, text="Current month working hours minus off days",
                                                              pady=20,
                                                              width=300,
                                                              height=300)
        self.current_working_hours_label = tkinter.Label(self.current_working_hours_frame,
                                                         text=f"Current:"
                                                              f" {count_working_hour_per_month(self.today_date.month,
                                                                                               self.today_date.year)} h",
                                                         font=("Segoe UI", 14, "bold"),
                                                         pady=20)
        self.holiday_spinbox_header = tkinter.Label(self.current_working_hours_frame, text="Provide off days number")
        self.holiday_spinbox = tkinter.Spinbox(self.current_working_hours_frame, from_=0, to=10,
                                               command=lambda: self.calc_hours_value())

        self.salary_per_hour_label.grid(row=2, column=0, pady=15)
        self.salary_per_hour_entry.grid(row=1, column=0)
        self.months_hours_frame.grid(row=0, column=0)

        self.current_working_hours_frame.grid(row=0, column=1)
        self.current_working_hours_label.pack()
        self.holiday_spinbox_header.pack()
        self.holiday_spinbox.pack()

        self.grid(row=0, column=0, sticky="news")
        self.working_hours_per_month()

    def working_hours_per_month(self):

        for month_number in range(1, 13):
            working_hours_per_month = count_working_hour_per_month(month_number, self.today_date.year)

            month_name = datetime.date(self.today_date.year, month_number, 1).strftime("%B")
            month_label_hour = tkinter.Label(self.months_hours_frame,
                                             text=f"{month_name}  --->  {working_hours_per_month} h")

            if self.today_date.month == month_number:
                month_label_hour.configure(font=("Segoe UI", 10, "bold"))

            month_label_hour.grid(row=month_number, column=0)

    def calc_hours_value(self):

        current_hours = count_working_hour_per_month(self.today_date.month,
                                                     self.today_date.year) - int(self.holiday_spinbox.get()) * 8

        self.current_working_hours_label.config(text=f"Current: {current_hours} h")
