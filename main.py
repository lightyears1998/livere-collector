import json
import tkinter as tk

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
    list_api_json = get_list_api_json_from_payload(payload)
    return resolve_list_api_json(list_api_json)


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

    payload_text.pack()
    button.pack()
    result_text.pack()

    window.mainloop()


if __name__ == '__main__':
    main()
