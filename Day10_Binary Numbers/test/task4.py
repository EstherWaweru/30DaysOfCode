test_str="Codility we test coders"
k=14

for i in range(len(test_str)):
    if len(test_str)==14:
        print(test_str)
    elif len(test_str)<14:
        print(test_str.strip())
    else:
        test_str1=test_str.split()
        print(test_str1)
        lenth=len(test_str1)
        print(lenth)
        new_array=[]
        for element in test_str:
            if len(element)==14:
                print(test_str)
                break
            elif len(element)<14:
                new_array.append(element)
                print(new_array)
            else:
                print('')
            

        