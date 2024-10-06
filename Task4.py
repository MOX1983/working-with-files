import xml.etree.ElementTree as ET

def add_product(tree, name, price, quantity, category):
    root = tree.getroot()
    new_product = ET.Element('product')

    name_elem = ET.SubElement(new_product, 'name')
    name_elem.text = name

    price_elem = ET.SubElement(new_product, 'price')
    price_elem.text = str(price)

    quantity_elem = ET.SubElement(new_product, 'quantity')
    quantity_elem.text = str(quantity)

    category_elem = ET.SubElement(new_product, 'category')
    category_elem.text = category

    root.append(new_product)

    tree.write("products.xml", encoding="UTF-8", xml_declaration=True)

def delete_product(tree, name):
    root = tree.getroot()
    for product in root.findall('product'):
        if product.find('name').text == name:
            root.remove(product)
            tree.write("products.xml", encoding="UTF-8", xml_declaration=True)
            return True
    return False


try:
    tree = ET.parse('products.xml')
    root = tree.getroot()

    data_list = []
    for person in root:
        person_data = {}
        for element in person:
            person_data[element.tag] = element.text.strip() if element.text else None
        data_list.append(person_data)
    for elem in root.iter():
        print(elem.tag, elem.text)

    sorted_data = sorted(data_list, key=lambda x: x["price"]) #reverse=True
    print(sorted_data, '\n', data_list)

    a, s, d, f = input('введите значение для\n"name": '), int(input('"price": ')), int(input('"quantity": ')), input('"category": ')
    add_product(tree, a, s, d, f)

    del_name = input('Введите название товара для удаления: ')
    if delete_product(tree, del_name):
        print(f"Товар '{del_name}' удалён.")
    else:
        print(f"Товар '{del_name}' не найден.")

    name = input("поиск категории или прайсу :  ")
    for  data in data_list:
        if data["price"] == name:
            print(data)
        elif data["category"] == name:
            print(data)


except Exception as ex:
    print(ex)