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
            
        
def summingnumber(s):   
    if len(s)<=1:
        totalsum=s[0]
        return totalsum
   
    else:
        totalsum=s[0]+summingnumber(s[1:])
        return totalsum
        
    

def findtriangularnumber(n): 
    if n==1:
        return n
    else:
        return n+findtriangularnumber(n-1)
    
    
def findingpermutations(string):
    anagrams=[]
    print('entering ',string)
    if len(string)<=1:
        return string
    elif len(string)==2:
        anagrams.append(string)
        anagrams.append(string[1]+string[0])
        return anagrams
    else:
     for s in string:
        
        remaining_elements = [c for c in string if c !=s]
        remaining_elements=''.join(remaining_elements)
        for a in findingpermutations(remaining_elements):
            anagrams.append(a+s)
           # anagrams.append(s+a)
        print('leaving',string)
     return anagrams
        
        
        
    
a=findingpermutations('abc')
print(a)