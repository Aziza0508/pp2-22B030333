def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

print(is_palindrome('AzizA'))
print(is_palindrome('Aziza'))