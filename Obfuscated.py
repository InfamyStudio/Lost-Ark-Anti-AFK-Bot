g ='Type Error: You Have Entered An Incorrect Type! Please Enter Either Y or N'#line:1
f ='Input Error: Please Enter Either Y or N'#line:2
e ='n'#line:3
d ='Type Error: You Have Entered An Incorrect Type! Please Enter An Integer'#line:4
c ='y'#line:5
b =')'#line:6
a =','#line:7
Z ='Mouse Clicked At: ('#line:8
N =int #line:9
I =ValueError #line:10
F =True #line:11
E =input #line:12
C ='~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'#line:13
B =str #line:14
A =print #line:15
import time as D ,pyautogui as H ,pytesseract as J ,os #line:16
O =os .environ .get ('USERNAME')#line:17
P ='C:/Users/'+O +'/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'#line:18
from PIL import Image #line:19
J .pytesseract .tesseract_cmd =P #line:20
from random import randint as G #line:21
def Q ():#line:22
	OOOOOO00000OO0OO0 =H .size ()#line:23
	if B (OOOOOO00000OO0OO0 )=='Size(width=640, height=480)':A ('Using 640x480, Changing Randomx and Randomy');OO0OOO0OO0OO00O00 =286 ;OOO00O00O0OOOO0OO =351 ;OO00O0O00O000O00O =135 ;OO0OO00OOOO000O00 =301 #line:24
	elif B (OOOOOO00000OO0OO0 )=='Size(width=1280, height=720)':A ('Using 1280x720, Changing Randomx and Randomy');OO0OOO0OO0OO00O00 =573 ;OOO00O00O0OOOO0OO =702 ;OO00O0O00O000O00O =271 ;OO0OO00OOOO000O00 =602 #line:25
	elif B (OOOOOO00000OO0OO0 )=='Size(width=1920, height=1080)':A ('Using 1920x1080, Changing Randomx and Randomy');OO0OOO0OO0OO00O00 =382 ;OOO00O00O0OOOO0OO =1582 ;OO00O0O00O000O00O =181 ;OO0OO00OOOO000O00 =903 #line:26
	elif B (OOOOOO00000OO0OO0 )=='Size(width=2560, height=1440)':A ('Using 2560x1440, Changing Randomx and Randomy');OO0OOO0OO0OO00O00 =496 ;OOO00O00O0OOOO0OO =2056 ;OO00O0O00O000O00O =235 ;OO0OO00OOOO000O00 =1173 #line:27
	elif B (OOOOOO00000OO0OO0 )=='Size(width=2048, height=1080)':A ('Using 2048x1080, Changing Randomx and Randomy');OO0OOO0OO0OO00O00 =404 ;OOO00O00O0OOOO0OO =1676 ;OO00O0O00O000O00O =191 ;OO0OO00OOOO000O00 =957 #line:28
	elif B (OOOOOO00000OO0OO0 )=='Size(width=3440, height=1440)':A ('Using 3440x1440, Changing Randomx and Randomy');OO0OOO0OO0OO00O00 =500 ;OOO00O00O0OOOO0OO =2900 ;OO00O0O00O000O00O =220 ;OO0OO00OOOO000O00 =1173 #line:29
	elif B (OOOOOO00000OO0OO0 )=='Size(width=3840, height=2160)':A ('Using 3840x2160, Changing Randomx and Randomy');OO0OOO0OO0OO00O00 =572 ;OOO00O00O0OOOO0OO =3084 ;OO00O0O00O000O00O =286 ;OO0OO00OOOO000O00 =1759 #line:30
	elif B (OOOOOO00000OO0OO0 )=='Size(width=5120, height=1440)':A ('Using 5120x1440, Changing Randomx and Randomy');OO0OOO0OO0OO00O00 =744 ;OOO00O00O0OOOO0OO =4009 ;OO00O0O00O000O00O =220 ;OO0OO00OOOO000O00 =1173 #line:31
	elif B (OOOOOO00000OO0OO0 )=='Size(width=7680, height=4320)':A ('Using 7680x4320, Changing Randomx and Randomy');OO0OOO0OO0OO00O00 =1488 ;OOO00O00O0OOOO0OO =6168 ;OO00O0O00O000O00O =572 ;OO0OO00OOOO000O00 =3518 #line:32
	else :A ('Using Non-Supported Res, Changing Randomx and Randomy to Default Location!');A ('Please raise an issue on GitHub with your screen res for future custom support!');OO0OOO0OO0OO00O00 =382 ;OOO00O00O0OOOO0OO =1582 ;OO00O0O00O000O00O =181 ;OO0OO00OOOO000O00 =903 #line:33
	return OO0OOO0OO0OO00O00 ,OOO00O00O0OOOO0OO ,OO00O0O00O000O00O ,OO0OO00OOOO000O00 #line:34
