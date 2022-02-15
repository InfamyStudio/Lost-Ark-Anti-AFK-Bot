M =ValueError #line:1
L =int #line:2
G ='~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'#line:3
F =True #line:4
D =input #line:5
B =str #line:6
A =print #line:7
import time as E ,pyautogui as H #line:8
from random import randint as C #line:9
def N ():#line:10
	OOO0000O0O0O000OO =H .size ()#line:11
	if B (OOO0000O0O0O000OO )=='Size(width=640, height=480)':A ('Using 640x480, Changing Randomx and Randomy');OOOO000OOO00OOOO0 =286 ;OO0OOOO0OO0OO0O0O =351 ;OOOO0OO0000OOO0OO =135 ;OO0O000O000OO0O0O =301 #line:12
	elif B (OOO0000O0O0O000OO )=='Size(width=1280, height=720)':A ('Using 1280x720, Changing Randomx and Randomy');OOOO000OOO00OOOO0 =573 ;OO0OOOO0OO0OO0O0O =702 ;OOOO0OO0000OOO0OO =271 ;OO0O000O000OO0O0O =602 #line:13
	elif B (OOO0000O0O0O000OO )=='Size(width=1920, height=1080)':A ('Using 1920x1080, Changing Randomx and Randomy');OOOO000OOO00OOOO0 =382 ;OO0OOOO0OO0OO0O0O =1582 ;OOOO0OO0000OOO0OO =181 ;OO0O000O000OO0O0O =903 #line:14
	elif B (OOO0000O0O0O000OO )=='Size(width=2560, height=1440)':A ('Using 2560x1440, Changing Randomx and Randomy');OOOO000OOO00OOOO0 =496 ;OO0OOOO0OO0OO0O0O =2056 ;OOOO0OO0000OOO0OO =235 ;OO0O000O000OO0O0O =1173 #line:15
	elif B (OOO0000O0O0O000OO )=='Size(width=2048, height=1080)':A ('Using 2048x1080, Changing Randomx and Randomy');OOOO000OOO00OOOO0 =404 ;OO0OOOO0OO0OO0O0O =1676 ;OOOO0OO0000OOO0OO =191 ;OO0O000O000OO0O0O =957 #line:16
	elif B (OOO0000O0O0O000OO )=='Size(width=3840, height=2160)':A ('Using 3840x2160, Changing Randomx and Randomy');OOOO000OOO00OOOO0 =744 ;OO0OOOO0OO0OO0O0O =3084 ;OOOO0OO0000OOO0OO =286 ;OO0O000O000OO0O0O =1759 #line:17
	elif B (OOO0000O0O0O000OO )=='Size(width=7680, height=4320)':A ('Using 7680x4320, Changing Randomx and Randomy');OOOO000OOO00OOOO0 =1488 ;OO0OOOO0OO0OO0O0O =6168 ;OOOO0OO0000OOO0OO =572 ;OO0O000O000OO0O0O =3518 #line:18
	else :A ('Using Non-Supported Res, Changing Randomx and Randomy to Default Location!');A ('Please raise an issue on GitHub with your screen res for future custom support!');OOOO000OOO00OOOO0 =382 ;OO0OOOO0OO0OO0O0O =1582 ;OOOO0OO0000OOO0OO =181 ;OO0O000O000OO0O0O =903 #line:19
	return OOOO000OOO00OOOO0 ,OO0OOOO0OO0OO0O0O ,OOOO0OO0000OOO0OO ,OO0O000O000OO0O0O #line:20
def O ():#line:21
	O0O0000O000OOOOOO ='This is to large of a time input!';OOOO00OOO0O0OOO00 ='Must Type an Integer > 0';A ('Usage Just Type an Integer e.g. 30')#line:22
	while F :#line:23
		try :#line:24
			O0OOO000OO00OOOO0 =L (D ('Please Enter The Shortest Amount of Seconds To Wait Before Input - Recommended (30 seconds): '))#line:25
			if O0OOO000OO00OOOO0 <=0 :A (OOOO00OOO0O0OOO00 )#line:26
			elif O0OOO000OO00OOOO0 >=4294967 :A (O0O0000O000OOOOOO )#line:27
			else :#line:28
				O0OOOOOOOO0O0OOOO =L (D ('Please Enter The Longest Amount of Seconds To Wait Before Input - Recommended (1200 seconds): '))#line:29
				if O0OOOOOOOO0O0OOOO <=0 :A (OOOO00OOO0O0OOO00 )#line:30
				elif O0OOOOOOOO0O0OOOO <=O0OOO000OO00OOOO0 :A ('This should be not equal to or larger then the lowest amount in range')#line:31
				elif O0OOOOOOOO0O0OOOO >=4294967 :A (O0O0000O000OOOOOO )#line:32
				else :break #line:33
		except M :A ('Invalid Entry: Usage Just Type an Integer e.g. 30')#line:34
	return O0OOO000OO00OOOO0 ,O0OOOOOOOO0O0OOOO #line:35
