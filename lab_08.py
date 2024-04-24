# this is lab 8
# var 6.

from dataclasses import dataclass  # библиотека для определения класса данных с автоматизированными методами
from typing import List  # библиотека отображения типов данных и аннотаций функций


# Определение класс Задач
@dataclass(frozen=True)
class Task:
    id: int
    title: str
    description: str
    status: str


#  Определение класса Менеджера Задач


@dataclass
class TaskManager:
    tasks: List[Task]

    # Создание нового объекта класса Менеджера Задач
    def __new__(cls, *args, **kwargs):
        if 'tasks' not in kwargs:
            kwargs['tasks'] = []
        return super().__new__(cls)

    # Функция добавления новых задач в менеджер задач

    def add_task(self, title: str, description: str, status: str = "в процессе") -> 'TaskManager':
        new_task = Task(
            id=len(self.tasks) + 1,
            title=title,
            description=description,
            status=status
        )
        return TaskManager(tasks=self.tasks + [new_task])

    # Функция обновления статуса задач из созданного списка задач

    def update_task_status(self, task_id: int, status: str) -> 'TaskManager':
        updated_tasks = []
        for task_ in self.tasks:
            if task_.id == task_id:
                updated_task = Task(
                    id=task_.id,
                    title=task_.title,
                    description=task_.description,
                    status=status
                )
                updated_tasks.append(updated_task)
            else:
                updated_tasks.append(task_)
        return TaskManager(tasks=updated_tasks)

    # функция удаления задач

    def remove_task(self, task_id: int) -> 'TaskManager':
        updated_tasks = [task_ for task_ in self.tasks if task_.id != task_id]
        return TaskManager(tasks=updated_tasks)

    # функция для получения всех списков задач
    def get_all_tasks(self) -> List[Task]:
        return self.tasks

    # пример использования


if __name__ == "__main__":
    task_manager = TaskManager(tasks=[])  # новый менеджер задач
    # новый список  с добавлением новых задач
    task_manager = task_manager.add_task("Проснуться и позавтракать", "совершить утренние рутины")
    task_manager = task_manager.add_task("Собраться и прийти в универ", "прибыть на лекцию")

    tasks = task_manager.get_all_tasks()
    print("Список задач:")
    for task in tasks:
        print(f"ID: {task.id}, Заголовок: {task.title}, Статус: {task.status}")

    # обновленный список задач с изменеием статуса и добавлением новых задач
    task_manager = task_manager.update_task_status(1, "завершен")
    task_manager = task_manager.update_task_status(2, "завершен")
    task_manager = task_manager.add_task("Посмотреть видеоуроки по Django", "Изучить новые материалы")
    task_manager = task_manager.add_task("Доработать веб-проекта по Django",
                                         "Исправить ошибки и добавить новые функции")

    tasks = task_manager.get_all_tasks()
    print("\nСписок задач после добавления новых задач:")
    for task in tasks:
        print(f"ID: {task.id}, Заголовок: {task.title}, Статус: {task.status}")

    # удаление завершенных задач со списка
    task_manager = task_manager.remove_task(1)
    task_manager = task_manager.remove_task(2)

    # получение оканчательного обновленного списка задач

    tasks = task_manager.get_all_tasks()
    print("\nСписок задач после удаления завершенной задачи:")
    for task in tasks:
        print(f"ID: {task.id}, Заголовок: {task.title}, Статус: {task.status}")
