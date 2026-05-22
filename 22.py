import turtle

# 设置画笔
t = turtle.Turtle()
t.speed(3)
t.color('red', 'pink')  # 线条颜色和填充颜色
turtle.bgcolor('white')

# 开始绘制爱心
t.penup()
t.goto(0, -100)  # 调整起点位置
t.pendown()

t.begin_fill()  # 开始填充

# 画左半边的曲线
t.left(140)
t.forward(224)
for _ in range(200):
    t.right(1)
    t.forward(2)

# 画右半边的曲线
t.left(120)
for _ in range(200):
    t.right(1)
    t.forward(2)

t.forward(224)
t.end_fill()

# 完成
t.hideturtle()
turtle.done()