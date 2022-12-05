import tkinter as tk


def get_values():
    v1 = float(e1.get())
    v2 = float(e2.get())
    v3 = float(e3.get())
    v4 = float(e4.get())
    v5 = float(e5.get())
    v6 = float(e6.get())
    mission1 = v1 / v4
    mission2 = v2 / v5
    mission3 = v3 / v6
    max_mission = max(mission1, mission2, mission3)
    if max_mission == mission1:
        m_num = 1
    elif max_mission == mission2:
        m_num = 2
    else:
        m_num = 3
    lb = tk.Label(root, text=f"Best mission to do is number {m_num}", font=("Arial", 40))
    lb.pack(pady=30)


root = tk.Tk()
root.title("Hero Zero Energy Calculator")
root.geometry("800x400")
root.resizable(False, False)
frame1 = tk.Frame(root)
tk.Label(frame1, text="Enter mission one XP:", font=("Arial", 14)).grid(row=0, column=0)
tk.Label(frame1, text="Enter mission two XP:", font=("Arial", 14)).grid(row=1, column=0)
tk.Label(frame1, text="Enter mission three XP:", font=("Arial", 14)).grid(row=2, column=0)
e1 = tk.Entry(frame1)
e2 = tk.Entry(frame1)
e3 = tk.Entry(frame1)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
tk.Label(frame1, text="Enter mission one Energy:", font=("Arial", 14)).grid(row=0, column=3)
tk.Label(frame1, text="Enter mission two Energy:", font=("Arial", 14)).grid(row=1, column=3)
tk.Label(frame1, text="Enter mission three Energy:", font=("Arial", 14)).grid(row=2, column=3)
e4 = tk.Entry(frame1)
e5 = tk.Entry(frame1)
e6 = tk.Entry(frame1)
e4.grid(row=0, column=4)
e5.grid(row=1, column=4)
e6.grid(row=2, column=4)
frame1.pack(pady=10)
tk.Button(root, text="Calculate", font=("Arial", 20), command=lambda : get_values()).pack(pady=10)
tk.Button(root, text="Exit", font=("Arial", 20), command=root.destroy).pack(pady=10, side=tk.BOTTOM)


root.mainloop()