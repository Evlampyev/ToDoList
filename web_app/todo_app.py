from pywebio.input import input, TEXT
from pywebio import start_server
from pywebio.output import put_button, put_table, clear, use_scope
import logging

from database import my_list as myl, select_tasks, create_tasks_table
from database import create_connection, execute_query, execute_read_query


logging.basicConfig(level=logging.INFO)


def data():
    put_button("Добавить задачу", onclick=add_data, color="success", outline=True)
    put_button("Удалить задачу", onclick=delete_data, color='warning', outline=True)
    # put_button("Обновить", onclick=lambda: run_js('window.location.reload()'))
    put_button("Обновить", onclick=update, color='info', outline=True)
    put_table([elem for elem in myl])


def copy_data(table):
    myl.append(['id', 'Description'])
    for line in table:
        task = [line[0], line[1]]
        myl.append(task)


@use_scope('update', clear=True)
def update():
    global myl
    myl = []
    tasks = execute_read_query(connection, select_tasks)
    copy_data(tasks)
    data()


def add_data():
    """Добавление задачи"""
    task_description = input("Введите описание новой задачи: ", type=TEXT)
    index = input("Введите её номер: ", type=TEXT)
    add_task_table = f"""
       INSERT INTO
         `tasks` (`id`, `Description`)
       VALUES
         ('{index}', '{task_description}');"""
    execute_query(connection, add_task_table)



def delete_data():
    """Удаление задачи"""
    delete_id = input("Введите номер задачи, которую вы хотите удалить: ", type=TEXT)
    delete_task = f"DELETE FROM tasks WHERE id = '{delete_id}'"
    execute_query(connection, delete_task)


def run_process():
    execute_query(connection, create_tasks_table)
    update()


if __name__ == "__main__":
    connection = create_connection('my_tasks.sqlite')
    start_server(run_process, port=80)


