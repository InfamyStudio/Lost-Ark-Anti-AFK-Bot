g='Type Error: You Have Entered An Incorrect Type! Please Enter Either Y or N'
f='Input Error: Please Enter Either Y or N'
e='n'
d='Type Error: You Have Entered An Incorrect Type! Please Enter An Integer'
c='y'
b=')'
a=','
Z='Mouse Clicked At: ('
N=int
I=ValueError
F=True
E=input
C='~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
B=str
A=print
import time as D,pyautogui as H,pytesseract as J,os
O=os.environ.get('USERNAME')
P='C:/Users/'+O+'/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'
from PIL import Image
J.pytesseract.tesseract_cmd=P
from random import randint as G
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
			B=N(E('Please Enter The Shortest Amount of Seconds To Wait Before Input - Recommended (30 seconds): '))
			if B<=0:A(D)
			elif B>=4294967:A(G)
			else:
				C=N(E('Please Enter The Longest Amount of Seconds To Wait Before Input - Recommended (1200 seconds): '))
				if C<=0:A(D)
				elif C<=B:A('This should be not equal to or larger then the lowest amount in range')
				elif C>=4294967:A(G)
				else:break
		except I:A('Invalid Entry: Usage Just Type an Integer e.g. 30')
	return B,C
def S(userTimeSettings):A=userTimeSettings;B=G(A[0],A[1]);return B
def K(timeSleepSettings):E=timeSleepSettings;C=S(E);A('Next Interaction Time: '+B(C)+' second(s) or '+B(C//60)+' minute(s) (Integer Division Not Accurate Minute Representation)!');D.sleep(C)
def T(resScreenSize):A=resScreenSize;B=G(A[0],A[1]);C=G(A[2],A[3]);return B,C
def U(retScreenSize):F=retScreenSize;C=T(F);D=C[0];E=C[1];H.moveTo(D,E);H.click();A(Z+B(D)+a+B(E)+b)
def V():
	C=['q','w','e','r','a','s','d','f'];A('The Default Button Click List Is:');A(C)
	while F:
		try:
			G=B(E('Would You Like To Add More Keys To The ButtonClickList? Enter (Y) or (N): ')).lower()
			if G==c:
				while F:
					try:
						D=N(E('How Many Keys Would You Like To Add To The List: '))
						for J in range(D):H=E("Please Press a Key or Write The Key, Such As 'space' and then press enter: ");C.append(H)
						break
					except I:A(d)
				break
			elif G==e:D=0;break
			else:A(f)
		except I:A(g)
	return C,D
def W(buttonSetup):C=buttonSetup;F=C[0];D=C[1]+7;A(B(D));I=G(0,D);E=F[I];H.press(E);A('Button Clicked: '+E)
def X():
	P='queueDetectionScreenshot.png'
	while F:
		try:
			A('Make Sure Nothing is covering your lost ark window, specifficaly the Queue Box!');G=B(E('Would You Like To Start Queue Detection? Enter (Y) or (N): ')).lower()
			if G==c:
				try:
					while F:
						M=H.screenshot(region=(771,435,373,204));M.save(P);N=P;A(C);A('Lost Ark Screen Being Analysed');D.sleep(1);O=J.image_to_string(Image.open(N))
						if'Waiting'in O:A(C);A('Still in Queue :(');A('~Waiting 10 Seconds To Reanylse Screen!');A('Sit Tight!');A(C);D.sleep(9)
						else:K=855;L=1014;A('Out of Queue! :)');A('Waiting 60 seconds to launch your character!');A(C);D.sleep(60);H.moveTo(K,L);H.click();A(Z+B(K)+a+B(L)+b);A('Character Launch In Progress!');A('30 Second Wait Time!');D.sleep(30);break
					break
				except I:A(d)
			elif G==e:break
			else:A(f)
		except I:A(g)
if __name__=='__main__':
	A(C);Y=Q();A(C);D.sleep(1);L=V();A(C);A('The Button Click List Is: ');A(L[0]);A(C);D.sleep(1);M=R();A(C);X();A(C)
	while F:K(M);U(Y);K(M);W(L)