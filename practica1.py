#importamos la biblioteca RPi:
import RPi.GPIO as GPIO

#indicanos que esquema de numeracion de pin vamos a usar: numeracin de pin f´ısico (BOARD) o
#numeracion segun Broadcom SOCchannel (BCM)
GPIO.setmode (GPIO.BOARD)

#indicamos que el pin que vamos a usar, el 11, va a ser de salida
GPIO.setup (11, GPIO.OUT)

#creamos un objeto PWM con el pin a usar y la frecuencia de trabajo como parametros:
pwm = GPIO.PWM (11,100)

#establecemos el ciclo de trabajo o DutyCyle (perıodo en que la senal esta en estado Alto)
pwm.start (50)
#si quisieseos cambiar el ciclo de trabajo:pwm.ChangeDutyCycle (ciclodetrabajodeseado)
#si quisiesemos cambiar la frecuencia de la señal:pwm.ChangeFrequency (frecuenciadeseada)
#para qui diese tiempo a hacerse estos cambios seria necesario usar un sleep o bien usando cualquier instruccion
#que fuerce a parar el programa como:input("Ejecutando hasta que pulse una tecla...")
input("Ejecutando hasta que pulse una tecla...")

#desactivamos el PWM con:
pwm.stop ()

#desactivamos los puertos GPIO:
GPIO.cleanup ()