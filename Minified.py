_G='Type Error: You Have Entered An Incorrect Type! Please Enter Either Y or N'
_F='Input Error: Please Enter Either Y or N'
_E='Type Error: You Have Entered An Incorrect Type! Please Enter An Integer'
_D='Mouse Clicked At: ('
_C=None
_B=True
_A='~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
import time,pyautogui,pytesseract,os,win32gui,win32com.client,win32ui,ctypes
from ctypes import windll
user32=ctypes.windll.user32
user=os.environ.get('USERNAME')
tesseractpath='C:/Users/'+user+'/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'
from PIL import Image
from PIL import ImageGrab
pytesseract.pytesseract.tesseract_cmd=tesseractpath
from random import randint
LAWindowTitle='LOST ARK (64-bit, DX11) v.2.0.2.1'
def ScreenSetup():D=win32gui.FindWindow(_C,LAWindowTitle);E,F,G,H=win32gui.GetWindowRect(D);B=G-E;C=H-F;A=LALocation();I=A[0]+round(B*0.198958);J=A[0]+round(B*0.823958);K=A[1]+round(C*0.1675925925925926);L=A[1]+round(C*0.8361111111111111);M=A[0]+round(B*0.4453125);N=A[1]+round(C*0.9388888888888889);O=round(B*0.4015625);P=round(C*0.4027777777777778);Q=round(B*0.19427083333333334);R=round(C*0.18888888888888888);return I,J,K,L,M,N,O,P,Q,R
def TimeSetup():
	D='This is to large of a time input!';C='Must Type an Integer > 0'
	while _B:
		try:
			A=int(30)
			if A<=0:print(C)
			elif A>=4294967:print(D)
			else:
				B=int(1200)
				if B<=0:print(C)
				elif B<=A:print('This should be not equal to or larger then the lowest amount in range')
				elif B>=4294967:print(D)
				else:break
		except ValueError:print('Invalid Entry: Usage Just Type an Integer e.g. 30')
	print('The Shortest Amount of Seconds To Wait Before Input - 30 seconds');print('The Longest Amount of Seconds To Wait Before Input - 1200 seconds');return A,B
def RandomTimeGen(userTimeSettings):A=userTimeSettings;B=randint(A[0],A[1]);return B
def TimeSleep(timeSleepSettings):B=timeSleepSettings;A=RandomTimeGen(B);print('Next Interaction Time: '+str(A)+' second(s) or '+str(A//60)+' minute(s) (Integer Division Not Accurate Minute Representation)!');time.sleep(A)
def RandomLocationGen(resScreenSize):A=resScreenSize;B=randint(A[0],A[1]);C=randint(A[2],A[3]);return B,C
def LAForeground():A=win32gui.FindWindow(_C,LAWindowTitle);B=win32com.client.Dispatch('WScript.Shell');B.SendKeys('%');win32gui.SetForegroundWindow(A)
def LALocation():
	if LAWindowTitle:
		B=win32gui.FindWindow(_C,LAWindowTitle)
		if B:A=win32gui.GetWindowRect(B);C=A[0];D=A[1];E=A[2]-C;F=A[3]-D;return C,D,E,F
		else:print('Window not found!')
def MouseClick(retScreenSize):LAForeground();D=retScreenSize;A=RandomLocationGen(D);B=A[0];C=A[1];pyautogui.moveTo(B,C);pyautogui.click();print(_D+str(B)+','+str(C)+')')
def ButtonSetup():
	A=['q','w','e','r','a','s','d','f'];print('The Default Button Click List Is:');print(A)
	while _B:
		try:
			C=str('n').lower()
			if C=='y':
				while _B:
					try:
						B=int(input('How Many Keys Would You Like To Add To The List: '))
						for E in range(B):D=input("Please Press a Key or Write The Key, Such As 'space' and then press enter: ");A.append(D)
						break
					except ValueError:print(_E)
				break
			elif C=='n':B=0;break
			else:print(_F)
		except ValueError:print(_G)
	return A,B
def ButtonClick(buttonSetup):A=buttonSetup;LAForeground();C=A[0];D=A[1]+7;E=randint(0,D);B=C[E];pyautogui.press(B);print('Button Clicked: '+B)
def screenshot(window_title=_C):F=retScreenSize[6];G=retScreenSize[7];J=F+retScreenSize[8];K=G+retScreenSize[9];B=win32gui.FindWindow(_C,LAWindowTitle);L,M,N,O=win32gui.GetWindowRect(B);P=N-L;Q=O-M;H=win32gui.GetWindowDC(B);C=win32ui.CreateDCFromHandle(H);D=C.CreateCompatibleDC();A=win32ui.CreateBitmap();A.CreateCompatibleBitmap(C,P,Q);D.SelectObject(A);S=windll.user32.PrintWindow(B,D.GetSafeHdc(),0);I=A.GetInfo();R=A.GetBitmapBits(_B);E=Image.frombuffer('RGB',(I['bmWidth'],I['bmHeight']),R,'raw','BGRX',0,1);win32gui.DeleteObject(A.GetHandle());D.DeleteDC();C.DeleteDC();win32gui.ReleaseDC(B,H);E=E.crop((F,G,J,K));return E
def QueueDetection(retScreenSize):
	I='queueDetectionScreenshot.png';E='Sit Tight!';D='~Waiting 10 Seconds To Reanylse Screen!';C='Still in Queue :(';A=retScreenSize;F=A[4];G=A[5];L=A[6];M=A[7];N=A[8];O=A[9]
	while _B:
		try:
			print('Make Sure Nothing is covering your lost ark window, specifficaly the Queue Box!');H=str(input('Would You Like To Start Queue Detection? Enter (Y) or (N): ')).lower()
			if H=='y':
				try:
					while _B:
						J=screenshot(LAWindowTitle);J.save(I);K=I;print(_A);print('Lost Ark Screen Being Analysed');time.sleep(1);B=pytesseract.image_to_string(Image.open(K))
						if'Waiting'in B:print(_A);print(C);print(D);print(E);print(_A);time.sleep(9)
						elif'Warten'in B:print(_A);print(C);print(D);print(E);print(_A);time.sleep(9)
						elif'Venter'in B:print(_A);print(C);print(D);print(E);print(_A);time.sleep(9)
						elif'Attendre'in B:print(_A);print(C);print(D);print(E);print(_A);time.sleep(9)
						elif'In attesa'in B:print(_A);print(C);print(D);print(E);print(_A);time.sleep(9)
						elif'Bekleme'in B:print(_A);print(C);print(D);print(E);print(_A);time.sleep(9)
						else:print('Out of Queue! :)');print('Waiting 60 seconds to launch your character!');print(_A);time.sleep(60);LAForeground();pyautogui.moveTo(F,G);pyautogui.click();print(_D+str(F)+','+str(G)+')');print('Character Launch In Progress!');print('30 Second Wait Time!');time.sleep(30);break
					break
				except ValueError:print(_E)
			elif H=='n':break
			else:print(_F)
		except ValueError:print(_G)
if __name__=='__main__':
	print(_A);retScreenSize=ScreenSetup();print(_A);time.sleep(1);buttonSetup=ButtonSetup();print(_A);time.sleep(1);timeSleepSettings=TimeSetup();print(_A);QueueDetection(retScreenSize);print(_A)
	while _B:TimeSleep(timeSleepSettings);MouseClick(retScreenSize);TimeSleep(timeSleepSettings);ButtonClick(buttonSetup)