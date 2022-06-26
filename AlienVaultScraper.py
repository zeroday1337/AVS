#Made by SpotnikSignal - 2021 - AlienVault scraper en anonfiles checker/downloader

import os #line:3
import requests #line:4
import threading #line:5
import json #line:6
import sys #line:7
import glob #line:8
import time #line:9
import random #line:10
from threading import Thread #line:11
try :#line:13
    from BeautifulSoup import BeautifulSoup #line:14
except ImportError :#line:15
    from bs4 import BeautifulSoup #line:16
class color :#line:19
   PURPLE ='\033[95m'#line:20
   CYAN ='\033[96m'#line:21
   DARKCYAN ='\033[36m'#line:22
   BLUE ='\033[94m'#line:23
   GREEN ='\033[92m'#line:24
   YELLOW ='\033[93m'#line:25
   RED ='\033[91m'#line:26
   BOLD ='\033[1m'#line:27
   UNDERLINE ='\033[4m'#line:28
   END ='\033[0m'#line:29
about_text ="About: AlienVault scraper and checker.";#line:31
year ="2021";#line:32
active_step =0 ;#line:33
intro_text =["\n  -------------------","  | /@@@@\\  /@@@@\\  |","  | @  \\_@  @  \\_@  |","  | @ \\     @ \\     |","  |  \\@@     \\@@    |","  |   \\ \\     \\ \\   |","  | @\\___@  @\\___@  |","  | \\@@@@/  \\@@@@/  |","  -------------------","~made by SpotnikSignal~ \n",about_text +" \n"];#line:46
loop_counter =0 ;#line:47
intro_shown =False ;#line:48
active_proxy_list =[];#line:50
use_proxies =False ;#line:51
def show_intro ():#line:54
	OO000000O0O0000OO =0 ;#line:55
	for OO00OO0OOO00O00OO in intro_text :#line:56
		if OO000000O0O0000OO ==0 :#line:57
			print (color .YELLOW +color .BOLD +OO00OO0OOO00O00OO +color .END );#line:58
		else :#line:59
			print (OO00OO0OOO00O00OO );#line:60
		O0OOOO00OOO00000O =OO00OO0OOO00O00OO .find ('SpotnikSignal');#line:62
		if O0OOOO00OOO00000O !=-1 :#line:63
			OO000000O0O0000OO =1 ;#line:64
def show_modes ():#line:67
	print ("Modes:");#line:68
	print ("[1] = Scraper");#line:69
	print ("[2] = Checker & Downloader");#line:70
	print ("[0] = Clean & Restart \n");#line:71
def show_first_step ():#line:74
	OO000O0OOOO00OOOO =False ;#line:75
	OO00OOO00OOOOO0O0 =1 ;#line:76
	while OO000O0OOOO00OOOO ==False :#line:78
		global input_mode ;#line:79
		O0000OO000OOO0OO0 =input ('Mode: ');#line:80
		if O0000OO000OOO0OO0 .isnumeric ():#line:81
			OO000O0OOOO00OOOO =True ;#line:82
			input_mode =int (O0000OO000OOO0OO0 );#line:83
		elif O0000OO000OOO0OO0 =="modes":#line:84
			show_modes ();#line:85
		elif O0000OO000OOO0OO0 =="exit":#line:86
			sys .exit ();#line:87
		elif O0000OO000OOO0OO0 =="help":#line:88
			show_help ();#line:89
			show_modes ();#line:90
		else :#line:91
			print ("Wrong input idiot, give a number or modes/exit/help.");#line:92
