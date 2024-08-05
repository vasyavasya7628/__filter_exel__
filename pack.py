import openpyxl


def read_exel(file_name):
    workbook = openpyxl.load_workbook(file_name)
    sheet = workbook.active
    rows = list(sheet.iter_rows(values_only=True))
    return rows, sheet


def write_to_exel_output(sheet, output_file):
    workbook = sheet.parent
    workbook.save(output_file)


row_list, sheet = read_exel('groups_test2.xlsx')

counter = 0
i = 1
while i < len(row_list):
    if row_list[i][0] is not None:
        i += 1
        continue

    first_none_index = i
    while i < len(row_list) and row_list[i][0] is None:
        counter += 1
        i += 1

    for k in range(first_none_index, first_none_index + counter):
        sheet.row_dimensions[k + 1].outlineLevel = 1

    counter = 0

# Save the changes to a new file
write_to_exel_output(sheet, 'output_fil.xlsx')
