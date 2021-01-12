from typing import List

class Solution:
    @staticmethod
    def solution(message: str, k: int) -> str:
        '''
        Function takes in message of type string and k of type int
        Returns cropped message containg only full words

        Example
        result = Solution.solution("Codility We test coders", 14)
        print(result)
        '''

        solution_list: List[str] = [] #List containing whole words of cropped string

        new_string: str = message[0:k] #splice message to k len

        spliced_string_list = new_string.split() #convert spliced string to list of words. Using list() results in string of alphabets
        new_message_list = message.split() #convert message to list 

        for i in spliced_string_list: #Iterate through each item in spliced list
            if i in new_message_list: #If word in spliced list is in new_message_list
                solution_list.append(i) #Append word to solution list

        return ' '.join(solution_list) #Return words in solution list as sentence

        
test = Solution.solution("Codility We test coders", 14)
test_two = Solution.solution("To crop or not to crop", 21)
test_three = Solution.solution("The quick brown fox jumps over the lazy dog", 39)
test_four=Solution.solution("Codility",14)
test_five=Solution.solution("Codilities we test",5)

print(test)
print(test_two)
print(test_three)
print(test_four)
