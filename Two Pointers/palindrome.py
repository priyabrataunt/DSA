class Solution:
    # def isPalindrome(self, s: str) -> bool:
    #     newStr = ""

    #     for c in s:
    #         if c.isalnum():
    #             newStr += c.lower()
    #     self.newStr = newStr
    #     self.revStr = newStr[::-1]
    #     return newStr == newStr[::-1]
    



    def isPlaindrom(self, str): 
        left, right = 0, len(str) - 1

        while left < right:
            while left < right and not self.isallNumeric(str[left]):
                left += 1
            while right > left and not self.isallNumeric(str[right]):
                right -= 1
            
            if str[left].lower() != str[right].lower():
                return False

            left += 1
            right -= 1

        return True

    def isallNumeric(self, char):
        return (ord('A') <= ord(char) <= ord('Z') or
                ord('a') <= ord(char) <= ord('z') or
                ord('0') <= ord(char) <= ord('9'))


sol = Solution()
print(sol.isPlaindrom(str="Was it a car or a cat I saw?"))
# print(f'New String is:  {sol.newStr}')
# print(f'New Reverse String : {sol.revStr}')