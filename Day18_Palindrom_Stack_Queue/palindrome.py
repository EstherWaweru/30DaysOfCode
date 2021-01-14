import sys
from collections import deque

class Solution:
    def __init__(self):
        self.stk=[]
        # self.que=[]
        self.que=deque()
    
    #pushes a character to the top of the stack(LIFO)
    def pushCharacter(self,s):
        self.stk.append(s)
    #retrieve the element from top of the stack
    def popCharacter(self):
        return self.stk.pop()
    #pushes a character to the end of the queue(FIFO)
    def enqueueCharacter(self,s):
        self.que.append(s)
   #retrieve a character form the beginning of the queue
    def dequeueCharacter(self):
        return self.que.popleft()
        # char = self.que[0]
        # self.que = self.que[1:]
        # return char
        
        

# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    