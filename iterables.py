# for x in "krishna Kamal Baishnab":
#     print(x)



# name = "krishna Kamal Baishnab"
# for idx in range(len(name)):
#     print("Index:", idx, ", Character:", name[idx])


countEvenNumber = 0
for number in range(1,20):
    if number % 2 == 0:
        print(number)
        countEvenNumber += 1

print("Total even numbers:", countEvenNumber)