 vowels = 'AEIOU'
    Stuart = 0
    Kevin = 0
    L=len(string)
    
    for i in range(len(string)):
        if string[i] not in vowels:
            Stuart +=(L-i)
        else:
            Kevin +=(L-i)


    if Stuart == Kevin:
        print('Draw')
    elif Stuart > Kevin:
        print('Stuart', Stuart)
    else:
        print('Kevin', Kevin)
