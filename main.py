import tkinter as tk

class TodoApp:
    def __init__(self, master):
        self.master = master
        master.title("To-Do List")

        self.tasks = []

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.listbox = tk.Listbox(master)
        self.listbox.pack()

        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()

    def add_task(self):
        task = self.entry.get()
        if task != "":
            self.tasks.append(task)
            self.listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)

    def delete_task(self):
        try:
            index = self.listbox.curselection()[0]
            del self.tasks[index]
            self.listbox.delete(index)
        except IndexError:
            pass

root = tk.Tk()
my_app = TodoApp(root)
root.mainloop()
