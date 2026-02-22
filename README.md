# Physics Mathematical Simulation

A set of training mathematical models for physical problems. Developed for the purpose of in-depth study of differential equations and mathematical modeling using the example of physical problems. Designed on/for Arch-like Linux systems.

## Phisics Models

### Lorenz Attractor
A 3D simulation Lorenz sysem "Butterfly Effect"
On the *Euler method* and *Runge-Kutti*

### Predator-Prey Dynamics
Classic simple ecological model
On the *Runge-Kutti*

### SIRS/SIRD Epidemic Models
Epidemic models whis immunity, quarantine, death
On the *Euler method*

### Parashute Jump Simulation
A base physical model of free fall with gynamic drag coef
On the *Euler method*

## Tech Stack
- Language: Python 3.12+
- Environment: Managed via uv (Fast Python package manager)
- Libraries: NumPy, SciPy, Matplotlib
- OS: Arch Linux

## Quick Start
If you have uv installed, simply run:
```bash
git clone [https://github.com/mhjfgjhg/physics_sym.git](https://github.com/mhjfgjhg/physics_sym.git)
cd physics_sim
uv sync
uv run main.py