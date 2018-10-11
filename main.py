import json
import re

"""
尝试做一个来必力的评论收集器
目前还没有写注释
@TODO 为parse函数添加异常处理代码
"""


def get_multiple_input():
    """
    从标准输入中获取多行输入，以空行为结束标志
    :return: 获取的输入，每行输入用'\n'连接，作为结束标志的空行不返回
    """
    lines = []
    for line in iter(input, ''):
        lines.append(line)
    return '\n'.join(lines)


def parse_list_query_payload(payload: str):
    payload = ''.join(payload.split('\n'))  # 如果响应负载为多行形式，将负载合并为一行
    data = payload.split('(', 1)[1].rstrip(');')  # 从响应负载中获取Json数据
    return data


def parse_list_query_json(data: str):
    return 2


def parse(data):
    try:
        root = json.loads(data)
    except json.decoder.JSONDecodeError:
        print('解析时似乎出现了错误')
    else:
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
    print('来必力评论采集工具v0.2')
    text = get_multiple_input()
    print(parse_list_query_payload(text))


if __name__ == '__main__':
    main()
