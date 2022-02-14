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
	O00OOOO00OO0O00O0 =H .size ()#line:11
	if B (O00OOOO00OO0O00O0 )=='Size(width=640, height=480)':A ('Using 640x480, Changing Randomx and Randomy');O0O0OO00O000O0000 =286.5 ;O0OOO0O0O0000O0O0 =351 ;OOOO00O000OO0OO0O =135 ;O0O0O00O00000OOOO =301 #line:12
	elif B (O00OOOO00OO0O00O0 )=='Size(width=1280, height=720)':A ('Using 1280x720, Changing Randomx and Randomy');O0O0OO00O000O0000 =573 ;O0OOO0O0O0000O0O0 =702 ;OOOO00O000OO0OO0O =271 ;O0O0O00O00000OOOO =602 #line:13
	elif B (O00OOOO00OO0O00O0 )=='Size(width=1920, height=1080)':A ('Using 1920x1080, Changing Randomx and Randomy');O0O0OO00O000O0000 =382 ;O0OOO0O0O0000O0O0 =1582 ;OOOO00O000OO0OO0O =181 ;O0O0O00O00000OOOO =903 #line:14
	elif B (O00OOOO00OO0O00O0 )=='Size(width=2560, height=1440)':A ('Using 2560x1440, Changing Randomx and Randomy');O0O0OO00O000O0000 =496 ;O0OOO0O0O0000O0O0 =2056 ;OOOO00O000OO0OO0O =235.3 ;O0O0O00O00000OOOO =1173.9 #line:15
	elif B (O00OOOO00OO0O00O0 )=='Size(width=2048, height=1080)':A ('Using 2048x1080, Changing Randomx and Randomy');O0O0OO00O000O0000 =404 ;O0OOO0O0O0000O0O0 =1676 ;OOOO00O000OO0OO0O =191 ;O0O0O00O00000OOOO =957 #line:16
	elif B (O00OOOO00OO0O00O0 )=='Size(width=3840, height=2160)':A ('Using 3840x2160, Changing Randomx and Randomy');O0O0OO00O000O0000 =744 ;O0OOO0O0O0000O0O0 =3084 ;OOOO00O000OO0OO0O =286 ;O0O0O00O00000OOOO =1759 #line:17
	elif B (O00OOOO00OO0O00O0 )=='Size(width=7680, height=4320)':A ('Using 7680x4320, Changing Randomx and Randomy');O0O0OO00O000O0000 =1488 ;O0OOO0O0O0000O0O0 =6168 ;OOOO00O000OO0OO0O =572 ;O0O0O00O00000OOOO =3518 #line:18
	else :A ('Using Non-Supported Res, Changing Randomx and Randomy to Default Location!');A ('Please raise an issue on GitHub with your screen res for future custom support!');O0O0OO00O000O0000 =382 ;O0OOO0O0O0000O0O0 =1582 ;OOOO00O000OO0OO0O =181 ;O0O0O00O00000OOOO =903 #line:19
	return O0O0OO00O000O0000 ,O0OOO0O0O0000O0O0 ,OOOO00O000OO0OO0O ,O0O0O00O00000OOOO #line:20
def O ():#line:21
	O0OO0OO00O0000O0O ='This is to large of a time input!';OO0OO000O000OOO0O ='Must Type an Integer > 0';A ('Usage Just Type an Integer e.g. 30')#line:22
	while F :#line:23
		try :#line:24
			O00O0O0O0OO000OOO =L (D ('Please Enter The Shortest Amount of Seconds To Wait Before Input - Recommended (30 seconds): '))#line:25
			if O00O0O0O0OO000OOO <=0 :A (OO0OO000O000OOO0O )#line:26
			elif O00O0O0O0OO000OOO >=4294967 :A (O0OO0OO00O0000O0O )#line:27
			else :#line:28
				O000000000000O00O =L (D ('Please Enter The Longest Amount of Seconds To Wait Before Input - Recommended (1200 seconds): '))#line:29
				if O000000000000O00O <=0 :A (OO0OO000O000OOO0O )#line:30
				elif O000000000000O00O <=O00O0O0O0OO000OOO :A ('This should be not equal to or larger then the lowest amount in range')#line:31
				elif O000000000000O00O >=4294967 :A (O0OO0OO00O0000O0O )#line:32
				else :break #line:33
		except M :A ('Invalid Entry: Usage Just Type an Integer e.g. 30')#line:34
	return O00O0O0O0OO000OOO ,O000000000000O00O #line:35
