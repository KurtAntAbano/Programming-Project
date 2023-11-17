import tkinter as tk
from tkinter import ttk

root = tk.Tk()


def on_get_index_clicked():
    # Get the selected index
    selected_iid = tv_test.focus()

    item_index = tv_test.index(selected_iid)
    print(item_index)


tv_test = ttk.Treeview(root, show="tree")
btn_move = ttk.Button(root, text="Get index", command=on_get_index_clicked)

tv_test.pack(expand=True, fill=tk.BOTH)
btn_move.pack()

tv_test.insert(parent="", index="end", text="Test1")
tv_test.insert(parent="", index="end", text="Test2")
tv_test.insert(parent="", index="end", text="Test3")

root.mainloop()