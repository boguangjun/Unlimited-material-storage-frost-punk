import tkinter as tk
import pyautogui
import threading
import time
from pynput import mouse, keyboard

print('——————————————欢迎来到冰汽时代的赛博材料存储中心——————————————')
print('如果是2k分辨率的话，那添加就是2080*747，减少就是2155*776')
print("别的欢迎尝试")
print('两秒钟后自动开始')
print('按键ctrl+alt+del之后自动结束')





class AutoClickerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("鼠标连点器")
        self.master.geometry("300x400")
        

        self.click_rate = 0.5  # 设置点击速率（每秒点击次数）
        self.is_clicking = False
        self.click_positions = []

        self.record_button = tk.Button(self.master, text="记录点击位置", command=self.record_position)
        self.record_button.pack(pady=20)

        self.start_button = tk.Button(self.master, text="开始执行计划", command=self.delayed_start_clicking)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(self.master, text="停止点击", command=self.stop_clicking)
        self.stop_button.pack()

        frame1 = tk.Frame(self.master)
        frame1.pack()

        frame2 = tk.Frame(self.master)
        frame2.pack()

        self.x_label = tk.Label(frame1, text="X 坐标：")
        self.x_label.pack(side=tk.LEFT)
        self.x_input = tk.Entry(frame1)
        self.x_input.pack(side=tk.LEFT)
        self.x_input.insert(0, "2080")  # 默认值为 "2080"

        self.y_label = tk.Label(frame2, text="Y 坐标：")
        self.y_label.pack(side=tk.LEFT)
        self.y_input = tk.Entry(frame2)
        self.y_input.pack(side=tk.LEFT)
        self.y_input.insert(0, "747")  # 默认值为 "747"

        self.set_coord_button_1 = tk.Button(self.master, text="将资源存入建设工程保管库", command=self.set_coordinates_1)
        self.set_coord_button_1.pack()

        self.set_coord_button_2 = tk.Button(self.master, text="将资源取出建设工程保管库", command=self.set_coordinates_2)
        self.set_coord_button_2.pack()

        self.add_position_button = tk.Button(self.master, text="添加计划锁定", command=self.add_position)
        self.add_position_button.pack()

        # 监听全局快捷键
        self.listener = keyboard.GlobalHotKeys({'<ctrl>+<alt>+b': self.start_clicking, '<ctrl>+<alt>+m': self.stop_clicking})




    def record_position(self):
        x, y = pyautogui.position()
        self.click_positions.append((x, y))
        print(f"记录点击位置：({x}, {y})")


    def set_coordinates_1(self):
        self.x_input.delete(0, tk.END)
        self.y_input.delete(0, tk.END)
        self.x_input.insert(0, "2080")
        self.y_input.insert(0, "747")

    def set_coordinates_2(self):
        self.x_input.delete(0, tk.END)
        self.y_input.delete(0, tk.END)
        self.x_input.insert(0, "2155")
        self.y_input.insert(0, "776")
        
    def add_position(self):
        try:
            x = int(self.x_input.get())
            y = int(self.y_input.get())
            self.click_positions.append((x, y))
            print(f"已添加坐标：({x}, {y})")
        except ValueError:
            print("请输入有效的坐标")


    def delayed_start_clicking(self):
        self.click_timer = threading.Timer(3, self.start_clicking)  # 2秒后执行start_clicking
        self.click_timer.start()


    def start_clicking(self):
        self.is_clicking = True
        self.click_thread = threading.Thread(target=self.click)
        self.click_thread.daemon = True  # 将点击线程设置为后台线程
        self.click_thread.start()


    def stop_clicking(self):
        self.is_clicking = False

    def click(self):
        while self.is_clicking:
            for position in self.click_positions:
                if not self.is_clicking:
                    break
                pyautogui.click(position[0], position[1])
                #time.sleep(0.00000001)


def main():
    root = tk.Tk()
    autoclicker_app = AutoClickerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()





    
    
