fileInput = open("input.txt","r")
listInput = fileInput.readlines()
amount = 1
curNum = int(listInput[0])
for num in listInput:
    if (curNum != int(num)):
        amount += 1
        curNum = int(num)
print(amount)