def custom_write(file_name, strings):
    file = open(file_name, 'w+', encoding='utf-8')
    strings_positions={}
    for counter in range(0, len(strings)):
        file.read()
        bait_stroki = file.tell()
        file.write(f'{strings[counter]}\n')
        strings_positions[ (counter+1, bait_stroki)] = strings[counter]
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
