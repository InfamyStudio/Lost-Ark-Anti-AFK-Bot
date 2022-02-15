N =ValueError #line:1
M =int #line:2
G ='~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'#line:3
F =True #line:4
E =input #line:5
B =str #line:6
A =print #line:7
import time as C ,pyautogui as H ,pytesseract as I ,os #line:8
O =os .environ .get ('USERNAME')#line:9
P ='C:/Users/'+O +'/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'#line:10
from PIL import Image #line:11
I .pytesseract .tesseract_cmd =P #line:12
from random import randint as D #line:13
def Q ():#line:14
	O0OO0OO00OO0O0000 =H .size ()#line:15
	if B (O0OO0OO00OO0O0000 )=='Size(width=640, height=480)':A ('Using 640x480, Changing Randomx and Randomy');OOO0OOOO00OOOO00O =286 ;OO0O0000OO0OO00O0 =351 ;OOOOOO00OOOOOO0O0 =135 ;OO0OO0O00O0000OO0 =301 #line:16
	elif B (O0OO0OO00OO0O0000 )=='Size(width=1280, height=720)':A ('Using 1280x720, Changing Randomx and Randomy');OOO0OOOO00OOOO00O =573 ;OO0O0000OO0OO00O0 =702 ;OOOOOO00OOOOOO0O0 =271 ;OO0OO0O00O0000OO0 =602 #line:17
	elif B (O0OO0OO00OO0O0000 )=='Size(width=1920, height=1080)':A ('Using 1920x1080, Changing Randomx and Randomy');OOO0OOOO00OOOO00O =382 ;OO0O0000OO0OO00O0 =1582 ;OOOOOO00OOOOOO0O0 =181 ;OO0OO0O00O0000OO0 =903 #line:18
	elif B (O0OO0OO00OO0O0000 )=='Size(width=2560, height=1440)':A ('Using 2560x1440, Changing Randomx and Randomy');OOO0OOOO00OOOO00O =496 ;OO0O0000OO0OO00O0 =2056 ;OOOOOO00OOOOOO0O0 =235 ;OO0OO0O00O0000OO0 =1173 #line:19
	elif B (O0OO0OO00OO0O0000 )=='Size(width=2048, height=1080)':A ('Using 2048x1080, Changing Randomx and Randomy');OOO0OOOO00OOOO00O =404 ;OO0O0000OO0OO00O0 =1676 ;OOOOOO00OOOOOO0O0 =191 ;OO0OO0O00O0000OO0 =957 #line:20
	elif B (O0OO0OO00OO0O0000 )=='Size(width=3440, height=1440)':A ('Using 3440x1440, Changing Randomx and Randomy');OOO0OOOO00OOOO00O =500 ;OO0O0000OO0OO00O0 =2900 ;OOOOOO00OOOOOO0O0 =220 ;OO0OO0O00O0000OO0 =1173 #line:21
	elif B (O0OO0OO00OO0O0000 )=='Size(width=3840, height=2160)':A ('Using 3840x2160, Changing Randomx and Randomy');OOO0OOOO00OOOO00O =572 ;OO0O0000OO0OO00O0 =3084 ;OOOOOO00OOOOOO0O0 =286 ;OO0OO0O00O0000OO0 =1759 #line:22
	elif B (O0OO0OO00OO0O0000 )=='Size(width=5120, height=1440)':A ('Using 5120x1440, Changing Randomx and Randomy');OOO0OOOO00OOOO00O =744 ;OO0O0000OO0OO00O0 =4009 ;OOOOOO00OOOOOO0O0 =220 ;OO0OO0O00O0000OO0 =1173 #line:23
	elif B (O0OO0OO00OO0O0000 )=='Size(width=7680, height=4320)':A ('Using 7680x4320, Changing Randomx and Randomy');OOO0OOOO00OOOO00O =1488 ;OO0O0000OO0OO00O0 =6168 ;OOOOOO00OOOOOO0O0 =572 ;OO0OO0O00O0000OO0 =3518 #line:24
	else :A ('Using Non-Supported Res, Changing Randomx and Randomy to Default Location!');A ('Please raise an issue on GitHub with your screen res for future custom support!');OOO0OOOO00OOOO00O =382 ;OO0O0000OO0OO00O0 =1582 ;OOOOOO00OOOOOO0O0 =181 ;OO0OO0O00O0000OO0 =903 #line:25
	return OOO0OOOO00OOOO00O ,OO0O0000OO0OO00O0 ,OOOOOO00OOOOOO0O0 ,OO0OO0O00O0000OO0 #line:26
def R ():#line:27
	O0OOO00000OO0O00O ='This is to large of a time input!';OO0000OO000OOO00O ='Must Type an Integer > 0';A ('Usage Just Type an Integer e.g. 30')#line:28
	while F :#line:29
		try :#line:30
			OO000OOOOOO00OOO0 =M (E ('Please Enter The Shortest Amount of Seconds To Wait Before Input - Recommended (30 seconds): '))#line:31
			if OO000OOOOOO00OOO0 <=0 :A (OO0000OO000OOO00O )#line:32
			elif OO000OOOOOO00OOO0 >=4294967 :A (O0OOO00000OO0O00O )#line:33
			else :#line:34
				O0O00O0OOOO000000 =M (E ('Please Enter The Longest Amount of Seconds To Wait Before Input - Recommended (1200 seconds): '))#line:35
				if O0O00O0OOOO000000 <=0 :A (OO0000OO000OOO00O )#line:36
				elif O0O00O0OOOO000000 <=OO000OOOOOO00OOO0 :A ('This should be not equal to or larger then the lowest amount in range')#line:37
				elif O0O00O0OOOO000000 >=4294967 :A (O0OOO00000OO0O00O )#line:38
				else :break #line:39
		except N :A ('Invalid Entry: Usage Just Type an Integer e.g. 30')#line:40
	return OO000OOOOOO00OOO0 ,O0O00O0OOOO000000 #line:41
