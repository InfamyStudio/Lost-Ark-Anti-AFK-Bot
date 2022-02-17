g='Type Error: You Have Entered An Incorrect Type! Please Enter Either Y or N'
f='Input Error: Please Enter Either Y or N'
e='n'
d='Type Error: You Have Entered An Incorrect Type! Please Enter An Integer'
c='y'
b=')'
a=','
Z='Mouse Clicked At: ('
N=int
L=ValueError
G=True
F=input
C=str
B='~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
A=print
import time as D,pyautogui as H,pytesseract as M,os
O=os.environ.get('USERNAME')
P='C:/Users/'+O+'/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'
from PIL import Image
M.pytesseract.tesseract_cmd=P
from random import randint as E
def Q():
	G=H.size()
	if C(G)=='Size(width=640, height=480)':A('Using 640x480, Changing Randomx and Randomy');B=286;D=351;E=135;F=301
	elif C(G)=='Size(width=1280, height=720)':A('Using 1280x720, Changing Randomx and Randomy');B=573;D=702;E=271;F=602
	elif C(G)=='Size(width=1920, height=1080)':A('Using 1920x1080, Changing Randomx and Randomy');B=382;D=1582;E=181;F=903
	elif C(G)=='Size(width=2560, height=1440)':A('Using 2560x1440, Changing Randomx and Randomy');B=496;D=2056;E=235;F=1173
	elif C(G)=='Size(width=2048, height=1080)':A('Using 2048x1080, Changing Randomx and Randomy');B=404;D=1676;E=191;F=957
	elif C(G)=='Size(width=3440, height=1440)':A('Using 3440x1440, Changing Randomx and Randomy');B=500;D=2900;E=220;F=1173
	elif C(G)=='Size(width=3840, height=2160)':A('Using 3840x2160, Changing Randomx and Randomy');B=572;D=3084;E=286;F=1759
	elif C(G)=='Size(width=5120, height=1440)':A('Using 5120x1440, Changing Randomx and Randomy');B=744;D=4009;E=220;F=1173
	elif C(G)=='Size(width=7680, height=4320)':A('Using 7680x4320, Changing Randomx and Randomy');B=1488;D=6168;E=572;F=3518
	else:A('Using Non-Supported Res, Changing Randomx and Randomy to Default Location!');A('Please raise an issue on GitHub with your screen res for future custom support!');B=382;D=1582;E=181;F=903
	return B,D,E,F
def R():
	E='This is to large of a time input!';D='Must Type an Integer > 0';A('Usage Just Type an Integer e.g. 30')
	while G:
		try:
			B=N(F('Please Enter The Shortest Amount of Seconds To Wait Before Input - Recommended (30 seconds): '))
			if B<=0:A(D)
			elif B>=4294967:A(E)
			else:
				C=N(F('Please Enter The Longest Amount of Seconds To Wait Before Input - Recommended (1200 seconds): '))
				if C<=0:A(D)
				elif C<=B:A('This should be not equal to or larger then the lowest amount in range')
				elif C>=4294967:A(E)
				else:break
		except L:A('Invalid Entry: Usage Just Type an Integer e.g. 30')
	return B,C
def S(userTimeSettings):A=userTimeSettings;B=E(A[0],A[1]);return B
def I(timeSleepSettings):E=timeSleepSettings;B=S(E);A('Next Interaction Time: '+C(B)+' second(s) or '+C(B//60)+' minute(s) (Integer Division Not Accurate Minute Representation)!');D.sleep(B)
def T(resScreenSize):A=resScreenSize;B=E(A[0],A[1]);C=E(A[2],A[3]);return B,C
def U(retScreenSize):F=retScreenSize;B=T(F);D=B[0];E=B[1];H.moveTo(D,E);H.click();A(Z+C(D)+a+C(E)+b)
def V():
	B=['q','w','e','r','a','s','d','f'];A('The Default Button Click List Is:');A(B)
	while G:
		try:
			E=C(F('Would You Like To Add More Keys To The ButtonClickList? Enter (Y) or (N): ')).lower()
			if E==c:
				while G:
					try:
						D=N(F('How Many Keys Would You Like To Add To The List: '))
						for I in range(D):H=F("Please Press a Key or Write The Key, Such As 'space' and then press enter: ");B.append(H)
						break
					except L:A(d)
				break
			elif E==e:D=0;break
			else:A(f)
		except L:A(g)
	return B,D
def W(buttonSetup):B=buttonSetup;G=B[0];D=B[1]+7;A(C(D));I=E(0,D);F=G[I];H.press(F);A('Button Clicked: '+F)
def X():
	S='queueDetectionScreenshot.png';K='Sit Tight!';J='~Waiting 10 Seconds To Reanylse Screen!';I='Still in Queue :('
	while G:
		try:
			A('Make Sure Nothing is covering your lost ark window, specifficaly the Queue Box!');N=C(F('Would You Like To Start Queue Detection? Enter (Y) or (N): ')).lower()
			if N==c:
				try:
					while G:
						Q=H.screenshot(region=(771,435,373,204));Q.save(S);R=S;A(B);A('Lost Ark Screen Being Analysed');D.sleep(1);E=M.image_to_string(Image.open(R))
						if'Waiting'in E:A(B);A(I);A(J);A(K);A(B);D.sleep(9)
						elif'Warten'in E:A(B);A(I);A(J);A(K);A(B);D.sleep(9)
						elif'Venter'in E:A(B);A(I);A(J);A(K);A(B);D.sleep(9)
						elif'Attendre'in E:A(B);A(I);A(J);A(K);A(B);D.sleep(9)
						elif'In attesa'in E:A(B);A(I);A(J);A(K);A(B);D.sleep(9)
						elif'Bekleme'in E:A(B);A(I);A(J);A(K);A(B);D.sleep(9)
						else:O=855;P=1014;A('Out of Queue! :)');A('Waiting 60 seconds to launch your character!');A(B);D.sleep(60);H.moveTo(O,P);H.click();A(Z+C(O)+a+C(P)+b);A('Character Launch In Progress!');A('30 Second Wait Time!');D.sleep(30);break
					break
				except L:A(d)
			elif N==e:break
			else:A(f)
		except L:A(g)
if __name__=='__main__':
	A(B);Y=Q();A(B);D.sleep(1);J=V();A(B);A('The Button Click List Is: ');A(J[0]);A(B);D.sleep(1);K=R();A(B);X();A(B)
	while G:I(K);U(Y);I(K);W(J)