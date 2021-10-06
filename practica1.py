
#importamos la biblioteca RPi:
import RPi.GPIO as GPIO
import time
#indicanos que esquema de numeracion de pin vamos a usar: numeracin de pin fisicoo (BOARD) o
#numeracion segun Broadcom SOCchannel (BCM)
GPIO.setmode (GPIO.BOARD)

#indicamos que el pin que vamos a usar, el 11, va a ser de salida
GPIO.setup (11, GPIO.OUT)

#creamos un objeto PWM con el pin a usar y la frecuencia de trabajo como parametros:
pwm = GPIO.PWM(11,100)

#establecemos el ciclo de trabajo o DutyCyle (perıodo en que la senal esta en estado Alto)
pwm.start (50)

#cambiamos la frecuencia de la señal(esta limitada en 100)
pwm.ChangeFrequency(50)
#para que de tiempo a hacerse los cambios de frecuencia o ciclo es necesario usar un sleep o bien usando cualquier instruccion
#que fuerce a parar el programa como:input("Ejecutando hasta que pulse una tecla...")
input("Ejecutando hasta que pulse una tecla...")

frecuencia = 5
while frecuencia < 50:
    #cambiamos el ciclo de trabajo
    pwm.ChangeDutyCycle(frecuencia)
    frecuencia+=5
    time.sleep(0.5)
    print(frecuencia)

while frecuencia > 0:
    pwm.ChangeDutyCycle(frecuencia)
    frecuencia-=5
    time.sleep(0.5)
    print(frecuencia)

#desactivamos el PWM con:
pwm.stop ()

#desactivamos los puertos GPIO:
GPIO.cleanup ()