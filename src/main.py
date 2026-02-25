import pyxel
from screens import Screen01

class App:
    def __init__(self):
        pyxel.init(256, 256, title="graw Game")
        
        self.screen = Screen01()
        pyxel.run(self.update, self.draw)

    def update(self):
        # 現在の画面（Screen01など）の更新処理を呼び出す
        self.screen.update()

    def draw(self):
        # 現在の画面（Screen01など）の描画処理を呼び出す
        self.screen.draw()

def main():
    App()
    print("Game Started!")

if __name__ == "__main__":
    main()