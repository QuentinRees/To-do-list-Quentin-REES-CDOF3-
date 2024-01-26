# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 15:06:25 2024

@author: reesq
"""

import os
import pickle

class TodoList:
    def __init__(self):
        self.tasks = []

    def display_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added successfully.")

    def delete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            deleted_task = self.tasks.pop(task_index - 1)
            print(f"Task '{deleted_task}' deleted successfully.")
        else:
            print("Invalid task index.")

    def complete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            completed_task = self.tasks.pop(task_index - 1)
            print(f"Task '{completed_task}' completed.")
        else:
            print("Invalid task index.")

    def save_to_file(self, filename='todolist.pkl'):
        with open(filename, 'wb') as file:
            pickle.dump(self.tasks, file)
            print("Tasks saved successfully.")

    def load_from_file(self, filename='todolist.pkl'):
        if os.path.exists(filename):
            with open(filename, 'rb') as file:
                self.tasks = pickle.load(file)
                print("Tasks loaded successfully.")

def main():
    todo_list = TodoList()

    # Load tasks from file if available
    todo_list.load_from_file()

    while True:
        print("\nTodo List Application")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Complete Task")
        print("5. Save and Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            todo_list.display_tasks()
        elif choice == '2':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '3':
            task_index = int(input("Enter the task index to delete: "))
            todo_list.delete_task(task_index)
        elif choice == '4':
            task_index = int(input("Enter the task index to mark as complete: "))
            todo_list.complete_task(task_index)
        elif choice == '5':
            todo_list.save_to_file()
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
