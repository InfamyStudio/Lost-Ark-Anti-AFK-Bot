g='Type Error: You Have Entered An Incorrect Type! Please Enter Either Y or N'
f='Input Error: Please Enter Either Y or N'
e='n'
d='Type Error: You Have Entered An Incorrect Type! Please Enter An Integer'
c='y'
b=')'
a=','
Z='Mouse Clicked At: ('
O=int
L=ValueError
H=True
G=input
C=str
B='~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
A=print
import time as D,pyautogui as N,pytesseract as M,os
P=os.environ.get('USERNAME')
Q='C:/Users/'+P+'/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'
from PIL import Image
M.pytesseract.tesseract_cmd=Q
from random import randint as E
def R():
	O='Using 2560x1440, Setting Randomx and Randomy';M=N.size()
	if C(M)=='Size(width=640, height=480)':A('Using 640x480, Setting Randomx and Randomy');B=286;D=351;E=135;F=301;G=855;H=1014;I=771;J=435;K=373;L=204
	elif C(M)=='Size(width=1280, height=720)':A('Using 1280x720, Setting Randomx and Randomy');B=573;D=702;E=271;F=602;G=855;H=1014;I=771;J=435;K=373;L=204
	elif C(M)=='Size(width=1920, height=1080)':A('Using 1920x1080, Setting Randomx and Randomy');B=382;D=1582;E=181;F=903;G=855;H=1014;I=771;J=435;K=373;L=204
	elif C(M)=='Size(width=2560, height=1440)':A(O);B=496;D=2056;E=235;F=1173;G=1135;H=1350;I=1030;J=609;K=496;L=220
	elif C(M)=='Size(width=2560, height=1080)':A(O);B=500;D=2100;E=181;F=903;G=1135;H=1350;I=1030;J=609;K=496;L=220
	elif C(M)=='Size(width=2048, height=1080)':A('Using 2048x1080, Setting Randomx and Randomy');B=404;D=1676;E=191;F=957;G=855;H=1014;I=771;J=435;K=373;L=204
	elif C(M)=='Size(width=3440, height=1440)':A('Using 3440x1440, Setting Randomx and Randomy');B=500;D=2900;E=220;F=1173;G=1720;H=716;I=1468;J=609;K=400;L=300
	elif C(M)=='Size(width=3840, height=2160)':A('Using 3840x2160, Setting Randomx and Randomy');B=572;D=3084;E=286;F=1759;G=855;H=1014;I=771;J=435;K=373;L=204
	elif C(M)=='Size(width=5120, height=1440)':A('Using 5120x1440, Setting Randomx and Randomy');B=744;D=4009;E=220;F=1173;G=855;H=1014;I=771;J=435;K=373;L=204
	elif C(M)=='Size(width=7680, height=4320)':A('Using 7680x4320, Setting Randomx and Randomy');B=1488;D=6168;E=572;F=3518;G=855;H=1014;I=771;J=435;K=373;L=204
	else:A('Using Non-Supported Res, Changing Randomx and Randomy to Default Location!');A('Please raise an issue on GitHub with your screen res for future custom support!');B=382;D=1582;E=181;F=903;G=855;H=1014;I=771;J=435;K=373;L=204
	return B,D,E,F,G,H,I,J,K,L
def S():
	E='This is to large of a time input!';D='Must Type an Integer > 0';A('Usage Just Type an Integer e.g. 30')
	while H:
		try:
			B=O(G('Please Enter The Shortest Amount of Seconds To Wait Before Input - Recommended (30 seconds): '))
			if B<=0:A(D)
			elif B>=4294967:A(E)
			else:
				C=O(G('Please Enter The Longest Amount of Seconds To Wait Before Input - Recommended (1200 seconds): '))
				if C<=0:A(D)
				elif C<=B:A('This should be not equal to or larger then the lowest amount in range')
				elif C>=4294967:A(E)
				else:break
		except L:A('Invalid Entry: Usage Just Type an Integer e.g. 30')
	return B,C
def T(userTimeSettings):A=userTimeSettings;B=E(A[0],A[1]);return B
def F(timeSleepSettings):E=timeSleepSettings;B=T(E);A('Next Interaction Time: '+C(B)+' second(s) or '+C(B//60)+' minute(s) (Integer Division Not Accurate Minute Representation)!');D.sleep(B)
def U(resScreenSize):A=resScreenSize;B=E(A[0],A[1]);C=E(A[2],A[3]);return B,C
def V(retScreenSize):F=retScreenSize;B=U(F);D=B[0];E=B[1];N.moveTo(D,E);N.click();A(Z+C(D)+a+C(E)+b)
def W():
	B=['q','w','e','r','a','s','d','f'];A('The Default Button Click List Is:');A(B)
	while H:
		try:
			E=C(G('Would You Like To Add More Keys To The ButtonClickList? Enter (Y) or (N): ')).lower()
			if E==c:
				while H:
					try:
						D=O(G('How Many Keys Would You Like To Add To The List: '))
						for I in range(D):F=G("Please Press a Key or Write The Key, Such As 'space' and then press enter: ");B.append(F)
						break
					except L:A(d)
				break
			elif E==e:D=0;break
			else:A(f)
		except L:A(g)
	return B,D
def X(buttonSetup):B=buttonSetup;D=B[0];F=B[1]+7;G=E(0,F);C=D[G];N.press(C);A('Button Clicked: '+C)
def Y(retScreenSize):
	X='queueDetectionScreenshot.png';K='Sit Tight!';J='~Waiting 10 Seconds To Reanylse Screen!';I='Still in Queue :(';E=retScreenSize;O=E[4];P=E[5];R=E[6];S=E[7];T=E[8];U=E[9]
	while H:
		try:
			A('Make Sure Nothing is covering your lost ark window, specifficaly the Queue Box!');Q=C(G('Would You Like To Start Queue Detection? Enter (Y) or (N): ')).lower()
			if Q==c:
				try:
					while H:
						V=N.screenshot(region=(R,S,T,U));V.save(X);W=X;A(B);A('Lost Ark Screen Being Analysed');D.sleep(1);F=M.image_to_string(Image.open(W))
						if'Waiting'in F:A(B);A(I);A(J);A(K);A(B);D.sleep(9)
						elif'Warten'in F:A(B);A(I);A(J);A(K);A(B);D.sleep(9)
						elif'Venter'in F:A(B);A(I);A(J);A(K);A(B);D.sleep(9)
						elif'Attendre'in F:A(B);A(I);A(J);A(K);A(B);D.sleep(9)
						elif'In attesa'in F:A(B);A(I);A(J);A(K);A(B);D.sleep(9)
						elif'Bekleme'in F:A(B);A(I);A(J);A(K);A(B);D.sleep(9)
						else:A('Out of Queue! :)');A('Waiting 60 seconds to launch your character!');A(B);D.sleep(60);N.moveTo(O,P);N.click();A(Z+C(O)+a+C(P)+b);A('Character Launch In Progress!');A('30 Second Wait Time!');D.sleep(30);break
					break
				except L:A(d)
			elif Q==e:break
			else:A(f)
		except L:A(g)
if __name__=='__main__':
	A(B);I=R();A(B);D.sleep(1);J=W();A(B);A('The Button Click List Is: ');A(J[0]);A(B);D.sleep(1);K=S();A(B);Y(I);A(B)
	while H:F(K);V(I);F(K);X(J)