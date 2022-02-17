g ='Type Error: You Have Entered An Incorrect Type! Please Enter Either Y or N'#line:1
f ='Input Error: Please Enter Either Y or N'#line:2
e ='n'#line:3
d ='Type Error: You Have Entered An Incorrect Type! Please Enter An Integer'#line:4
c ='y'#line:5
b =')'#line:6
a =','#line:7
Z ='Mouse Clicked At: ('#line:8
N =int #line:9
L =ValueError #line:10
G =True #line:11
F =input #line:12
C =str #line:13
B ='~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'#line:14
A =print #line:15
import time as D ,pyautogui as H ,pytesseract as M ,os #line:16
O =os .environ .get ('USERNAME')#line:17
P ='C:/Users/'+O +'/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'#line:18
from PIL import Image #line:19
M .pytesseract .tesseract_cmd =P #line:20
from random import randint as E #line:21
def Q ():#line:22
	O0O000OO00OOOOOO0 =H .size ()#line:23
	if C (O0O000OO00OOOOOO0 )=='Size(width=640, height=480)':A ('Using 640x480, Changing Randomx and Randomy');O00O0O0O0OO00O0O0 =286 ;OO0OOO0OOOO0O0OO0 =351 ;O000OOOO000O0O0OO =135 ;OO00O00O0O0O0O0O0 =301 #line:24
	elif C (O0O000OO00OOOOOO0 )=='Size(width=1280, height=720)':A ('Using 1280x720, Changing Randomx and Randomy');O00O0O0O0OO00O0O0 =573 ;OO0OOO0OOOO0O0OO0 =702 ;O000OOOO000O0O0OO =271 ;OO00O00O0O0O0O0O0 =602 #line:25
	elif C (O0O000OO00OOOOOO0 )=='Size(width=1920, height=1080)':A ('Using 1920x1080, Changing Randomx and Randomy');O00O0O0O0OO00O0O0 =382 ;OO0OOO0OOOO0O0OO0 =1582 ;O000OOOO000O0O0OO =181 ;OO00O00O0O0O0O0O0 =903 #line:26
	elif C (O0O000OO00OOOOOO0 )=='Size(width=2560, height=1440)':A ('Using 2560x1440, Changing Randomx and Randomy');O00O0O0O0OO00O0O0 =496 ;OO0OOO0OOOO0O0OO0 =2056 ;O000OOOO000O0O0OO =235 ;OO00O00O0O0O0O0O0 =1173 #line:27
	elif C (O0O000OO00OOOOOO0 )=='Size(width=2048, height=1080)':A ('Using 2048x1080, Changing Randomx and Randomy');O00O0O0O0OO00O0O0 =404 ;OO0OOO0OOOO0O0OO0 =1676 ;O000OOOO000O0O0OO =191 ;OO00O00O0O0O0O0O0 =957 #line:28
	elif C (O0O000OO00OOOOOO0 )=='Size(width=3440, height=1440)':A ('Using 3440x1440, Changing Randomx and Randomy');O00O0O0O0OO00O0O0 =500 ;OO0OOO0OOOO0O0OO0 =2900 ;O000OOOO000O0O0OO =220 ;OO00O00O0O0O0O0O0 =1173 #line:29
	elif C (O0O000OO00OOOOOO0 )=='Size(width=3840, height=2160)':A ('Using 3840x2160, Changing Randomx and Randomy');O00O0O0O0OO00O0O0 =572 ;OO0OOO0OOOO0O0OO0 =3084 ;O000OOOO000O0O0OO =286 ;OO00O00O0O0O0O0O0 =1759 #line:30
	elif C (O0O000OO00OOOOOO0 )=='Size(width=5120, height=1440)':A ('Using 5120x1440, Changing Randomx and Randomy');O00O0O0O0OO00O0O0 =744 ;OO0OOO0OOOO0O0OO0 =4009 ;O000OOOO000O0O0OO =220 ;OO00O00O0O0O0O0O0 =1173 #line:31
	elif C (O0O000OO00OOOOOO0 )=='Size(width=7680, height=4320)':A ('Using 7680x4320, Changing Randomx and Randomy');O00O0O0O0OO00O0O0 =1488 ;OO0OOO0OOOO0O0OO0 =6168 ;O000OOOO000O0O0OO =572 ;OO00O00O0O0O0O0O0 =3518 #line:32
	else :A ('Using Non-Supported Res, Changing Randomx and Randomy to Default Location!');A ('Please raise an issue on GitHub with your screen res for future custom support!');O00O0O0O0OO00O0O0 =382 ;OO0OOO0OOOO0O0OO0 =1582 ;O000OOOO000O0O0OO =181 ;OO00O00O0O0O0O0O0 =903 #line:33
	return O00O0O0O0OO00O0O0 ,OO0OOO0OOOO0O0OO0 ,O000OOOO000O0O0OO ,OO00O00O0O0O0O0O0 #line:34
