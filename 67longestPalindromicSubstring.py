#Problem: #Find longest substring which is a palindrome. 
#Real-world use: #DNA sequence analysis, spell-checkers, text editors.

def longestPalindrome(s):
    res = ""
    for i in range(len(s)):
        #odd length
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:  # Fixed: added 'and'
            if (r-l+1) > len(res):
                res = s[l:r+1]
            l -= 1; r += 1
            
        #Even length
        l, r = i, i+1
        while l >= 0 and r < len(s) and s[l] == s[r]:  # Fixed: s[l] not s[1]
            if (r-l+1) > len(res):
                res = s[l:r+1]
            l -= 1; r += 1
                
    return res  # Fixed: proper indentation

#Example
print(longestPalindrome("babad"))  # "bab" or "aba"

#logic:- expand around each center(odd/even) - keep max length.