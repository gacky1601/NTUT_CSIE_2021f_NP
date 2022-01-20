def tob(a):
    ans = format(a, "b")
    while(len(ans) != 8):
        ans = '0' + ans
    return ans


def to(a):
    ans = 0
    for i in range(len(a)):
        if(a[i] == '1'):
            ans = ans + (2 ** (7 - i))
    return ans


aaas = input().split('.')
temp = aaas[3].split('/')
aaas.append(temp[1])
aaas[3] = temp[0]
temp = int(aaas[4])
temp = 32 - temp
temp3 = temp
aaas.pop()
for i in range(len(aaas)):
    aaas[i] = int(aaas[i])


if(int(aaas[0]) <= 126):
    print('A')
elif(int(aaas[0]) <= 191):
    print('B')
else:
    print('C')
for i in range(len(aaas)):
    aaas[i] = tob(aaas[i])


ans2 = 0 - temp
while(ans2 < 0):
    ans2 = ans2 + 8
print(2 ** ans2)


temp2 = 3
while(temp >= 8):
    if(temp2 == 3):
        aaas[temp2] = "00000001"
    else:
        aaas[temp2] = "00000000"
    temp = temp - 8
    temp2 = temp2 - 1

temp4 = ''
for i in range(7, -1, -1):
    if(temp2 == 3 and i == 7):
        temp4 = '1'
        temp = temp - 1
    elif(temp > 0):
        temp4 = '0' + temp4
        temp = temp - 1
    else:
        temp4 = aaas[temp2][i] + temp4
aaas[temp2] = temp4

for i in range(len(aaas)):
    print(to(aaas[i]), end='')
    if(i < 3):
        print('.', end='')
print(' ~ ', end='')
temp = temp3
temp2 = 3
while(temp >= 8):
    if(temp2 == 3):
        aaas[temp2] = "11111110"
    else:
        aaas[temp2] = "11111111"
    temp = temp - 8
    temp2 = temp2 - 1
temp4 = ''
for i in range(7, -1, -1):
    if(temp2 == 3 and i == 7):
        temp4 = '0'
        temp = temp - 1
    elif(temp > 0):
        temp4 = '1' + temp4
        temp = temp - 1
    else:
        temp4 = aaas[temp2][i] + temp4
aaas[temp2] = temp4


for i in range(len(aaas)):
    print(to(aaas[i]), end='')
    if(i < 3):
        print('.', end='')
