P=True
O=input
N=int
B=str
A=print
import time,pyautogui as H
from random import randint as C
def F():
	G=H.size()
	if B(G)=='Size(width=640, height=480)':A('Using 640x480, Changing Randomx and Randomy');C=286.5;D=351;E=135;F=301
	elif B(G)=='Size(width=1280, height=720)':A('Using 1280x720, Changing Randomx and Randomy');C=573;D=702;E=271;F=602
	elif B(G)=='Size(width=1920, height=1080)':A('Using 1920x1080, Changing Randomx and Randomy');C=382;D=1582;E=181;F=903
	elif B(G)=='Size(width=2560, height=1440)':A('Using 2560x1440, Changing Randomx and Randomy');C=496;D=2056;E=235.3;F=1173.9
	elif B(G)=='Size(width=2048, height=1080)':A('Using 2048x1080, Changing Randomx and Randomy');C=404;D=1676;E=191;F=957
	elif B(G)=='Size(width=3840, height=2160)':A('Using 3840x2160, Changing Randomx and Randomy');C=744;D=3084;E=286;F=1759
	elif B(G)=='Size(width=7680, height=4320)':A('Using 7680x4320, Changing Randomx and Randomy');C=1488;D=6168;E=572;F=3518
	else:A('Using Non-Supported Res, Changing Randomx and Randomy to Default Location!');A('Please raise an issue on GitHub with your screen res for future custom support!');C=382;D=1582;E=181;F=903
	return C,D,E,F
def G():
	D='Must Type an Integer > 0';A('Usage Just Type an Integer e.g. 30')
	while P:
		try:
			B=N(O('Please Enter The Shortest Amount of Seconds To Wait Before Input - Recommended (30 seconds): '))
			if B<=0:A(D)
			else:
				C=N(O('Please Enter The Longest Amount of Seconds To Wait Before Input - Recommended (1200 seconds): '))
				if C<=0:A(D)
				else:break
		except ValueError:A('Invalid Entry: Usage Just Type an Integer e.g. 30')
	return B,C
def I(userTimeSettings):A=userTimeSettings;B=C(A[0],A[1]);return B
def D(timeSleepSettings):D=timeSleepSettings;C=I(D);A('Time Waiting Before Next Input: '+B(C)+' second(s) or '+B(C/60)+' minute(s)!');time.sleep(C)
def J(resScreenSize):A=resScreenSize;B=C(A[0],A[1]);D=C(A[2],A[3]);return B,D
def K(retScreenSize):F=retScreenSize;C=J(F);D=C[0];E=C[1];H.moveTo(D,E);H.click();A('Mouse Clicked At: ('+B(D)+','+B(E)+')')
def L():D=['q','w','e','r','a','s','d','f'];E=C(0,7);B=D[E];H.press(B);A('Button Clicked: '+B)
if __name__=='__main__':
	M=F();E=G()
	while P:D(E);K(M);D(E);L()