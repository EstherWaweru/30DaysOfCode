class Difference:
    def __init__(self, a):
        self.__elements = a
        

    # Add your code here
    def computeDifference(self):
        diff_array=[]
        #loop through the i+1 to the last element and through the first ement to the second last element
        for i in range(len(self.__elements)-1):
            for j in range(i+1,len(self.__elements)):
                
                diff=abs(self.__elements[j]-self.__elements[i])
                diff_array.append(diff)
        
        self.maximumDifference=max(diff_array)
            
            
            
        

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)