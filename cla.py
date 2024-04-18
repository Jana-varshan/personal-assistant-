import time
import math


class Clock:

    def draw_hand(self, can, angle, length, width=2, color='black', tag="", ):
        center_x, center_y = 380, 100
        end_x = center_x + length * math.cos(math.radians(angle))
        end_y = center_y - length * math.sin(math.radians(angle))

        can.create_line(center_x, center_y, end_x, end_y, width=width, fill=color, tags=tag)

    def update_clc(self, a):
        cur_t = time.localtime(time.time())
        hr = cur_t.tm_hour
        min = cur_t.tm_min
        sec = cur_t.tm_sec
        a.delete("clock_face", "hour_hand", "minute_hand", "second_hand")
        # a.create_oval(300, 5, 535, 240, outline="#EFE1D1", width=3, tags="clock_face")
        self.draw_hand(can=a, angle=90 - (hr % 12) * 30 - min / 2, length=105, width=3, color='#183D3D', tag="hour_hand")
        self.draw_hand(can=a, angle=90 - min * 6, length=90, width=3, color='#5C8374', tag="minute_hand")
        # self.draw_hand(can=a, angle=90 - sec * 6, length=70, width=2, color='#93B1A6', tag="second_hand")

        a.after(1000, self.update_clc, a)
        # self.update_clc(a)
