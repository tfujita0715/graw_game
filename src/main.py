import pyxel
from screens import Screen01

class App:
    def __init__(self):
        # 1. initは1回。サイズも固定する
        pyxel.init(256, 256, title="grow Game")
        pyxel.mouse(True)
        
        # 2. 最初は None（空）にしておき、落ちないように対策する
        self.screen = None
        
        pyxel.run(self.update, self.draw)

    def update(self):
        # 画面がセットされている時だけ更新する
        if self.screen is not None:
            self.screen.update()
            
        # 3. カッコをつけて実体を作る（インスタンス化）
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.screen = Screen01() 

    def draw(self):
        pyxel.cls(0)
        if self.screen is not None:
            self.screen.draw()
        else:
            # 起動直後の画面
            pyxel.text(80, 120, "PRESS SPACE TO START", 7)

def main():
    print("Game Started!")
    App()

if __name__ == "__main__":
    main()