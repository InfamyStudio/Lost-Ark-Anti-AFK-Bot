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
	OO00O0OO00O0O00O0 =H .size ()#line:23
	if C (OO00O0OO00O0O00O0 )=='Size(width=640, height=480)':A ('Using 640x480, Changing Randomx and Randomy');O00O0OO00OOO00OOO =286 ;OO0OOOOO0000OO00O =351 ;O00O0OO0O0OO00OOO =135 ;OOOOOO0OOOOO0O0OO =301 #line:24
	elif C (OO00O0OO00O0O00O0 )=='Size(width=1280, height=720)':A ('Using 1280x720, Changing Randomx and Randomy');O00O0OO00OOO00OOO =573 ;OO0OOOOO0000OO00O =702 ;O00O0OO0O0OO00OOO =271 ;OOOOOO0OOOOO0O0OO =602 #line:25
	elif C (OO00O0OO00O0O00O0 )=='Size(width=1920, height=1080)':A ('Using 1920x1080, Changing Randomx and Randomy');O00O0OO00OOO00OOO =382 ;OO0OOOOO0000OO00O =1582 ;O00O0OO0O0OO00OOO =181 ;OOOOOO0OOOOO0O0OO =903 #line:26
	elif C (OO00O0OO00O0O00O0 )=='Size(width=2560, height=1440)':A ('Using 2560x1440, Changing Randomx and Randomy');O00O0OO00OOO00OOO =496 ;OO0OOOOO0000OO00O =2056 ;O00O0OO0O0OO00OOO =235 ;OOOOOO0OOOOO0O0OO =1173 #line:27
	elif C (OO00O0OO00O0O00O0 )=='Size(width=2048, height=1080)':A ('Using 2048x1080, Changing Randomx and Randomy');O00O0OO00OOO00OOO =404 ;OO0OOOOO0000OO00O =1676 ;O00O0OO0O0OO00OOO =191 ;OOOOOO0OOOOO0O0OO =957 #line:28
	elif C (OO00O0OO00O0O00O0 )=='Size(width=3440, height=1440)':A ('Using 3440x1440, Changing Randomx and Randomy');O00O0OO00OOO00OOO =500 ;OO0OOOOO0000OO00O =2900 ;O00O0OO0O0OO00OOO =220 ;OOOOOO0OOOOO0O0OO =1173 #line:29
	elif C (OO00O0OO00O0O00O0 )=='Size(width=3840, height=2160)':A ('Using 3840x2160, Changing Randomx and Randomy');O00O0OO00OOO00OOO =572 ;OO0OOOOO0000OO00O =3084 ;O00O0OO0O0OO00OOO =286 ;OOOOOO0OOOOO0O0OO =1759 #line:30
	elif C (OO00O0OO00O0O00O0 )=='Size(width=5120, height=1440)':A ('Using 5120x1440, Changing Randomx and Randomy');O00O0OO00OOO00OOO =744 ;OO0OOOOO0000OO00O =4009 ;O00O0OO0O0OO00OOO =220 ;OOOOOO0OOOOO0O0OO =1173 #line:31
	elif C (OO00O0OO00O0O00O0 )=='Size(width=7680, height=4320)':A ('Using 7680x4320, Changing Randomx and Randomy');O00O0OO00OOO00OOO =1488 ;OO0OOOOO0000OO00O =6168 ;O00O0OO0O0OO00OOO =572 ;OOOOOO0OOOOO0O0OO =3518 #line:32
	else :A ('Using Non-Supported Res, Changing Randomx and Randomy to Default Location!');A ('Please raise an issue on GitHub with your screen res for future custom support!');O00O0OO00OOO00OOO =382 ;OO0OOOOO0000OO00O =1582 ;O00O0OO0O0OO00OOO =181 ;OOOOOO0OOOOO0O0OO =903 #line:33
	return O00O0OO00OOO00OOO ,OO0OOOOO0000OO00O ,O00O0OO0O0OO00OOO ,OOOOOO0OOOOO0O0OO #line:34
