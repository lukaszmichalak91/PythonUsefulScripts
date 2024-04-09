import salary_calc
from salary_as_words import get_salary_words

my_salary = salary_calc.SalaryCalc(168, 135, 23)

print(f"In current month I worked {my_salary.working_hours} for {my_salary.pay_for_hour} per hour")
print(f"My salary is {my_salary.salary_net} net plus {my_salary.tax} tax, so it is {my_salary.salary_gross} gross")
print(f"Tax only is {my_salary.tax_amount}")

salary_words = get_salary_words(my_salary.salary_gross)
print(salary_words)

