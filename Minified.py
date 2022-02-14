M=ValueError
L=int
G='~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
F=True
D=input
B=str
A=print
import time as E,pyautogui as H
from random import randint as C
def N():
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
def O():
	G='This is to large of a time input!';E='Must Type an Integer > 0';A('Usage Just Type an Integer e.g. 30')
	while F:
		try:
			B=L(D('Please Enter The Shortest Amount of Seconds To Wait Before Input - Recommended (30 seconds): '))
			if B<=0:A(E)
			elif B>=4294967:A(G)
			else:
				C=L(D('Please Enter The Longest Amount of Seconds To Wait Before Input - Recommended (1200 seconds): '))
				if C<=0:A(E)
				elif C<=B:A('This should be not equal to or larger then the lowest amount in range')
				elif C>=4294967:A(G)
				else:break
		except M:A('Invalid Entry: Usage Just Type an Integer e.g. 30')
	return B,C
def P(userTimeSettings):A=userTimeSettings;B=C(A[0],A[1]);return B
def I(timeSleepSettings):D=timeSleepSettings;C=P(D);A('Time Waiting Before Next Interaction: '+B(C)+' second(s) or '+B(C/60)+' minute(s)!');E.sleep(C)
def Q(resScreenSize):A=resScreenSize;B=C(A[0],A[1]);D=C(A[2],A[3]);return B,D
def R(retScreenSize):F=retScreenSize;C=Q(F);D=C[0];E=C[1];H.moveTo(D,E);H.click();A('Mouse Clicked At: ('+B(D)+','+B(E)+')')
def S():
	C=['q','w','e','r','a','s','d','f'];A('The Default Button Click List Is:');A(C)
	while F:
		try:
			E=B(D('Would You Like To Add More Keys To The ButtonClickList? Enter (Y) or (N): ')).lower()
			if E=='y':
				while F:
					try:
						G=L(D('How Many Keys Would You Like To Add To The List: '))
						for I in range(G):H=D("Please Press a Key or Write The Key, Such As 'space' and then press enter: ");C.append(H)
						break
					except M:A('Type Error: You Have Entered An Incorrect Type! Please Enter An Integer')
				break
			elif E=='n':break
			else:A('Input Error: Please Enter Either Y or N')
		except M:A('Type Error: You Have Entered An Incorrect Type! Please Enter Either Y or N')
	return C
def T(buttonSetup):D=buttonSetup;E=C(0,7);B=D[E];H.press(B);A('Button Clicked: '+B)
if __name__=='__main__':
	A(G);U=N();A(G);E.sleep(2);J=S();A('The Button Click List Is: ');A(J);A(G);E.sleep(2);K=O();A(G)
	while F:I(K);R(U);I(K);T(J)