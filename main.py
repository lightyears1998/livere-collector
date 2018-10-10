import json

"""
尝试做一个来必力的评论收集器
目前还没有写注释
@TODO 为parse函数添加异常处理代码
"""


def get_input():
    data = input()
    while 1:
        nxt = input()
        if nxt == '':
            break
        else:
            data = data + nxt
    return data


def parse(data):
    try:
        root = json.loads(data)
    except:
        print('解析时似乎出现了错误')
    results = root.get('results')
    parents = results.get('parents')
    children = results.get('children')
    for comment in parents:
        name = comment.get('name')
        content = comment.get('content')
        print(name, content)
    for comment in children:
        name = comment.get('name')
        content = comment.get('content')
        print(name, content)


def main():
    print('来必力评论收集器')
    parse(get_input())


if __name__ == '__main__':
    main()
