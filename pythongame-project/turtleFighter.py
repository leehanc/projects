import turtle
import math
import random
from time import sleep
### 1. 기본 설정
#화면 크기 설정
turtle.setup(800, 640)
# 땅 만들기
ground = turtle.Turtle()
ground.hideturtle()
ground.penup()
ground.goto(-300, -20)
ground.pendown()
ground.forward(600)




#앵그리 터틀 위치 및 이미지 설정
x = -280
y = 0
s = turtle.Screen() #####
s.bgpic(picname = "pythongame-project/image/background.gif")


# 타겟 설정
target = turtle.Turtle()
image1 = "pythongame-project/image/mon.gif"
s.addshape(image1)
target.shape(image1)
target.up()
target.goto(random.randrange(0, 290), 0) #랜덤위치

#플레이어 만들기
player = turtle.Turtle()
image = "pythongame-project/image/turtle.gif"
s.addshape(image)
player.shape(image)
player.up()
player.goto(x, y)
player.speed(1)
screen = player.getscreen()

# 남은 기회 위치 및 이미지 설정
image2 = "pythongame-project/image/small turtle.gif"
life1 = turtle.Turtle('circle')
s.addshape(image2)
life1.shape(image2)
life1.penup()
life2 = turtle.Turtle('circle')
s.addshape(image2)
life2.shape(image2)
life2.penup()
life3 = turtle.Turtle('circle')
s.addshape(image2)
life3.shape(image2)
life3.penup()
life1.goto(-300, 200)
life2.goto(-270, 200)
life3.goto(-240, 200)

# 방향표시 설정 (날라가는 방향 화살표로 표시)
arrow =turtle.Turtle()
arrow.shape("triangle")
arrow.penup()
arrow.goto(x+20, y+20)




#힘과 각도 출력할 터틀
strAngle = turtle.Turtle()
# 속도 및 각도 설정
velocity = 50
angle = 0




### 2. 함수 설정


# 힘과 각도 출력하는 함수
def drawText():
    global angle
    strAngle.clear()
    strAngle.hideturtle()
    strAngle.up()
    strAngle.goto(-320, 250)
    strAngle.write("power : " +   str(velocity))
    strAngle.goto(-320, 230)
    strAngle.write("angle : " +   str(angle))


# 각도 위로 올리는 함수
def turnleft():
    global angle
    if angle < 85:
        player.left(5)
        angle = player.heading()
        arrow.left(5)
        drawText() # 올릴때 마다 함수 실행
        
# 각도 내리는 함수
def turnright():
    global angle
    if angle > 5:
        player.right(5)
        angle = player.heading()
        arrow.right(5)
        drawText() # 올릴때 마다 함수 실행
        
# 파워 올리는 함수
def turnup():
    global velocity
    if velocity < 100:#힘제한 최대 100까지
        velocity = velocity + 2
        drawText() # 올릴때 마다 함수 실행
        
def turndown():
    global velocity
    if velocity > 50: #힘제한 최저 50까지
        velocity = velocity - 2
        drawText() # 올릴때 마다 함수 실행

        
# 시작시 힘과 각도 출력하는 함수
def init():
    drawText()


    
# 발사하는 함수
def fire():
    global x
    global y
    global velocity
    global angle
    vx = velocity * math.cos(angle * 3.14 / 180.0) # X 좌표 포물선
    vy = velocity * math.sin(angle * 3.14 / 180.0) # Y 좌표 포물선
    
    while True:
        vy = vy - 10
        x += vx
        y += vy
        
        if y < 0: # 거북이가 땅에 닿으면 시작위치로 돌아가기
            x -= vx
            y -= vy
            ty = y
            tv = 0.1
            
            while ty > 0:
                ty = y
                ty = ty + vy * tv
                tv = tv + 0.1
            x = x + vx * tv
            y = y + vy * tv
            break
        
        player.goto(x, y)
    player.goto(x, 1)
    sleep(1)#1초 멈추기
    
    # 타겟을 맞추면
    if player.distance(target) < 40:
        player.penup()
        player.goto(0,150)
        player.pendown()
        player.pencolor('blue')
        player.write('축하합니다', move=False, align='center', font=('Arial', 50))
        player.penup()

    # 못맞추면
    else:
        if life3.isvisible() == True:
            life3.hideturtle()
            player.goto(x, y)
        elif life3.isvisible() == False:
            if life2.isvisible() == True:
                 life2.hideturtle()
                 player.goto(x, y)
            else:
                 life1.hideturtle()
                 player.penup()
                 player.goto(0,150)
                 player.pendown()
                 player.pencolor('yellow')
                 player.write('바보', move=False, align='center', font=('Arial', 50))
                 player.penup()
                 
    #플레이어는 원래 위치로
    x = -280
    y = 0
    player.goto(x, y)







    
screen.onkeypress(turnleft, "Left")
screen.onkeypress(turnright, "Right")
screen.onkeypress(turnup, "Up")
screen.onkeypress(turndown, "Down")
screen.onkeypress(fire, "space")
screen.listen()
init()
turtle.mainloop()