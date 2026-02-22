import numpy as np
import matplotlib.pyplot as plt

def run_simulation():

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

    attracror_l()