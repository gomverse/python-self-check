from tkinter import *
from tkinter import colorchooser


class MyPaint(Tk):
    def __init__(self):
        super().__init__()

        self.title("My Paint")

        self.width = 3  # 초기 펜 두께
        self.pen_color = "blue"  # 초기 펜 색상
        self.bg_color = "white"  # 초기 배경색
        self.old_x = None  # 선을 그리기 위해 이전 좌표를 기억
        self.old_y = None
        self.undo_trigger = False  # 이전에 그렸던 선들의 좌표를 기억하기 위한 트리거
        self.undo_memory = []  # 이전에 그렸던 좌표를 기억
        self.redo_memory = []  # undo로 지운 좌표를 기억

        # 메뉴 프레임
        self.controls = Frame(self, padx=5, pady=5)

        # 펜 두께 슬라이더와 색 변경 버튼 추가
        self.slider = Scale(
            master=self.controls,
            from_=1,
            to=30,
            command=self.change_width,
            orient=HORIZONTAL,
        )
        self.slider.set(10)
        self.slider.pack(side=LEFT, fill="x", expand=True)

        # 펜 색상 설정 버튼
        self.color = Button(
            master=self.controls, text="펜색 설정", command=self.change_color
        )
        self.color.pack(side=LEFT, fill="x", expand=True)

        # 배경색 설정 버튼
        self.set_bgcolor = Button(
            master=self.controls, text="배경색 설정", command=self.change_bgcolor
        )
        self.set_bgcolor.pack(side=LEFT, fill="x", expand=True)

        # 초기화 버튼
        self.eraser = Button(master=self.controls, text="초기화", command=self.eraser)
        self.eraser.pack(side=LEFT, fill="x", expand=True)

        # 저장 버튼
        self.save = Button(master=self.controls, text="저장하기", command=self.save)
        self.save.pack(side=LEFT, fill="x", expand=True)

        # Undo 버튼
        self.undo = Button(master=self.controls, text="Undo", command=self.undo)
        self.undo.pack(side=LEFT, fill="x", expand=True)

        # Redo 버튼
        self.redo = Button(master=self.controls, text="Redo", command=self.redo)
        self.redo.pack(side=LEFT, fill="x", expand=True)

        # Canvas 생성
        self.canvas = Canvas(self, width=512, height=384, bg=self.bg_color)

        # 마우스 이벤트 연결
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.reset_xy)
        self.canvas.bind("<Button-1>", self.clicked)

        # 배치
        self.controls.pack(fill=BOTH, expand=True)
        self.canvas.pack(fill=BOTH, expand=True)

    # 펜 두께 변경
    def change_width(self, e):
        self.width = e

    # 펜 색상 변경
    def change_color(self):
        self.pen_color = colorchooser.askcolor(
            color=self.pen_color, title="Choose color"
        )[1]

    # 배경색 변경
    def change_bgcolor(self):
        self.bg_color = colorchooser.askcolor(
            color=self.pen_color, title="Choose color"
        )[1]
        self.canvas.config(bg=self.bg_color)

    # 초기화 기능
    def eraser(self):
        self.canvas.delete("all")

    # 저장 기능
    def save(self):
        self.canvas.postscript(file="output.eps")
        img = Image.open("output.eps")
        img.save("output.png", "png")

    # 그리기 기능
    def draw(self, e):
        if self.old_x and self.old_y:
            self.canvas.create_line(
                self.old_x,
                self.old_y,
                e.x,
                e.y,
                width=self.width,
                fill=self.pen_color,
                capstyle=ROUND,
                smooth=True,
            )

        self.old_x = e.x
        self.old_y = e.y

        self.undo_memory.append((self.old_x, self.old_y))

    # 마우스 버튼을 땠을 때
    def reset_xy(self, e):
        self.old_x = None
        self.old_y = None
        self.undo_trigger = False

    # 마우스 버튼을 눌렀을 때
    def clicked(self, e):
        self.undo_trigger = True
        self.undo_memory.clear()

    # Undo 기능
    def undo(self):
        if self.undo_memory:
            redo_items = []
            for x, y in self.undo_memory:
                items = self.canvas.find_overlapping(x, y, x, y)
                for item in items:
                    redo_items.append((item, self.canvas.coords(item)))
                    self.canvas.delete(item)
                self.redo_memory.append(redo_items)

    # Redo 기능
    def redo(self):
        if self.redo_memory:
            items = self.redo_memory.pop()
            for t, coords in items:
                self.canvas.create_line(
                    *coords,
                    width=self.width,
                    fill=self.pen_color,
                    capstyle=ROUND,
                    smooth=True
                )


if __name__ == "__main__":
    MyPaint().mainloop()
