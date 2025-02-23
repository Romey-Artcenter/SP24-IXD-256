import os, sys, io
import M5
from M5 import *
from hardware import *
import time

pin41 = None
pin1 = None

def setup():
  global pin41, pin1
  M5.begin()
  # initialize pin 41 (screen button on AtomS3 board) as input: 
  pin41 = Pin(41, mode=Pin.IN)
  # initialize pin 1 (bottom connector white wire) as output:
  pin1 = Pin(1, mode=Pin.OUT)

def loop():
  global pin41, pin1
  M5.update()
  if pin41.value():
    pin1.on()
  else:
    pin1.off()
  time.sleep_ms(100)

if __name__ == '__main__':
  try:
    setup()
    while True:
      loop()
  except (Exception, KeyboardInterrupt) as e:
    try:
      from utility import print_error_msg
      print_error_msg(e)
    except ImportError:
      print("please update to latest firmware")

