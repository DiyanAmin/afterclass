string=str(input('Enter string to reverse it: '))
class reverse:
    def __init__(self,s):
        self.s=string
    def revStr(self,s):
        rev=s[::-1]
        return rev
ob=reverse(string)
print(f'Original String: {string}\nReverse String: {ob.revStr(string)}')