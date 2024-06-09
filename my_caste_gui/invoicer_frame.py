import datetime
import re
import tkinter
from tkinter import filedialog

from invoicer import salary_calc
from invoicer.create_invoice import fill_invoice, get_invoice_title
from invoicer.salary_as_words import get_salary_words
from invoicer.work_time_read_write import create_work_report_from_txt, get_amount_of_working_hours
from work_predicter.hours_per_month import count_working_hour_per_month


class InvoicerFrame(tkinter.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.today_date = datetime.date.today()
        self.txt_file = None
        self.current_hours = 0
        self.hours_according_to_report = 0
        self.months_hours_frame = tkinter.LabelFrame(self, text="Working hours per month", padx=20, pady=20, width=300,
                                                     height=300)
        self.current_working_hours_frame = tkinter.LabelFrame(self, text="Current month working hours minus off days",
                                                              pady=20,
                                                              padx=10,
                                                              width=300,
                                                              height=300)

        self.time_report_frame = tkinter.LabelFrame(self, text="Xlsx time report", pady=20, padx=10, width=300,
                                                    height=300)

        self.invoice_frame = tkinter.LabelFrame(self, text="Create invoice")
        self.salary_per_hour_label = tkinter.Label(self.invoice_frame, text="Provide amount per hour")
        self.salary_per_hour_entry = tkinter.Entry(self.invoice_frame)
        self.create_invoice_button = tkinter.Button(self.invoice_frame, text="Create invoice",
                                                    command=lambda: self.create_invoice())

        self.open_worktime_txt_button = tkinter.Button(self.time_report_frame, text="Open txt with worktime",
                                                       command=lambda: self.open_worktime_txt())

        self.generate_xlsx_report_button = tkinter.Button(self.time_report_frame, text="Generate Time Report",
                                                          command=lambda: self.create_xlsx_report())

        self.txt_file_name_label = tkinter.Label(self.time_report_frame, text="TXT File", fg="#bcbcbc")

        self.current_hours = count_working_hour_per_month(self.today_date.month, self.today_date.year)

        self.current_working_hours_label = tkinter.Label(self.current_working_hours_frame,
                                                         text=f"Current: {self.current_hours} h",
                                                         font=("Segoe UI", 14, "bold"),
                                                         pady=20,
                                                         padx=20)
        self.hour_comparison_label = tkinter.Label(self.time_report_frame,
                                                   text=f"Calendar: {self.current_hours}, Report: {self.hours_according_to_report}")
        self.holiday_spinbox_header = tkinter.Label(self.current_working_hours_frame, text="Provide off days number")
        self.holiday_spinbox = tkinter.Spinbox(self.current_working_hours_frame, from_=0, to=10,
                                               command=lambda: self.calc_hours_value())

        self.txt_file_name_label.pack()
        self.open_worktime_txt_button.pack(pady=10)
        self.generate_xlsx_report_button.pack(pady=10)
        self.hour_comparison_label.pack()

        self.salary_per_hour_label.grid(row=0, column=0, pady=5)
        self.salary_per_hour_entry.grid(row=0, column=1)
        self.create_invoice_button.grid(row=0, column=2, padx=8)

        self.current_working_hours_frame.grid(row=0, column=0, padx=10, sticky="news")
        self.months_hours_frame.grid(row=0, column=1, rowspan=2, sticky="news")
        self.time_report_frame.grid(row=1, column=0, padx=10, sticky="news")
        self.invoice_frame.grid(row=3, column=0, columnspan=2, sticky="news")

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

        self.current_hours = count_working_hour_per_month(self.today_date.month,
                                                          self.today_date.year) - int(self.holiday_spinbox.get()) * 8

        self.current_working_hours_label.config(text=f"Current: {self.current_hours} h")
        self.hour_comparison_label.config(
            text=f"Calendar: {self.current_hours}, Report: {self.hours_according_to_report}")

        if self.current_hours != self.hours_according_to_report:
            self.hour_comparison_label.config(fg="#FF0000")
        else:
            self.hour_comparison_label.config(fg="#00ff00")

    def open_worktime_txt(self):

        self.txt_file = filedialog.askopenfilename(title="Open files", filetypes=[("Text files", ".txt")])
        print(self.txt_file)
        txt_file_name = re.search(r"/([^/]+)$", self.txt_file).group(1)

        self.txt_file_name_label.config(text=txt_file_name, fg="#000000")

    def create_xlsx_report(self):
        save_path = filedialog.asksaveasfilename(filetypes=[("Excel files", ".xlsx")])
        create_work_report_from_txt(self.txt_file, save_path)
        self.hours_according_to_report = get_amount_of_working_hours(f"{save_path}.xlsx")
        self.hour_comparison_label.config(
            text=f"Calendar: {self.current_hours}, Report: {self.hours_according_to_report}")

        if self.current_hours != self.hours_according_to_report:
            self.hour_comparison_label.config(fg="#FF0000")
        else:
            self.hour_comparison_label.config(fg="#00ff00")

    def create_invoice(self):

        invoice_default_title = get_invoice_title()

        save_path = filedialog.asksaveasfilename(initialfile=invoice_default_title, filetypes=[("Word files", ".docx")])

        hour_salary = self.salary_per_hour_entry.get()

        my_salary = salary_calc.SalaryCalc(self.hours_according_to_report, int(hour_salary), 23)
        salary_words = get_salary_words(my_salary.salary_gross)

        fill_invoice(my_salary.salary_net,
                     my_salary.salary_net,
                     my_salary.salary_gross,
                     my_salary.tax,
                     my_salary.tax_amount,
                     salary_words,
                     save_path)
