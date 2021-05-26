import random
import operator

def flatten(data):
    output = []
    for item in data:
        if type(item) == list:
            output += flatten(item)
        else:
            output.append(item)
    return output

def lotto_a(value):
    list_a = range(1,45+1)
    numbers = []

    for i in range(value):
        numbers.append(random.sample(list_a,k = 6))

    numbers = flatten(numbers)
    # print(numbers)
    counter = {}
    numbers = sorted(numbers)
    # print(numbers)
    for number in numbers:
        if number in counter:
            counter[number] = counter[number] + 1
        else:
            counter[number] = 1
    # print(counter)

    sdict= sorted(counter.items(), key=operator.itemgetter(1),reverse=True)
    lotto = []
    # print(sdict)
    for i in range(6):
        lotto.append(sdict[i][0])
    return sorted(lotto)

