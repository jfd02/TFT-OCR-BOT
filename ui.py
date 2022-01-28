import ui_color
from win32gui import SetWindowLong, GetWindowLong, SetLayeredWindowAttributes
from win32con import WS_EX_LAYERED, WS_EX_TRANSPARENT, GWL_EXSTYLE
import tkinter as tk


class Ui:
    def __init__(self, message_queue):
        self.label_container = []
        self.message_queue = message_queue
        self.root = tk.Tk()
        self.root.geometry('1920x1080')
        self.root.overrideredirect(True)
        self.root.config(bg='#000000')
        self.root.attributes("-alpha", 1)
        self.root.wm_attributes("-topmost", 1)
        self.root.attributes('-transparentcolor', '#000000', '-topmost', 1)
        self.root.resizable(False, False)
        self.set_clickthrough(self.root.winfo_id())
        self.console = tk.Text(self.root, state='disabled', width=80, height=13, bg=ui_color.transparent,
                               fg=ui_color.console_text, font=("Consolas", 12, "bold"), bd=0)
        self.console.place(x=20, y=25)

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
            if 'CONSOLE' in message[0]:
                padding = "   "
                if 'Round' in message[1] or 'Queue' in message[1]:
                    padding = ""
                    self.console.configure(state='normal')
                    self.console.delete("1.0", "end")
                    self.console.configure(state='disabled')
                    for label in self.label_container:
                        label.destroy()
                    self.label_container.clear()

                self.console.configure(state='normal')
                self.console.insert(tk.END, f'{padding}{message[1]}' + '\n')
                self.console.configure(state='disabled')
                self.console.yview(tk.END)

            elif 'LABEL' in message[0]:
                for labels in message[1]:
                    label = tk.Label(self.root, text=f"{labels[0]}", bg=ui_color.transparent, fg=ui_color.console_text,
                                     font=("Consolas", 13, "bold"), bd=0)
                    label.place(x=labels[1][0] - 15, y=labels[1][1] + 30)
                    self.label_container.append(label)

        self.root.after(ms=1, func=self.consume_text)

    def ui_loop(self):
        self.consume_text()
        self.root.mainloop()
