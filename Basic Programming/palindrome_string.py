#PF-Assgn-31
def check_palindrome(word):
    palindrome_word=word[::-1]
    if(word==palindrome_word):
        return True
    else:
        return False
    #Remove pass and write your logic here
    
status=check_palindrome("malayalam")
if(status):
    print("Word is palindrome")
else:
    print("Word is not palindrome")