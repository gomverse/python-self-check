"""
opencv와 numpy를 이용해서 점을 선으로 잇는 프로그램
"""

import numpy as np
from random import randint
import cv2 as cv


# 마우스 콜백 함수
def draw_circle(event, x, y, flags, previous_locate):

    # flags 예시: if event == cv2.EVENT_LBUTTONDOWN and flags != cv2.EVENT_FLAG_SHIFTKEY:
    if event == cv.EVENT_LBUTTONDOWN:
        # 전역 변수 img 사용
        # Numpy is mutable
        cv.circle(
            img,
            (x, y),
            10,
            (randint(0, 255), randint(0, 255), randint(0, 255)),
            -1,
        )

        if click_number[0] != 0:
            # 선을 그리는 코드
            cv.line(
                img,
                previous_locate[0],
                (x, y),
                (randint(0, 255), randint(0, 255), randint(0, 255)),
                2,
            )
            pass

        # 현재 좌표를 이전 좌표 변수에 저장
        previous_locate[0] = (x, y)

        # 클릭 횟수를 저장
        click_number[0] += 1
        print("점의 개수 = ", click_number[0])


# 검은 바탕 화면을 만들기
img = np.full((512, 512, 3), (0, 0, 0), dtype=np.uint8)  # BGR

cv.namedWindow("Image")  # 창(Window)의 이름 주의

# 이전 좌표와 클릭 횟수를 기록할 변수
previous_locate = [(0, 0)]
click_number = [0]

# 마우스 이벤트 콜백 연결
cv.setMouseCallback("Image", draw_circle, previous_locate)

while True:

    cv.imshow("Image", img)

    if cv.waitKey(20) == ord("q"):
        break

cv.destroyAllWindows()
