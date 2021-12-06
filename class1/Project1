import re

f=open("data.txt")
list = []
line = f.readline() #按行读取文件
reg = "[^0-9A-Za-z]"
while line:
    # list.append(line.replace(".",""))
    # print(line)
    list.append(re.sub(reg, " ", line))
    # print(type(line))
    line = f.readline()
f.close()

print(list)
dict = {}


for i in range(len(list)):
    words = list[i].lower().split()
    # print(words)
    for word in words:
        if word in dict.keys():
            dict[word].add("d" + str(i+1))
        else:
            dict[word] = {"d" + str(i+1)}

print(dict)
while(True):
    keywords = input("请输入关键词 Please input keywords: ")
    if keywords.lower() in dict.keys():
        print("检索结果 Search result: ", dict[keywords.lower()])
    else:
        print("Not Found.")


