my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
elem = my_list[index]
while elem >= 0 and index < len(my_list):
    elem = my_list[index] #Сначала взяли нулевой индекс
    index += 1 #Затем к нему начали прибавлять +1
    if elem < 0:
        break
    elif elem == 0:
        continue
    else:
        print(elem)