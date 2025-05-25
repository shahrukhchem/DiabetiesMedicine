'''
reversing a string
base case
hen length of string is one it retruns the same string
else
'''

def reversestring(s):
    print('entering ith ',s)
    if len(s)<=1:
        return s
    else:
        k=reversestring(s[1:])+s[0]
    
    return k
        
'''
palindrome check
a string is if its same from foreard and backard
if size is 1 then its yes

'''   
def checkpalindrome(s):
    print('entering ith ',s)
    if len(s)<=1:
        return True
    else:
        c1=s[0]
        c2=s[-1]
        if c1 !=c2:
            k= False
        else:
            k=True
            k=checkpalindrome(s[1:-1])
            
    print('leaving ith',s[1:-1])
    return k
            
        
        

    
l=checkpalindrome('naman')
print(l)