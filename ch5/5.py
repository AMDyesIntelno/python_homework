str1=input("请输入字符串: ")
sum_en,sum_space,sum_num,sum_other_ch=0,0,0,0
for i in str1:
    if 'a'<=i<='z' or 'A'<=i<='Z':
        sum_en+=1
    elif '0'<=i<='9':
        sum_num+=1
    elif i==' ':
        sum_space+=1
    else:
        sum_other_ch+=1
print("英文字母个数: %d"%sum_en)
print("空格个数: %d"%sum_space)
print("数字个数: %d"%sum_num)
print("其他字符个数: %d"%sum_other_ch)