def step_1_scraper ():#line:95
	global active_proxy_list ;#line:96
	global use_proxies ;#line:97
	print ("Beginning scraping process.");#line:99
	O00OO00O0O0000OOO =input ('Check domain [like example.com]: ');#line:100
	OOOOOOOO0O0000O00 =input ('Cookie value [leave empty for none]: ');#line:101
	active_proxy_list =[];#line:102
	OOOOO00O00000O000 =True ;#line:103
	use_proxies =input ("Use proxy list named proxies.txt? Yes/(N)o: ");#line:106
	if use_proxies =="y"or use_proxies =="Y"or use_proxies =="Yes"or use_proxies =="yes":#line:107
		use_proxies =True ;#line:108
	elif use_proxies =="n"or use_proxies =="N"or use_proxies =="":#line:109
		use_proxies =False ;#line:110
	else :#line:111
		use_proxies =False ;#line:112
	if use_proxies ==True :#line:114
		if os .path .isfile ("proxies.txt")!=True :#line:115
			print ("No proxies.txt file found, set on No again!");#line:116
			use_proxies =False ;#line:117
		else :#line:118
			print ("[Testing given proxy list]");#line:120
			OO0O00OO0000O0OOO =open ('proxies.txt','r').read ().splitlines ();#line:121
			for O000OO00O0000OO0O in OO0O00OO0000O0OOO :#line:122
				try :#line:123
					OO0O0OOOO00OOO0O0 =requests .Session ();#line:124
					OO000O0O000O00O0O =OO0O0OOOO00OOO0O0 .head ("http://example.com",timeout =10 ,headers ={},proxies ={'http':'http://'+O000OO00O0000OO0O });#line:125
				except IOError :#line:126
				    print (color .RED +"Proxy "+O000OO00O0000OO0O +" offline (will not be used)"+color .END );#line:127
				else :#line:128
				    print (color .GREEN +"Proxy "+O000OO00O0000OO0O +" active!"+color .END );#line:129
				    active_proxy_list .append (O000OO00O0000OO0O );#line:130
			if len (active_proxy_list )==0 :#line:131
				print ("No available proxies found, stopping script!");#line:132
				OOOOO00O00000O000 =False ;#line:133
	if use_proxies :#line:135
		OOO0O0O0O0000O00O =random .choice (active_proxy_list );#line:136
		OO0O00OO0000O0OOO ={'http':"http://"+OOO0O0O0O0000O00O }#line:139
	else :#line:140
		OOO0O0O0O0000O00O ="[none]";#line:141
		OO0O00OO0000O0OOO ={};#line:142
	if OOOOO00O00000O000 ==True :#line:144
		O0O00O0OO0000OO0O ="https://otx.alienvault.com/otxapi/pulses/?limit=20&page=1&sort=-modified&q="+O00OO00O0O0000OOO ;#line:145
		O0O00OO0O0O0O0O0O ={'content-type':'application/json; charset=utf-8','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36','origin':O00OO00O0O0000OOO };#line:150
		if OOOOOOOO0O0000O00 !="":#line:152
			O0O00OO0O0O0O0O0O .update ({'Cookie':OOOOOOOO0O0000O00 });#line:153
		print ("Checking (may take a minute)...");#line:155
		OO0O0OOOO00OOO0O0 =requests .Session ();#line:156
		OO000O0O000O00O0O =OO0O0OOOO00OOO0O0 .get (O0O00O0OO0000OO0O ,timeout =100 ,headers =O0O00OO0O0O0O0O0O ,proxies =OO0O00OO0000O0OOO );#line:157
		OOO00O0O00OO00OO0 =OO000O0O000O00O0O .json ();#line:158
		OO0OO0O0OO0000OOO =OOO00O0O00OO00OO0 ['count'];#line:159
		if OO0OO0O0OO0000OOO !=0 :#line:161
			print (color .GREEN +str (OO0OO0O0OO0000OOO )+" pulses found! "+O00OO00O0O0000OOO +" is active."+color .END );#line:162
			OO000OO00OOOOOO0O =input ('Start at page [default=1]: ');#line:164
			if OO000OO00OOOOOO0O =="":#line:165
				OO000OO00OOOOOO0O =1 ;#line:166
			elif OO000OO00OOOOOO0O .isnumeric ()==False :#line:167
				OO000OO00OOOOOO0O =1 ;#line:168
				print ("Not numeric, using default!");#line:169
			else :#line:170
				OO000OO00OOOOOO0O =int (OO000OO00OOOOOO0O );#line:171
			OO0O0O000OOO00O0O =input ('Amount of pages [max=20, default=20]: ');#line:173
			if OO0O0O000OOO00O0O =="":#line:174
				OO0O0O000OOO00O0O =20 ;#line:175
			elif OO0O0O000OOO00O0O .isnumeric ()==False :#line:176
				OO0O0O000OOO00O0O =20 ;#line:177
				print ("Not numeric, using default!");#line:178
			elif int (OO0O0O000OOO00O0O )>20 :#line:179
				OO0O0O000OOO00O0O =20 ;#line:180
				print ("Too high, using default!");#line:181
			else :#line:182
				OO0O0O000OOO00O0O =int (OO0O0O000OOO00O0O );#line:183
			O0O00OOOOO0O0OO0O =input ('Number per page [default=100]: ');#line:185
			if O0O00OOOOO0O0OO0O =="":#line:186
				O0O00OOOOO0O0OO0O =100 ;#line:187
			elif O0O00OOOOO0O0OO0O .isnumeric ()==False :#line:188
				O0O00OOOOO0O0OO0O =100 ;#line:189
				print ("Not numeric, using default!");#line:190
			else :#line:191
				O0O00OOOOO0O0OO0O =int (O0O00OOOOO0O0OO0O );#line:192
			OOOOO0OO0OOOO0OO0 =input ('Seconds between requests [default = 2, min = 1, let\'s not spam pls]: ');#line:194
			if OOOOO0OO0OOOO0OO0 =="":#line:195
				OOOOO0OO0OOOO0OO0 =2 ;#line:196
			elif OOOOO0OO0OOOO0OO0 .isnumeric ()==False :#line:197
				OOOOO0OO0OOOO0OO0 =2 ;#line:198
				print ("Not numeric, using default!");#line:199
			elif int (OOOOO0OO0OOOO0OO0 )<1 :#line:200
				OOOOO0OO0OOOO0OO0 =2 ;#line:201
				print ("Too low! Using default!");#line:202
			else :#line:203
				OOOOO0OO0OOOO0OO0 =int (OOOOO0OO0OOOO0OO0 );#line:204
			print ("Starting crawler...");#line:206
			if os .path .isfile ("found_urls.txt")!=True :#line:208
				O00000OOO0O00OOO0 =open ("found_urls.txt","w");#line:209
				O00000OOO0O00OOO0 .close ();#line:210
			O0O0000O00OOOO000 =open ("found_urls.txt","r+");#line:212
			OOOOO0OO00O000OOO =O0O0000O00OOOO000 .readlines ();#line:213
			O0O0000O00OOOO000 .close ();#line:214
			O00000OOO0O00OOO0 =open ("found_urls.txt","a");#line:216
			O00OO00O00O00000O =0 ;#line:217
			for OOOOOOO000OO0O0OO in range (OO000OO00OOOOOO0O ,(OO0O0O000OOO00O0O +1 )):#line:218
				if use_proxies :#line:219
					OOO0O0O0O0000O00O =random .choice (active_proxy_list );#line:220
					OO0O00OO0000O0OOO ={'http':"http://"+OOO0O0O0O0000O00O }#line:223
				else :#line:224
					OOO0O0O0O0000O00O ="";#line:225
					OO0O00OO0000O0OOO ={};#line:226
				O0O00O0OO0000OO0O ="https://otx.alienvault.com/otxapi/indicators/domain/url_list/"+O00OO00O0O0000OOO +"?limit="+str (O0O00OOOOO0O0OO0O )+"&page="+str (OOOOOOO000OO0O0OO );#line:228
				OO0O0OOOO00OOO0O0 =requests .Session ();#line:229
				OO000O0O000O00O0O =OO0O0OOOO00OOO0O0 .get (O0O00O0OO0000OO0O ,timeout =20 ,headers =O0O00OO0O0O0O0O0O ,proxies =OO0O00OO0000O0OOO );#line:230
				OOO00O0O00OO00OO0 =OO000O0O000O00O0O .json ();#line:231
				O00O000O0O0000OOO =OOO00O0O00OO00OO0 ;#line:232
				OO00000OO000OO000 =0 ;#line:234
				if 'url_list'in O00O000O0O0000OOO :#line:235
					O0OOO0OO000O0OOO0 =O00O000O0O0000OOO ['url_list'];#line:236
					for O0OOOO00O000O0OO0 in O0OOO0OO000O0OOO0 :#line:237
						OO0OOO0O0O0O0OOOO =O0OOOO00O000O0OO0 ['url'];#line:238
						O00O0OOOOOO0000OO =False ;#line:239
						if len (OOOOO0OO00O000OOO )>0 :#line:240
							for OO0OO0O00O000OOO0 in OOOOO0OO00O000OOO :#line:241
								if OO0OO0O00O000OOO0 ==OO0OOO0O0O0O0OOOO +"\n":#line:242
									print (color .RED +"Line "+OO0OOO0O0O0O0OOOO +" already exists, skipping"+color .END );#line:243
									O00O0OOOOOO0000OO =True ;#line:244
						if O00O0OOOOOO0000OO ==False :#line:245
							O00000OOO0O00OOO0 .write (OO0OOO0O0O0O0OOOO +"\n");#line:246
							O00OO00O00O00000O +=1 ;#line:247
							OO00000OO000OO000 +=1 ;#line:248
				print ("Sleep and next call ("+str (OO00000OO000OO000 )+" urls founds) with proxy: "+OOO0O0O0O0000O00O );#line:249
				time .sleep (OOOOO0OO0OOOO0OO0 );#line:250
			O00000OOO0O00OOO0 .close ();#line:251
			print (color .GREEN +str (O00OO00O00O00000O )+" url's found, added to found_urls.txt file."+color .END );#line:252
			main ();#line:253
		else :#line:254
			print (color .RED +"0 pulses found, not a correct domain! start over"+color .END );#line:255
			main ();#line:256
