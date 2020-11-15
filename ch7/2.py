class LengthError(Exception):
    def __init__(self,length):
        Exception.__init__(self, length)
        self.length=length
    def __str__(self):
        return "当前字符串长度为%d"%(self.length)+",请将长度控制在0~10之间"
def get_length(s):
    length=len(s)
    if length<0 or length>10:
        raise LengthError(length)
    return length
s1="asdf"
print(get_length(s1))
s2="asdfasdfasdf"
print(get_length(s2))