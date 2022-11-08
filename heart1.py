from turtle import *
from math import sqrt
import random
width, height = 800, 600
screen = Screen()     # 创建窗口对象
screen.setup(width, height)    # 设置窗口的宽高
screen.delay(0)    # 设置无延时绘画
screen.bgcolor('pink')     # 设置背景颜色为粉色

# # 设置画笔的统一属性
# t = Turtle(visible=False, shape='circle')
# t.shapesize(10, 10)
# t.pencolor('red')
# t.fillcolor('red')
# t.penup()
# # 克隆一个圆形，设置位置
# circle1 = t.clone()
# circle1.goto(-sqrt(10*10*160)/2, 0)
# # 克隆第二个圆形，设置位置
# circle2 = t.clone()
# circle2.goto(sqrt(10*10*160)/2, 0)
# # 克隆一个正方形，设置位置并旋转角度
# square = t.clone()
# square.shape("square")
# square.setheading(45)
# square.goto(0, -sqrt(10*10*160)/2)
# # 显示图形
# circle1.showturtle()
# circle2.showturtle()
# square.showturtle()
# done()
class Heart:
    def __init__(self, x, y, size):
        self.size = size    # 心形大小
        self.speed = size    # 移动速度根据大小变化
        t = Turtle(visible=False, shape='circle')
        t.shapesize(size, size)
        color = (1, 1- size/4, 1-size/4)     # 颜色修改为根据大小变化的粉色
        t.pencolor(color)
        t.fillcolor(color)
        t.penup()
        t.write('暴富',font=("Verdana", 40, "bold"))
        self.circle1 = t.clone()
        self.circle1.goto(x-sqrt(size*size*160)/2, y)
        self.circle2 = t.clone()
        self.circle2.goto(x+sqrt(size*size*160)/2, y)
        self.square = t.clone()
        self.square.shape("square")
        self.square.setheading(45)
        self.square.goto(x, y-sqrt(size * size * 160)/2)
        self.circle1.showturtle()
        self.circle2.showturtle()
        self.square.showturtle()
    def move(self):
        self.circle1.setx(self.circle1.xcor()-self.speed)
        self.square.setx(self.square.xcor() - self.speed)
        self.circle2.setx(self.circle2.xcor() - self.speed)

    def moveTo(self, x, y):

    # 隐藏形状后再移动防止看到移动轨迹
        self.circle1.hideturtle()
        self.circle2.hideturtle()
        self.square.hideturtle()
    # 移动到指定位置
        self.circle1.goto(x - sqrt(self.size * self.size * 160) / 2, y)
        self.circle2.goto(x + sqrt(self.size * self.size * 160) / 2, y)
        self.square.goto(x, y - sqrt(self.size * self.size * 160) / 2)
    # 恢复显示
        self.circle1.showturtle()
        self.circle2.showturtle()
        self.square.showturtle()
hearts = []
for i in range(25):
    heart = Heart(width/2 + random.randint(1, width), random.randint(-height/2, height/2), random.random()*3)
    hearts.append(heart)
while True:
    for heart in hearts:
        heart.move()
        if heart.square.xcor() < -width / 2:     # 如果爱心移动出屏幕左侧
            heart.moveTo(width / 2 + random.randint(1, width), random.randint(-height / 2, height / 2))   # 回到右侧随机位置