def P (OO0O000O0OOO00000 ):OOO000O00OO00OO00 =OO0O000O0OOO00000 ;O00OOOOOO0OO000O0 =C (OOO000O00OO00OO00 [0 ],OOO000O00OO00OO00 [1 ]);return O00OOOOOO0OO000O0 #line:36
def I (O0OOOO0OOOOOOOOOO ):OOO000O00000OO00O =O0OOOO0OOOOOOOOOO ;OOO00O0000000OO00 =P (OOO000O00000OO00O );A ('Time Waiting Before Next Interaction: '+B (OOO00O0000000OO00 )+' second(s) or '+B (OOO00O0000000OO00 /60 )+' minute(s)!');E .sleep (OOO00O0000000OO00 )#line:37
def Q (O0OO00OO00O000OO0 ):O00O00O000OO0000O =O0OO00OO00O000OO0 ;O0OO0OO0OO0O0OO0O =C (O00O00O000OO0000O [0 ],O00O00O000OO0000O [1 ]);O0OOO0O00O0000O0O =C (O00O00O000OO0000O [2 ],O00O00O000OO0000O [3 ]);return O0OO0OO0OO0O0OO0O ,O0OOO0O00O0000O0O #line:38
def R (OOOO0OO00O00OO0O0 ):O00OOOO00O000OOO0 =OOOO0OO00O00OO0O0 ;O0OO0O00O000000OO =Q (O00OOOO00O000OOO0 );O0000O00OOO000OO0 =O0OO0O00O000000OO [0 ];OO000O0OO0OOO000O =O0OO0O00O000000OO [1 ];H .moveTo (O0000O00OOO000OO0 ,OO000O0OO0OOO000O );H .click ();A ('Mouse Clicked At: ('+B (O0000O00OOO000OO0 )+','+B (OO000O0OO0OOO000O )+')')#line:39
def S ():#line:40
	O0000OOO0O000O00O =['q','w','e','r','a','s','d','f'];A ('The Default Button Click List Is:');A (O0000OOO0O000O00O )#line:41
	while F :#line:42
		try :#line:43
			O0OO00OO0OO0O0O0O =B (D ('Would You Like To Add More Keys To The ButtonClickList? Enter (Y) or (N): ')).lower ()#line:44
			if O0OO00OO0OO0O0O0O =='y':#line:45
				while F :#line:46
					try :#line:47
						O00O0O0OO00OOO00O =L (D ('How Many Keys Would You Like To Add To The List: '))#line:48
						for OO00O000OO0O0O00O in range (O00O0O0OO00OOO00O ):OOO00OO0OOOOOOOO0 =D ("Please Press a Key or Write The Key, Such As 'space' and then press enter: ");O0000OOO0O000O00O .append (OOO00OO0OOOOOOOO0 )#line:49
						break #line:50
					except M :A ('Type Error: You Have Entered An Incorrect Type! Please Enter An Integer')#line:51
				break #line:52
			elif O0OO00OO0OO0O0O0O =='n':break #line:53
			else :A ('Input Error: Please Enter Either Y or N')#line:54
		except M :A ('Type Error: You Have Entered An Incorrect Type! Please Enter Either Y or N')#line:55
	return O0000OOO0O000O00O #line:56
def T (OOOOOO000O00O00O0 ):OOO0OOOO0OOO0000O =OOOOOO000O00O00O0 ;O000OOOOO00000O00 =C (0 ,7 );OO0000OO0OO0000O0 =OOO0OOOO0OOO0000O [O000OOOOO00000O00 ];H .press (OO0000OO0OO0000O0 );A ('Button Clicked: '+OO0000OO0OO0000O0 )#line:57
if __name__ =='__main__':#line:58
	A (G );U =N ();A (G );E .sleep (2 );J =S ();A ('The Button Click List Is: ');A (J );A (G );E .sleep (2 );K =O ();A (G )#line:59
	while F :I (K );R (U );I (K );T (J )