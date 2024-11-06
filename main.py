class ToDoList:
    type = {}

    def __init__(self):
        self.todolist = {}

    def add_task(self, task):
        self.todolist[task] = 'not completed'

    def complete_task(self, task):
        if task not in self.todolist:
            print(f'Задачи {task} в списке нет')
        else:
            self.todolist[task] = 'completed'

    def remove_task(self, task):
        if task not in self.todolist:
            print(f'Задачи {task} в списке нет')
        else:
            del self.todolist[task]

    def list_tasks(self):
        print(self.todolist, sep='\n')


cleaning = ToDoList()

cleaning.add_task('vacuum')
cleaning.add_task('floors')
cleaning.add_task('wash')
cleaning.add_task('dust')

cleaning.complete_task('vacuum')
cleaning.complete_task('wash')
cleaning.complete_task('dishes')

cleaning.remove_task('dust')
cleaning.remove_task('dishes')

cleaning.list_tasks()