def P (O0OO000OOO00000OO ):OOOO00O00OO000OO0 =O0OO000OOO00000OO ;OOO0000O0O00O0O00 =C (OOOO00O00OO000OO0 [0 ],OOOO00O00OO000OO0 [1 ]);return OOO0000O0O00O0O00 #line:36
def I (OOO0OOO0000OO0OOO ):OOOOOO00000OO0OO0 =OOO0OOO0000OO0OOO ;OO000O000000OOO0O =P (OOOOOO00000OO0OO0 );A ('Next Interaction Time: '+B (OO000O000000OOO0O )+' second(s) or '+B (OO000O000000OOO0O //60 )+' minute(s) (Integer Division Not Accurate Minute Representation)!');E .sleep (OO000O000000OOO0O )#line:37
def Q (O0OO0OOOOOO0OOO0O ):O00O00OO0OOO0O0OO =O0OO0OOOOOO0OOO0O ;OOOO0O000OO0OOOO0 =C (O00O00OO0OOO0O0OO [0 ],O00O00OO0OOO0O0OO [1 ]);O00O000OOO0O00O00 =C (O00O00OO0OOO0O0OO [2 ],O00O00OO0OOO0O0OO [3 ]);return OOOO0O000OO0OOOO0 ,O00O000OOO0O00O00 #line:38
def R (O00O00O00OO0OO000 ):O00O00O00O00O0OO0 =O00O00O00OO0OO000 ;O0O00OOOOO000O000 =Q (O00O00O00O00O0OO0 );O0OOO000O0OOO0O0O =O0O00OOOOO000O000 [0 ];OO00OOO0000OO0O0O =O0O00OOOOO000O000 [1 ];H .moveTo (O0OOO000O0OOO0O0O ,OO00OOO0000OO0O0O );H .click ();A ('Mouse Clicked At: ('+B (O0OOO000O0OOO0O0O )+','+B (OO00OOO0000OO0O0O )+')')#line:39
def S ():#line:40
	O0OOO0OOO00O000OO =['q','w','e','r','a','s','d','f'];A ('The Default Button Click List Is:');A (O0OOO0OOO00O000OO )#line:41
	while F :#line:42
		try :#line:43
			O000O00OOO0O000OO =B (D ('Would You Like To Add More Keys To The ButtonClickList? Enter (Y) or (N): ')).lower ()#line:44
			if O000O00OOO0O000OO =='y':#line:45
				while F :#line:46
					try :#line:47
						OOOOO0O0OO00000OO =L (D ('How Many Keys Would You Like To Add To The List: '))#line:48
						for OOO0OOOOOO000O0OO in range (OOOOO0O0OO00000OO ):OO0OOOO0O0OOOO0O0 =D ("Please Press a Key or Write The Key, Such As 'space' and then press enter: ");O0OOO0OOO00O000OO .append (OO0OOOO0O0OOOO0O0 )#line:49
						break #line:50
					except M :A ('Type Error: You Have Entered An Incorrect Type! Please Enter An Integer')#line:51
				break #line:52
			elif O000O00OOO0O000OO =='n':break #line:53
			else :A ('Input Error: Please Enter Either Y or N')#line:54
		except M :A ('Type Error: You Have Entered An Incorrect Type! Please Enter Either Y or N')#line:55
	return O0OOO0OOO00O000OO #line:56
def T (OOO0OO000O000OO0O ):O000OO0OO0O000O0O =OOO0OO000O000OO0O ;O00000O0O00OO0OOO =C (0 ,7 );O00OOOOO0O000OO00 =O000OO0OO0O000O0O [O00000O0O00OO0OOO ];H .press (O00OOOOO0O000OO00 );A ('Button Clicked: '+O00OOOOO0O000OO00 )#line:57
if __name__ =='__main__':#line:58
	A (G );U =N ();A (G );E .sleep (2 );J =S ();A ('The Button Click List Is: ');A (J );A (G );E .sleep (2 );K =O ();A (G )#line:59
	while F :I (K );R (U );I (K );T (J )
