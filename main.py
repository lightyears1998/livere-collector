import json


def get_multiple_input(hint: str=''):
    """
    从标准输入中获取多行输入，以空行为结束标志
    :return: 获取的输入，每行输入用'\n'连接，作为结束标志的空行不返回
    """
    print(hint, end='')
    lines = []
    for line in iter(input, ''):
        lines.append(line)
    return '\n'.join(lines)


def resolve_list_api(payload: str):
    data = resolve_list_api_payload(payload)
    return resolve_list_api_json(data)


def resolve_list_api_payload(payload: str):
    payload = ''.join(payload.split('\n'))  # 如果响应负载为多行形式，将负载合并为一行
    data = payload.split('(', 1)[1].rstrip(');')  # 从响应负载中获取Json数据
    return data


def resolve_list_api_json(data: str):
    try:
        root = json.loads(data)
    except json.decoder.JSONDecodeError as e:
        print('解析Json数据时出现问题')
        print(e)
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
    print('来必力评论采集工具v0.3')
    text = get_multiple_input("在此处黏贴List API的响应:\n")
    resolve_list_api(text)


if __name__ == '__main__':
    main()