def R ():#line:35
	OOOOO0O0OO0O0O000 ='This is to large of a time input!';O0OOO0O00OO0OO00O ='Must Type an Integer > 0';A ('Usage Just Type an Integer e.g. 30')#line:36
	while G :#line:37
		try :#line:38
			O0O00OO0OO0O0OOO0 =N (F ('Please Enter The Shortest Amount of Seconds To Wait Before Input - Recommended (30 seconds): '))#line:39
			if O0O00OO0OO0O0OOO0 <=0 :A (O0OOO0O00OO0OO00O )#line:40
			elif O0O00OO0OO0O0OOO0 >=4294967 :A (OOOOO0O0OO0O0O000 )#line:41
			else :#line:42
				O00OOOOO00OO00O0O =N (F ('Please Enter The Longest Amount of Seconds To Wait Before Input - Recommended (1200 seconds): '))#line:43
				if O00OOOOO00OO00O0O <=0 :A (O0OOO0O00OO0OO00O )#line:44
				elif O00OOOOO00OO00O0O <=O0O00OO0OO0O0OOO0 :A ('This should be not equal to or larger then the lowest amount in range')#line:45
				elif O00OOOOO00OO00O0O >=4294967 :A (OOOOO0O0OO0O0O000 )#line:46
				else :break #line:47
		except L :A ('Invalid Entry: Usage Just Type an Integer e.g. 30')#line:48
	return O0O00OO0OO0O0OOO0 ,O00OOOOO00OO00O0O #line:49
