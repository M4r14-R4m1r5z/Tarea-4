\(\textbf{Ecuaciones Diferenciales Ordinarias (ODEs)}\)


Para esta tarea se usaron tres distintos métodos para trabajar con ecuaciones diferenciales no lineales.

1) Método de Euler 


El método de Euler se basa en una expansión de Taylor de la función de x(t). Por ser un método simple, su aproximación es menos precisa en comparación a los otros métodos utilizados. Para iniciar este método se debe encontrar el número de pasos que vamos a considerar. Mediante la siguiente ecuación: 

$$N=\frac{(tf-t0)}{h}$$

N siendo el número de pasos, tf tiempo final y t0 tiempo inicial. Luego para hacer las iteraciones el valor de x me varía de la forma:

$${x(t + h) = x(t) + hf(x,t)}$$

Y t varía de la forma:
 
$${t_{n+1}=t_n+h}$$


2) Método de Runge-Kutta 2do Orden (RK2)
Este método también es llamado punto medio, ya que se basa en este principio matemático. Se inicia con las siguientes dos ecuaciones:
 
$$k_1=hf(x_0, t_0)$$

$$k_2=hf(x_0+\frac {k1}{2}, t_0 + \frac{h}{2})$$

Luego con estos valores encontrados, podemos actualizar los valores de x y t, con las siguientes ecuaciones: 

$$x(t+h)=x(t)+k_2$$

$$t=t+h$$

Y este proceso se repite de manera iterativa, hasta llegar al tiempo final deseado. 

3) Método de Runge-Kutta 4to Orden (RK4)

Por último se trabaja con este método, que sigue la misma idea de RK2. La diferencia es que se trabajan con más ecuaciones de k, mostradas a continuación: 

$$k1 = h * f(x[n], t[n])$$

$$k2 = h * f(x[n] + 0.5 * k1, t[n] + 0.5 * h)$$

$$k3 = h * f(x[n] + 0.5 * k2, t[n] + 0.5 * h)$$

$$k4 = h * f(x[n] + k3, t[n] + h)$$

Luego se actualizan los valores de x, t, con: 

$$x[n + 1] = x[n] + \frac{(k1 + 2*k2 + 2*k3 + k4)}{6}$$

$$t[n + 1] = t[n] + h$$

De los tres métodos utilizados en este proyecto, este es el que mejores valores aproximados genera.

