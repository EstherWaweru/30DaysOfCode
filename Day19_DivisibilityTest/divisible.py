class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        count=[]
        divisors_sum=0
        #getting the multiples of a number
        for i in range(1,n+1):
            if n%i==0:
                divisors_sum+=i      
        return divisors_sum       
            
            
        


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)