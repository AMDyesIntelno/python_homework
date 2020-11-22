class pwd_check:
    score=0
    upper_check=0
    lower_check=0
    num_check=0
    symbol_check=0
    def __init__(self,pwd):
        self.pwd=pwd
        self.__get_score()
    def __pwd_length_check(self):
        if len(self.pwd)<=4:
            self.score+=5
        elif len(self.pwd)<7:
            self.score+=10
        else:
            self.score+=25
    def __pwd_char_check(self):
        for i in self.pwd:
            if 65<=ord(i)<=90:
                self.upper_check+=1
            elif 97<=ord(i)<=122:
                self.lower_check+=1
            elif 48<=ord(i)<=57:
                self.num_check+=1
            else:
                self.symbol_check+=1
    def __get_score(self):
        self.__pwd_length_check()
        self.__pwd_char_check()
        #upper/lower score
        if self.upper_check==0 and self.lower_check==0:
            self.score+=0
        elif self.upper_check and self.lower_check==0:
            self.score+=10
        elif self.upper_check==0 and self.lower_check:
            self.score+=10
        else:
            self.score+=20
        #num score
        if self.num_check==0:
            self.score+=0
        elif self.num_check==1:
            self.score+=10
        else:
            self.score+=20
        #symbol score
        if self.symbol_check==0:
            self.score+=0
        elif self.symbol_check==1:
            self.score+=10
        else:
            self.score+=25
        #addition score
        if (self.upper_check or self.lower_check) and self.num_check:
            self.score+=2
        if (self.upper_check or self.lower_check) and self.num_check and self.symbol_check:
            self.score+=3
        if self.upper_check and self.lower_check and self.num_check and self.symbol_check:
            self.score+=3
    def __str__(self):
        if self.score>=90:
            return "very secure"
        elif self.score>=80:
            return "secure"
        elif self.score>=70:
            return "very strong"
        elif self.score>=60:
            return "strong"
        elif self.score>=50:
            return "average"
        elif self.score>=25:
            return "weak"
        else:
            return "very weak"
print(pwd_check("asdf"))
print(pwd_check("asdfqwer"))
print(pwd_check("asdfqwer123"))
print(pwd_check("asdfqwer123!@#"))
print(pwd_check("asdfQWER123!@#"))