def S (O00OOOOO0OOOOOOOO ):O00O0O0000OO00O00 =O00OOOOO0OOOOOOOO ;OO0OOO0O0OOO00000 =E (O00O0O0000OO00O00 [0 ],O00O0O0000OO00O00 [1 ]);return OO0OOO0O0OOO00000 #line:50
def I (OOO00O0OO00O0OO00 ):OO0O0OO00OOO00O00 =OOO00O0OO00O0OO00 ;OOOOO0OO000O0000O =S (OO0O0OO00OOO00O00 );A ('Next Interaction Time: '+C (OOOOO0OO000O0000O )+' second(s) or '+C (OOOOO0OO000O0000O //60 )+' minute(s) (Integer Division Not Accurate Minute Representation)!');D .sleep (OOOOO0OO000O0000O )#line:51
def T (O0OOO0O00OOO0OOO0 ):OO0O000OO000O0000 =O0OOO0O00OOO0OOO0 ;O0OOOO0OO0OO0O00O =E (OO0O000OO000O0000 [0 ],OO0O000OO000O0000 [1 ]);OOO000OOOOOO00O00 =E (OO0O000OO000O0000 [2 ],OO0O000OO000O0000 [3 ]);return O0OOOO0OO0OO0O00O ,OOO000OOOOOO00O00 #line:52
def U (O0OO00OO0OOO0O0OO ):OO00OOOOO0O0OO00O =O0OO00OO0OOO0O0OO ;OO0O0O0OOOO000OOO =T (OO00OOOOO0O0OO00O );O0O00OOOOO0000000 =OO0O0O0OOOO000OOO [0 ];OO000000O0O0O00O0 =OO0O0O0OOOO000OOO [1 ];H .moveTo (O0O00OOOOO0000000 ,OO000000O0O0O00O0 );H .click ();A (Z +C (O0O00OOOOO0000000 )+a +C (OO000000O0O0O00O0 )+b )#line:53
def V ():#line:54
	OOOOO0OOO00OOOOO0 =['q','w','e','r','a','s','d','f'];A ('The Default Button Click List Is:');A (OOOOO0OOO00OOOOO0 )#line:55
	while G :#line:56
		try :#line:57
			O0OO0O0000O0OOO00 =C (F ('Would You Like To Add More Keys To The ButtonClickList? Enter (Y) or (N): ')).lower ()#line:58
			if O0OO0O0000O0OOO00 ==c :#line:59
				while G :#line:60
					try :#line:61
						O0OOOOOO00OOO0OOO =N (F ('How Many Keys Would You Like To Add To The List: '))#line:62
						for OOOO0O0O00O00O00O in range (O0OOOOOO00OOO0OOO ):OO0O00O0O00O0O00O =F ("Please Press a Key or Write The Key, Such As 'space' and then press enter: ");OOOOO0OOO00OOOOO0 .append (OO0O00O0O00O0O00O )#line:63
						break #line:64
					except L :A (d )#line:65
				break #line:66
			elif O0OO0O0000O0OOO00 ==e :O0OOOOOO00OOO0OOO =0 ;break #line:67
			else :A (f )#line:68
		except L :A (g )#line:69
	return OOOOO0OOO00OOOOO0 ,O0OOOOOO00OOO0OOO #line:70
def W (OO0O0000O00O00OO0 ):O0O0O00OOO00O0000 =OO0O0000O00O00OO0 ;O000OOO0OO00OO000 =O0O0O00OOO00O0000 [0 ];O0O0OO0O00O0O0O00 =O0O0O00OOO00O0000 [1 ]+7 ;O000O000000OOO000 =E (0 ,O0O0OO0O00O0O0O00 );OO0O000OO0O0O0O0O =O000OOO0OO00OO000 [O000O000000OOO000 ];H .press (OO0O000OO0O0O0O0O );A ('Button Clicked: '+OO0O000OO0O0O0O0O )#line:71
def X ():#line:72
	O0OOOO000O00O0OOO ='queueDetectionScreenshot.png';OO00O00O0OO0OOOO0 ='Sit Tight!';O0OO0OO0000O000O0 ='~Waiting 10 Seconds To Reanylse Screen!';OO0O000O000O00OOO ='Still in Queue :('#line:73
	while G :#line:74
		try :#line:75
			A ('Make Sure Nothing is covering your lost ark window, specifficaly the Queue Box!');O00000OO0OO0OO0O0 =C (F ('Would You Like To Start Queue Detection? Enter (Y) or (N): ')).lower ()#line:76
			if O00000OO0OO0OO0O0 ==c :#line:77
				try :#line:78
					while G :#line:79
						OOOOOO000O0O000OO =H .screenshot (region =(771 ,435 ,373 ,204 ));OOOOOO000O0O000OO .save (O0OOOO000O00O0OOO );O00OOO0000O000O0O =O0OOOO000O00O0OOO ;A (B );A ('Lost Ark Screen Being Analysed');D .sleep (1 );OOO0O0OOO0O0O000O =M .image_to_string (Image .open (O00OOO0000O000O0O ))#line:80
						if 'Waiting'in OOO0O0OOO0O0O000O :A (B );A (OO0O000O000O00OOO );A (O0OO0OO0000O000O0 );A (OO00O00O0OO0OOOO0 );A (B );D .sleep (9 )#line:81
						elif 'Warten'in OOO0O0OOO0O0O000O :A (B );A (OO0O000O000O00OOO );A (O0OO0OO0000O000O0 );A (OO00O00O0OO0OOOO0 );A (B );D .sleep (9 )#line:82
						elif 'Venter'in OOO0O0OOO0O0O000O :A (B );A (OO0O000O000O00OOO );A (O0OO0OO0000O000O0 );A (OO00O00O0OO0OOOO0 );A (B );D .sleep (9 )#line:83
						elif 'Attendre'in OOO0O0OOO0O0O000O :A (B );A (OO0O000O000O00OOO );A (O0OO0OO0000O000O0 );A (OO00O00O0OO0OOOO0 );A (B );D .sleep (9 )#line:84
						elif 'In attesa'in OOO0O0OOO0O0O000O :A (B );A (OO0O000O000O00OOO );A (O0OO0OO0000O000O0 );A (OO00O00O0OO0OOOO0 );A (B );D .sleep (9 )#line:85
						elif 'Bekleme'in OOO0O0OOO0O0O000O :A (B );A (OO0O000O000O00OOO );A (O0OO0OO0000O000O0 );A (OO00O00O0OO0OOOO0 );A (B );D .sleep (9 )#line:86
						else :OO0O000OOOOOOO000 =855 ;O00OOO0000000O00O =1014 ;A ('Out of Queue! :)');A ('Waiting 60 seconds to launch your character!');A (B );D .sleep (60 );H .moveTo (OO0O000OOOOOOO000 ,O00OOO0000000O00O );H .click ();A (Z +C (OO0O000OOOOOOO000 )+a +C (O00OOO0000000O00O )+b );A ('Character Launch In Progress!');A ('30 Second Wait Time!');D .sleep (30 );break #line:87
					break #line:88
				except L :A (d )#line:89
			elif O00000OO0OO0OO0O0 ==e :break #line:90
			else :A (f )#line:91
		except L :A (g )#line:92
if __name__ =='__main__':#line:93
	A (B );Y =Q ();A (B );D .sleep (1 );J =V ();A (B );A ('The Button Click List Is: ');A (J [0 ]);A (B );D .sleep (1 );K =R ();A (B );X ();A (B )#line:94
	while G :I (K );U (Y );I (K );W (J )