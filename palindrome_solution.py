from curses.ascii import isalnum
# from turtle import st
# import re

# ------- My way --------
# def palindrome_sentens(string):
#     return string[::-1].casefold() == string.casefold()


# sentence = input("Please write sentens: ")
# re_string = re.sub(r'[^\w\s]', '', sentence)
# re_space_string = re.sub(r"\s+", "", re_string)
# print(re_space_string)
# if palindrome_sentens(re_space_string):
#     print("'{}' is a palidrome".format(re_space_string))
# else:
#     print("'{}' is not palidrome".format(re_space_string))


# ----------- other way -------------
def palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    print(string)
    return string[::-1].casefold() == string.casefold()      


word = input("Please enter  word or sentece to chack: ")
if palindrome_sentence(word):
    print("'{}' is a palidrome".format(word))
else:
    print("'{}' is not palidrome".format(word))

