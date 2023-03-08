def isPalindrome(data: str):
    print(data == "".join(list(reversed(data))))


isPalindrome("abadaba")