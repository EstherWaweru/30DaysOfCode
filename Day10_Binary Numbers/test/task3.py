array=[-6,-91,1011,-100,84,-22,0,1,473]
mini=array[0]
for i in range(len(array)):
    if array[i]<mini:
        if array[i]%11==0:

            mini=array[i]
print(mini)