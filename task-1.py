def UP(f_str):
 res=""
 k=0
 tmp=str(f_str).split()
 for i in tmp:
    for i in tmp[k].split():
        a=''.join(tmp[k])
        if len(a)==1:
                res=res+a[0].upper()+' '
        else:
                res=res+a[0].upper()+a[1:-1]+a[-1]. upper()+' '
        k=k+1
 return res


f_str = input("Input str > ")
l = len(f_str)
integ = []
integ2 = []
i = 0
while i < l:
    str_int = ''
    a = f_str[i]
    while '0' <= a <= '9':
        str_int += a
        i += 1
        if i < l:
            a = f_str[i]
        else:
            break
    i += 1
    if str_int != '':
        integ.append(int(str_int))
print("Only numbers:",integ)
MAX_n = max(integ)
print("Max=",MAX_n)
for i in range(len(integ)):
    if integ[i] != MAX_n:
        integ2.append(integ[i]**i)
print("The numbers are raised to the power of them index:",integ2)
for d in '1234567890':
    f_str=f_str.replace(d, '')
f_str.strip(' ')
while f_str.find('  ') != -1:
    f_str = f_str.replace('  ', ' ')
print("letters:",f_str)
print("first and last letter big:",UP(f_str))
