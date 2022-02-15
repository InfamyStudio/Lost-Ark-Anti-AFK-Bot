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
	O0OOOO000OOO0OOOO =H .size ()#line:11
	if B (O0OOOO000OOO0OOOO )=='Size(width=640, height=480)':A ('Using 640x480, Changing Randomx and Randomy');OOOOO000OO0O00OOO =286.5 ;OOO0OO0O00O0O00O0 =351 ;OO00OO000O0OO0000 =135 ;OO0O0OOO00OO00000 =301 #line:12
	elif B (O0OOOO000OOO0OOOO )=='Size(width=1280, height=720)':A ('Using 1280x720, Changing Randomx and Randomy');OOOOO000OO0O00OOO =573 ;OOO0OO0O00O0O00O0 =702 ;OO00OO000O0OO0000 =271 ;OO0O0OOO00OO00000 =602 #line:13
	elif B (O0OOOO000OOO0OOOO )=='Size(width=1920, height=1080)':A ('Using 1920x1080, Changing Randomx and Randomy');OOOOO000OO0O00OOO =382 ;OOO0OO0O00O0O00O0 =1582 ;OO00OO000O0OO0000 =181 ;OO0O0OOO00OO00000 =903 #line:14
	elif B (O0OOOO000OOO0OOOO )=='Size(width=2560, height=1440)':A ('Using 2560x1440, Changing Randomx and Randomy');OOOOO000OO0O00OOO =496 ;OOO0OO0O00O0O00O0 =2056 ;OO00OO000O0OO0000 =235.3 ;OO0O0OOO00OO00000 =1173.9 #line:15
	elif B (O0OOOO000OOO0OOOO )=='Size(width=2048, height=1080)':A ('Using 2048x1080, Changing Randomx and Randomy');OOOOO000OO0O00OOO =404 ;OOO0OO0O00O0O00O0 =1676 ;OO00OO000O0OO0000 =191 ;OO0O0OOO00OO00000 =957 #line:16
	elif B (O0OOOO000OOO0OOOO )=='Size(width=3840, height=2160)':A ('Using 3840x2160, Changing Randomx and Randomy');OOOOO000OO0O00OOO =744 ;OOO0OO0O00O0O00O0 =3084 ;OO00OO000O0OO0000 =286 ;OO0O0OOO00OO00000 =1759 #line:17
	elif B (O0OOOO000OOO0OOOO )=='Size(width=7680, height=4320)':A ('Using 7680x4320, Changing Randomx and Randomy');OOOOO000OO0O00OOO =1488 ;OOO0OO0O00O0O00O0 =6168 ;OO00OO000O0OO0000 =572 ;OO0O0OOO00OO00000 =3518 #line:18
	else :A ('Using Non-Supported Res, Changing Randomx and Randomy to Default Location!');A ('Please raise an issue on GitHub with your screen res for future custom support!');OOOOO000OO0O00OOO =382 ;OOO0OO0O00O0O00O0 =1582 ;OO00OO000O0OO0000 =181 ;OO0O0OOO00OO00000 =903 #line:19
	return OOOOO000OO0O00OOO ,OOO0OO0O00O0O00O0 ,OO00OO000O0OO0000 ,OO0O0OOO00OO00000 #line:20
def O ():#line:21
	O00O000OOO00OOO0O ='This is to large of a time input!';O00O0OOO0O0OOOO00 ='Must Type an Integer > 0';A ('Usage Just Type an Integer e.g. 30')#line:22
	while F :#line:23
		try :#line:24
			OOOO0O0OOO0O00OOO =L (D ('Please Enter The Shortest Amount of Seconds To Wait Before Input - Recommended (30 seconds): '))#line:25
			if OOOO0O0OOO0O00OOO <=0 :A (O00O0OOO0O0OOOO00 )#line:26
			elif OOOO0O0OOO0O00OOO >=4294967 :A (O00O000OOO00OOO0O )#line:27
			else :#line:28
				O00O00OO00O00O0O0 =L (D ('Please Enter The Longest Amount of Seconds To Wait Before Input - Recommended (1200 seconds): '))#line:29
				if O00O00OO00O00O0O0 <=0 :A (O00O0OOO0O0OOOO00 )#line:30
				elif O00O00OO00O00O0O0 <=OOOO0O0OOO0O00OOO :A ('This should be not equal to or larger then the lowest amount in range')#line:31
				elif O00O00OO00O00O0O0 >=4294967 :A (O00O000OOO00OOO0O )#line:32
				else :break #line:33
		except M :A ('Invalid Entry: Usage Just Type an Integer e.g. 30')#line:34
	return OOOO0O0OOO0O00OOO ,O00O00OO00O00O0O0 #line:35
