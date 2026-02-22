import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D

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

def attracror_l():
    sig=10.0
    ro=28.0
    beta=8/3
    x=[1]
    y=[1]
    z=[1]
    t_max=100
    dt=0.0001
    time_steps=np.arange(0,t_max,dt)
    for _ in time_steps[:-1]:
        x_curr=x[-1]
        y_curr=y[-1]
        z_curr=z[-1]

        dx=sig*(y_curr-x_curr)
        dy=x_curr*(ro-z_curr)-y_curr
        dz=x_curr*y_curr-beta*z_curr

        x.append(x_curr+dx*dt)
        y.append(y_curr+dy*dt)
        z.append(z_curr+dz*dt)
    
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Рисуем линию в пространстве
    ax.plot(x, y, z, lw=0.5, color='magenta')
    
    # Оформление
    ax.set_xlabel("Ось X")
    ax.set_ylabel("Ось Y")
    ax.set_zlabel("Ось Z")
    plt.title("Аттрактор Лоренца")
    plt.show()

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

def SIRS():
    N=1000
    beta_norm=0.4
    beta_karantin = beta_norm/3
    gamma=0.1
    ksi=0.1
    mu=0.005
    t_kar=20
    dt=0.01
    t_max=100
    S=[N-1]
    I=[1]
    R=[0]
    D=[0]
    time_steps=np.arange(0,t_max,dt)

    for _ in time_steps[:-1]:
        if _ <t_kar:
            beta = beta_norm
        elif _ >t_kar and _<t_kar+5:
            beta = beta_norm+((beta_karantin-beta_norm)/5) * (_-t_kar)
        else:
            beta = beta_karantin

        s_curr = S[-1]
        i_curr = I[-1]
        r_curr = R[-1]
        d_curr = D[-1]

        dS=-beta*s_curr*i_curr / N + ksi * r_curr
        dI=beta*s_curr*i_curr / N - gamma * i_curr - mu * i_curr
        dR=gamma*i_curr - ksi*r_curr
        dD=mu * i_curr

        S.append(s_curr + dS*dt)
        I.append(i_curr + dI*dt)
        R.append(r_curr + dR*dt)
        D.append(d_curr + dD*dt)

    plt.figure(figsize=(10, 5))
    plt.plot(time_steps, S, label='Здоровье S', color='blue')
    plt.plot(time_steps, I, label='Больные I', color='red')
    plt.plot(time_steps, R, label='Выздоровевшие R', color='green')
    plt.plot(time_steps, D, label='Умершие D', color='black')
    #plt.plot(S,I)
    plt.title("Модель пандемии SIR")
    #plt.xlabel("Здоровые")
    #plt.ylabel("Больные")
    plt.xlabel("Дни")
    plt.ylabel("Кол-во людей")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()

def parashute():
    print("Hello from physics-sim!")
    g=9.81
    m=80.0
    # k=0.25
    dt=0.01
    t_max=50

    k_initial = 0.25
    k_parashute = 5.0
    t_open = 15.0
    t_for_open = 2.0

    time_steps = np.arange(0, t_max, dt)
    velocity = [0.0]

    k_values = []

    for t in time_steps[:-1]:
        v_current = velocity[-1]

        if t<t_open:
            k= k_initial

        elif t_open<t and t<t_open+t_for_open:
            #k=k_parashute
            k=k_initial+((k_parashute-k_initial)/t_for_open)*(t-t_open)

        else:
            k=k_parashute

        k_values.append(k)

        a=g-(k/m)*v_current**2
        v_next = v_current+a*dt
        velocity.append(v_next)

    # Визуализация
    plt.figure(figsize=(12, 6))
    plt.plot(time_steps, velocity, label='Скорость v(t)', color='cyan', linewidth=2)
    plt.axvline(x=t_open, color='r', linestyle='--', label='Раскрытие прашюта')
    plt.title("Модель падения с парашютом")
    plt.xlabel("Время (с)")
    plt.ylabel("Скорость (м/с)")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main_lorenz()
