import easygui as sg

# 信息弹窗
sg.msgbox("这是一个提示消息")

# 确认弹窗
if sg.ynbox("是否继续？", choices=["是", "否"]):
    print("用户点击是")
else:
    print("用户点击否")

# 输入弹窗
name = sg.enterbox("请输入你的名字")
if name == "王楦博":
    print(f"{name},你好，傻逼")
else:
    print(f'你好,{name}')