def P (OOOO00O0O000OOOO0 ):OOOO0000OO00O0O00 =OOOO00O0O000OOOO0 ;O0000000O000OO000 =C (OOOO0000OO00O0O00 [0 ],OOOO0000OO00O0O00 [1 ]);return O0000000O000OO000 #line:36
def I (O0O0O00OO000OOO00 ):OO0000O000OOO0O00 =O0O0O00OO000OOO00 ;O0O0O0OO0OO0OO00O =P (OO0000O000OOO0O00 );A ('Next Interaction Time: '+B (O0O0O0OO0OO0OO00O )+' second(s) or '+B (O0O0O0OO0OO0OO00O //60 )+' minute(s) (Integer Division Not Accurate Minute Representation)!');E .sleep (O0O0O0OO0OO0OO00O )#line:37
def Q (OOO00O00000O0OO0O ):OO0000000000O0O00 =OOO00O00000O0OO0O ;O0O0O00O0OOOOOOO0 =C (OO0000000000O0O00 [0 ],OO0000000000O0O00 [1 ]);O00OO0OO00O00OO00 =C (OO0000000000O0O00 [2 ],OO0000000000O0O00 [3 ]);return O0O0O00O0OOOOOOO0 ,O00OO0OO00O00OO00 #line:38
def R (OOO000000OOOO0OO0 ):O00OOO00O000OOO0O =OOO000000OOOO0OO0 ;OOOOOOOO000O00000 =Q (O00OOO00O000OOO0O );OO0OO0OOOOOOOO000 =OOOOOOOO000O00000 [0 ];OOOOO0000O0000O00 =OOOOOOOO000O00000 [1 ];H .moveTo (OO0OO0OOOOOOOO000 ,OOOOO0000O0000O00 );H .click ();A ('Mouse Clicked At: ('+B (OO0OO0OOOOOOOO000 )+','+B (OOOOO0000O0000O00 )+')')#line:39
def S ():#line:40
	O000OOO00OOOO0OO0 =['q','w','e','r','a','s','d','f'];A ('The Default Button Click List Is:');A (O000OOO00OOOO0OO0 )#line:41
	while F :#line:42
		try :#line:43
			O00OOO0O00O000000 =B (D ('Would You Like To Add More Keys To The ButtonClickList? Enter (Y) or (N): ')).lower ()#line:44
			if O00OOO0O00O000000 =='y':#line:45
				while F :#line:46
					try :#line:47
						O00OOO000O0OOO000 =L (D ('How Many Keys Would You Like To Add To The List: '))#line:48
						for O0OO0O00O00OOOOOO in range (O00OOO000O0OOO000 ):O0O0O0O0OOOO0O0O0 =D ("Please Press a Key or Write The Key, Such As 'space' and then press enter: ");O000OOO00OOOO0OO0 .append (O0O0O0O0OOOO0O0O0 )#line:49
						break #line:50
					except M :A ('Type Error: You Have Entered An Incorrect Type! Please Enter An Integer')#line:51
				break #line:52
			elif O00OOO0O00O000000 =='n':break #line:53
			else :A ('Input Error: Please Enter Either Y or N')#line:54
		except M :A ('Type Error: You Have Entered An Incorrect Type! Please Enter Either Y or N')#line:55
	return O000OOO00OOOO0OO0 #line:56
def T (O0OO0OOO00OOOOOOO ):O0000OO0000O00OO0 =O0OO0OOO00OOOOOOO ;O00OOOO0OOO00O000 =C (0 ,7 );OOO000OOOO000O0O0 =O0000OO0000O00OO0 [O00OOOO0OOO00O000 ];H .press (OOO000OOOO000O0O0 );A ('Button Clicked: '+OOO000OOOO000O0O0 )#line:57
if __name__ =='__main__':#line:58
	A (G );U =N ();A (G );E .sleep (2 );J =S ();A ('The Button Click List Is: ');A (J );A (G );E .sleep (2 );K =O ();A (G )#line:59
	while F :I (K );R (U );I (K );T (J )