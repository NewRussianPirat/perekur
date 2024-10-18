import tkinter as tk
import cv2
import time
import threading

running = False


def show_image(interval):
    global running
    while running:

        image = cv2.imread('img\\perekur.jpg')

        for _ in range(int(interval * 10)):
            if not running:
                return
            time.sleep(0.1)

        cv2.namedWindow('Перекур', cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty('Перекур', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.setWindowProperty('Перекур', cv2.WND_PROP_TOPMOST, 1)
        cv2.imshow('Перекур', image)

        cv2.waitKey(0)
        cv2.destroyAllWindows()


def start_showing():
    global running
    running = True
    interval = float(interval_entry.get())
    threading.Thread(target=show_image, args=(interval,)).start()


def stop_showing():
    global running
    running = False


def on_closing():
    global running
    running = False
    root.destroy()


root = tk.Tk()
root.title("Перекур")
root.geometry("600x338")

description_label = tk.Label(root,
                             text='''Напоминает делать перекур через время
Перекур длится сколько захотите, по его завершении таймер обновится
Для завершения перекура нажмите любую кнопку на клавиатуре
Кнопка "Запустить" начинает цикл перекура
Кнопка "Остановить" останавливает цикл''')
description_label.pack(pady=10)

interval_label = tk.Label(root, text="Интервал (секунды):")
interval_label.pack(pady=5)
interval_entry = tk.Entry(root)
interval_entry.pack(pady=5)
interval_entry.insert(0, "5")  # Устанавливаем значение по умолчанию

start_button = tk.Button(root, text="Запустить", command=start_showing)
start_button.pack(pady=10)

stop_button = tk.Button(root, text="Остановить", command=stop_showing)
stop_button.pack(pady=10)

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
