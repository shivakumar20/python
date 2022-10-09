'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

print("Hello World")

dic = {}

list = [['a',1],['b',2],['c',3],['d',4]]

for i in range(len(list)):
    if list[i][0] in dic.keys():
        dic[list[i][0]].append(list[i][1])
        
    else:
        dic[list[i][0]] = []
        dic[list[i][0]].append(int(list[i][1]))

print(dic)