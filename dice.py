B

    í#]+1  ã            	   @   s~  d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlmZm	Z	m
Z
 d dlmZ d dlmZ ej
dd ejddZejd	d
d dd e ¡ Zed
dƒZe ¡ ZW dQ R X e e¡Zee
jej d e
j ej d e
j ej d e
j ej d e
j  d e
j ej d e
j ej d e
j  d e
j ej d e
j ej d e
j ej! d e
j ej d e
j ej d e
j ej d e
j ej d e
j ej d e
j ej d e
j  d e
j ej d  e
j  d! e
j ej d" e
j  d# ƒ e
jej Z"e
j Z#e
jej Z$e
jej Z%e
jej Z&e
jej! Z'e
jej! Z(e  )¡ Z*d$Z+d%ed& d'd(d)d*d+œZ,d,d-„ Z-d.d/„ Z.d0d1„ Z/e*j0e+e,d2d3ed4 d5 ed4 d6 d7d8œd9Z1e e1j2¡Z3y4ee"d: e$ d e# e4e5e3d; d< ƒd= ƒ ƒ W n   ed>ƒ e 6¡  Y nX e5e3d; d< ƒd= e5d?ƒkrPee"d@ ƒ e 6¡  e/e7e5edA ƒd= ƒe7e5edB ƒd= ƒƒ dS )Cé    N)ÚForeÚBackÚStyle)Úrandint)ÚdatetimeT)Z	autoresetz<999 Dice Bot | This Is Gambling Bot Plase Take Own Your Risk)Údescriptionz-cz--betsetz%Enter Your Betset Number (default: 0))ÚdefaultÚhelpzconfig.jsonÚrz‘      ___  _           ___       __
     / _ \(_)______   / _ )___  / /_
    / // / / __/ -_) / _  / _ \/ __/
   /____/_/\__/\__/ /____/\___/\__/z)
=======================================
zAuthor By  z: zKadal15
zChannel Yt ú:z Jejaka Tutorialz
999 Dice Botz | zLose Streak ú|z Win Streak
z:support by botakberambut(hijrah) And All Termux Id Member
zDonate z BTC z#18961sqv9fPuBcEbbi1gHub8ydWePB8yaG
z
         LTC z#LNRkk6o9h1Rh98sDW8byeH9HbeUHwNohDu
z         Doge z$DJG4YG3ARUkSt9e5xvHvSS3faVx3v1HM9p