def step_2_checker ():#line:258
	global active_proxy_list ;#line:259
	global use_proxies ;#line:260
	print ("Starting checker and downloader.");#line:263
	print ("Modes [1 = anonfiles, 0 = direct download]");#line:264
	O0O0O0O00OOOOOO0O =input ("Mode [default=1]: ");#line:265
	if O0O0O0O00OOOOOO0O =="":#line:266
		O0O0O0O00OOOOOO0O =1 ;#line:267
	elif O0O0O0O00OOOOOO0O .isnumeric ()==False :#line:268
		O0O0O0O00OOOOOO0O =1 ;#line:269
		print ("Not numeric, using default!");#line:270
	else :#line:271
		O0O0O0O00OOOOOO0O =int (O0O0O0O00OOOOOO0O );#line:272
	if use_proxies ==True :#line:275
		OO00OO00OO0OOO00O =input ("Ignore existing proxy list? (N)o/Yes");#line:276
		if OO00OO00OO0OOO00O =="y"or OO00OO00OO0OOO00O =="yes":#line:277
			use_proxies =False ;#line:278
	O0O0OO00O0OO0OOOO =open ("found_urls.txt","r+");#line:280
	OO00O0OO0OO00O00O =O0O0OO00O0OO0OOOO .readlines ();#line:281
	O0O0OO00O0OO0OOOO .close ();#line:282
	OO0OOO00OOOO0OOO0 =[];#line:283
	O0OO0000OO0OOOOOO =input ("Auto download? [yes/no yes=default]: ");#line:284
	OO0OOOO00OOOOOO0O =False ;#line:285
	OO00O0O0O000OO00O =True ;#line:286
	if O0OO0000OO0OOOOOO ==""or O0OO0000OO0OOOOOO =="yes"or O0OO0000OO0OOOOOO =="y":#line:287
		OO0OOOO00OOOOOO0O =True ;#line:288
	if OO0OOOO00OOOOOO0O ==True :#line:290
		OOO0OO00O0OOOO0O0 =input ("Max filesize [in bytes, default:100mil]: ");#line:291
		if OOO0OO00O0OOOO0O0 =="":#line:292
			OOO0OO00O0OOOO0O0 =(1000 *1000 )*100 ;#line:293
		elif OOO0OO00O0OOOO0O0 .isnumeric ()==False :#line:294
			OOO0OO00O0OOOO0O0 =(1000 *1000 )*100 ;#line:295
			print ("Not numeric, using default!");#line:296
		else :#line:297
			OOO0OO00O0OOOO0O0 =int (OOO0OO00O0OOOO0O0 );#line:298
		O000OOOO000OOO00O =input ("Max download amount [0=all,default=0]: ");#line:300
		if O000OOOO000OOO00O =="":#line:301
			O000OOOO000OOO00O =0 ;#line:302
		elif O000OOOO000OOO00O .isnumeric ()==False :#line:303
			O000OOOO000OOO00O =0 ;#line:304
			print ("Not numeric, using default!");#line:305
		else :#line:306
			O000OOOO000OOO00O =int (O000OOOO000OOO00O );#line:307
		OOO0O000OO0OOO0O0 =input ("Only download files with string comma seperated [empty=all]: ");#line:309
		OOOOOO000OOO00000 =input ("Ignore string comma seperated [empty=all]: ");#line:310
	if OO0OOOO00OOOOOO0O ==True :#line:312
		O00OOOO0OOO000OO0 =input ("Number of threads for download (1 = default, 5 max): ");#line:313
		if O00OOOO0OOO000OO0 =="":#line:314
			O00OOOO0OOO000OO0 =1 ;#line:315
		elif not O00OOOO0OOO000OO0 .isnumeric ():#line:316
			O00OOOO0OOO000OO0 =1 ;#line:317
			print ("Not a number, will use default");#line:318
		else :#line:319
			O00OOOO0OOO000OO0 =int (O00OOOO0OOO000OO0 );#line:320
		if O00OOOO0OOO000OO0 >5 :#line:322
			O00OOOO0OOO000OO0 =5 ;#line:323
	print ("\nChecking...\n");#line:325
	O000OOOOO0OOO0000 =0 ;#line:326
	if len (OO00O0OO0OO00O00O )>0 :#line:327
		for OO00OOOO0000O0OOO in OO00O0OO0OO00O00O :#line:328
			if OO00O0O0O000OO00O ==True :#line:329
				if O0O0O0O00OOOOOO0O ==1 :#line:330
					if use_proxies :#line:331
						O00OOO0O0000O000O =random .choice (active_proxy_list );#line:332
						O0O00O00000O0000O ={'http':"http://"+O00OOO0O0000O000O }#line:335
					else :#line:336
						O00OOO0O0000O000O ="[none]";#line:337
						O0O00O00000O0000O ={};#line:338
					O00OO000OOO0O0O00 =OO00OOOO0000O0OOO .replace ("\n","");#line:340
					OOOO0OOO000OO0O00 ={'content-type':'text/html; charset=utf-8','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36','origin':'anonfiles.com'};#line:345
					try :#line:347
						OO00OO0O0OO00000O =requests .Session ();#line:348
						OOOO00OO0OO00O00O =OO00OO0O0OO00000O .get (O00OO000OOO0O0O00 ,timeout =40 ,headers =OOOO0OOO000OO0O00 ,proxies =O0O00O00000O0000O );#line:349
						O0O0000OO0O00OO00 =OOOO00OO0OO00O00O ;#line:350
						OO00000OOO0000OO0 =BeautifulSoup (O0O0000OO0O00OO00 .text ,"lxml");#line:351
						OO00OOOO00O00OOOO =OO00000OOO0000OO0 .body .find ('h1',attrs ={'class':'text-center text-wordwrap'});#line:354
						O0OO0O00OOOO00O00 ="";#line:355
						print ("Response of: "+O00OO000OOO0O0O00 +" used proxy: "+O00OOO0O0000O000O );#line:356
						try :#line:357
							O0OO0O00OOOO00O00 =OO00OOOO00O00OOOO .text ;#line:358
							print ("title: "+O0OO0O00OOOO00O00 );#line:359
						except :#line:360
							print (color .RED +"title not found"+color .END );#line:361
						OO0O00OOO00O0OOO0 =OO00000OOO0000OO0 .body .find ('a',attrs ={'id':'download-url'})#line:364
						OOO0O000OOO0OO0O0 ="";#line:365
						try :#line:366
							OOO0O000OOO0OO0O0 =OO0O00OOO00O0OOO0 ['href'];#line:367
							print ("url: "+OOO0O000OOO0OO0O0 );#line:368
						except :#line:369
							print (color .RED +"href not found"+color .END );#line:370
						if "POTENTIAL VIRUS"in O0O0000OO0O00OO00 .text :#line:372
							print (color .RED +"Potential virus warning!"+color .END );#line:373
						OOO00O0O000OOO00O =0 ;#line:376
						if OOO0O000OO0OOO0O0 !="":#line:377
							OO0000O00O0O0O00O =OOO0O000OO0OOO0O0 .split (",");#line:378
							if len (OO0000O00O0O0O00O )>0 :#line:379
								for O0O00O000OOOO0O00 in OO0000O00O0O0O00O :#line:380
									if OOO0O000OOO0OO0O0 .find (O0O00O000OOOO0O00 )!=-1 or O0OO0O00OOOO00O00 .find (O0O00O000OOOO0O00 )!=-1 :#line:381
										OOO00O0O000OOO00O =1 ;#line:382
								if OOO00O0O000OOO00O ==0 :#line:383
									print (color .RED +"Search term(s) not found, skipping!"+color .END );#line:384
									OOO00O0O000OOO00O =-1 ;#line:385
						O0O0OO0OO0OOO0OO0 =0 ;#line:388
						if OOO00O0O000OOO00O !=-1 :#line:389
							if OOOOOO000OOO00000 !="":#line:390
								OOO0OO0OO0O00O0OO =OOOOOO000OOO00000 .split (",");#line:391
								if len (OOO0OO0OO0O00O0OO )>0 :#line:392
									for OOOOO0OO00OO0OO0O in OOO0OO0OO0O00O0OO :#line:393
										if OOO0O000OOO0OO0O0 .find (OOOOO0OO00OO0OO0O )!=-1 or O0OO0O00OOOO00O00 .find (OOOOO0OO00OO0OO0O )!=-1 :#line:394
											print (color .RED +"Excluded search term found, skipping!"+color .END );#line:395
											O0O0OO0OO0OOO0OO0 =1 ;#line:396
									if O0O0OO0OO0OOO0OO0 ==0 :#line:397
										O0O0OO0OO0OOO0OO0 =-1 ;#line:398
						if OO0OOOO00OOOOOO0O ==True and OOO0O000OOO0OO0O0 !=""and O0OO0O00OOOO00O00 !=""and OOO00O0O000OOO00O !=-1 and O0O0OO0OO0OOO0OO0 !=1 :#line:401
							try :#line:402
								if O000OOOO000OOO00O >0 :#line:403
									if O000OOOOO0OOO0000 >=O000OOOO000OOO00O :#line:404
										if OO00O0O0O000OO00O ==True :#line:405
											print ("Max amount hit!");#line:406
											OO00O0O0O000OO00O =False ;#line:407
								if OO00O0O0O000OO00O ==True :#line:410
									if os .path .isdir ('Downloads')==False :#line:411
										os .mkdir ('Downloads');#line:412
									O0O0O00OO0O00O0O0 ="Downloads/"+O0OO0O00OOOO00O00 ;#line:414
									if os .path .isfile (O0O0O00OO0O00O0O0 )==False :#line:415
										OOOO00OO0OO00O00O =OO00OO0O0OO00000O .head (OOO0O000OOO0OO0O0 ,timeout =5 ,headers =OOOO0OOO000OO0O00 ,proxies =O0O00O00000O0000O );#line:416
										OOO0O00O0O00OO00O =int (OOOO00OO0OO00O00O .headers ['content-length']);#line:417
										if OOO0O00O0O00OO00O >0 and OOO0O00O0O00OO00O <OOO0OO00O0OOOO0O0 :#line:419
											print (color .GREEN +"Added to thread list"+color .END );#line:420
											OO0OOO00OOOO0OOO0 .append ([OOO0O000OOO0OO0O0 ,O0O0O00OO0O00O0O0 ,O0OO0O00OOOO00O00 ]);#line:421
											O000OOOOO0OOO0000 +=1 ;#line:422
										else :#line:423
											if OOO0O00O0O00OO00O ==0 :#line:424
												print (color .RED +"Empty file!"+color .END )#line:425
											elif OOO0O00O0O00OO00O >=OOO0OO00O0OOOO0O0 :#line:426
												print (color .RED +"Max file size activated!"+color .END )#line:427
									else :#line:428
										print (color .RED +"File exists"+color .END );#line:429
							except :#line:430
								print (color .RED +"Error in downloading file!"+color .END );#line:431
						print ("\n");#line:433
					except :#line:434
						print (O0O0000OO0O00OO00 );#line:435
						print ("Error");#line:436
				elif O0O0O0O00OOOOOO0O ==0 :#line:437
					print ("Coming soon!");#line:438
					break ;#line:439
				else :#line:440
					print ("Mode not available!");#line:441
					break ;#line:442
			else :#line:443
				print ("Max download hit! starting download threads..");#line:444
				break ;#line:445
		O0OO0OO0O000O0O00 =[];#line:448
		if OO0OOOO00OOOOOO0O ==True and len (OO0OOO00OOOO0OOO0 )>0 :#line:449
			for OO0OOO0OO0O000OOO in range (O00OOOO0OOO000OO0 ):#line:450
			    O0OO0OO0O000O0O00 .append (Thread (target =download_files ,args =[divide_stuff (OO0OOO00OOOO0OOO0 ,O00OOOO0OOO000OO0 )[OO0OOO0OO0O000OOO ],OO0OOO0OO0O000OOO ,OO00OO0O0OO00000O ]))#line:451
			    O0OO0OO0O000O0O00 [OO0OOO0OO0O000OOO ].start ()#line:452
			for OO0OOOOOOOO0O0000 in O0OO0OO0O000O0O00 :#line:453
			    OO0OOOOOOOO0O0000 .join ()#line:454