def R ():#line:35
	O0OO0OO0O00OOO0O0 ='This is to large of a time input!';OOO0O00000O00000O ='Must Type an Integer > 0';A ('Usage Just Type an Integer e.g. 30')#line:36
	while G :#line:37
		try :#line:38
			O000OOOO00000OOO0 =N (F ('Please Enter The Shortest Amount of Seconds To Wait Before Input - Recommended (30 seconds): '))#line:39
			if O000OOOO00000OOO0 <=0 :A (OOO0O00000O00000O )#line:40
			elif O000OOOO00000OOO0 >=4294967 :A (O0OO0OO0O00OOO0O0 )#line:41
			else :#line:42
				O0OOOOOOO0OO0OOOO =N (F ('Please Enter The Longest Amount of Seconds To Wait Before Input - Recommended (1200 seconds): '))#line:43
				if O0OOOOOOO0OO0OOOO <=0 :A (OOO0O00000O00000O )#line:44
				elif O0OOOOOOO0OO0OOOO <=O000OOOO00000OOO0 :A ('This should be not equal to or larger then the lowest amount in range')#line:45
				elif O0OOOOOOO0OO0OOOO >=4294967 :A (O0OO0OO0O00OOO0O0 )#line:46
				else :break #line:47
		except L :A ('Invalid Entry: Usage Just Type an Integer e.g. 30')#line:48
	return O000OOOO00000OOO0 ,O0OOOOOOO0OO0OOOO #line:49
