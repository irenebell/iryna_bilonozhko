def palindrome(n):
    n = str(n).lower().replace(' ', '').replace(',', '').replace("'", '')
    if n == n[::-1]:
        print("Yes, it's a palindrome")
        return True
    else:
        print("No, it's not a palindrome")
        return False

palindrome(555676555)
