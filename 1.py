str=input ('''请输入待检测字符串:
''')
a=len(str)
for i in range(0,a//2):
    if str[i]!=str[a-i-1]:
        print('false')
        break
    elif i==a//2-1:
        print('true')