import ctypes
import time
import random
import math

class MouseSim:
    MOUSEEVENTF_LEFTDOWN   = 0x0002
    MOUSEEVENTF_LEFTUP     = 0x0004
    MOUSEEVENTF_RIGHTDOWN  = 0x0008
    MOUSEEVENTF_RIGHTUP    = 0x0010
    MOUSEEVENTF_MIDDLEDOWN = 0x0020
    MOUSEEVENTF_MIDDLEUP   = 0x0040
    MOUSEEVENTF_WHEEL      = 0x0800

    class POINT(ctypes.Structure):
        _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]

    def __init__(self, noise_range=3, base_delay=0.01):
        self.noise_range = noise_range
        self.base_delay = base_delay
        self.user32 = ctypes.windll.user32

    def get_position(self):
        pt = self.POINT()
        self.user32.GetCursorPos(ctypes.byref(pt))
        return pt.x, pt.y

    def ease_in_out(self, t):
        return -0.5 * (math.cos(math.pi * t) - 1)

    def move(self, x_target, y_target, steps=100):
        x_start, y_start = self.get_position()
        for i in range(steps):
            t = i / steps
            eased_t = self.ease_in_out(t)
            x = int(x_start + (x_target - x_start) * eased_t + random.uniform(-self.noise_range, self.noise_range))
            y = int(y_start + (y_target - y_start) * eased_t + random.uniform(-self.noise_range, self.noise_range))

            # Mikro geri çekilme
            if random.random() < 0.05:
                x -= random.randint(1,3)
                y -= random.randint(1,3)

            self.user32.SetCursorPos(x, y)
            time.sleep(self.base_delay + random.uniform(-self.base_delay/2, self.base_delay/2))

        self.user32.SetCursorPos(x_target, y_target)

    def left_click(self):
        self.user32.mouse_event(self.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        self.user32.mouse_event(self.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

    def right_click(self):
        self.user32.mouse_event(self.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
        self.user32.mouse_event(self.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)

    def middle_click(self):
        self.user32.mouse_event(self.MOUSEEVENTF_MIDDLEDOWN, 0, 0, 0, 0)
        self.user32.mouse_event(self.MOUSEEVENTF_MIDDLEUP, 0, 0, 0, 0)

    def double_click(self, interval=0.1):
        self.left_click()
        time.sleep(interval)
        self.left_click()

    def left_click_and_hold(self):
        self.user32.mouse_event(self.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)

    def left_release_click(self):
        self.user32.mouse_event(self.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

    def right_click_and_hold(self):
        self.user32.mouse_event(self.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)

    def right_release_click(self):
        self.user32.mouse_event(self.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)

    def scroll(self, amount):
        self.user32.mouse_event(self.MOUSEEVENTF_WHEEL, 0, 0, amount, 0)

    def drag_and_drop(self, x1, y1, x2, y2, steps=100):
        self.move(x1, y1, steps=steps//2)
        time.sleep(0.05)
        self.left_click_and_hold()
        time.sleep(0.05)
        self.move(x2, y2, steps=steps)
        time.sleep(0.05)
        self.left_release_click()
