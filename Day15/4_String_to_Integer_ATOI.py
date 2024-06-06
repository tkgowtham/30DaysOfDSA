class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()  # Remove leading and trailing whitespace
        if not s:  # Check if the string is empty
            return 0

        negative = False
        i = 0
        
        # Check if the first character is '-' or '+'
        if s[0] == '-':
            negative = True
            i += 1
        elif s[0] == '+':
            i += 1
        
        # Remove leading zeros
        while i < len(s) and s[i] == '0':
            i += 1

        r = ''
        while i < len(s) and s[i].isdigit():  # Check if the character is a digit
            r += s[i]
            i += 1
        
        if not r:  # If no digits were found
            return 0

       
        val = 0
        for char in r:
            val = val * 10 + (ord(char) - ord('0'))  # Convert the string of digits to an integer

        # Apply the negative sign if needed
        if negative:
            val = -val

        # Clamp the value to the 32-bit signed integer range
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if val > INT_MAX:
            return INT_MAX
        if val < INT_MIN:
            return INT_MIN

        return val    