def divide_stuff (O000O0O00OO0OO00O ,OOO00O00OOO000O00 ):#line:456
    return [O000O0O00OO0OO00O [O00000OO0O0O0O000 ::OOO00O00OOO000O00 ]for O00000OO0O0O0O000 in range (OOO00O00OOO000O00 )]#line:457
def download_files (O00O00OOO0O0O0O0O ,O0OOOO00OOO000O0O ,O0O0O0OOO0000O00O ):#line:459
	global active_proxy_list ;#line:460
	global use_proxies ;#line:461
	if use_proxies :#line:463
		OO0O0OO0OO0000OOO =random .choice (active_proxy_list );#line:464
		OO00O00O0OOO0O0O0 ={'http':"http://"+OO0O0OO0OO0000OOO }#line:467
	else :#line:468
		OO0O0OO0OO0000OOO ="[none]";#line:469
		OO00O00O0OOO0O0O0 ={};#line:470
	O0OOOOO0000OO00O0 ={'content-type':'text/html; charset=utf-8','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36','origin':'anonfiles.com'};#line:476
	for OOOOOO0O0OO0O0O0O in O00O00OOO0O0O0O0O :#line:478
		print ("Downloading: "+OOOOOO0O0OO0O0O0O [0 ]);#line:479
		O0O00OO0OOOO00OOO =O0O0O0OOO0000O00O .get (OOOOOO0O0OO0O0O0O [0 ],headers =O0OOOOO0000OO00O0 ,proxies =OO00O00O0OOO0O0O0 );#line:480
		if len (O0O00OO0OOOO00OOO .content )>0 :#line:481
			OOOOO0O0O0OOOOO00 =open (OOOOOO0O0OO0O0O0O [1 ],"wb");#line:482
			OOOOO0O0O0OOOOO00 .write (O0O00OO0OOOO00OOO .content );#line:483
			OOOOO0O0O0OOOOO00 .close ();#line:484
			time .sleep (0.5 );#line:485
			print (color .GREEN +"Download done: "+OOOOOO0O0OO0O0O0O [2 ]+" on thread: "+str (O0OOOO00OOO000O0O )+" used proxy: "+OO0O0OO0OO0000OOO +color .END );#line:486
def show_help ():#line:489
	print ("\nHelp section, each step has it's own help text!");#line:490
	O00OO000O0000O0OO =["Just follow the steps for now (give a mode given in the intro screen)!"]#line:493
	print ("Answer: "+O00OO000O0000O0OO [active_step -1 ]);#line:494
def main ():#line:497
	global intro_shown ;#line:498
	if intro_shown ==False :#line:500
		show_intro ();#line:501
		intro_shown =True ;#line:502
	show_modes ();#line:504
	show_first_step ();#line:505
	if input_mode ==0 :#line:507
		clean_screen ();#line:508
		main ();#line:509
	elif input_mode ==1 :#line:510
		step_1_scraper ();#line:511
	elif input_mode ==2 :#line:512
		step_2_checker ();#line:513
def clean_screen ():#line:516
	os .system ('cls'if os .name =='nt'else 'clear')#line:517
main ();