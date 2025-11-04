def remove_every_other(my_list):
    tempArr = []

    for i in range(0, len(my_list),2):
        tempArr.append(my_list[i])
    return tempArr
        
list1 = [1,2,3,4,5,6,7,8,9]
print(remove_every_other(list1))

