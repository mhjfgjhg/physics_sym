import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def run_simulation():

    def lorenz(state, t, sigma, rho, beta):
        x, y, z = state # Распаковываем текущее состояние
        dxdt = sigma * (y - x)
        dydt = x * (rho - z) - y
        dzdt = x * y - beta * z
        return [dxdt, dydt, dzdt] # Возвращаем производные
    def main_lorenz():
        # Параметры
        sigma = 10.0
        rho = 28.0
        beta = 8/3
        
        # Начальное состояние
        state0 = [1.0, 1.0, 1.0]
        
        # Сетка времени (теперь это просто точки, в которых мы хотим ПОЛУЧИТЬ ответ)
        t = np.linspace(0, 50, 10000)

        # 2. РЕШАЕМ в одну строку
        # Аргументы: функция, нач. состояние, время, дополнительные параметры (args)
        states = odeint(lorenz, state0, t, args=(sigma, rho, beta))

        # states — это матрица, где колонки — это X, Y и Z
        x = states[:, 0]
        y = states[:, 1]
        z = states[:, 2]

        # Визуализация
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(x, y, z, color='magenta', lw=0.7)
        
        ax.set_title("Аттрактор Лоренца (SciPy Solve)")
        plt.show()

    main_lorenz()