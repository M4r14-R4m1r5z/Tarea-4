import numpy as np

def euler(f, y0, t0, tf, h):
    """
    Éste método nos permite resolver una ODE usando el método de Euler.

    Examples:
        >>> def f(y, t): return y + t
        >>> euler(f, 0, 0, 1, 0.1)
        [0, 0.1, 0.2, 0.3]

    Parameters:
        f (function): Función que describe la ecuación diferencial de primer orden: dy/dt = f(y, t)
        y0 (float): El valor inicial de y
        t0 (float): El tiempo inicial
        tf (float): El tiempo final
        h (float): Paso de tiempo

    Returns:
        list: Lista de valores de y en cada paso de tiempo (h).
    """

    y = y0
    y_array = [y]
    t = t0
    while t < tf:
        y = y + h * f(y, t)
        t = t + h
        y_array.append(y)
    return y_array

def rk2(f, y0, t0, tf, h):
    """
    Éste método, logra resolver una ODE usando el método de Runge-Kutta de segundo orden (RK2).

    Examples:
        >>> def f(y, t): return y + t
        >>> rk2(f, 0, 0, 1, 0.1)
        [0, 0.1, 0.2, 0.3]

    Parameters:
        f (function): Función que describe la ecuación diferencial de primer orden: dy/dt = f(y, t)
        y0 (float): El valor inicial de y
        t0 (float): El tiempo inicial
        tf (float): El tiempo final
        h (float): Paso de tiempo

    Returns:
        list: Lista de valores de y en cada paso de tiempo (h).
    """

    y = y0
    y_array = [y]
    t = t0
    while t < tf:
        k1 = h * f(y, t)
        k2 = h * f(t + 0.5 * h, y + 0.5 * k1)
        y = y + k2
        t = t + h
        y_array.append(y)
    return y_array

def rk4(f, y0, t0, tf, h):
    """
    Éste método nos permite resolver una ODE usando el método de Runge-Kutta de cuarto orden (RK4).

    Examples:
        >>> def f(y, t): return y + t
        >>> rk4(f, 0, 0, 1, 0.1)
        [0, 0.1, 0.2, 0.3]

    Parameters:
        f (function): Función que describe la ecuación diferencial de primer orden: dy/dt = f(y, t)
        y0 (float): El valor inicial de y
        t0 (float): El tiempo inicial
        tf (float): El tiempo final
        h (float): Paso de tiempo

    Returns:
        list: Lista de valores de y en cada paso de tiempo (h).
    """

    y = y0
    y_array = [y]
    t = t0
    while t < tf:
        k1 = h * f(y, t)
        k2 = h * f(t + 0.5 * h, y + 0.5 * k1)
        k3 = h * f(t + 0.5 * h, y + 0.5 * k2)
        k4 = h * f(t + h, y + k3)
        y = y + (1/6) * (k1 + 2 * k2 + 2 * k3 + k4)
        t = t + h
        y_array.append(y)
    return y_array

