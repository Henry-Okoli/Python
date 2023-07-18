 


# alternating between capital and small letters

def alternate_string (string):
    result = " "
    for i, char in enumerate (string):
        if i % 2 ==0:
            result += char.upper()
        else:
            result += char.lower()
    return result
input_string = input("Enter the sentence: ")
string_characters = alternate_string(input_string)
print(string_characters)


# string_input = input("Enter the string characers: ")
# alternating_string = " "
# for i, char in enumerate(string_input):
#     if i % 2 == 0:
#         alternating_string += char.upper()
#     else:
#         alternating_string += char.lower()
# print ("Alternating characters: ", alternating_string)


word_input =str(input("Enter the sentence you want to split: "))
# split the input 
word_split = word_input.split()

alternate_word = []
for i, word in enumerate(word_split):
    if i % 2 == 0:
        alternate_word.append(word.upper())
    else:
        alternate_word.append(word.lower())

alternate_text = ' '.join(alternate_word)

print (alternate_text)

num_list = [1,4,2,7,5,9]
print(num_list[1:2])