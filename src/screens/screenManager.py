import pyxel

#画面インポート
from .sampleScreen01 import Screen01


#現在mainから01を直接呼んでいます。将来的にここから画面遷移を行いま。

def get_screen(screen_name): # クラスの外に置く
    if screen_name == "01":
        return Screen01()
    elif screen_name == "id":
        return "dammy"
    else:
        return None