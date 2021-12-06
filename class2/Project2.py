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




get_docu_dic()
get_words_list_and_set()
get_inverted_index()
# print(inverted_index)
get_words_frequency()
print(inverted_index)
# get_all_frequency()
inverted_index_to_json()

while(True):
    keywords = input("请输入关键词 Please input keywords: ")
    if keywords.lower() in inverted_index.keys():
        print("检索结果 Search result: ", tuple(inverted_index[keywords.lower()].keys()))
        print("出现的文档数为：", len(inverted_index[keywords.lower()]))
        print("词频为：", get_all_frequency(keywords.lower()))
    else:
        print("Not Found.")

