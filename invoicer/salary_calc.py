class SalaryCalc:

    def __init__(self, working_hours, pay_for_hour, tax):
        self.working_hours = working_hours
        self.pay_for_hour = pay_for_hour
        self.tax = tax
        self.tax_factor = tax / 100
        self.salary_net = working_hours * pay_for_hour
        self.salary_gross = f"{self.salary_net * (self.tax_factor + 1):.2f}"
        self.tax_amount = f"{self.salary_net * self.tax_factor:.2f}"


if __name__ == "__main__":
    test_salary = SalaryCalc(168, 135, 23)
    print(test_salary.salary_gross)
    print(test_salary.tax_amount)
