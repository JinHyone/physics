from vpython import *


'''
	자유낙하운동 구현함.
'''


# 초기화
ball = sphere(radius=0.2)

ball.pos = vector(0, 3, 0) # 물체의 좌표 설정
ball.v = vector(0, 0, 0)   # 물체의 속도 설정
ball.a = vector(0, -2, 0)  # 물체의 가속도 설정(여기서는 중력가속도)


#  바닥
plate = box(width=5, height=0.3)
plate.rotate(3.141592 / 2, axis=vector(0, 1, 0))  # 라디안으로 회전
plate.pos = vector(0, -3, 0)

t = 0
dt = 0.016


def collision():
	r = ball.radius
	height = plate.height

	if ball.v.dot(ball.pos - plate.pos) > 0:  # 오류 방지를 위해서 멀어지면 충돌체크 x
		'''
			dot(내적) 연산: 두 벡터의 유사도를 구하는 연산(정확한 정의 아님)
			이를 이용하여 멀어지고 있는지, 가까워지고 있는지 판단 가능
		'''

		return

	if r + height > mag(ball.pos - plate.pos):
		ball.v *= -0.8  # 바닥과 충돌 구현


# 시뮬레이션
while True:
	rate(1 / dt)
	collision()

	ball.v += + ball.a * dt
	ball.pos += ball.v * dt

	t += dt

