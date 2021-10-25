from tkinter import *
from tkinter import ttk
import numpy as np
import time


def show(n: int, data: list, colours: list):

    canvas.delete('all')


    width = 1560 / (3 * n - 1)


    gap = width / 2

    for i in range(n):

        canvas.create_rectangle(7 + i * width + i * gap, 0, 7 +
                                (i + 1) * width + i * gap, data[i],
                                fill=colours[i])


    win.update_idletasks()


def shuffle():
    np.random.shuffle(arr)
    show(N, arr, color)


def mergesort(arr, left, right):
    if left < right:
        m = (left + right) // 2
        mergesort(arr, left, m)
        mergesort(arr, m + 1, right)

        j = m + 1
        if arr[m] <= arr[m + 1]:
            return

        while left <= m and j <= right:
            show(N, arr, ['blue' if x == left or x ==
                                    j else 'grey' for x in range(N)])
            time.sleep(1 / speed)
            if arr[left] <= arr[j]:
                left += 1
            else:
                show(N, arr, ['red' if x == left or x ==
                                       j else 'grey' for x in range(N)])


                time.sleep(1 / speed)
                temp = arr[j]


                i = j
                while i != left:
                    arr[i] = arr[i - 1]
                    show(N, arr, ['red' if x == i or x ==
                                           j else 'grey' for x in range(N)])
                    time.sleep(1 / speed)
                    i -= 1


                arr[left] = temp

                show(N, arr, ['green' if x == left or x ==
                                         j else 'grey' for x in range(N)])
                time.sleep(1 / speed)
                left += 1
                m += 1
                j += 1



def start():
    mergesort(arr, 0, N - 1)
    show(N, arr, ['purple' for _ in range(N)])


win = Tk()

N = 50
speed = 100


arr = np.linspace(10, 390, N, dtype=np.uint16)

color = ['grey' for _ in range(N)]

ttk.Label(win, text='Merge Sort visualizer').pack()
canvas = Canvas(win, width=800, height=400, bg='white')
canvas.pack()

ttk.Button(win, text='Start sorting', command=start).pack(
    side='right', padx=5, pady=5)

ttk.Button(win, text='Shuffle array', command=shuffle).pack(side='right')
shuffle()
show(N, arr, color)

win.mainloop()