def R ():#line:35
	O0O0OOO000O00O000 ='This is to large of a time input!';OO00O00000OOOOOO0 ='Must Type an Integer > 0';A ('Usage Just Type an Integer e.g. 30')#line:36
	while F :#line:37
		try :#line:38
			OO0O00O0OO0O00O00 =N (E ('Please Enter The Shortest Amount of Seconds To Wait Before Input - Recommended (30 seconds): '))#line:39
			if OO0O00O0OO0O00O00 <=0 :A (OO00O00000OOOOOO0 )#line:40
			elif OO0O00O0OO0O00O00 >=4294967 :A (O0O0OOO000O00O000 )#line:41
			else :#line:42
				O00O0O00OO000O000 =N (E ('Please Enter The Longest Amount of Seconds To Wait Before Input - Recommended (1200 seconds): '))#line:43
				if O00O0O00OO000O000 <=0 :A (OO00O00000OOOOOO0 )#line:44
				elif O00O0O00OO000O000 <=OO0O00O0OO0O00O00 :A ('This should be not equal to or larger then the lowest amount in range')#line:45
				elif O00O0O00OO000O000 >=4294967 :A (O0O0OOO000O00O000 )#line:46
				else :break #line:47
		except I :A ('Invalid Entry: Usage Just Type an Integer e.g. 30')#line:48
	return OO0O00O0OO0O00O00 ,O00O0O00OO000O000 #line:49
