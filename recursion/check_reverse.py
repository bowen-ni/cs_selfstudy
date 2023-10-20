def is_palindrome(my_string):
    if len(my_string) == 0:
        return True
    if len(my_string) == 1 or len(my_string) == 2:
        return (my_string[0] == my_string[-1])
    return(my_string[0] == my_string[-1] and is_palindrome(my_string[1:-1]))

print(is_palindrome("abba") == True)
print(is_palindrome("abcba") == True)
print(is_palindrome("") == True)
print(is_palindrome("abcd") == False)