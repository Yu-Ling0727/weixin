import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

# 创建主窗口
root = tk.Tk()
root.withdraw()  # 隐藏主窗口

# 弹出消息提示框
messagebox.showinfo("提示", "这是一个弹窗消息")

# 弹出确认框（返回 True 或 False）
result = messagebox.askyesno("确认", "你确定要继续吗？")
print("用户选择：", result)

# 弹出输入框，获取用户输入
user_input = simpledialog.askstring("输入", "请输入你的名字：")
if user_input == "王楦博":
    print(f"{user_input},你好，傻逼")
else:
    print(f'你好，{user_input}')
# 关闭窗口
root.destroy()