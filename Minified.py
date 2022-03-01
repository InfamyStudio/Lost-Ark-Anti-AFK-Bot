_F='Type Error: You Have Entered An Incorrect Type! Please Enter Either Y or N'
_E='Input Error: Please Enter Either Y or N'
_D='Type Error: You Have Entered An Incorrect Type! Please Enter An Integer'
_C='Mouse Clicked At: ('
_B=True
_A='~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
import time,pyautogui,pywinauto,pytesseract,os,win32gui,win32com.client,win32ui,ctypes
from ctypes import windll
user32=ctypes.windll.user32
user=os.environ.get('USERNAME')
tesseractpath='C:/Users/'+user+'/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'
from PIL import Image
from PIL import ImageGrab
pytesseract.pytesseract.tesseract_cmd=tesseractpath
from random import randint
LAWindowTitle='LOST ARK (64-bit, DX11)'
hwnd=pywinauto.findwindows.find_window(best_match=LAWindowTitle)
def ScreenSetup():D,E,F,G=win32gui.GetWindowRect(hwnd);B=F-D;C=G-E;A=LALocation();H=A[0]+round(B*0.198958);I=A[0]+round(B*0.823958);J=A[1]+round(C*0.1675925925925926);K=A[1]+round(C*0.8361111111111111);L=A[0]+round(B*0.4453125);M=A[1]+round(C*0.9388888888888889);N=round(B*0.4015625);O=round(C*0.4027777777777778);P=round(B*0.19427083333333334);Q=round(C*0.18888888888888888);return H,I,J,K,L,M,N,O,P,Q
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
def LAForeground():A=win32com.client.Dispatch('WScript.Shell');A.SendKeys('%');win32gui.SetForegroundWindow(hwnd);time.sleep(0.5)
def LALocation():
	if LAWindowTitle:
		if hwnd:A=win32gui.GetWindowRect(hwnd);B=A[0];C=A[1];D=A[2]-B;E=A[3]-C;return B,C,D,E
		else:print('Window not found!')
def MouseClick(retScreenSize):LAForeground();LALocation();D=retScreenSize;A=RandomLocationGen(D);B=A[0];C=A[1];pyautogui.moveTo(B,C);pyautogui.click();print(_C+str(B)+','+str(C)+')')
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
					except ValueError:print(_D)
				break
			elif C=='n':B=0;break
			else:print(_E)
		except ValueError:print(_F)
	return A,B
def ButtonClick(buttonSetup):A=buttonSetup;LAForeground();C=A[0];D=A[1]+7;E=randint(0,D);B=C[E];pyautogui.press(B);print('Button Clicked: '+B)
def screenshot(window_title=None):LALocation();E=retScreenSize[6];F=retScreenSize[7];I=E+retScreenSize[8];J=F+retScreenSize[9];K,L,M,N=win32gui.GetWindowRect(hwnd);O=M-K;P=N-L;G=win32gui.GetWindowDC(hwnd);B=win32ui.CreateDCFromHandle(G);C=B.CreateCompatibleDC();A=win32ui.CreateBitmap();A.CreateCompatibleBitmap(B,O,P);C.SelectObject(A);R=windll.user32.PrintWindow(hwnd,C.GetSafeHdc(),0);H=A.GetInfo();Q=A.GetBitmapBits(_B);D=Image.frombuffer('RGB',(H['bmWidth'],H['bmHeight']),Q,'raw','BGRX',0,1);win32gui.DeleteObject(A.GetHandle());C.DeleteDC();B.DeleteDC();win32gui.ReleaseDC(hwnd,G);D=D.crop((E,F,I,J));return D
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
						else:print('Out of Queue! :)');print('Waiting 60 seconds to launch your character!');print(_A);time.sleep(60);LAForeground();pyautogui.moveTo(F,G);pyautogui.click();print(_C+str(F)+','+str(G)+')');print('Character Launch In Progress!');print('30 Second Wait Time!');time.sleep(30);break
					break
				except ValueError:print(_D)
			elif H=='n':break
			else:print(_E)
		except ValueError:print(_F)
if __name__=='__main__':
	print(_A);retScreenSize=ScreenSetup();print(_A);time.sleep(1);buttonSetup=ButtonSetup();print(_A);time.sleep(1);timeSleepSettings=TimeSetup();print(_A);QueueDetection(retScreenSize);print(_A)
	while _B:TimeSleep(timeSleepSettings);MouseClick(retScreenSize);TimeSleep(timeSleepSettings);ButtonClick(buttonSetup)