# prices = [10,20,30]
# sum = 0
# for i in prices:
#     sum = sum + i
# print(sum)



#print the following pattern


# XXXXX
# XX
# XXXXX
# XX
# XX
# XX


pattern=[5,2,5,2,2,2]


for xCount in pattern:
    output = ''
    for count in range(xCount):
        output = output+'X'
    print(output)