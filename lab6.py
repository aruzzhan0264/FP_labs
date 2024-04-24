#   lab 6 var 6. 2nd solution

# импортировка нужных библиотек
import tkinter as tk
from rx.subject import Subject


# Функция для изменения значения слайдера
def changed_slider_value(value):
    slider_subject.on_next(value)


# Создаем графический интерфейс
root = tk.Tk()
root.title("Пример Слайдера")

# Создаем слайдер
my_slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL)
my_slider.pack(pady=100)

# Подписываемся на изменения слайдера
slider_subject = Subject()
slider_subject.subscribe(lambda value: label.config(text=f"текущее значение: {value}"))

my_slider.config(command=changed_slider_value)

label = tk.Label(root, text="исходное значение: 0")
label.pack()

# Запускаем главный цикл событий
root.mainloop()
