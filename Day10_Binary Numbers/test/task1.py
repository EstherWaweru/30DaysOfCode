binary_no=[]
n=int(input())
while n>0:
    #getting the binary representation
    quotient=n%2
    n=int(n/2)
    binary_no.append(quotient)
    print("Binary represrentation is",binary_no)
print(binary_no)
binary_no=binary_no[::-1]
print(binary_no[::-1])

binary=''.join([str(e) for e in binary_no])
print(binary)
print(len(max(binary.strip('0').split('1'))) )

# if binary_no[0]==0:
#     print(binary_no.pop(0))
# if binary_no[-1]==0:
#     print(binary_no.pop(-1))
# print(binary_no)
# binary=''.join([str(e) for e in binary_no])
# print(len(max(binary.split('1'))))

# for i in binary_no:
#     if i==0


    #finding the binary gaps and returning the maximum length
    #converting list to a string
# binary=''.join([str(e) for e in binary_no])
# print(binary)
# print(''.join(binary))
# print("first index",binary[0])
# print("last index",binary[-1])
# print("pop first",binary.pop(0))
# print(len(max(binary.split)))

##remove the 0 which are in the boundary
# if binary[0]==0:
#     binary.pop(0)
#     print("pop first",binary)
# if binary[-1]==0:
#     binary.pop(-1)
#     print("pop last",binary)

# print("modified srtr",binary)
# print(len(max(binary.split('1'))))