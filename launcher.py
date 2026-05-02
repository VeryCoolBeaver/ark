import customtkinter as ctk
import random

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


app = ctk.CTk()
app.title("agario.launcher")
app.geometry("450x400")
app.resizable(False, False)


# ---------- TITLE ----------
title = ctk.CTkLabel(app, text="AGARIO LAUNCHER", font=("Arial", 24))
title.pack(pady=10)


# ---------- INPUTS ----------
nick = ctk.CTkEntry(app, placeholder_text="Ваш нік")
nick.pack(pady=5)

ip = ctk.CTkEntry(app, placeholder_text="IP")
ip.pack(pady=5)

port = ctk.CTkEntry(app, placeholder_text="Порт")
port.pack(pady=5)


# ---------- LOG ----------
log = ctk.CTkTextbox(app, height=80)
log.pack(pady=10)
log.insert("end", "Готовий до запуску...\n")


# ---------- RGB COLOR ----------
rgb = ctk.CTkEntry(app, placeholder_text="RGB (255,0,0)")
rgb.pack(pady=5)


def apply_color():
    try:
        r, g, b = map(int, rgb.get().split(","))
        color = f"#{r:02x}{g:02x}{b:02x}"

        title.configure(text_color=color)
        btn.configure(fg_color=color)

        log.insert("end", f"Колір змінено: {color}\n")
    except:
        log.insert("end", "Помилка RGB\n")


ctk.CTkButton(app, text="Застосувати колір", command=apply_color).pack(pady=5)


# ---------- THEME ----------
theme = ctk.CTkSwitch(app, text="Light / Dark",
                      command=lambda: ctk.set_appearance_mode("light" if theme.get() else "dark"))
theme.pack(pady=5)


# ---------- LOGIN ----------
def login():
    data = f"{nick.get()}|{ip.get()}|{port.get()}"

    if "|" in data and nick.get() and ip.get() and port.get():
        log.insert("end", f"Підключення: {data}\n")

        with open("server.txt", "w") as f:
            f.write(data)
    else:
        log.insert("end", "Заповни всі поля\n")


btn = ctk.CTkButton(app, text="УВІЙТИ", command=login)
btn.pack(pady=10)


# ---------- LOAD LAST SERVER ----------
try:
    with open("server.txt", "r") as f:
        n, i, p = f.read().split("|")
        nick.insert(0, n)
        ip.insert(0, i)
        port.insert(0, p)
except:
    pass


# ---------- SIMPLE ANIMATION (FLOATING DOTS) ----------
dots = []

for _ in range(6):
    d = ctk.CTkLabel(app, text="●", font=("Arial", 16), text_color="gray")
    d.place(x=random.randint(0, 400), y=random.randint(0, 350))
    dots.append(d)


def animate():
    for d in dots:
        x = d.winfo_x() + random.randint(-2, 2)
        y = d.winfo_y() + random.randint(-2, 2)

        if x < 0: x = 400
        if x > 400: x = 0
        if y < 0: y = 350
        if y > 350: y = 0

        d.place(x=x, y=y)

    app.after(50, animate)


animate()
app.mainloop()