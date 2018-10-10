import json


def get_input():
    """
    从命令行获取输入
    """
    data = input()
    while 1:
        nxt = input()
        if nxt == '':
            break
        else:
            data = data + nxt
    return data


def parse(data):
    root = json.loads(data)
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
