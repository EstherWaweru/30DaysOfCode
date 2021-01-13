import re
S="We test coders. Give us a try?"

    # write your code in Python 3.6
new_sentence=S.replace('?','.')
new_sentence=S.replace('!','.')
sentences=new_sentence.split('.')

words=[]
for word in sentences:
    words.append(word.split())
    

return len(max(words,key=len))