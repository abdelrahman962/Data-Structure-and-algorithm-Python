def is_Palindrome(word):
    stack=[]
    for i in word:
        stack.append(i)
    word2=""
    while stack:
        word2+=stack.pop()

    if word==word2:
        return True
    return False
 
    
def is_Palindrome_two_pointer(word:str):
    l=0
    r=len(word)-1
    while l<r:
        if word[l]!=word[r]:
            return False
        l+=1
        r-=1
    return True    


word=input("Enter word: ")
print(is_Palindrome(word))