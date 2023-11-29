#5. Написать программу для замены определенного слова или фразы в текстовом файле.
#   Записать строки, включающую фразу в текстовый другой файл.

old_word = str(input('enter a word or phrase to search for: '))
new_word = '******'

with open('old.txt', 'r', encoding='utf-8') as file:
    if old_word in file.read(): print('success')
    else: print('not found')

with open('old.txt', 'r', encoding='utf-8') as file1:
    data = file1.readlines()  # файл, как список строк

with open('new.txt', 'w', encoding='utf-8') as file2:
    for line in data:
        if old_word in line:
            new_line = line.replace(old_word, new_word)
            file2.write(new_line)