def S (O0OO0OOO0O0000O00 ):O0O0OO00O00OOOO00 =O0OO0OOO0O0000O00 ;O0O00O000OO0O00OO =G (O0O0OO00O00OOOO00 [0 ],O0O0OO00O00OOOO00 [1 ]);return O0O00O000OO0O00OO #line:50
def K (O0OO0O0OO0OOO0000 ):O000OOOOO000000OO =O0OO0O0OO0OOO0000 ;OOO000OOOOOOO00OO =S (O000OOOOO000000OO );A ('Next Interaction Time: '+B (OOO000OOOOOOO00OO )+' second(s) or '+B (OOO000OOOOOOO00OO //60 )+' minute(s) (Integer Division Not Accurate Minute Representation)!');D .sleep (OOO000OOOOOOO00OO )#line:51
def T (OO0O0OOO000OOO0O0 ):OOOO0OO0O000000OO =OO0O0OOO000OOO0O0 ;OO0O0OOO00O0000O0 =G (OOOO0OO0O000000OO [0 ],OOOO0OO0O000000OO [1 ]);OO00OO0O0O0OO00O0 =G (OOOO0OO0O000000OO [2 ],OOOO0OO0O000000OO [3 ]);return OO0O0OOO00O0000O0 ,OO00OO0O0O0OO00O0 #line:52
def U (OOOO00O0OOO0OO0OO ):OO0OOOOO0O00OOO0O =OOOO00O0OOO0OO0OO ;O00O0OOOOO0O000OO =T (OO0OOOOO0O00OOO0O );OOOOO0O000OOO0OO0 =O00O0OOOOO0O000OO [0 ];OOOOOO000O0000O00 =O00O0OOOOO0O000OO [1 ];H .moveTo (OOOOO0O000OOO0OO0 ,OOOOOO000O0000O00 );H .click ();A (Z +B (OOOOO0O000OOO0OO0 )+a +B (OOOOOO000O0000O00 )+b )#line:53
def V ():#line:54
	OO0000OO0OOO000O0 =['q','w','e','r','a','s','d','f'];A ('The Default Button Click List Is:');A (OO0000OO0OOO000O0 )#line:55
	while F :#line:56
		try :#line:57
			O0OOO000O0O00OOO0 =B (E ('Would You Like To Add More Keys To The ButtonClickList? Enter (Y) or (N): ')).lower ()#line:58
			if O0OOO000O0O00OOO0 ==c :#line:59
				while F :#line:60
					try :#line:61
						O00000O0O00OO000O =N (E ('How Many Keys Would You Like To Add To The List: '))#line:62
						for OOOO000OO0OO0O00O in range (O00000O0O00OO000O ):O0O0000O00O000O00 =E ("Please Press a Key or Write The Key, Such As 'space' and then press enter: ");OO0000OO0OOO000O0 .append (O0O0000O00O000O00 )#line:63
						break #line:64
					except I :A (d )#line:65
				break #line:66
			elif O0OOO000O0O00OOO0 ==e :O00000O0O00OO000O =0 ;break #line:67
			else :A (f )#line:68
		except I :A (g )#line:69
	return OO0000OO0OOO000O0 ,O00000O0O00OO000O #line:70
def W (O0OO0OO00OOOO0O0O ):O00000O0O00000O0O =O0OO0OO00OOOO0O0O ;O0OO0O000OO0OOO00 =O00000O0O00000O0O [0 ];O0OO0O0OO0OO0O000 =O00000O0O00000O0O [1 ]+7 ;A (B (O0OO0O0OO0OO0O000 ));O0OOO00O0000O0OO0 =G (0 ,O0OO0O0OO0OO0O000 );O0O00O00OO0OOOOO0 =O0OO0O000OO0OOO00 [O0OOO00O0000O0OO0 ];H .press (O0O00O00OO0OOOOO0 );A ('Button Clicked: '+O0O00O00OO0OOOOO0 )#line:71
def X ():#line:72
	O0O0O0O0O0O000OO0 ='queueDetectionScreenshot.png'#line:73
	while F :#line:74
		try :#line:75
			A ('Make Sure Nothing is covering your lost ark window, specifficaly the Queue Box!');O0000O000OO000000 =B (E ('Would You Like To Start Queue Detection? Enter (Y) or (N): ')).lower ()#line:76
			if O0000O000OO000000 ==c :#line:77
				try :#line:78
					while F :#line:79
						OO000O0000OOO0OO0 =H .screenshot (region =(771 ,435 ,373 ,204 ));OO000O0000OOO0OO0 .save (O0O0O0O0O0O000OO0 );OO000O0OO0O00OO0O =O0O0O0O0O0O000OO0 ;A (C );A ('Lost Ark Screen Being Analysed');D .sleep (1 );O0OOOOO0OO000000O =J .image_to_string (Image .open (OO000O0OO0O00OO0O ))#line:80
						if 'Waiting'in O0OOOOO0OO000000O :A (C );A ('Still in Queue :(');A ('~Waiting 10 Seconds To Reanylse Screen!');A ('Sit Tight!');A (C );D .sleep (9 )#line:81
						else :OOOOO00O0O00OO000 =855 ;OOO0OO0OOOO0OOO0O =1014 ;A ('Out of Queue! :)');A ('Waiting 60 seconds to launch your character!');A (C );D .sleep (60 );H .moveTo (OOOOO00O0O00OO000 ,OOO0OO0OOOO0OOO0O );H .click ();A (Z +B (OOOOO00O0O00OO000 )+a +B (OOO0OO0OOOO0OOO0O )+b );A ('Character Launch In Progress!');A ('30 Second Wait Time!');D .sleep (30 );break #line:82
					break #line:83
				except I :A (d )#line:84
			elif O0000O000OO000000 ==e :break #line:85
			else :A (f )#line:86
		except I :A (g )#line:87
if __name__ =='__main__':#line:88
	A (C );Y =Q ();A (C );D .sleep (1 );L =V ();A (C );A ('The Button Click List Is: ');A (L [0 ]);A (C );D .sleep (1 );M =R ();A (C );X ();A (C )#line:89
	while F :K (M );U (Y );K (M );W (L )