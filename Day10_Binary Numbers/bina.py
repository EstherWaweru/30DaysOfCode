data = '11110000111110000011111010101010101011111111'
print('----',max(data.split('0')))
print ("Maximum Number of consecutive one's: ",max(map(len,data.split('0'))) )
#converting array to a string
data1=['2','3']
array=''.join(data1)
print(array)
data2=[1,2,3]
#list comprehension
array_1=''.join([str(e) for e in data2])
arr=[]
for elem in data2:
    arr.append(str(elem))

print(array_1)
print(''.join(arr))