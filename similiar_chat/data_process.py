import json

from collections import defaultdict


def data_process(url):
    with open(url, 'r', encoding='UTF-8') as f:
        datas = json.load(f)

    input = []
    QA_dict = defaultdict()

    for data in datas:
        input.append(data.get('input'))
        QA_dict[data.get('input')] = data.get('output')

    return input, QA_dict


if __name__ == '__main__':
    inputList = data_process('./train.json')

    print(inputList)
