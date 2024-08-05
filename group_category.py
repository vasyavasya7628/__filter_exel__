from utils import read_programs_list, write_to_exel_output, word_miss_percent

exel_file = read_programs_list()
temp_list = [exel_file[0][1]]  # Инициализируем temp_list первым элементом exel_file
last_index = 0

for i in range(1, len(exel_file)):  # Начинаем с 1, так как 0-й элемент уже в temp_list
    added = False
    for j in range(len(temp_list) - 1, -1, -1):  # Итерация в обратном порядке
        if word_miss_percent(exel_file[i][1], temp_list[j][0]) >= 75:
            temp_list.insert(j + 1, (
                '', exel_file[i][0], exel_file[i][1], exel_file[i][2], exel_file[i][3], exel_file[i][4],
                exel_file[i][5], exel_file[i][6]))
            last_index = j
            added = True
            break

    if not added:
        temp_list.append((
            exel_file[i][1], '', '', '', '', '',
            '', ''))
        temp_list.append((
            '', exel_file[i][0], exel_file[i][1], exel_file[i][2], exel_file[i][3], exel_file[i][4],
            exel_file[i][5], exel_file[i][6]))

write_to_exel_output(temp_list, 'groups_test2')
