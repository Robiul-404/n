#make by Samir
#Full Credit By Samir
import random,string,time,re,sys,os
from concurrent.futures import ThreadPoolExecutor as tdp
try:
    import requests as r
    from bs4 import BeautifulSoup as bs
except:
    os.system("pip install bs4 requests")
    os.system('pkg install espeak')
    os.system("clear")
def clear():
	os.system('clear')
	print(logo)
def logo():
	print(logo)
def v():	
	print("")
def linex():
	print("")

os.system('clear')
#os.system('pkg install espeak')
os.system('')
black="\033[1;30m";red="\x1b[38;5;160m";green="\x1b[38;5;46m"
logo=(f""" 
\033[1;32m

Y88b    / 888 Y88b      / 888~~S4
 Y88b  /  888  Y88b    /  888___ 
  Y88b/   888   Y88b  /   888    
  /Y88b   888    Y888/    888 
 /  Y88b  888     Y8/     888    
/    Y88b 888      Y      888[\033[1;97m1.0.0{green}]
\033[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
#__________________MAIN____________#
def linex():
	print('\033[1;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
def clear():
	os.system('clear')
	print(logo)
#print("\033[1;32m [•]\033[1;37m Join My FaceBook Group...! \033[1;32mThnx");time.sleep(2);os.system('xdg-open https://facebook.com/groups/1245912839659325/')

#    except: 
 #       sys.exit()
######## CLEAR #######

#def clear():os.system('clear');print(logo);print(48*'═')#print('\t\033[1;37m\033[1;42mEID MUBARAK ALL GYZ\033[1;0m\33[1;37m');print(41*'═')

 
######### LINE #########

def line():print(48*'\033[1;92m═')


 
###########______###########

uids=[]
n=0
c=0
  
clear()
#file=input("ENTER ")
try:
    open(file,"r").read()
except:
    file="/sdcard/logo-DUMP.txt"

def s(code):
    ln=15-len(code)
    lim=int("9"*(ln))+1
    for i in range(lim):
        uids.append(code+str(i).zfill(ln))
        
def line():print(48*'\033[1;92m═')

def gen(code,tt):
    clear()
   # print('[1] START FOR AUTO DUMP ..')
#    linex()
 #   op=int(input("""select : \x1b[38;5;46m """))
    op=(int(1))
#    clear()
    #print(f" Your Key : \x1b[1;31mNix1x6b7b5c1031985b8n9nfdi15319")
   # print('\033[1;92m------------------------------------------------')        
   # print('None')
    #print(f'\033[1;92m (√) \033[1;92mTotal IDs  :\033[1;92m 74677')
    v()
    #print('\033[1;92m [•] \033[1;92mYour \033[1;92mOK\033[1;92m/\033[1;92mCP\033[1;92m IDs Save in \033[1;92m>\033[1;92m /sdcard/NIX');line()    
   # linex()
    if op==2:
        s(code)
    else:
        for i in range(tt):
            uids.append(code+''.join(random.choice(string.digits) for _ in range(
        15-len(code)
        )))
        
def geno(code,l,tt):
    for i in range(tt):
        uids.append(code+''.join(random.choice(string.digits) for _ in range(
        l-len(code)
        )))


uao=['Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/45.0.2454101','Mozilla/5.0 (Linux; Android 8.1.0; vivo 1812 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/7.9.0.1','Dalvik/2.1.0 (Linux; U; Android 5.1; Lenovo P1ma40 Build/LMY47D)',
'Dalvik/1.6.0 (Linux; U; Android 4.4.2; SM-G7102 Build/KOT49H)',
'Dalvik/2.1.0 (Linux; U; Android 7.0; SM-G920K Build/NRD90M)']

ux=['Mozilla/5.0 (Linux; Android 6.0; LG-H500 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/54.0.2840.68 Mobile Safari/537.36']

def inputs():
    os.system("clear")
    os.system("ENTER YOUR DUMP LIMIT")
    print(logo)
#    print('\n')
  #  print("\x1b[1;95m[+]  10001 • 100089 • 100090** etc")
  #  linex()
  #  code=input("ENTER YOUR DUMP LIMIT : \x1b[38;5;46m ")
    code="10004"
#    clear()
  #  os.system("ENTER YOUR COUNT LIMIT")
 #   print('\n')
  #  linex()
 #   print("\x1b[1;95m[+] 10000 • 100000 • 300000 • 3000484")
  #  linex()
  #  tt=int(input("ENTER YOUR COUNT LIMIT : \x1b[38;5;46m"))
    tt=(int(9999))
    l=0
    if len(code)<4:
        l=int(input("Uid length: "))
    return code,tt,l
    
    

def getname(uid):
    global n,c
    ua=random.choice(ux)
    hd={'authority':'m.facebook.com',

           'method': 'GET',
            'user-agent':ua
            
        
            
            }
    url="https://m.facebook.com/profile.php?id="+uid
    pi=r.get(url,headers=hd)
    bp=bs(pi.content,"html.parser")
    name=bp.find("title").text.split("|")[0].strip()
    if "Content not found" not in name and "Log in to Facebook" not in name:
        n+=1
        
        density = random.choice(['c_user=61571375130237;xs=15:F7VF40QuXhUMIQ:2:1736328143:-1:-1;fr=0oDhtMEEpIoE9Hoci.AWUdPAYJWbe9MQO3JDjSXaf3k44.BnfkPP..AAA.0.0.BnfkPP.AWW6SuM8dbE;datr=z0N-Z5hz5u9kK6-Egd4bNkeX',
'c_user=61571375130237;xs=23:Vb_87dtr_fCaDg:2:1736329888:-1:-1;fr=0UHKl0Wh2cs3WEadd.AWWsr4QXil4YNE7SufUkggL5FHA.Bnfkqg..AAA.0.0.Bnfkqg.AWWMcdzMXjs;datr=oEp-Z0kMiE2U3QSy2BftZj-o',
'c_user=61571672723124;xs=22:ZMfm7CdrpNiiNw:2:1736330399:-1:-1;fr=0QrDQs8dYg7noTksM.AWVN6fgOMQa6TW4BVQT6kra5Wi8.Bnfkyf..AAA.0.0.Bnfkyf.AWWIZ0LJxpQ;datr=n0x-Z0NLJ_LA3Qdzz7CI1Y-G',
'c_user=61571664053668;xs=29:L2Y-a5p9wRG7WQ:2:1736330402:-1:-1;fr=0PzmdIf1YNejGAxzK.AWVFK2VmTjXwRBtjaDdVqva9WGc.Bnfkyi..AAA.0.0.Bnfkyi.AWXOLjKInHw;datr=okx-Z-MK5Dgjw_1CzQdK_8gx',
'c_user=61571229915843;xs=3:F7wvqKSYNBCTug:2:1736330405:-1:-1;fr=0oTODT4issKEUBk5j.AWWpd2dAlHMxT654MDoDe_0EuxM.Bnfkyk..AAA.0.0.Bnfkyk.AWXR900WYXY;datr=pEx-Z_sc0sH99HH3OJ9cA2xb',
'c_user=61571199797409;xs=19:LMJvRcrbvYEO4w:2:1736330408:-1:-1;fr=0cfhTzLT1LZTBhUDK.AWWtOPBmTRae8lOxDUFr0TFkVmc.Bnfkyn..AAA.0.0.Bnfkyn.AWW23HiOaS4;datr=p0x-ZyS9AJf9Qg7281MsuJ34',
'c_user=61571605286686;xs=19:ZodBsI1vKmoRVQ:2:1736330411:-1:-1;fr=0BVwRifvtaGqb3g2f.AWXveZcGjQ9Ny3rk_kg6GM57lpk.Bnfkyr..AAA.0.0.Bnfkyr.AWUdhsVbfgM;datr=q0x-Z5wJ7evoIClI9HTmMzgU',
'c_user=61571234535439;xs=15:_8OHP5B_SzXQwg:2:1736330415:-1:-1;fr=0PIWpc2Y7T9bqu72i.AWU3YjSt9joTyFkkFQOMU5z-ryI.Bnfkyu..AAA.0.0.Bnfkyu.AWUGMbdE73A;datr=rkx-Z-jSkvnwXE62E4UJKaGZ',
'c_user=61571375130237;xs=30:dVlJrxSZLxcJdA:2:1736330440:-1:-1;fr=02YzWD6fOounyNtWW.AWXvAan0jEEHWpQuUavJMkks_9A.BnfkzI..AAA.0.0.BnfkzI.AWU-_tudBsc;datr=yEx-Z1MFzkk6zjxVbrT0hO54',
'c_user=61571672723124;xs=41:f1nxiRC0hI2RMA:2:1736411508:-1:-1;fr=0dQqtj5YAcycrgdGt.AWXoy_92RmD9SlJ6uYGhFPVdvzA.Bnf4lz..AAA.0.0.Bnf4lz.AWWF7cYYm7k;datr=c4l_Z9pl_F_MXkiiiEuG_lz7',
'c_user=61571664053668;xs=41:02Hfk_24ha6b6g:2:1736411512:-1:-1;fr=0zn9o1hoWxzk3ezzD.AWXzxOJbFEkRLRq4VH6uL0yUKcI.Bnf4l3..AAA.0.0.Bnf4l3.AWUF9lm6fZM;datr=d4l_Z7kBFsvXZR83XsWloyzE',
'c_user=61571229915843;xs=36:ujAZRKHuu5vwrg:2:1736411517:-1:-1;fr=0qV45IK03XRaT2vp3.AWWW1BDJCJSCQHHfab9Gn2E5E3o.Bnf4l8..AAA.0.0.Bnf4l8.AWWJEnZlWDE;datr=fIl_Z2hkyJYLH85LxMMdKucT',
'c_user=61571234535439;xs=26:ArBxlIuYzThTbg:2:1736411536:-1:-1;fr=03NTSZggaJlR3srOt.AWV_xd9Pp1vJePYJpBeNDoDiJPk.Bnf4mP..AAA.0.0.Bnf4mP.AWXIs2TqpPA;datr=j4l_ZyFC6sjc-0Ff9Ir9YZtc',
'c_user=61571375130237;xs=18:xtAF70A9nH2VoQ:2:1736411571:-1:-1;fr=0jpOQakp63GSMgZwK.AWUvVjAvhrez2qkHHqUPn7-2Jz8.Bnf4my..AAA.0.0.Bnf4my.AWVA2-35JQw;datr=sol_Zy4eV-KMsKFJqK_orXOM'])
        print(f"\033[1;92m[XIVE-OK] {uid} | {name}")
        print(f"{density}")
        open(file,"a").write("{g}[XIVE-OK] "+uid+" | "+name+"\n"+"{g}[COOKIE] :{w} "+density+"\n")
    #else:
      #  print(f"\033[1;34m[AUTO-DUMP-SUCCESFULL]\033[1;32m{uid} • {name}")
    
    c+=1
    print(f'\033[1;92m[\033[1;92m[XIVE-M]\033[1;92m] {c} | \033[1;92mOK:-\033[1;92m\033[1;32m%s\033[1;92m'%(n),end="\r")


def run():
    with tdp(max_workers=30) as t:
        for uid in uids:
            t.submit(getname,uid)

while True:
    code,tt,l=inputs()
    if len(code)>=4:
        gen(code,tt)
    else:
        geno(code,l,tt)
    
    run()
    print("DUMP IDS ARE SAVE: "+file)
    rr=input("DUMP AGAIN? [Y or N]")
    if rr in ["Y","y"]:
        code,tt,l=inputs()
        n=0
        c=0
        uids=[]
        gen(code,tt)
        run()
    else:
        break
