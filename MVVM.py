import tkinter as tk

class Model:
    def __init__(self):
        self._data = 0

    def get_data(self):
        return self._data

    def set_data(self, new_data):
        self._data = new_data
        self.notify()

    def bind_to(self, callback):
        self.notify = callback


class ViewModel:
    def __init__(self, model):
        self.model = model
        self.view = None

    def set_view(self, view):
        self.view = view

    def update_data(self, new_data):
        self.model.set_data(new_data)

    def data_changed(self):
        if self.view:
            new_data = self.model.get_data()
            self.view.update(new_data)


class View:
    def __init__(self, master, view_model):
        self.master = master
        self.view_model = view_model
        self.entry = tk.Entry(master)
        self.button = tk.Button(master, text="Update", command=self.update_model)
        self.label = tk.Label(master, text="Data: 0")

        self.entry.pack()
        self.button.pack()
        self.label.pack()

        self.view_model.set_view(self)

    def update_model(self):
        new_data = int(self.entry.get())
        self.view_model.update_data(new_data)

    def update(self, new_data):
        self.label.config(text=f"Data: {new_data}")


root = tk.Tk()
model = Model()
view_model = ViewModel(model)
view = View(root, view_model)
model.bind_to(view_model.data_changed)

root.mainloop()