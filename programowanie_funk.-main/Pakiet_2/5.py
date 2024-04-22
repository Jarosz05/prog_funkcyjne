is_palindrome = lambda s: (cleaned := ''.join(char.lower() for char in s if char.isalnum())) == cleaned[::-1]

print(is_palindrome("hello"))