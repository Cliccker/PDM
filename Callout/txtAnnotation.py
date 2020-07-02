from openpyxl import load_workbook
import json


def readXlsx():  # 读取xlsx文件创建标注字典

    form = load_workbook(r'../data/taggedDicts/压力容器字典构建.xlsx')
    idxDict = {}
    sheet = form["Sheet2"]
    for i in sheet.columns:
        cols = []
        for j in i:
            if j.value != 0:
                cols.append(j.value)
        for term in cols[3:]:
            idxDict[term] = cols[0:3]

    return (idxDict)


def Mark(magazine):
    print("开始标注……")
    procPath = '../data/Processed/' + magazine + '_proc.txt'
    jsonPath = '../data/Processed/' + magazine + '_marked.json'
    input_file = open(procPath, 'r', encoding='utf-8')
    lines = input_file.readlines()
    idxDict = readXlsx()
    txtAftLabeling = []
    for line in lines:
        words = line.split(' ')
        count = 0
        for word in words:
            wordDict = {'id': count, 'word': word}
            if word in idxDict.keys():
                wordDict['seg'] = 'vn'  # 特殊名词
                wordDict['type0'] = idxDict[word][0]
                wordDict['type1'] = idxDict[word][1]
                wordDict['type2'] = idxDict[word][2]
                txtAftLabeling.append([wordDict])
            else:
                wordDict['seg'] = 'n'  # 未标记名词
                txtAftLabeling.append([wordDict])

            count += 1
        with open(jsonPath, 'w', encoding='utf-8') as f:
            json.dump(txtAftLabeling, f, ensure_ascii=False)
    print('标注完成')

Mark('压力容器')
