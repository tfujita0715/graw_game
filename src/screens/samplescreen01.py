# screen/screen01.py
import pyxel

class Screen01:
    def __init__(self):
        self.message = "This is sample"

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)
        pyxel.text(10, 10, self.message, 7)
