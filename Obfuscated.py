b =')'#line:1
a =','#line:2
Z ='Mouse Clicked At: ('#line:3
N =ValueError #line:4
M =int #line:5
G ='~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'#line:6
F =True #line:7
E =input #line:8
B =str #line:9
A =print #line:10
import time as C ,pyautogui as H ,pytesseract as I ,os #line:11
O =os .environ .get ('USERNAME')#line:12
P ='C:/Users/'+O +'/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'#line:13
from PIL import Image #line:14
I .pytesseract .tesseract_cmd =P #line:15
from random import randint as D #line:16
def Q ():#line:17
	O0O00OO0O000OOO0O =H .size ()#line:18
	if B (O0O00OO0O000OOO0O )=='Size(width=640, height=480)':A ('Using 640x480, Changing Randomx and Randomy');OOO00OOO0OO0OO00O =286 ;O00O0O00000O0000O =351 ;OOO0O0O0OO00O0O00 =135 ;OOO0O00OOOOOO000O =301 #line:19
	elif B (O0O00OO0O000OOO0O )=='Size(width=1280, height=720)':A ('Using 1280x720, Changing Randomx and Randomy');OOO00OOO0OO0OO00O =573 ;O00O0O00000O0000O =702 ;OOO0O0O0OO00O0O00 =271 ;OOO0O00OOOOOO000O =602 #line:20
	elif B (O0O00OO0O000OOO0O )=='Size(width=1920, height=1080)':A ('Using 1920x1080, Changing Randomx and Randomy');OOO00OOO0OO0OO00O =382 ;O00O0O00000O0000O =1582 ;OOO0O0O0OO00O0O00 =181 ;OOO0O00OOOOOO000O =903 #line:21
	elif B (O0O00OO0O000OOO0O )=='Size(width=2560, height=1440)':A ('Using 2560x1440, Changing Randomx and Randomy');OOO00OOO0OO0OO00O =496 ;O00O0O00000O0000O =2056 ;OOO0O0O0OO00O0O00 =235 ;OOO0O00OOOOOO000O =1173 #line:22
	elif B (O0O00OO0O000OOO0O )=='Size(width=2048, height=1080)':A ('Using 2048x1080, Changing Randomx and Randomy');OOO00OOO0OO0OO00O =404 ;O00O0O00000O0000O =1676 ;OOO0O0O0OO00O0O00 =191 ;OOO0O00OOOOOO000O =957 #line:23
	elif B (O0O00OO0O000OOO0O )=='Size(width=3440, height=1440)':A ('Using 3440x1440, Changing Randomx and Randomy');OOO00OOO0OO0OO00O =500 ;O00O0O00000O0000O =2900 ;OOO0O0O0OO00O0O00 =220 ;OOO0O00OOOOOO000O =1173 #line:24
	elif B (O0O00OO0O000OOO0O )=='Size(width=3840, height=2160)':A ('Using 3840x2160, Changing Randomx and Randomy');OOO00OOO0OO0OO00O =572 ;O00O0O00000O0000O =3084 ;OOO0O0O0OO00O0O00 =286 ;OOO0O00OOOOOO000O =1759 #line:25
	elif B (O0O00OO0O000OOO0O )=='Size(width=5120, height=1440)':A ('Using 5120x1440, Changing Randomx and Randomy');OOO00OOO0OO0OO00O =744 ;O00O0O00000O0000O =4009 ;OOO0O0O0OO00O0O00 =220 ;OOO0O00OOOOOO000O =1173 #line:26
	elif B (O0O00OO0O000OOO0O )=='Size(width=7680, height=4320)':A ('Using 7680x4320, Changing Randomx and Randomy');OOO00OOO0OO0OO00O =1488 ;O00O0O00000O0000O =6168 ;OOO0O0O0OO00O0O00 =572 ;OOO0O00OOOOOO000O =3518 #line:27
	else :A ('Using Non-Supported Res, Changing Randomx and Randomy to Default Location!');A ('Please raise an issue on GitHub with your screen res for future custom support!');OOO00OOO0OO0OO00O =382 ;O00O0O00000O0000O =1582 ;OOO0O0O0OO00O0O00 =181 ;OOO0O00OOOOOO000O =903 #line:28
	return OOO00OOO0OO0OO00O ,O00O0O00000O0000O ,OOO0O0O0OO00O0O00 ,OOO0O00OOOOOO000O #line:29
def R ():#line:30
	O0O00OO000O0O0000 ='This is to large of a time input!';OOOO0OOO000O0000O ='Must Type an Integer > 0';A ('Usage Just Type an Integer e.g. 30')#line:31
	while F :#line:32
		try :#line:33
			O000OO00O0O000OO0 =M (E ('Please Enter The Shortest Amount of Seconds To Wait Before Input - Recommended (30 seconds): '))#line:34
			if O000OO00O0O000OO0 <=0 :A (OOOO0OOO000O0000O )#line:35
			elif O000OO00O0O000OO0 >=4294967 :A (O0O00OO000O0O0000 )#line:36
			else :#line:37
				O0O0O0OOO0000O000 =M (E ('Please Enter The Longest Amount of Seconds To Wait Before Input - Recommended (1200 seconds): '))#line:38
				if O0O0O0OOO0000O000 <=0 :A (OOOO0OOO000O0000O )#line:39
				elif O0O0O0OOO0000O000 <=O000OO00O0O000OO0 :A ('This should be not equal to or larger then the lowest amount in range')#line:40
				elif O0O0O0OOO0000O000 >=4294967 :A (O0O00OO000O0O0000 )#line:41
				else :break #line:42
		except N :A ('Invalid Entry: Usage Just Type an Integer e.g. 30')#line:43
	return O000OO00O0O000OO0 ,O0O0O0OOO0000O000 #line:44
