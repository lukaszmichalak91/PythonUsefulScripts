from datetime import date, datetime, timedelta
from openpyxl import Workbook, load_workbook


def copy_time_report_txt_to_list(source_path):
    work_time_file = open(source_path, 'r')
    return work_time_file.readlines()


def get_last_day_of_current_month():
    current_date_for_today = datetime.today()
    my_next_month = current_date_for_today.replace(day=28) + timedelta(days=4)
    my_last_day = my_next_month - timedelta(days=my_next_month.day)
    return my_last_day.day


def get_int_day(str_date):
    return int(str_date[0:2])


def int_day_to_string(int_day):
    if len(str(int_day)) == 1:
        return str(f"0{int_day}")
    else:
        return str(int_day)


def int_month_to_string():
    int_month = date.today().month
    if len(str(int_month)) == 1:
        return str(f"0{int_month}")
    else:
        return str(int_month)


def updated_list_to_dict(lines_list):
    last_day = get_last_day_of_current_month()
    lines_dict = {}

    if (lines_list[0])[0:2] != "01":
        lines_list.insert(0, f"01.{int_month_to_string()}:")

    for line in lines_list:
        if lines_list.index(line) != len(lines_list) - 1:
            next_line = lines_list[lines_list.index(line) + 1]
            if get_int_day(line) + 1 != get_int_day(next_line):
                lines_list.insert(lines_list.index(line) + 1, f"{int_day_to_string(get_int_day(line) + 1)}"
                                                              f".{int_month_to_string()}:")
        if lines_list[lines_list.index(line)] == lines_list[-1] and (lines_list[-1])[0:2] != str(last_day):
            lines_list.insert(lines_list.index(line) + 1, f"{int_day_to_string(get_int_day(line) + 1)}"
                                                          f".{int_month_to_string()}:")
        if line[-1] == '\n':
            lines_list[lines_list.index(line)] = line[:-1]

        date_and_activity = line.split(":")
        lines_dict.update({f"{date_and_activity[0]}.{date.today().year}": date_and_activity[1]})

    return lines_dict


def save_dict_in_result(date_activity_dict):
    work_book = Workbook()
    work_sheet = work_book.active
    work_sheet.title = "WorkTimeReport"

    table_headings = ["Date", "Name and surname", "Client", "Standard Time", "Overtime", "Task description"]

    work_sheet.append(table_headings)

    for date_key in date_activity_dict:
        if not date_activity_dict[date_key]:
            row_of_table = [f"{date_key}", "John Doe", "TestClient", 0, 0, date_activity_dict[date_key]]
        else:
            row_of_table = [f"{date_key}", "John Doe", "TestClient", 8, 0, date_activity_dict[date_key]]
        work_sheet.append(row_of_table)

    work_sheet[f"D{work_sheet.max_row + 1}"] = f"=SUM(D1:D{work_sheet.max_row})"
    work_book.save("result.xlsx")


def create_work_report_xlsx():
    list_of_lines = copy_time_report_txt_to_list("work-report.txt")
    dict_of_line = updated_list_to_dict(list_of_lines)
    save_dict_in_result(dict_of_line)


def get_amount_of_working_hours():
    work_book = load_workbook("result.xlsx")
    work_sheet = work_book.active

    hours_sum = 0

    for line in range(2, work_sheet.max_row):
        hours_sum += work_sheet[f"D{line}"].value

    print(hours_sum)
    return hours_sum


if __name__ == "__main__":
    create_work_report_xlsx()
    get_amount_of_working_hours()