def S (O000O0O00O0O00OO0 ):O0OOOOOO00O00O00O =O000O0O00O0O00OO0 ;O00O00O000000O0O0 =D (O0OOOOOO00O00O00O [0 ],O0OOOOOO00O00O00O [1 ]);return O00O00O000000O0O0 #line:42
def J (OO00O0OO0OOOOO000 ):OOO000OO00OOOO0OO =OO00O0OO0OOOOO000 ;O0OOO000O0OOOO000 =S (OOO000OO00OOOO0OO );A ('Next Interaction Time: '+B (O0OOO000O0OOOO000 )+' second(s) or '+B (O0OOO000O0OOOO000 //60 )+' minute(s) (Integer Division Not Accurate Minute Representation)!');C .sleep (O0OOO000O0OOOO000 )#line:43
def T (OO0OOOO0OOOO00OO0 ):OOOOO0OOO00O00OOO =OO0OOOO0OOOO00OO0 ;O0OO0O0O000OO00O0 =D (OOOOO0OOO00O00OOO [0 ],OOOOO0OOO00O00OOO [1 ]);OO0O00O0O0O0OOOO0 =D (OOOOO0OOO00O00OOO [2 ],OOOOO0OOO00O00OOO [3 ]);return O0OO0O0O000OO00O0 ,OO0O00O0O0O0OOOO0 #line:44
def U (OOOOO0OOO0O0OOO00 ):OO0OOOO00OO0O00OO =OOOOO0OOO0O0OOO00 ;O0OO00OOOOO0OO000 =T (OO0OOOO00OO0O00OO );O00OO0O0O000O000O =O0OO00OOOOO0OO000 [0 ];O0OOO0O000OO00O00 =O0OO00OOOOO0OO000 [1 ];H .moveTo (O00OO0O0O000O000O ,O0OOO0O000OO00O00 );H .click ();A ('Mouse Clicked At: ('+B (O00OO0O0O000O000O )+','+B (O0OOO0O000OO00O00 )+')')#line:45
def V ():#line:46
	OOO0O00OOOO0O0O0O =['q','w','e','r','a','s','d','f'];A ('The Default Button Click List Is:');A (OOO0O00OOOO0O0O0O )#line:47
	while F :#line:48
		try :#line:49
			O00OOOOO0000O000O =B (E ('Would You Like To Add More Keys To The ButtonClickList? Enter (Y) or (N): ')).lower ()#line:50
			if O00OOOOO0000O000O =='y':#line:51
				while F :#line:52
					try :#line:53
						OO0O0000OOO0OO0OO =M (E ('How Many Keys Would You Like To Add To The List: '))#line:54
						for O0OOOO00OO0O0OO00 in range (OO0O0000OOO0OO0OO ):O00OO000O00000OO0 =E ("Please Press a Key or Write The Key, Such As 'space' and then press enter: ");OOO0O00OOOO0O0O0O .append (O00OO000O00000OO0 )#line:55
						break #line:56
					except N :A ('Type Error: You Have Entered An Incorrect Type! Please Enter An Integer')#line:57
				break #line:58
			elif O00OOOOO0000O000O =='n':OO0O0000OOO0OO0OO =0 ;break #line:59
			else :A ('Input Error: Please Enter Either Y or N')#line:60
		except N :A ('Type Error: You Have Entered An Incorrect Type! Please Enter Either Y or N')#line:61
	return OOO0O00OOOO0O0O0O ,OO0O0000OOO0OO0OO #line:62
def W (O00OOO00O00000OOO ):OO0O00OO00OOOOOOO =O00OOO00O00000OOO ;OO0OO000000OO00OO =OO0O00OO00OOOOOOO [0 ];O0O0000000OOOO0O0 =OO0O00OO00OOOOOOO [1 ]+7 ;A (B (O0O0000000OOOO0O0 ));O000OOO0O00000O0O =D (0 ,O0O0000000OOOO0O0 );O0O000OO0O0O0OO00 =OO0OO000000OO00OO [O000OOO0O00000O0O ];H .press (O0O000OO0O0O0OO00 );A ('Button Clicked: '+O0O000OO0O0O0OO00 )#line:63
def X ():#line:64
	O00OOOO0O0O00000O ='queueDetectionScreenshot.png'#line:65
	while F :#line:66
		OO00OO000OO00OO00 =H .screenshot (region =(771 ,435 ,373 ,204 ));OO00OO000OO00OO00 .save (O00OOOO0O0O00000O );O0O00OOO0O00O00O0 =O00OOOO0O0O00000O ;A ('Lost Ark Screen Being Analysed');O0OOO0OO0OOO0O0O0 =I .image_to_string (Image .open (O0O00OOO0O00O00O0 ))#line:67
		if 'Waiting'in O0OOO0OO0OOO0O0O0 :A ('Still in Queue :(');A ('~Waiting 10 Seconds To Reanylse Screen!');A ('Sit Tight!');C .sleep (10 )#line:68
		else :break #line:69
if __name__ =='__main__':#line:70
	A (G );Y =Q ();A (G );C .sleep (2 );K =V ();A ('The Button Click List Is: ');A (K [0 ]);A (G );C .sleep (2 );L =R ();A (G );X ();A (G )#line:71
	while F :J (L );U (Y );J (L );W (K )