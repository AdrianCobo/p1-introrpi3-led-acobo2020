# P1-IntroRPi3-LED

## (CC-BY-NC-SA) Adrián Cobo Merino

El objetivo de este esta práctica es tener la primera toma de contacto con los componentes y pines de la raspberry pi encendiendo y apagando
un led.

Algo que me ha parecido interesante es la simulación de un puerto análogico modificando la frecuencia de un pulso digital.
Codigo de ejemplo:

```python
#creamos un objeto PWM con el pin a usar y la frecuencia de trabajo como parametros:
pwm = GPIO.PWM (11,100)

#establecemos el ciclo de trabajo o DutyCyle (perıodo en que la senal esta en estado Alto)
pwm.start (50)
```
Si quieres ver un video de demostracion, pulsa [aqui](https://drive.google.com/file/d/1mhw5sa_ZHguVLDJr6MUOeQjgKJUKqnlC/view?usp=sharing).
En el video podemos ver como al ejecutar el programa se enciende el led y como se apaga tras pulsar enter.

Para ver un video de como se cambia el brillo de un led, pulsa [aqui](https://drive.google.com/file/d/1e5ObOYfce3r9FPLGaUlrA7qm6x5Lfiq2/view?usp=sharing).

Para cualquier duda: <a.cobo.2020@alumos.urjc.es>
