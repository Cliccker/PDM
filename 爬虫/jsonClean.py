import json


def json_extraction():
    dictList = []
    magazine = "压力容器"
    path = '../data/srcData/' + magazine + '_data.json'
    dp = '../data/Dicts/' + magazine + '_dict.txt'

    content = json.load(open(path, 'r', encoding='utf-8'))  # 读取json文件
    for paper in content:
        for word in paper[0]['keywords']:
            dictList.append(word)
    dictList = set(dictList)  # 去重
    file = open(dp, 'w', encoding='utf-8')
    count = 1
    for i in dictList:
        count += 1
        file.write(i)
        file.write('\n')
    print('共有%d个关键词' % count)
    print("保存完毕")


if __name__ == '__main__':
    json_extraction()
