import json

try:
    with open('library.json') as f:
        templates = json.load(f)
except FileNotFoundError as ex:
    print(f"Ошибка: файл не найден - {ex}")
try:
    sorted_data = json.dumps(sorted(templates, key=lambda x: x["title"]), indent=1) #reverse=True
    # №1
    print(sorted_data, '\n') # №1

    # №2
    a, s, d, f, g = input('введите значение для\n"title": '), input('"author": '), int(input('"year": ')), input('"genre": '), int(input('"copies": '))
    new_data = [a, s, d, f, g]
    k = ["title", "author", "year", "genre", "copies"]

    templates.append(dict(zip(k, new_data)))
    with open('library.json', 'w') as f:
        json.dump(templates, f, indent=1)
    print('запись прошла успешно :)')

    # №3
    ind = int(input('какой элемент хотите удалить (число)? : '))
    del templates[ind - 1]
    with open('library.json', 'w') as f:
        json.dump(templates, f, indent=1)
    print('удаление прошло успешно :)')

    # №4
    name = input("введите атора или жанр ")
    for data in templates:
        if data["genre"] == name:
            print(data)
        elif data["author"] == name:
            print(data)

except Exception as ex:
    print(ex)