import salary_calc
from salary_as_words import get_salary_words
from work_time_read_write import create_work_report_xlsx, get_amount_of_working_hours
from create_invoice import fill_invoice

create_work_report_xlsx()
working_hours = get_amount_of_working_hours()

my_salary = salary_calc.SalaryCalc(working_hours, 135, 23)

print(f"In current month I worked {my_salary.working_hours} for {my_salary.pay_for_hour} per hour")
print(f"My salary is {my_salary.salary_net} net plus {my_salary.tax} tax, so it is {my_salary.salary_gross} gross")
print(f"Tax only is {my_salary.tax_amount}")

salary_words = get_salary_words(my_salary.salary_gross)

fill_invoice(my_salary.salary_net,
             my_salary.salary_net,
             my_salary.salary_gross,
             my_salary.tax,
             my_salary.tax_amount,
             salary_words)

