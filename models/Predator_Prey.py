import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def run_simulation():

    def volkzayac(state, t, a, b, c, d):
        x, y = state
        dxdt=a*x-b*x*y
        dydt=c*x*y-d*y
        return [dxdt, dydt]
    def main_volkzayac():
        a=1.0 #рождаемость жертв
        b=0.1 #эффективность охоты
        c=0.075 #конверсия пищи в охотника
        d=1.5 #смертность хищников
        state0 = [10, 5]
        t = np.linspace(0, 50, 10000)
        states = odeint(volkzayac, state0, t, args=(a,b,c,d))

        # states — это матрица, где колонки — это X, Y и Z
        x = states[:, 0]
        y = states[:, 1]
        # plt.plot(time_steps, x, label='Зайцы x', color='blue')
        # plt.plot(time_steps, y, label='Волки y', color='red')
        # plt.xlabel("Дни")
        # plt.ylabel("Животные")

        # 1. Векторное поле (стрелочки)
        X_grid, Y_grid = np.meshgrid(np.linspace(0, 80, 25), np.linspace(0, 50, 25))
        DX = a*X_grid - b*X_grid*Y_grid
        DY = c*X_grid*Y_grid - d*Y_grid
        
        # Чтобы задать прозрачность в streamplot, можно использовать цвет с альфа-каналом 
        # или просто оставить 'gray', убрав alpha
        plt.streamplot(X_grid, Y_grid, DX, DY, color='lightgray')
        # 2. Твоя траектория (добавили label!)
        plt.plot(x, y, label='Траектория системы', color='tab:blue', linewidth=2)
        # 3. Точка равновесия (бонус - чтобы видеть, вокруг чего крутимся)
        plt.plot(d/c, a/b, 'ro', label='Точка равновесия')
        plt.title("Фазовый портрет: Волки vs Зайцы")

        plt.xlabel("Зайцы")
        plt.ylabel("Волки")

        plt.grid(True, alpha=0.2)
        plt.legend() # Теперь сработает без предупреждений
        plt.show()

    main_volkzayac()