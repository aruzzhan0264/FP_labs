#  var 6. lab 6 another solution

# импортировка нужных библиотек
import tkinter as tk
from rx.subject import Subject

# Создаем Subject для слайдера
slider_subject = Subject()


# Функция для изменения значения слайдера
def change_slider_value(value):
    slider_subject.on_next(value)


# Создаем функцию-обработчик изменения слайдера
def on_slider_change(value):
    print(f"Текущее значение слайдера: {value}")


# Подписываемся на изменения слайдера
slider_subject.subscribe(on_next=on_slider_change)

# Создаем графический интерфейс
root = tk.Tk()
root.title("Пример Слайдера")

# Создаем слайдер
slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=change_slider_value)
slider.pack(pady=10)

# Запускаем главный цикл событий
root.mainloop()