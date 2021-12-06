import re
import json

docu_dic = {}   # 字典存储每一行句子
all_words_list = []  # 列表存储句子的分词
all_words_set = set()  # 对每一个单词去重
inverted_index = dict()  # 倒排索引
inverted_index_json = "" # 倒排索引转换成 json 格式
all_frequency = 0 # 单词的总词频

# 将每行句子存到字典中
def get_docu_dic():
    f = open("data.txt")
    # list = []
    line = f.readline()
    reg = "[^0-9A-Za-z]"
    i = 0
    while line:
        i += 1
        docu_dic[i] = re.sub(reg, " ", line)
        line = f.readline()
    f.close()
def get_words_list_and_set():
    for line in docu_dic.values():
        cut = line.split()
        # print(type(cut))
        all_words_list.append(cut)
        # print(all_words_list)
        for i in cut:
            # print(type(i))
            all_words_set.add(i)


# 将倒排索引存储到字典中，格式如：{'关键词': {所在文件的序号: 在该文件出现的频率}}
def get_inverted_index():
    for word in all_words_set:
        temp = {}
        # print(word)
        for key in docu_dic.keys():
            split_field = [x.lower() for x in docu_dic[key].split()]
            # print(split_field)
            # print(word)
            if word.lower() in split_field:
                temp[key] = 0
        inverted_index[word.lower()] = temp
    # print(inverted_index)

def get_words_frequency():
    for word in all_words_set:
        for i in range(len(all_words_list)):
            for j in range(len(all_words_list[i])):
                if word == all_words_list[i][j]:
                    try:
                        inverted_index[word.lower()][i + 1] += 1
                        # temp = inverted_index[word.lower()][str("d" + str(i + 1))]
                    except:
                        continue
# 获得总词频
def get_all_frequency(key):
    # print(inverted_index.keys())
    all_frequency = 0
    if key in inverted_index.keys():
        for i in inverted_index[key].keys():
            all_frequency += inverted_index[key][i]
    # print(all_frequency)
    return all_frequency

# 倒排索引转换成 json 并保存到文件中
def inverted_index_to_json():
    inverted_index_json = json.dumps(inverted_index)
    # print(inverted_index_json)
    with open("output.json", "w", encoding='UTF-8') as f:
        json.dump(inverted_index, f, sort_keys=True, indent=4)
        print("保存 json 文件完成")

# 求交集
def get_intersection(keywords):
    print(keywords)
    result = {}
    if len(keywords) == 1 and keywords[0] in inverted_index.keys():
        result = set(inverted_index[keywords[0]].keys())
        # print(type(inverted_index[keywords[0]].keys()))
        print(result)
    elif len(keywords) > 1:
        flag=True
        for i in range(len(keywords) - 1):
            if i==0 and keywords[i] in inverted_index.keys() and keywords[i+1] in inverted_index.keys():
                result=inverted_index[keywords[i]].keys() & inverted_index[keywords[i + 1]].keys()
            else:
                if keywords[i + 1] in inverted_index.keys():
                    # print(inverted_index[keywords[i]].keys())
                    result = result & inverted_index[keywords[i + 1]].keys()
                    # result = result & inverted_index[keywords[i]].keys()
                else:
                    flag=False

        if not flag:
            print("Not Found")
        elif not result:
            print("The result of intersection is Null.")
        else:
            print(result)
    elif len(keywords) == 0:
        print('The input is null, please input again.')
    else:
        print("Not Found")

# 求交集
def get_intersection_2(keywords):
    print(keywords)
    result = []
    temp1 = []
    temp2 = []
    if len(keywords) == 1 and keywords[0] in inverted_index.keys():
        result.append(list(inverted_index[keywords[0]].keys()))
        print(result)
    elif len(keywords) == 2 and keywords[0] in inverted_index.keys() and keywords[1] in inverted_index.keys():
        for x in list(inverted_index[keywords[0]].keys()):
            temp1.append(x)
        for y in list(inverted_index[keywords[1]].keys()):
            temp2.append(y)
        i = 0
        j = 0
        while i < len(temp1) and j < len(temp2):
            if temp1[i] == temp2[j]:
                result.append(temp1[i])
                i += 1
                j += 1
            elif temp1[i] < temp2[j]:
                i += 1
            else:
                j += 1
        if not result:
            print("The result of intersection is Null.")
        else:
            print(result)
    elif len(keywords) == 0:
        print("Please input again!")
    elif (not keywords[0] in inverted_index.keys()) or (not keywords[1] in inverted_index.keys()):
        print("Not Found")






get_docu_dic()
get_words_list_and_set()
get_inverted_index()
# print(inverted_index)
get_words_frequency()
print(inverted_index)
# get_all_frequency()
inverted_index_to_json()

while(True):
    # keywords = []
    # keywords.append(input("请输入关键词 Please input keywords: ").split(" "))
    keywords = input("请输入关键词 Please input keywords: ").lower().split()
    # get_intersection_2(keywords)
    get_intersection(keywords)
    # print(keywords)
    # num = len(keywords)
    # result = set()
    # for i in range(len(keywords)-1):
    #     if keywords[i] in inverted_index.keys() and keywords[i+1] in inverted_index.keys():
    #         # print(inverted_index[keywords[i]].keys())
    #         result = inverted_index[keywords[i]].keys() & inverted_index[keywords[i+1]].keys()
    #         if not result:
    #             print("Not Found")
    #         else:
    #             print(result)
    #     else:
    #         print("Not Found")
    # if keywords.lower() in inverted_index.keys():
    #     print("检索结果 Search result: ", tuple(inverted_index[keywords.lower()].keys()))
    #     print("出现的文档数为：", len(inverted_index[keywords.lower()]))
    #     print("词频为：", get_all_frequency(keywords.lower()))
    # else:
    #     print("Not Found.")

