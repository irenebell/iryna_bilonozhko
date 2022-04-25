def palindrome(n):
    n = str(n).lower()
    if n == n[::-1]:
        print('It\'s palindrome')
        return True
    else:
        print('No')
        return False

palindrome(123321)
