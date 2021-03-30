# Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

# Examples:

# spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"

# spinWords( "This is a test") => returns "This is a test"

# spinWords( "This is another test" )=> returns "This is rehtona test"

def spin_words(sentence):
    # Your code goes here
    if len(sentence)<5:
        return sentence
    else:
        new_list=sentence.split()
        for word in range(len(new_list)):
            if len(new_list[word])>=5:
                new_list[word]=new_list[word][::-1]
    return " ".join(new_list)
    
    