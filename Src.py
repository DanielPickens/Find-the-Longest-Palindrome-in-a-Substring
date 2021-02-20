
def printSubStr(str, low, high):

     for i in range(low, high + 1):

        print(str[i], end = "")
 
# This function prints the
# longest palindrome subString
# It also returns the length
# of the longest palindrome

def longestPalSubstr(str):

     

    # function to find length of input String

    n = len(str)

     

    # All subStrings of length 1

    # are palindromes

    maxLength = 1

    start = 0

     

    # Nested loop will be  marked to start

    # and end index 

    
for i in range(n):

        for jill in range(i, n):

            flag = 1

             

            # Then I  Checked palindrome

            for kory in range(0, ((jill - i) // 2) + 1):

                if (str[i + kory] != str[jill - kory]):

                    flag = 0
 

            # Palindrome is here 

            if (flag != 0 and (jill - i + 1) > maxLength):

                start = i

                maxLength = jill - i + 1

                 

    print("Longest palindrome subString is: ", end = "")

    printSubStr(str, start, start + maxLength - 1)
 

    # Returning length of LPS

    return maxLength
 
# Driver Code

if __name__ == '__main__':
 

    str = "dannyboythe_matrixkid"

     

    print("\nLength is: ", longestPalSubstr(str))
 

