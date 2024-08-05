# # # Исходный список предложений
# # from fuzzywuzzy import fuzz
# #
# # sentences = [
# #     "1C Предприятие",
# #     "1C Предприятие 7.7",
# #     "1C:Enterprise 8",
# #     "1C:Enterprise 8 (x86-64) (8.3.22.1923)",
# #     "1C:Enterprise 8 (x86-64) (8.3.23.1997)",
# #     "1C:Enterprise 8 (x86-64) Thin client (8.3.22.2239)",
# #     "1C:Enterprise 8. Cryptographic extension for Chrome and Firefox",
# #     "1C:Enterprise 8. Filesystem extension for Chrome and Firefox",
# #     "1C:Enterprise 8. Filesystem extension for Internet Explorer",
# #     "1С:Предприятие",
# #     "1С:Предприятие – оповещения и запуск",
# #     "1С:Предприятие 7.7 для SQL",
# #     "1С:Предприятие 8",
# #     "1С:Предприятие 8 (x86-64) Сервер",
# #     "1С:Предприятие 8 (x86-64) Тонкий клиент",
# #     "1С:Предприятие 8 (учебная версия) (8.3.24.1368)",
# #     "1С:Предприятие 8 Агент КИП (x86-64)",
# #     "1С:Предприятие 8 Тонкий клиент (8.3.20.1710)",
# #     "1С:Предприятие 8 Тонкий клиент (8.3.23.1912)",
# #     "1С:Предприятие 8.0",
# #     "1С-Коннект",
# #     "1С-Рарус: Система программного лицензирования конфигураций",
# #     "7-Zip",
# #     "ABBYY FineReader",
# #     "Adobe Acrobat  9 Pro - English, Russian",
# #     "Adobe Acrobat (64-bit)",
# #     "Adobe Acrobat 2017",
# #     "Adobe Acrobat DC",
# #     "Adobe Acrobat DC (64-bit)",
# #     "Adobe Acrobat Reader",
# #     "Adobe Acrobat Reader - Russian",
# #     "Adobe Acrobat Reader DC",
# #     "Adobe Acrobat Reader DC - Russian",
# #     "Adobe Acrobat Reader DC (2015) MUI",
# #     "Adobe Acrobat Reader DC MUI",
# #     "Adobe Acrobat Reader MUI",
# #     "Adobe Acrobat XI Pro",
# #     "Adobe After Effects 2024"
# # ]
# #
# # # Список слов для поиска
# # words = ["1C Предриятие", "1С:Предприятие 8 Агент КИП (x86-64)"]
# #
# # # Список для хранения предложений, содержащих оба слова
# # filtered = []
# # print(fuzz.token_sort_ratio(words[0], sentences[0]))
# #
# #
# # def check_miss_percent(sentence_):
# #     for j in range(len(words)):
# #         if fuzz.ratio(sentence_, words[j]) > 80:
# #             return words[j]
# #         else:
# #             return False
# #
# #
# # for i in range(len(sentences)):
# #     if check_miss_percent(sentences[i]) is not False:
# #         filtered.append(check_miss_percent(sentences[i]))
# #
# # print(filtered)
#
# def find_repeated_words(words):
#     word_count = {}
#     repeated_words = []
#
#     for word in words:
#         if word in word_count:
#             if word_count[word] == 1:
#                 repeated_words.append(word)
#             word_count[word] += 1
#         else:
#             word_count[word] = 1
#
#     return repeated_words
#
#
# data = [
#     ('АУ', 'Яндекс Музыка 5.1.4', '5.1.4', 'Яндекс Музыка', 2, 1, None),
#     ('АУ', 'Яндекс Музыка 5.2.2', '5.2.2', 'Яндекс Музыка', 1, 1, None),
#     ('АУ', 'Яндекс Музыка 5.3.2', '5.3.2', 'Яндекс Музыка', 1, 1, None),
#     ('Краснобродский', 'Яндекс Музыка 5.3.2', '5.3.2', 'Яндекс Музыка', 1, 1, None),
#     ('АУ', 'Яндекс\xa0Диск', '1.0', 'Google\\Chrome', 1, 1, None),
#     ('Калтан', 'Яндекс\xa0Игры', '1.0', 'Google\\Chrome', 1, 1, None),
#     ('АУ', 'Яндекс.Бар 6.7 для Internet Explorer', '6.7.0.1919', 'Яндекс', 1, 1, None),
#     ('АУ', 'Яндекс.Диск', '1.0', 'Yandex\\YandexBrowser', 2, 2, None),
#     ('АУ', 'Яндекс.Диск', '1.1.11.4442', 'Яндекс', 1, 1, None),
#     ('АУ', 'Яндекс.Диск', '1.4.17.5360', 'Яндекс', 1, 1, None),
#     ('АУ', 'Яндекс.Диск', '1.4.22.5513', 'Яндекс', 1, 1, None),
#     ('АУ', 'Яндекс.Диск', '3.2.28.4901', 'Яндекс', 1, 1, None),
#     ('АУ', 'Яндекс.Диск', '3.2.31.4925', 'Яндекс', 1, 1, None),
#     ('АУ', 'Яндекс.Диск', '3.2.32.4945', 'Яндекс', 1, 1, None),
#     ('АУ', 'Яндекс.Диск', '3.2.38.4985', 'Яндекс', 12, 6, None),
#     ('Краснобродский', 'Яндекс.Диск', '3.2.38.4985', 'Яндекс', 1, 1, None),
#     ('АУ', 'Яндекс.Телемост', '1.0.34.1167', 'Яндекс', 1, 1, None),
#     ('АУ', 'Яндекс.Телемост', '1.0.58.1525', 'Яндекс', 18, 8, None),
#     ('Калтан', 'Яндекс.Телемост', '1.0.58.1525', 'Яндекс', 1, 1, None)
# ]
# # Словарь для отслеживания, какие значения уже встречались
# seen_programs = set()
#
# # Новый список для хранения результатов
# new_data = []
#
# # Проходимся по исходному списку
# for entry in data:
#     program_name = entry[1]
#     if program_name in seen_programs:
#         new_entry = (entry[0], ' ',) + entry[2:]
#     else:
#         new_entry = entry
#         seen_programs.add(program_name)
#     new_data.append(new_entry)
#
# # Выводим результат
# for item in new_data:
#     print(item)
#
# from rapidfuzz import fuzz
#
# a = fuzz.token_sort_ratio('1C:Enterprise 8 (x86-64) Thin client (8.3.22.2239)',
#                           '1C:Enterprise 8 (x86-64) (8.3.21.1624)')
# print(a)
import openpyxl


def read_excel(file_name):
    workbook = openpyxl.load_workbook(file_name)
    sheet = workbook.active
    rows = list(sheet.iter_rows(values_only=True))
    return rows, sheet


def write_to_excel_output(sheet, output_file):
    workbook = sheet.parent
    workbook.save(output_file)


row_list, sheet = read_excel('groups_test2.xlsx')

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
write_to_excel_output(sheet, 'output_fil.xlsx')
