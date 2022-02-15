b=')'
a=','
Z='Mouse Clicked At: ('
N=ValueError
M=int
G='~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
F=True
E=input
B=str
A=print
import time as C,pyautogui as H,pytesseract as I,os
O=os.environ.get('USERNAME')
P='C:/Users/'+O+'/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'
from PIL import Image
I.pytesseract.tesseract_cmd=P
from random import randint as D
def Q():
	G=H.size()
	if B(G)=='Size(width=640, height=480)':A('Using 640x480, Changing Randomx and Randomy');C=286;D=351;E=135;F=301
	elif B(G)=='Size(width=1280, height=720)':A('Using 1280x720, Changing Randomx and Randomy');C=573;D=702;E=271;F=602
	elif B(G)=='Size(width=1920, height=1080)':A('Using 1920x1080, Changing Randomx and Randomy');C=382;D=1582;E=181;F=903
	elif B(G)=='Size(width=2560, height=1440)':A('Using 2560x1440, Changing Randomx and Randomy');C=496;D=2056;E=235;F=1173
	elif B(G)=='Size(width=2048, height=1080)':A('Using 2048x1080, Changing Randomx and Randomy');C=404;D=1676;E=191;F=957
	elif B(G)=='Size(width=3440, height=1440)':A('Using 3440x1440, Changing Randomx and Randomy');C=500;D=2900;E=220;F=1173
	elif B(G)=='Size(width=3840, height=2160)':A('Using 3840x2160, Changing Randomx and Randomy');C=572;D=3084;E=286;F=1759
	elif B(G)=='Size(width=5120, height=1440)':A('Using 5120x1440, Changing Randomx and Randomy');C=744;D=4009;E=220;F=1173
	elif B(G)=='Size(width=7680, height=4320)':A('Using 7680x4320, Changing Randomx and Randomy');C=1488;D=6168;E=572;F=3518
	else:A('Using Non-Supported Res, Changing Randomx and Randomy to Default Location!');A('Please raise an issue on GitHub with your screen res for future custom support!');C=382;D=1582;E=181;F=903
	return C,D,E,F
def R():
	G='This is to large of a time input!';D='Must Type an Integer > 0';A('Usage Just Type an Integer e.g. 30')
	while F:
		try:
			B=M(E('Please Enter The Shortest Amount of Seconds To Wait Before Input - Recommended (30 seconds): '))
			if B<=0:A(D)
			elif B>=4294967:A(G)
			else:
				C=M(E('Please Enter The Longest Amount of Seconds To Wait Before Input - Recommended (1200 seconds): '))
				if C<=0:A(D)
				elif C<=B:A('This should be not equal to or larger then the lowest amount in range')
				elif C>=4294967:A(G)
				else:break
		except N:A('Invalid Entry: Usage Just Type an Integer e.g. 30')
	return B,C
def S(userTimeSettings):A=userTimeSettings;B=D(A[0],A[1]);return B
def J(timeSleepSettings):E=timeSleepSettings;D=S(E);A('Next Interaction Time: '+B(D)+' second(s) or '+B(D//60)+' minute(s) (Integer Division Not Accurate Minute Representation)!');C.sleep(D)
def T(resScreenSize):A=resScreenSize;B=D(A[0],A[1]);C=D(A[2],A[3]);return B,C
def U(retScreenSize):F=retScreenSize;C=T(F);D=C[0];E=C[1];H.moveTo(D,E);H.click();A(Z+B(D)+a+B(E)+b)
def V():
	C=['q','w','e','r','a','s','d','f'];A('The Default Button Click List Is:');A(C)
	while F:
		try:
			G=B(E('Would You Like To Add More Keys To The ButtonClickList? Enter (Y) or (N): ')).lower()
			if G=='y':
				while F:
					try:
						D=M(E('How Many Keys Would You Like To Add To The List: '))
						for I in range(D):H=E("Please Press a Key or Write The Key, Such As 'space' and then press enter: ");C.append(H)
						break
					except N:A('Type Error: You Have Entered An Incorrect Type! Please Enter An Integer')
				break
			elif G=='n':D=0;break
			else:A('Input Error: Please Enter Either Y or N')
		except N:A('Type Error: You Have Entered An Incorrect Type! Please Enter Either Y or N')
	return C,D
def W(buttonSetup):C=buttonSetup;G=C[0];E=C[1]+7;A(B(E));I=D(0,E);F=G[I];H.press(F);A('Button Clicked: '+F)
def X():
	L='queueDetectionScreenshot.png'
	while F:
		G=H.screenshot(region=(771,435,373,204));G.save(L);J=L;A('Lost Ark Screen Being Analysed');K=I.image_to_string(Image.open(J))
		if'Waiting'in K:A('Still in Queue :(');A('~Waiting 10 Seconds To Reanylse Screen!');A('Sit Tight!');C.sleep(10)
		else:D=855;E=1014;A('Out of Queue! :)');A('Waiting 60 seconds to launch your character!');C.sleep(60);H.moveTo(D,E);H.click();A(Z+B(D)+a+B(E)+b);A('Character Launch In Progress!');A('30 Second Wait Time!');C.sleep(30);break
if __name__=='__main__':
	A(G);Y=Q();A(G);C.sleep(2);K=V();A('The Button Click List Is: ');A(K[0]);A(G);C.sleep(2);L=R();A(G);X();A(G)
	while F:J(L);U(Y);J(L);W(K)