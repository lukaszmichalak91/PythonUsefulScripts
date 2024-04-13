from datetime import datetime, timedelta
from dateutil import relativedelta
from docx.api import Document


def fill_invoice(price_net, value_net, value_gross, tax, tax_value, salary_in_words):
    document = Document("data_source/inv-template.docx")

    text_data_dict = inv_text_data(value_gross, salary_in_words)
    table_data_dict = inv_table_data(price_net, value_net, tax, tax_value, value_gross)

    for paragraph in document.paragraphs:

        for key, value in text_data_dict.items():
            if key in paragraph.text:
                for run in paragraph.runs:
                    run.text = run.text.replace(key, str(value))

    for table in document.tables:
        for row in table.rows:
            for key, value in table_data_dict.items():
                for cell in row.cells:
                    if key in cell.text:
                        for run in cell.paragraphs[0].runs:
                            run.text = run.text.replace(key, str(value))

    document.save("data_result/invoice.docx")


def inv_text_data(value_gross, salary_in_words):
    text_data = {
        "[Invoice Number]": get_invoice_number(),
        "[Date Of Completion]": get_date_of_completion(),
        "[Contractor Data]": "JD Ltd. John Doe \nNIP:1234567890 \nKonto: T Bank\n11 0000 0000 0000 0000 0000 0000",
        "[Client Data]": "Long name of client company\nTest Street 10/1 floor, 00-000 TestCity\nNIP: 987-654-32-10",
        "[Pay Day]": get_day_of_payment(),
        "[Value Gross]": value_gross,
        "[Salary in Words]": salary_in_words
    }
    return text_data


def inv_table_data(price_net, value_net, tax, tax_value, value_gross):
    table_data = {
        "[Price Net]": f"{round(price_net, 2):.2f}",
        "[Value Net]": f"{round(value_net, 2):.2f}",
        "[Tax]": f"{tax}%",
        "[Tax Value]": tax_value,
        "[Value Gross]": value_gross
    }
    return table_data


def get_date_of_completion():
    next_month = datetime.today().replace(day=28) + timedelta(days=4)
    last_day_of_month = next_month - timedelta(days=next_month.day)
    return last_day_of_month.date().strftime("%d-%m-%Y")


def get_invoice_number():
    return datetime.today().date().strftime("%m/%y")


def get_day_of_payment():
    day_of_payment = datetime.today().replace(day=21) + relativedelta.relativedelta(months=1)
    return day_of_payment.strftime("%d.%m.%Y")
