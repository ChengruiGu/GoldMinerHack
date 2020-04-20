import webbrowser
import win32gui, win32api, win32con
import GMconst, target
from PIL import ImageGrab, Image
import time
# https://www.cnblogs.com/reader/p/10111777.html
# https://www.jianshu.com/p/c20adfa72733



def open_game():
    '''Open the game on 4399'''
    webbrowser.open("http://www.4399.com/flash/1602.htm")
    
class GMhack:

    def __init__(self, wdname):
        self.hwnd = win32gui.FindWindow(0, wdname)
        if not self.hwnd:
            print("窗口找不到，请确认窗口句柄名称：【%s】" % wdname )
            exit()
         
        win32gui.SetForegroundWindow(self.hwnd)

    def screenshot(self):
        image = ImageGrab.grab(GMconst.game_coordinates)
        return image
        
    def mine(self):
        win32api.SendMessage(self.hwnd, win32con.WM_KEYDOWN, 40, 0)
        win32api.SendMessage(self.hwnd, win32con.WM_KEYUP, 40, 0)

    def start(self):
        while True:
            #self.screenshot()
            self.mine()
    
    
if __name__ == '__main__':
    # wdname = u'黄金矿工中文版小游戏,在线玩,4399小游戏 4399.com - Google Chrome'
    demo = GMhack(GMconst.wdname)
    demo.start()