z$https://www.999doge.com/api/web.aspxzfile://z
User-Agentz!application/x-www-form-urlencodedz*/*z#id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7zcom.reland.relandicebot)ZOriginz
user-agentzContent-typeZAcceptzAccept-LanguagezX-Requested-Withc             C   s¤   t dt| ƒ d ƒ}|dks,|dks,|dkrbt | d¡d ƒ}dt|ƒ }tt|ƒd	|  ƒada|d
ksŠ|dksŠ|dksŠ|d
ksŠ|dkr dat| d¡d ƒad S )Ni?B éd   ÚHiÚhiZHIÚ.é   é   é
   ÚLoZLOWÚlowÚLowZLOr   )ÚstrÚfloatÚsplitÚlenÚintr   Úhigh)ZpersenZtaruhanÚcÚnZpangkat© r   ú
999dice.pyÚkonvert2   s    (r!   c             C   sž   t | ƒdk r4tdt | ƒ ƒ}|d t| ƒ } d|  }t | ƒdkrjtdt | ƒ ƒ}|d t| ƒ } d|  }n0t | ƒ}| dd … }| d |d … }|d | }|S )Né   Ú0z0.iøÿÿÿr   )r   r   r   )ÚnumZpanjang_nolÚresultZlen_numÚendÚfirstr   r   r    Úrev@   s    
r(   c       #      C   s`  t jdkst jdkst jdkrZd}d}x<|d7 }ytd | d }W q(   P Y q(X q(W n
tt jƒ}ttd | d ƒd	 }ttd | d
 ƒd }tttd | d ƒd ƒ}ttd | d
 td | d d ƒ |}dtd |ttt	ddƒdddœ}	
y¤t
jtt
|	d}
t |
j¡}|d t|d ƒ t|ƒ }t|d ƒt|ƒ }
t|d t|d ƒ t|ƒ | ƒd }ttd tttt|d ƒt|
ƒ ƒd ƒ ƒ tdtd | d  ƒ d}d}d}d}t ¡  d¡}t|ƒttd ƒ }d}d}d}d}d}d}td | d }td | d }	xx|dksD|dksD|d krJd}nd!}td | d" dkstd | d" d kstd | d" dkržtj d#¡ n&|tttd | d" ƒd ƒkrÄ|}td | d d$ d% d&kstd | d d$ d% d'kstd | d d$ d% d(krô|d7 }|d!krŒ|ttd | d d$ d) ƒd krZd*}|ttd | d d$ d) ƒd+ d krŒd}d}|d!kr|ttd | d d$ d, ƒd krÀd*}|ttd | d d$ d, ƒd+ d krd}d}ntd | d d }t jdks,t jdks,t jdkrät ¡  d¡}t|ƒt|d ƒkrît|ƒttd ƒ }|d7 }||krzd}td-td | d  d. ƒ ttd | d ƒd	 }ttd | d
 ƒd }tttd | d ƒd ƒ}n
tt jƒ}td | d/ d% d'ks<td | d/ d% d&ks<td | d/ d% d(krøtt ttd | d/ d0 ƒttd | d/ d1 ƒ¡d+ƒ}tt|ƒƒ}|d2kr¤tj d3t|ƒ d4 ¡ |d5krÆtj d3t|ƒ d6 ¡ |d7krètj d3t|ƒ d8 ¡ t|t|ƒƒ nttd | d
 t|ƒƒ t  t|ƒ¡ t|ƒ}|d7 }dtd |ttt	ddƒdddœ}	|ttd9 ƒkrÐttd: t d; t t|ƒ ƒ t! "d<t|ƒ ¡ t  d¡ t! "d=ttt|d ƒt|
ƒ ƒd ƒ ¡ t #¡  t
jtt
|	d}
t |
j¡}t|d t|d ƒ t|ƒ | ƒd }t|d ƒt|ƒ }
|d | krîtt$d> t t|ƒ t$ d? t% tt|ƒd ƒ tttt|d ƒt|
ƒ ƒd ƒ t%d@ tt|ƒ ƒ ttdA ƒ t! "dB¡ t  d¡ t! "d=ttt|d ƒt|
ƒ ƒd ƒ ¡ t #¡  |d |k rÀtt$d> t t|ƒ t$ dC t& dD tt|ƒd ƒ tttt|d ƒt|
ƒ ƒd ƒ t&dE tt|ƒ ƒ tt'j(t)j* dF ƒ t! "dG¡ t  d¡ t! "d=ttt|d ƒt|
ƒ ƒd ƒ ¡ t #¡  |d dk		rÆ|d7 }d}t|d ƒt|
ƒ } |dk	rPtt$d> t t|ƒ t$ d? t% tt+t|ƒƒƒ ttt+t| ƒƒƒ t%d@ tt|ƒ ƒ nVtt$d> t t|ƒ t$ d? t% tt+t|ƒƒƒ ttt+t| ƒƒƒ t&dE tt|ƒ ƒ t|ƒttd | d) ƒ }nd}|d7 }d}!d!}t|d ƒt|
ƒ } |dk
rTtt$d> t t|ƒ t$ dC t& dD tt+t|ƒƒƒ ttt+t| ƒƒƒ t%d@ tt|ƒ ƒ nZtt$d> t t|ƒ t$ dC t& dD tt+t|ƒƒƒ ttt+t| ƒƒƒ t&dE tt|ƒ ƒ t|ƒttd | d, ƒ }|d!k
rð|!d7 }!|!|kr0d}!d}n@||kr0d}|d!kr,|t|ƒkr0|}t|ƒt|ƒ }n|}||krJd!}d}|d7 }||krdd!}d}|d7 }tj tdH t t|ƒ t, dI t t|ƒ d3 ¡ q&W W nº   td#ƒ t! "dJ¡ y~t-dKdLƒj}"|" d>t ¡  dM¡ dN t|ƒ dI t|ƒ dO ttt|d ƒt|
ƒ ƒd ƒ dP t|ƒ dQ ¡ W d Q R X W n   tdRƒ Y nX t #¡  Y nX d S )SNZAutoÚautoZAUTOr   r   ZConfigzName Bet SetZIntervaliè  zReset If WinzBase Beti áõZChanceZBetZPlaceBetZ
SessionCookiei?B ZdogeÚ2)ÚaÚsZPayInr   ZHighZ
ClientSeedZCurrencyZProtocolVersion)ÚheadersÚdataZStartingBalanceZPayOutz


Starting BalancezAnda Menggunakan BetSet Ke Fz%Mr   zReset If ProfitZOFFZOffZoffTzMax BetÚ zHi / LowZToggleZOnZONÚonzIf Winr   é   zIf LosezChange Bet Set z                           z
Random ChanceZMinZMaxé   ú
z   é   z  é   ú z
Target Profitz%
Yay.! 
Profit Mencapai Target.....!
zProfit ztermux-toast You win ztermux-toast Total Balance ú[z] ZProfitz)Yay.!
Balance Sudah Memenuhi Target.....!z&termux-toast Target Win Sudah Tercapaiú]ú-zLose zLose Target....!ztermux-toast Lose Target z        Win Streak z
 Lose Streak ztermux-toast Betting Stopzhistory.logza+z%Y/%m/%d %H:%M:%Sz
] Win Streak z | Balance z Profit Ú
zStop Betting).Úmy_namespaceZbetsetÚobjr   r   r!   Újsr   r   r   r   ZpostÚurlÚuaÚjsonÚloadsÚtextÚprintÚhijauÚresr   r   ÚnowÚstrftimeÚsysÚstdoutÚwriteÚroundÚrandomÚuniformr   ÚtimeÚsleepÚosÚsystemÚexitÚunguÚhijau2Úred2r   ÚBRIGHTr   ÚREDr(   ÚredÚopen)#ZwsZlsZurutZjumlahulangZpesanZslpZlimit_aZpayinZamountr.   Zr1ZjsnZjumblZjumZprofr   ZburstZstats_rolebet_loseZstats_rolebet_winZmenitZno_winZno_loseZ	total_winZ
total_loseZ
no_rolebetZrolebetZreset_if_profitZ
tot_if_profitZstats_if_profitZwaktuZhasil_chanceZcokZbalÚiÚfr   r   r    ÚdiceR   sZ   
&(.B"Z
&*
&*$

N:


 
*(f

*j

*
XV 
\Z





>
rr\   ZLoginZ 7ec7f8a2c9724b2cbb8ed75e72b47ee9ZAccountÚUsernameÚPasswordr/   )r+   ZKeyr]   r^   ZTotp)r-   r.   zBalance ZDogeZBalancei áõz%Check Your Username And Your Passwordg     @@z|

Maaf Versi Ini Cuma Support Untuk Balance Dibawah 500 Doge
Silahkan Hubungi Author Untuk Full Version
Hub : +6285336117892z
Target WinzLose Target)8Zrequestsr@   rN   rH   rL   rP   ÚargparseZcoloramar   r   r   r   r   ÚinitÚArgumentParserÚparserÚadd_argumentÚ
parse_argsr;   rY   ZmyfileÚreadr.   rA   r<   rC   ZNORMALZMAGENTAZGREENrV   ZDIMZWHITEZ	RESET_ALLrW   rD   rE   Zabu2rS   rT   rU   rX   Zsessionr   r>   r?   r!   r(   r\   Úgetr
   rB   r=   r   r   rR   r   r   r   r   r    Ú<module>   s\   8
ÿ G I,4
