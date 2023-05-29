def rhythm(str):
    str = str.split()
    arr = []
    for word in str:
        sum = 0
        for i in word:
            if i in 'аеёиоуыэюя':
                sum += 1
        arr.append(sum)
    return len(arr) == arr.count(arr[0])


str = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
if rhythm(str):
    print('Парам пам-пам')
else:
    print('Пам парам')
