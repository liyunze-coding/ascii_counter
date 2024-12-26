import time
import os


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


numbers = '''
00000000   
0      0   
0      0   
0      0   
0      0   
0      0   
00000000   

       1   
       1   
       1   
       1   
       1   
       1   
       1   

22222222   
       2   
       2   
22222222   
2          
2          
22222222   

33333333   
       3   
       3   
33333333   
       3   
       3   
33333333   

4      4   
4      4   
4      4   
44444444   
       4   
       4   
       4   

55555555   
5          
5          
55555555   
       5   
       5   
55555555   

66666666   
6          
6          
66666666   
6      6   
6      6   
66666666   

7777777   
      7   
      7   
      7   
      7   
      7   
      7   

88888888   
8      8   
8      8   
88888888   
8      8   
8      8   
88888888   

99999999   
9      9   
9      9   
99999999   
       9   
       9   
99999999   '''

numbers_ascii_art = []
index = -1
for line in numbers.split('\n'):
    if line == '':
        numbers_ascii_art.append([])
        index += 1
    numbers_ascii_art[index].append(line)

clearConsole()
for x in range(0, 11)[::-1]:
    res = ''
    number = f"{x:02d}"
    for i in range(8):
        for digit in number:
            res += numbers_ascii_art[int(digit)][i]
        res += '\n'
    print(res)
    time.sleep(1)
    clearConsole()


# print(res)