def S (O0OOO0000O00OO000 ):O0OO0O00000O0000O =O0OOO0000O00OO000 ;OOO0O0O0000O0O00O =E (O0OO0O00000O0000O [0 ],O0OO0O00000O0000O [1 ]);return OOO0O0O0000O0O00O #line:50
def I (O00000O00OOOO0OOO ):O0OOOOOOOO0O0OOO0 =O00000O00OOOO0OOO ;OO0O0O0OOOOOO0000 =S (O0OOOOOOOO0O0OOO0 );A ('Next Interaction Time: '+C (OO0O0O0OOOOOO0000 )+' second(s) or '+C (OO0O0O0OOOOOO0000 //60 )+' minute(s) (Integer Division Not Accurate Minute Representation)!');D .sleep (OO0O0O0OOOOOO0000 )#line:51
def T (O0OO0O00O0O00O000 ):OO00OO0OO00000000 =O0OO0O00O0O00O000 ;O0OOOOOO0OOOOOO0O =E (OO00OO0OO00000000 [0 ],OO00OO0OO00000000 [1 ]);O00OOOO0O00O0O0OO =E (OO00OO0OO00000000 [2 ],OO00OO0OO00000000 [3 ]);return O0OOOOOO0OOOOOO0O ,O00OOOO0O00O0O0OO #line:52
def U (O000OO0O000OO00O0 ):OOO000O0OO00O00O0 =O000OO0O000OO00O0 ;OO0OOOOO0O0O00O00 =T (OOO000O0OO00O00O0 );OOOO00000OOOOOOOO =OO0OOOOO0O0O00O00 [0 ];O0OO0O0O0O0000OOO =OO0OOOOO0O0O00O00 [1 ];H .moveTo (OOOO00000OOOOOOOO ,O0OO0O0O0O0000OOO );H .click ();A (Z +C (OOOO00000OOOOOOOO )+a +C (O0OO0O0O0O0000OOO )+b )#line:53
def V ():#line:54
	O00O00OO0OO00O0O0 =['q','w','e','r','a','s','d','f'];A ('The Default Button Click List Is:');A (O00O00OO0OO00O0O0 )#line:55
	while G :#line:56
		try :#line:57
			OO0O0O000OOO0OO00 =C (F ('Would You Like To Add More Keys To The ButtonClickList? Enter (Y) or (N): ')).lower ()#line:58
			if OO0O0O000OOO0OO00 ==c :#line:59
				while G :#line:60
					try :#line:61
						OOO00OO0O00OOO0O0 =N (F ('How Many Keys Would You Like To Add To The List: '))#line:62
						for OO0000O0OO0O00O00 in range (OOO00OO0O00OOO0O0 ):O0OO00OO0O0O0OO0O =F ("Please Press a Key or Write The Key, Such As 'space' and then press enter: ");O00O00OO0OO00O0O0 .append (O0OO00OO0O0O0OO0O )#line:63
						break #line:64
					except L :A (d )#line:65
				break #line:66
			elif OO0O0O000OOO0OO00 ==e :OOO00OO0O00OOO0O0 =0 ;break #line:67
			else :A (f )#line:68
		except L :A (g )#line:69
	return O00O00OO0OO00O0O0 ,OOO00OO0O00OOO0O0 #line:70
def W (O0O0OOO0O0O00OO0O ):O00O0OOOO0OOO00OO =O0O0OOO0O0O00OO0O ;OO0O00O00OO0O0000 =O00O0OOOO0OOO00OO [0 ];OO00O0000O0OOO0OO =O00O0OOOO0OOO00OO [1 ]+7 ;A (C (OO00O0000O0OOO0OO ));O000OO0O00000O0O0 =E (0 ,OO00O0000O0OOO0OO );O0000O0OO0OOOOO00 =OO0O00O00OO0O0000 [O000OO0O00000O0O0 ];H .press (O0000O0OO0OOOOO00 );A ('Button Clicked: '+O0000O0OO0OOOOO00 )#line:71
def X ():#line:72
	O0OO00OOO00O00000 ='queueDetectionScreenshot.png';OO00O0O0OOO000O00 ='Sit Tight!';O000000O000O0O000 ='~Waiting 10 Seconds To Reanylse Screen!';OO0O0OO00OO000OOO ='Still in Queue :('#line:73
	while G :#line:74
		try :#line:75
			A ('Make Sure Nothing is covering your lost ark window, specifficaly the Queue Box!');O0OOOO0OOOO00000O =C (F ('Would You Like To Start Queue Detection? Enter (Y) or (N): ')).lower ()#line:76
			if O0OOOO0OOOO00000O ==c :#line:77
				try :#line:78
					while G :#line:79
						OO0OO000OO0OOOO0O =H .screenshot (region =(771 ,435 ,373 ,204 ));OO0OO000OO0OOOO0O .save (O0OO00OOO00O00000 );O000OOOO0O0OO0000 =O0OO00OOO00O00000 ;A (B );A ('Lost Ark Screen Being Analysed');D .sleep (1 );O0O0O000OO00OO0O0 =M .image_to_string (Image .open (O000OOOO0O0OO0000 ))#line:80
						if 'Waiting'in O0O0O000OO00OO0O0 :A (B );A (OO0O0OO00OO000OOO );A (O000000O000O0O000 );A (OO00O0O0OOO000O00 );A (B );D .sleep (9 )#line:81
						elif 'Warten'in O0O0O000OO00OO0O0 :A (B );A (OO0O0OO00OO000OOO );A (O000000O000O0O000 );A (OO00O0O0OOO000O00 );A (B );D .sleep (9 )#line:82
						elif 'Venter'in O0O0O000OO00OO0O0 :A (B );A (OO0O0OO00OO000OOO );A (O000000O000O0O000 );A (OO00O0O0OOO000O00 );A (B );D .sleep (9 )#line:83
						elif 'Attendre'in O0O0O000OO00OO0O0 :A (B );A (OO0O0OO00OO000OOO );A (O000000O000O0O000 );A (OO00O0O0OOO000O00 );A (B );D .sleep (9 )#line:84
						elif 'In attesa'in O0O0O000OO00OO0O0 :A (B );A (OO0O0OO00OO000OOO );A (O000000O000O0O000 );A (OO00O0O0OOO000O00 );A (B );D .sleep (9 )#line:85
						elif 'Bekleme'in O0O0O000OO00OO0O0 :A (B );A (OO0O0OO00OO000OOO );A (O000000O000O0O000 );A (OO00O0O0OOO000O00 );A (B );D .sleep (9 )#line:86
						else :O00OOO00OOO000OOO =855 ;O0000000OOOOOO0O0 =1014 ;A ('Out of Queue! :)');A ('Waiting 60 seconds to launch your character!');A (B );D .sleep (60 );H .moveTo (O00OOO00OOO000OOO ,O0000000OOOOOO0O0 );H .click ();A (Z +C (O00OOO00OOO000OOO )+a +C (O0000000OOOOOO0O0 )+b );A ('Character Launch In Progress!');A ('30 Second Wait Time!');D .sleep (30 );break #line:87
					break #line:88
				except L :A (d )#line:89
			elif O0OOOO0OOOO00000O ==e :break #line:90
			else :A (f )#line:91
		except L :A (g )#line:92
if __name__ =='__main__':#line:93
	A (B );Y =Q ();A (B );D .sleep (1 );J =V ();A (B );A ('The Button Click List Is: ');A (J [0 ]);A (B );D .sleep (1 );K =R ();A (B );X ();A (B )#line:94
	while G :I (K );U (Y );I (K );W (J )