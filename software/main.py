
import tkinter as tk
from tkinter import ttk
import os


class TrajectoryGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Параметры траектории")

        # Фрейм для выбора ввода координат или обобщенных координат
        mode_frame = ttk.LabelFrame(root, text="Тип ввода")
        mode_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.input_mode = tk.StringVar(value="coordinates")

        coordinates_radio = ttk.Radiobutton(mode_frame, text="Декартовы ", variable=self.input_mode,
                                            value="coordinates", command=self.update_input_mode)
        coordinates_radio.grid(row=0, column=0, padx=5, pady=5)

        generalized_radio = ttk.Radiobutton(mode_frame, text="Обобщенные", variable=self.input_mode,
                                            value="generalized", command=self.update_input_mode)
        generalized_radio.grid(row=0, column=1, padx=5, pady=5)

        coord_frame = ttk.LabelFrame(root, text="Декартовы координаты")
        coord_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        self.create_coordinates_inputs(coord_frame)

        angle_frame = ttk.LabelFrame(root, text="Углы Эйлера")
        angle_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        self.create_angles_inputs(angle_frame)

        q_frame = ttk.LabelFrame(root, text="Обощенные координаты")
        q_frame.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

        self.create_generalized_coordinates_inputs(q_frame)

        time_points_frame = ttk.LabelFrame(root, text="Время и точки")
        time_points_frame.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

        self.create_time_points_inputs(time_points_frame)

        self.submit_button = ttk.Button(root, text="Сохранить", command=self.submit)
        self.submit_button.grid(row=5, column=0, padx=10, pady=10)

        self.update_input_mode()

    def create_coordinates_inputs(self, frame):
        ttk.Label(frame, text="X:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.x_entry = ttk.Entry(frame)
        self.x_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Y:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.y_entry = ttk.Entry(frame)
        self.y_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Z:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.z_entry = ttk.Entry(frame)
        self.z_entry.grid(row=2, column=1, padx=5, pady=5)

    def create_angles_inputs(self, frame):
        ttk.Label(frame, text="Alpha:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.alpha_entry = ttk.Entry(frame)
        self.alpha_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Beta:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.beta_entry = ttk.Entry(frame)
        self.beta_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Gamma:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.gamma_entry = ttk.Entry(frame)
        self.gamma_entry.grid(row=2, column=1, padx=5, pady=5)

    def create_generalized_coordinates_inputs(self, frame):
        ttk.Label(frame, text="Q1:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.q1_entry = ttk.Entry(frame, state='disabled')
        self.q1_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Q2:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.q2_entry = ttk.Entry(frame, state='disabled')
        self.q2_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Q3:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.q3_entry = ttk.Entry(frame, state='disabled')
        self.q3_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Q4:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.q4_entry = ttk.Entry(frame, state='disabled')
        self.q4_entry.grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Q5:").grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.q5_entry = ttk.Entry(frame, state='disabled')
        self.q5_entry.grid(row=4, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Q6:").grid(row=5, column=0, padx=5, pady=5, sticky="e")
        self.q6_entry = ttk.Entry(frame, state='disabled')
        self.q6_entry.grid(row=5, column=1, padx=5, pady=5)

    def create_time_points_inputs(self, frame):
        ttk.Label(frame, text="Время, с:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.time_entry = ttk.Entry(frame)
        self.time_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Количество точек:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.points_entry = ttk.Entry(frame)
        self.points_entry.grid(row=1, column=1, padx=5, pady=5)

    def update_input_mode(self):
        if self.input_mode.get() == "coordinates":
            self.enable_coordinates(True)
            self.enable_generalized_coordinates(False)
        else:
            self.enable_coordinates(False)
            self.enable_generalized_coordinates(True)

    def enable_coordinates(self, enable):
        state = 'normal' if enable else 'disabled'
        self.x_entry.config(state=state)
        self.y_entry.config(state=state)
        self.z_entry.config(state=state)
        self.alpha_entry.config(state=state)
        self.beta_entry.config(state=state)
        self.gamma_entry.config(state=state)

    def enable_generalized_coordinates(self, enable):
        state = 'normal' if enable else 'disabled'
        self.q1_entry.config(state=state)
        self.q2_entry.config(state=state)
        self.q3_entry.config(state=state)
        self.q4_entry.config(state=state)
        self.q5_entry.config(state=state)
        self.q6_entry.config(state=state)

    def submit(self):
        time = self.time_entry.get()
        points = self.points_entry.get()

        if self.input_mode.get() == "coordinates":
            x = self.x_entry.get()
            y = self.y_entry.get()
            z = self.z_entry.get()
            alpha = self.alpha_entry.get()
            beta = self.beta_entry.get()
            gamma = self.gamma_entry.get()

            # Удаление файла с обобщенными координатами, если он существует
            if os.path.exists('generalized_coordinates.txt'):
                os.remove('generalized_coordinates.txt')

            # Сохранение координат в файл
            with open('coordinates.txt', 'w') as f:
                f.write(
                    f"X: {x}\nY: {y}\nZ: {z}\nAlpha: {alpha}\nBeta: {beta}\nGamma: {gamma}\nTime: {time}\nPoints: {points}\n")
        else:
            q1 = self.q1_entry.get()
            q2 = self.q2_entry.get()
            q3 = self.q3_entry.get()
            q4 = self.q4_entry.get()
            q5 = self.q5_entry.get()
            q6 = self.q6_entry.get()

            # Удаление файла с координатами, если он существует
            if os.path.exists('coordinates.txt'):
                os.remove('coordinates.txt')

            # Сохранение обобщенных координат в файл
            with open('generalized_coordinates.txt', 'w') as f:
                f.write(f"Q1: {q1}\nQ2: {q2}\nQ3: {q3}\nQ4: {q4}\nQ5: {q5}\nQ6: {q6}\nTime: {time}\nPoints: {points}\n")

        print("Данные успешно сохранены.")


# Создание основного окна приложения
root = tk.Tk()
app = TrajectoryGUI(root)
root.mainloop()
