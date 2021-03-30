# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

# is_isogram("Dermatoglyphics" ) == true
# is_isogram("aba" ) == false
# is_isogram("moOse" ) == false # -- ignore letter case


def is_isogram(string):
    is_isogram=True
    if len(string)==0:
        return True
    string=string.lower()
    
    for i in range(0,len(string)-1,1):
        for j in range(i+1,len(string),1):
            if string[i]==string[j]:
                is_isogram=False
    return is_isogram
            
if __name__ == '__main__' :
    print(is_isogram("aba")   )   
    print(is_isogram("moOse")   )  
    print(is_isogram("abc")   )
        
    