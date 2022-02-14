I=str
H=print
import time,pyautogui as B
from random import randint as A
def D():B=A(30,120);return B
def C():A=D();time.sleep(A)
def E():B=A(382,1582);C=A(181,903);return B,C
def F():A=E();C=A[0];D=A[1];B.moveTo(C,D);B.click();H('Mouse Clicked At: ('+I(C)+','+I(D)+')')
def G():D=['q','w','e','r','a','s','d','f'];E=A(0,7);C=D[E];B.press(C);H('Button Clicked: '+C)
if __name__=='__main__':
	while True:C();F();C();G()
