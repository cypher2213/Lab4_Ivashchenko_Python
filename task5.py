def add_vowels_to_set():
    set_cd = {'c', 'd'}
    vowels = {'a', 'e', 'i', 'o', 'u'}
    try:
        result = set_cd.union(vowels)
    except TypeError:
        result = list(set_cd) + list(vowels)
        result = set(result) 
    
    print("Результат:", result)

add_vowels_to_set()
