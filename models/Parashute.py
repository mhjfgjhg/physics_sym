import numpy as np
import matplotlib.pyplot as plt

def run_simulation():
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

    parashute()
