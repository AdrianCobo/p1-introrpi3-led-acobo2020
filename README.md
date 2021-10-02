# P1-IntroRPi3-LED

## (CC-BY-NC-SA) Adrián Cobo Merino

El objetivo de este esta practica es conocer tener la primera toma de contacto con los componentes y pines de la raspberry pi.

Algo que me ha parecido interesante es la simulacion de un puerto analogico modificando la frecuencia de un pulso digital.
Codigo de ejemplo:

```python
#creamos un objeto PWM con el pin a usar y la frecuencia de trabajo como parametros:
pwm = GPIO.PWM (11,100)

#establecemos el ciclo de trabajo o DutyCyle (perıodo en que la senal esta en estado Alto)
pwm.start (50)
```
Pulsa [aqui](https://github.com/clases-julio)para ver un video del programa.

Para cualquier duda: <a.cobo.2020@alumos.urjc.es>
