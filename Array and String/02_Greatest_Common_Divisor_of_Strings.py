#################### TYPE ----- 1  ------  ##################
from math import gcd


def gcdOfStrings( str1, str2):
    if(str1+str2 != str2+str1):
        return ""
    
    sub = gcd(len(str1),len(str2))

    return str1[:sub]

str1 = "ABCABC"
str2 = "ABC"
print(gcdOfStrings(str1,str2))

#################### TYPE ----- 2  ------  ##################

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if(str1+str2 != str2+str1):
            return ""
        a = len(str1)
        b = len(str2)
        while(b%a != 0):
            rem = b % a 
            b = a
            a = rem
        ans = str1[:a]
        return ans

'''Time Complexity:
The time complexity of this function mainly depends on two operations: the string concatenation operation (str1 + str2 and str2 + str1) and the greatest common divisor computation (gcd(len(str1), len(str2))).

String Concatenation: If str1 is of length n and str2 of length m, the concatenation will take O(n + m) time as each character from both strings need to be combined once.

Checking String Equality: Comparing the concatenated strings takes O(n + m) time. If the strings differ, the method returns early.

Greatest Common Divisor: The gcd function typically employs Euclid's algorithm, which has a time complexity of O(log(min(n, m))) where n and m are the lengths of the strings.

Therefore, the overall time complexity combines these operations resulting in O(n + m + log(min(n, m))). However, the dominating factor for large values of n and m will tend to be the concatenation and comparison, so we can approximate the time complexity as O(n + m).

Space Complexity:
The space complexity of the gcdOfStrings function can be analyzed as follows:

Temporary Strings: The creation of concatenated strings str1 + str2 and str2 + str1 requires additional space of O(n + m).

GCD Computation: The gcd function itself may use constant space, O(1), if the Euclidean algorithm is implemented in an iterative manner.

As such, no additional space that grows with the input size is required except for the string concatenation. Hence, the space complexity is O(n + m).'''