import os
import easygui as eg
eg.msgbox(os.getcwd())
fname='/Users/moko/bin/test.texto'
def touch(fname, times=None):
    with file(fname, 'a'):
        os.utime(fname, times)
        

f=open(fname,'w')
f.write(str(os.getcwd()))
f.close()
