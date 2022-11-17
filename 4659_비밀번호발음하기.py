vowels = {'a','e','i','o','u'}
while 1:
    word = input()
    if word == 'end':
        break
    if len(word) == 1:
        if word in vowels:
            print(f'<{word}> is acceptable.')
        else:
            print(f'<{word}> is not acceptable.')
        continue
    if len(word) == 2:
        flag = 0
        for w in word:
            if w in vowels:
                flag = 1
        if flag == 0:
            print(f'<{word}> is not acceptable.')
        else:
            if word[0] != word[1]:
                print(f'<{word}> is acceptable.')
            else:
                if word == 'ee' or word == 'oo':
                    print(f'<{word}> is acceptable.')
                else:
                    print(f'<{word}> is not acceptable.')
        continue

    flag = 0
    mo = 0
    za = 0
    check = 0
    tmp = 'tmp'
    for w in word:
        if w in vowels:
            flag = 1
            mo += 1
            za = 0
        else:
            za += 1
            mo = 0
        if mo == 3 or za == 3:
            print(f'<{word}> is not acceptable.')
            check = 1
            break
        if tmp == w and w != 'e' and w!= 'o':
            print(f'<{word}> is not acceptable.')
            check = 1
            break
        tmp = w
    if check == 1:
        continue
    if flag == 0:
        print(f'<{word}> is not acceptable.')
        continue
    print(f'<{word}> is acceptable.')