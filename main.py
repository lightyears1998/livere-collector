import time
import re
import json
import tkinter as tk

intro = """v0.4只能提取评论中的作者和评论内容o(*￣▽￣*)ブ

使用步骤
=======
1. 打开含有来必力的网站，并启用开发人员工具
2. 切换到开发人员工具的网络选项卡，寻找一个以“list?callback=...”开头的GET请求
3. 单击这个请求，在右侧弹出的面板中选择“响应”选项卡
4. 将该请求的响应载荷（payload）复制到“解析”按钮上方的文本框中，按下“解析”按钮
"""


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


def deal_with_time(date: str):
    print(date)
    pattern = r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})T(?P<hour>\d{2}):(?P<minute>\d{2}):(?P<second>\d{2}).*'
    match = re.match(pattern, date)
    year = int(match.group('year'))
    month = int(match.group('month'))
    day = int(match.group('day'))
    hour = int(match.group('hour'))
    minute = int(match.group('minute'))
    second = int(match.group('second'))
    return None


def resolve_list_api(payload: str):
    list_api_json = get_list_api_json_from_payload(payload)
    ret = resolve_list_api_json(list_api_json)
    return ret


def get_list_api_json_from_payload(payload: str):
    payload = ''.join(payload.split('\n'))  # 如果响应负载为多行形式，将负载合并为一行
    data = payload.split('(', 1)[1].rstrip(');')  # 从响应负载中获取Json数据
    return data


def resolve_list_api_json(data: str):
    lines = []
    try:
        root = json.loads(data)
    except json.decoder.JSONDecodeError as e:
        lines.append('JSON数据的格式不正确')
        lines.append(e)
    else:
        results = root.get('results')
        parents = results.get('parents')
        children = results.get('children')
        for comment in parents:
            name = comment.get('name')
            date = comment.get('regdate')
            deal_with_time(date)
            content = comment.get('content')
            lines.append('\n'.join([name, content]))
        for comment in children:
            name = comment.get('name')
            content = comment.get('content')
            lines.append('\n'.join([name, content]))
    finally:
        return '\n\n'.join(lines)


def main():
    window = tk.Tk()
    window.title('来必力评论采集工具v0.4')
    window.geometry('480x320')

    payload_text = tk.Text(window, height=1)
    result_text = tk.Text(window)

    def on_button_click():
        result_text.delete('1.0', tk.END)
        result_text.insert(tk.END, resolve_list_api(payload_text.get('1.0', tk.END)))

    button = tk.Button(window, text='解析', command=on_button_click)

    result_text.insert(tk.END, intro)  # 向对话框中插入注释

    payload_text.pack()
    button.pack()
    result_text.pack()

    window.mainloop()


if __name__ == '__main__':
    main()
