# You are given a string s and an array of strings words of the same length. Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.

# You can return the answer in any order.

 

# Example 1:

# Input: s = "barfoothefoobarman", words = ["foo","bar"]
# Output: [0,9]
# Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
# The output order does not matter, returning [9,0] is fine too.

# Example 2:

# Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
# Output: []

# Example 3:

# Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
# Output: [6,9,12]

 

# Constraints:

#     1 <= s.length <= 104
#     s consists of lower-case English letters.
#     1 <= words.length <= 5000
#     1 <= words[i].length <= 30
#     words[i] consists of lower-case English letters.


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_size=len(words[0])
        
        #get the word count
        word_count=len(words)
        #get the characters
        size_words=word_size*word_count
        result=[]
        if size_words>len(s):
            return result
        hash_map={}
        for i in range(word_count):
            if words[i] in hash_map:
                hash_map[words[i]]+=1
            else:
                hash_map[words[i]]=1
       
        for i in range(0,len(s)-size_words+1,1):
            temp_hash=hash_map.copy()
          
            j=i
            count=word_count
           
            #traverse the substring
            while j<i+size_words:
                
                #extract the word
                word=s[j:j+word_size]
                
                if word not in hash_map or temp_hash[word]==0:
                    break
                else:
                    temp_hash[word]-=1
                    count-=1
                j+=word_size
                
            if count==0:
                result.append(i)
        return result
        
                
        
