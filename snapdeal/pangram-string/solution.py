# code
no_of_testcases = int(input())

while no_of_testcases:
    mapper_dict = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0
    }
    entered_string = input()
    for character in entered_string:
        lower_character = character.lower()
        if mapper_dict.get(lower_character) is not None:
            mapper_dict[lower_character] += 1
    for key, value in mapper_dict.items():
        if value == 0:
            print(0)
            break
    else:
        print(1)
    no_of_testcases -= 1
