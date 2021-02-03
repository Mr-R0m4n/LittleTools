message = "AAAAAAAAAAAAAAAAABBBBBBBBBCCCCCCCCCCCDDDDDDDDDD"


def rle(data):
    i = 0
    counter = 1
    result = ""

    while i < len(data)-1:
        if data[i] == data[i+1]:
            counter = counter + 1
        else:
            result = result + str(counter) + data[i]
            counter = 1
        i = i + 1
    if i == len(data)-1:
        result = result + str(counter) + data[i]

    print(result)


rle(message)
