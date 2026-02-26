import pyxel
#画面の基底クラス共通の機能、初期化

class Setting():
    def __init__(self):
        self.number = False
    def update_common(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            if 0 <= pyxel.mouse_x <= 64 and 0 <= pyxel.mouse_y <= 64:
                self.number = True
    def draw_common(self):
        pyxel.rect(0, 0, 64, 64, 8) # x, y, w, h, col
