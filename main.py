import tkinter as tk
from time import strftime
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Digital Clock")

# ==== Image load karna ====
image = Image.open(r"D:\work\Digtal_clock\img.jpg")
image = image.resize((500, 300))
bg_image = ImageTk.PhotoImage(image)

# ==== Canvas ====
canvas = tk.Canvas(root, width=500, height=300)
canvas.pack(fill="both", expand=True)

# Background image lagana
canvas.create_image(0, 0, image=bg_image, anchor="nw")

# ==== Time function ====
def time():
    canvas.delete("time_text")  # Purana text remove karo
    string = strftime('%H:%M:%S %p \n %D')
    canvas.create_text(250, 150, text=string, fill="white",
                       font=('calibri', 50, 'bold'),
                       tags="time_text")
    root.after(1000, time)

time()
root.mainloop()
