import pandas as pd

# 逆转排序，方便处理数据
def reverse(*args):
    new_col = []
    for i in args:
        j = i[::-1]
        new_col.append(j)
    return new_col


magazine = "压力容器"
path = './data/' + magazine + '.csv'
new_file = './data/' + magazine + '_sorted.csv'
content = pd.read_csv(path)
titles = list(content)
dict = {}
for i in range(len(titles)):
    title = titles[i]
    columns = content[title].tolist()  # 读取行并转化为列表
    columns = [incom for incom in columns if str(incom) != 'nan']  # 去除nan字符
    columns = reverse(*columns)
    columns.sort()
    columns = reverse(*columns)
    dict[str(title)] = columns
print(dict)
new_data = pd.DataFrame.from_dict(dict, orient='index')
new_data.to_csv(new_file, encoding='utf_8_sig')  # 防止出现乱码
