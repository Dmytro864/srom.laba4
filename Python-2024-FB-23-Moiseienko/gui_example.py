import tkinter as tk
from tkinter import ttk

# Функція для обчислення результатів
def calculate():
    try:
        A = entry_A.get()
        B = entry_B.get()
        N = entry_N.get()

        # Конвертація введених даних у числа
        A = int(A, 16)
        B = int(B, 16)
        N = int(N, 16)

        # Виконання обчислень
        result_add = hex((A + B) % N)
        result_mult = hex((A * B) % N)
        result_square = hex((A**2) % N)

        # Оновлення результатів
        result_A_plus_B.config(text=f"A + B = {result_add}")
        result_A_times_B.config(text=f"A * B = {result_mult}")
        result_A_square.config(text=f"A^2 = {result_square}")
    except ValueError:
        result_A_plus_B.config(text="Помилка: перевірте введені дані!")
        result_A_times_B.config(text="")
        result_A_square.config(text="")

# Створення головного вікна
root = tk.Tk()
root.title("Обчислення з модулем N")

# Розташування елементів
label_A = tk.Label(root, text="A =", font=("Arial", 12))
label_A.grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_A = tk.Entry(root, font=("Arial", 12))
entry_A.grid(row=0, column=1, padx=5, pady=5)

label_B = tk.Label(root, text="B =", font=("Arial", 12))
label_B.grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_B = tk.Entry(root, font=("Arial", 12))
entry_B.grid(row=1, column=1, padx=5, pady=5)

label_N = tk.Label(root, text="N =", font=("Arial", 12))
label_N.grid(row=2, column=0, padx=5, pady=5, sticky="e")
entry_N = tk.Entry(root, font=("Arial", 12))
entry_N.grid(row=2, column=1, padx=5, pady=5)

# Кнопка для обчислення
btn_calculate = tk.Button(root, text="Обчислити", font=("Arial", 12), command=calculate)
btn_calculate.grid(row=3, column=0, columnspan=2, pady=10)

# Поля для результатів
result_A_plus_B = tk.Label(root, text="A + B =", font=("Arial", 12))
result_A_plus_B.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

result_A_times_B = tk.Label(root, text="A * B =", font=("Arial", 12))
result_A_times_B.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

result_A_square = tk.Label(root, text="A^2 =", font=("Arial", 12))
result_A_square.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

# Запуск головного циклу
root.mainloop()
