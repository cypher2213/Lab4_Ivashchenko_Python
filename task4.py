def negative_func():
    array_neg = []
    user_input = input("Введіть елементи списку через пробіл: ")
    lst = user_input.split() 
    for i in lst:
        numb = int(i)
        if numb < 0:
            array_neg.append(numb)
        else:
            continue
        
    if(len(array_neg) == 0):
        print("No negative numbers were found.")
        return
    return print(sum(array_neg)/len(array_neg))

negative_func()