from win32gui import SetWindowLong, GetWindowLong, SetLayeredWindowAttributes
from win32con import WS_EX_LAYERED, WS_EX_TRANSPARENT, GWL_EXSTYLE
import screeninfo
import tkinter as tk

class Ui:

    def __init__(self, message_queue):
        self.champ_text = Ui.rgb_convert((255, 255, 255))
        self.transparent = Ui.rgb_convert((0, 0, 0))
        self.label_container = []
        self.message_queue = message_queue
        self.root = tk.Tk()
        self.setup_window_size()
        self.root.overrideredirect(True)
        self.root.config(bg='#000000')
        self.root.attributes("-alpha", 1)
        self.root.wm_attributes("-topmost", 1)
        self.root.attributes('-transparentcolor', '#000000', '-topmost', 1)
        self.root.resizable(False, False)
        self.set_clickthrough(self.root.winfo_id())

    @classmethod
    def rgb_convert(cls, rgb):
        return "#%02x%02x%02x" % rgb

    def setup_window_size(self):
        primary_monitor = None
        for monitor in screeninfo.get_monitors():
            if monitor.is_primary:
                primary_monitor = monitor
                break

        if primary_monitor is None:
            print("No primary monitor found... Using 1920x1080")
            self.root.geometry("1920x1080")
            return
        self.root.geometry(f'{primary_monitor.width}x{primary_monitor.height}')

    def set_clickthrough(self, hwnd):
        try:
            styles = GetWindowLong(hwnd, GWL_EXSTYLE)
            styles = WS_EX_LAYERED | WS_EX_TRANSPARENT
            SetWindowLong(hwnd, GWL_EXSTYLE, styles)
            SetLayeredWindowAttributes(hwnd, 0, 255, 0x00000001)
        except Exception as e:
            print(e)

    def consume_text(self):
        if self.message_queue.empty() is False:

            message = self.message_queue.get()
            if 'CLEAR' in message:
                for label in self.label_container:
                    label.destroy()
                self.label_container.clear()
            else:
                for labels in message[1]:
                    label = tk.Label(self.root, text=f"{labels[0]}", bg=self.transparent, fg=self.champ_text,
                                        font=("Yu Gothic UI Semibold", 13), bd=0)
                    label.place(x=labels[1][0] - 15, y=labels[1][1] + 30)
                    self.label_container.append(label)

        self.root.after(ms=1, func=self.consume_text)

    def ui_loop(self):
        self.consume_text()
        self.root.mainloop()
