import tkinter as tk
import platform
import shutil

def check_system():
    computer = platform.node()
    operating_system = platform.system()
    total, used, free = shutil.disk_usage("C:\\")
    result.config(
        text=f"Computer: {computer}\n"
        f"Operating System: {operating_system}\n"
        f"Free Disk Space: {free // (2**30)} GB"
    )
app = tk.Tk()
app.title("Mitch's IT Toolkit")
app.geometry("450x300")

heading = tk.Label(app, text="System Health Checker")
heading.pack(pady=20)

button = tk.Button (
app,
text="Check My Computer",
command=check_system
)
button.pack(pady=10)

result = tk.Label(app, text="Click the button to begin.")
result.pack(pady=20)

app.mainloop()