def S (O0OO0O0O0OO00O0OO ):OO0000O000000O000 =O0OO0O0O0OO00O0OO ;O00000000000000OO =D (OO0000O000000O000 [0 ],OO0000O000000O000 [1 ]);return O00000000000000OO #line:45
def J (O0000000OO0OOO0O0 ):O000000OO0O000OOO =O0000000OO0OOO0O0 ;O00O0O0O00O0O0OO0 =S (O000000OO0O000OOO );A ('Next Interaction Time: '+B (O00O0O0O00O0O0OO0 )+' second(s) or '+B (O00O0O0O00O0O0OO0 //60 )+' minute(s) (Integer Division Not Accurate Minute Representation)!');C .sleep (O00O0O0O00O0O0OO0 )#line:46
def T (O0O0OOO00OOO0000O ):OOOO0O0OO0OO0OO00 =O0O0OOO00OOO0000O ;O00O00O00OOO0O0O0 =D (OOOO0O0OO0OO0OO00 [0 ],OOOO0O0OO0OO0OO00 [1 ]);O00OOOOO000OO000O =D (OOOO0O0OO0OO0OO00 [2 ],OOOO0O0OO0OO0OO00 [3 ]);return O00O00O00OOO0O0O0 ,O00OOOOO000OO000O #line:47
def U (O0OO0000000000000 ):OOOOOO000OOOOO0OO =O0OO0000000000000 ;O0000O0O000O0OO0O =T (OOOOOO000OOOOO0OO );OO0OOO00O0OOOO000 =O0000O0O000O0OO0O [0 ];O0O0OOOO000OO0O0O =O0000O0O000O0OO0O [1 ];H .moveTo (OO0OOO00O0OOOO000 ,O0O0OOOO000OO0O0O );H .click ();A (Z +B (OO0OOO00O0OOOO000 )+a +B (O0O0OOOO000OO0O0O )+b )#line:48
def V ():#line:49
	OO0O0O000O0O0O000 =['q','w','e','r','a','s','d','f'];A ('The Default Button Click List Is:');A (OO0O0O000O0O0O000 )#line:50
	while F :#line:51
		try :#line:52
			OOOO0OOOO000OOOOO =B (E ('Would You Like To Add More Keys To The ButtonClickList? Enter (Y) or (N): ')).lower ()#line:53
			if OOOO0OOOO000OOOOO =='y':#line:54
				while F :#line:55
					try :#line:56
						OOO0O00O000O0OO00 =M (E ('How Many Keys Would You Like To Add To The List: '))#line:57
						for O000OOOOO00OO0OOO in range (OOO0O00O000O0OO00 ):O0000O0O000OO0OO0 =E ("Please Press a Key or Write The Key, Such As 'space' and then press enter: ");OO0O0O000O0O0O000 .append (O0000O0O000OO0OO0 )#line:58
						break #line:59
					except N :A ('Type Error: You Have Entered An Incorrect Type! Please Enter An Integer')#line:60
				break #line:61
			elif OOOO0OOOO000OOOOO =='n':OOO0O00O000O0OO00 =0 ;break #line:62
			else :A ('Input Error: Please Enter Either Y or N')#line:63
		except N :A ('Type Error: You Have Entered An Incorrect Type! Please Enter Either Y or N')#line:64
	return OO0O0O000O0O0O000 ,OOO0O00O000O0OO00 #line:65
def W (O0O00O000O0O0OO00 ):O000O0O0O00O0O0O0 =O0O00O000O0O0OO00 ;OO00OOOO0OO0O000O =O000O0O0O00O0O0O0 [0 ];O0O000000000O0O00 =O000O0O0O00O0O0O0 [1 ]+7 ;A (B (O0O000000000O0O00 ));OO00OOOOOOO0OO00O =D (0 ,O0O000000000O0O00 );OOOO00OO0O0O0O0OO =OO00OOOO0OO0O000O [OO00OOOOOOO0OO00O ];H .press (OOOO00OO0O0O0O0OO );A ('Button Clicked: '+OOOO00OO0O0O0O0OO )#line:66
def X ():#line:67
	OO00O00O0O0000O00 ='queueDetectionScreenshot.png'#line:68
	while F :#line:69
		OO000O000000OO000 =H .screenshot (region =(771 ,435 ,373 ,204 ));OO000O000000OO000 .save (OO00O00O0O0000O00 );OOO000000OOO00OO0 =OO00O00O0O0000O00 ;A ('Lost Ark Screen Being Analysed');OOO0O0OOO0000OO00 =I .image_to_string (Image .open (OOO000000OOO00OO0 ))#line:70
		if 'Waiting'in OOO0O0OOO0000OO00 :A ('Still in Queue :(');A ('~Waiting 10 Seconds To Reanylse Screen!');A ('Sit Tight!');C .sleep (10 )#line:71
		else :OO0OOOOO00O0OO00O =855 ;O00O0O0OOO0000OOO =1014 ;A ('Out of Queue! :)');A ('Waiting 60 seconds to launch your character!');C .sleep (60 );H .moveTo (OO0OOOOO00O0OO00O ,O00O0O0OOO0000OOO );H .click ();A (Z +B (OO0OOOOO00O0OO00O )+a +B (O00O0O0OOO0000OOO )+b );A ('Character Launch In Progress!');A ('30 Second Wait Time!');C .sleep (30 );break #line:72
if __name__ =='__main__':#line:73
	A (G );Y =Q ();A (G );C .sleep (2 );K =V ();A ('The Button Click List Is: ');A (K [0 ]);A (G );C .sleep (2 );L =R ();A (G );X ();A (G )#line:74
	while F :J (L );U (Y );J (L );W (K )