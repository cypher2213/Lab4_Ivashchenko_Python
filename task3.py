def remove_element_from_list():
    user_input = input("Введіть елементи списку через пробіл: ")
    lst = user_input.split() 
    element_to_remove = input("Введіть елемент, який потрібно видалити: ")
    if element_to_remove in lst:
        lst.remove(element_to_remove)
        print("Елемент видалено!")
    else:
        print("Такого елемента у списку немає!")
    print("Оновлений список:", lst)
remove_element_from_list()