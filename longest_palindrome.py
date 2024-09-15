def longest_palindrome(s):
    # Helper function to expand around the center
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Return the palindrome substring
        #print("BBB", left + 1, right)
        #print("CCC",s[left + 1:right])
        return s[left + 1:right]

    if len(s) == 0:
        return ""

    longest = ""

    for i in range(len(s)):
        # Check for odd-length palindromes (single character center)
        #print("ODD", i, i)
        odd_palindrome = expand_around_center(i, i)
        if len(odd_palindrome) > len(longest):
            longest = odd_palindrome

        # Check for even-length palindromes (two character center)
        #print("EVEN", i, i+1)
        even_palindrome = expand_around_center(i, i + 1)
        if len(even_palindrome) > len(longest):
            longest = even_palindrome

    return longest


# Example usage
string = "racecarcivicasdfghjklkjhgfdsa"
result = longest_palindrome(string)
print(f"The longest palindromic substring in '{string}' is '{result}'")
