import os
import sys
import random
from datetime import datetime
from os import execl
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.functions.account import UpdateProfileRequest
from Config import STRING, SUDO, BIO_MESSAGE, API_ID, API_HASH, STRING2, STRING3, STRING4 ,STRING5, STRING6, STRING7, STRING8 ,STRING9, STRING10, STRING11, STRING12 , STRING13 , STRING14 , STRING15 ,STRING16 , STRING17 , STRING18 , STRING19 , STRING20 , STRING21 , STRING22 , STRING23 , STRING24 , STRING25 , STRING26 , STRING27 , STRING28 , STRING29 , STRING30
import asyncio
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from Utils import RAID, EAGLE , RRAID


a = API_ID
b = API_HASH
smex = STRING
smexx = STRING2
smexxx = STRING3
smexxxx = STRING4
smexxxxx = STRING5
sixth = STRING6
seven = STRING7
eight = STRING8
ninth = STRING9
tenth = STRING10
eleve = STRING11
twelv = STRING12
thirt = STRING13
forte = STRING14
fifth = STRING15
sieee = STRING16
seeee = STRING17
eieee = STRING18
nieee = STRING19
gandu = STRING20
ekish = STRING21
baish = STRING22
teish = STRING23
tfour = STRING24
tfive = STRING25
tsix = STRING26
tseven = STRING27
teight = STRING28
tnine = STRING29
thirty = STRING30



idk = ""
ydk = ""
wdk = ""
sdk = ""
hdk = ""
adk = ""
bdk = ""
cdk = ""
edk = ""
ddk = ""
vkk = ""
kkk = ""
lkk = ""
mkk = ""
sid = ""
shy = ""
aan = ""
ake = ""
eel = ""
khu = ""
shi = ""
yaa = ""
dav = ""
raj = ""
put = ""
eag = ""
gle = ""
wal = ""
aaa = ""
boy = ""



que = {}

SMEX_USERS = []
for x in SUDO: 
    SMEX_USERS.append(x)
    
async def start_yukki():
    global idk
    global ydk
    global wdk
    global sdk
    global hdk
    global adk
    global bdk
    global cdk
    global ddk
    global edk
    global vkk
    global kkk
    global lkk
    global mkk
    global sid
    global shy
    global aan
    global ake
    global eel
    global khu
    global shi
    global yaa
    global dav
    global raj
    global put
    global eag
    global gle
    global wal
    global aaa
    global boy
    if smex:
        session_name = str(smex)
        print("String 1 Found")
        idk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 1")
            await idk.start()
            botme = await idk.get_me()
            await idk(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await idk(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await idk(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await idk(functions.channels.JoinChannelRequest(channel="@EAGLE_SPAMMER"))
            await idk(functions.channels.JoinChannelRequest(channel="@BLACK_MAFIA_OP_BOLTE"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            idk = "smex"
            print(e)
            pass
    else:
        print("Session 1 not Found")
        session_name = "startup"
        idk = TelegramClient(session_name, a, b)
        try:
            await idk.start()
        except Exception as e:
            pass
   
    if smexx:
        session_name = str(smexx)
        print("String 2 Found")
        ydk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 2")
            await ydk.start()
            await ydk(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await ydk(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await ydk(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await ydk(functions.channels.JoinChannelRequest(channel="@EAGLE_SPAMMER"))
            await ydk(functions.channels.JoinChannelRequest(channel="@BLACK_MAFIA_OP_BOLTE"))
            botme = await ydk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 2 not Found")
        pass
        session_name = "startup"
        ydk = TelegramClient(session_name, a, b)
        try:
            await ydk.start()
        except Exception as e:
            pass

    if smexxx:
        session_name = str(smexxx)
        print("String 3 Found")
        wdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 3")
            await  wdk.start()
            await wdk(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await wdk(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await wdk(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await wdk(functions.channels.JoinChannelRequest(channel="@EAGLE_SPAMMER"))
            await wdk(functions.channels.JoinChannelRequest(channel="@BLACK_MAFIA_OP_BOLTE"))
            botme = await wdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 3 not Found")
        pass
        session_name = "startup"
        wdk = TelegramClient(session_name, a, b)
        try:
            await wdk.start()
        except Exception as e:
            pass

    if smexxxx:
        session_name = str(smexxxx)
        print("String 4 Found")
        hdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 4")
            await hdk.start()
            await hdk(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await hdk(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await hdk(functions.channels.JoinChannelRequest(channel="@EAGLE_SPAMMER"))
            await hdk(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            
            await hdk(functions.channels.JoinChannelRequest(channel="@BLACK_MAFIA_OP_BOLTE"))
            botme = await hdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 4 not Found")
        pass
        session_name = "startup"
        hdk = TelegramClient(session_name, a, b)
        try:
            await hdk.start()
        except Exception as e:
            pass

    if smexxxxx:
        session_name = str(smexxxxx)
        print("String 5 Found")
        sdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 5")
            await sdk.start()
            await sdk(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await sdk(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await sdk(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await sdk(functions.channels.JoinChannelRequest(channel="@EAGLE_SPAMMER"))
            await sdk(functions.channels.JoinChannelRequest(channel="@BLACK_MAFIA_OP_BOLTE"))
            botme = await sdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 5 not Found")
        pass
        session_name = "startup"
        sdk = TelegramClient(session_name, a, b)
        try:
            await sdk.start()
        except Exception as e:
            pass
                  
    if sixth:
        session_name = str(sixth)
        print("String 6 Found")
        adk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 6")
            await adk.start()
            await adk(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await adk(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await adk(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await adk(functions.channels.JoinChannelRequest(channel="@EAGLE_SPAMMER"))
            await adk(functions.channels.JoinChannelRequest(channel="@BLACK_MAFIA_OP_BOLTE"))
            botme = await adk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 6 not Found")
        pass
        session_name = "startup"
        adk = TelegramClient(session_name, a, b)
        try:
            await adk.start()
        except Exception as e:
            pass

    if seven:
        session_name = str(seven)
        print("String 7 Found")
        bdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 7")
            await bdk.start()
            await bdk(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await bdk(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await bdk(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await bdk(functions.channels.JoinChannelRequest(channel="@EAGLE_SPAMMER"))
            await bdk(functions.channels.JoinChannelRequest(channel="@BLACK_MAFIA_OP_BOLTE"))
            botme = await bdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 7 not Found")
        pass
        session_name = "startup"
        bdk = TelegramClient(session_name, a, b)
        try:
            await bdk.start()
        except Exception as e:
            pass    
        
    
    if eight:
        session_name = str(eight)
        print("String 8 Found")
        cdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 8")
            await cdk.start()
            await cdk(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await cdk(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await cdk(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await cdk(functions.channels.JoinChannelRequest(channel="@EAGLE_SPAMMER"))
            await cdk(functions.channels.JoinChannelRequest(channel="@BLACK_MAFIA_OP_BOLTE"))
            botme = await cdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 8 not Found")
        pass
        session_name = "startup"
        cdk = TelegramClient(session_name, a, b)
        try:
            await cdk.start()
        except Exception as e:
            pass   
        
    if ninth:
        session_name = str(ninth)
        print("String 9 Found")
        ddk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 9")
            await ddk.start()
            await ddk(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await ddk(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await ddk(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await ddk(functions.channels.JoinChannelRequest(channel="@EAGLE_SPAMMER"))
            await ddk(functions.channels.JoinChannelRequest(channel="@BLACK_MAFIA_OP_BOLTE"))
            botme = await ddk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 9 not Found")
        pass
        session_name = "startup"
        ddk = TelegramClient(session_name, a, b)
        try:
            await ddk.start()
        except Exception as e:
            pass   
    
  
    if tenth:
        session_name = str(tenth)
        print("String 10 Found")
        edk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 10")
            await edk.start()
            await edk(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await edk(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await edk(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await edk(functions.channels.JoinChannelRequest(channel="@EAGLE_SPAMMER"))
            await edk(functions.channels.JoinChannelRequest(channel="@BLACK_MAFIA_OP_BOLTE"))
            botme = await edk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 10 not Found")
        pass
        session_name = "startup"
        edk = TelegramClient(session_name, a, b)
        try:
            await edk.start()
        except Exception as e:
            pass 
        
    
    if eleve:
        session_name = str(eleve)
        print("String 11 Found")
        vkk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 11")
            await vkk.start()
            await vkk(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await vkk(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await vkk(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await vkk(functions.channels.JoinChannelRequest(channel="@EAGLE_SPAMMER"))
            await vkk(functions.channels.JoinChannelRequest(channel="@BLACK_MAFIA_OP_BOLTE"))
            botme = await vkk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 11 not Found")
        pass
        session_name = "startup"
        vkk = TelegramClient(session_name, a, b)
        try:
            await vkk.start()
        except Exception as e:
            pass
        
    
    if twelv:
        session_name = str(twelv)
        print("String 12 Found")
        kkk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 12")
            await kkk.start()
            await kkk(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await kkk(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await kkk(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await kkk(functions.channels.JoinChannelRequest(channel="@EAGLE_SPAMMER"))
            await kkk(functions.channels.JoinChannelRequest(channel="@BLACK_MAFIA_OP_BOLTE"))
            botme = await kkk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 12 not Found")
        pass
        session_name = "startup"
        kkk = TelegramClient(session_name, a, b)
        try:
            await kkk.start()
        except Exception as e:
            pass   
    
  
    if thirt:
        session_name = str(thirt)
        print("String 13  Found")
        lkk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 13")
            await lkk.start()
            await lkk(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await lkk(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await lkk(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await lkk(functions.channels.JoinChannelRequest(channel="@EAGLE_SPAMMER"))
            await lkk(functions.channels.JoinChannelRequest(channel="@BLACK_MAFIA_OP_BOLTE"))
            botme = await lkk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 13 not Found")
        pass
        session_name = "startup"
        lkk = TelegramClient(session_name, a, b)
        try:
            await lkk.start()
        except Exception as e:
            pass 
        
    
    if forte:
        session_name = str(forte)
        print("String 14 Found")
        mkk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 14")
            await mkk.start()
            await mkk(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await mkk(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await mkk(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await mkk(functions.channels.JoinChannelRequest(channel="@EAGLE_SPAMMER"))
            await mkk(functions.channels.JoinChannelRequest(channel="@BLACK_MAFIA_OP_BOLTE"))
            botme = await mkk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 14 not Found")
        pass
        session_name = "startup"
        mkk = TelegramClient(session_name, a, b)
        try:
            await mkk.start()
        except Exception as e:
            pass
        
    
    if fifth:
        session_name = str(fifth)
        print("String 15 Found")
        sid = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 15")
            await sid.start()
            await sid(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await sid(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await sid(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await sid(functions.channels.JoinChannelRequest(channel="@EAGLE_SPAMMER"))
            await sid(functions.channels.JoinChannelRequest(channel="@BLACK_MAFIA_OP_BOLTE"))
            botme = await sid.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 15 not Found")
        pass
        session_name = "startup"
        sid = TelegramClient(session_name, a, b)
        try:
            await sid.start()
        except Exception as e:
            pass


    if sieee:
        session_name = str(sieee)
        print("String 16 Found")
        shy = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 16")
            await shy.start()
            botme = await shy.get_me()
            await shy(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await shy(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await shy(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await shy(functions.channels.JoinChannelRequest(channel="@EAGLE_SPAMMER"))
            await shy(functions.channels.JoinChannelRequest(channel="@BLACK_MAFIA_OP_BOLTE"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 16 not Found")
        session_name = "startup"
        shy = TelegramClient(session_name, a, b)
        try:
            await shy.start()
        except Exception as e:
            pass
   
    if seeee:
        session_name = str(seeee)
        print("String 17 Found")
        aan = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 17")
            await aan.start()
            botme = await aan.get_me()
            await aan(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await aan(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await aan(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await aan(functions.channels.JoinChannelRequest(channel="@EAGLE_SPAMMER"))
            await aan(functions.channels.JoinChannelRequest(channel="@BLACK_MAFIA_OP_BOLTE"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 17 not Found")
        session_name = "startup"
        aan = TelegramClient(session_name, a, b)
        try:
            await aan.start()
        except Exception as e:
            pass
   
    if eieee:
        session_name = str(eieee)
        print("String 18 Found")
        ake = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 18")
            await ake.start()
            botme = await ake.get_me()
            await ake(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await ake(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await ake(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await ake(functions.channels.JoinChannelRequest(channel="@EAGLE_SPAMMER"))
            await ake(functions.channels.JoinChannelRequest(channel="@BLACK_MAFIA_OP_BOLTE"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 18 not Found")
        session_name = "startup"
        ake = TelegramClient(session_name, a, b)
        try:
            await ake.start()
        except Exception as e:
            pass
   
    if nieee:
        session_name = str(nieee)
        print("String 19 Found")
        eel = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 19")
            await eel.start()
            botme = await eel.get_me()
            await eel(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await eel(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await eel(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await eel(functions.channels.JoinChannelRequest(channel="@EAGLE_SPAMMER"))
            await eel(functions.channels.JoinChannelRequest(channel="@BLACK_MAFIA_OP_BOLTE"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 19 not Found")
        session_name = "startup"
        eel = TelegramClient(session_name, a, b)
        try:
            await idk.start()
        except Exception as e:
            pass
   
    if gandu:
        session_name = str(gandu)
        print("String 20 Found")
        khu = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 20")
            await khu.start()
            botme = await khu.get_me()
            await khu(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await khu(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await khu(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await khu(functions.channels.JoinChannelRequest(channel="@EAGLE_SPAMMER"))
            await khu(functions.channels.JoinChannelRequest(channel="@BLACK_MAFIA_OP_BOLTE"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 20 not Found")
        session_name = "startup"
        khu = TelegramClient(session_name, a, b)
        try:
            await khu.start()
        except Exception as e:
            pass
   
    if ekish:
        session_name = str(ekish)
        print("String 21 Found")
        shi = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 21")
            await shi.start()
            botme = await shi.get_me()
            await shi(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await shi(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await shi(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await shi(functions.channels.JoinChannelRequest(channel="@EAGLE_SPAMMER"))
            await shi(functions.channels.JoinChannelRequest(channel="@BLACK_MAFIA_OP_BOLTE"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 21 not Found")
        session_name = "startup"
        shi = TelegramClient(session_name, a, b)
        try:
            await shi.start()
        except Exception as e:
            pass
   
    if baish:
        session_name = str(baish)
        print("String 22 Found")
        yaa = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 22")
            await yaa.start()
            botme = await yaa.get_me()
            await yaa(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await yaa(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await yaa(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await yaa(functions.channels.JoinChannelRequest(channel="@EAGLE_SPAMMER"))
            await yaa(functions.channels.JoinChannelRequest(channel="@BLACK_MAFIA_OP_BOLTE"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 22 not Found")
        session_name = "startup"
        yaa = TelegramClient(session_name, a, b)
        try:
            await yaa.start()
        except Exception as e:
            pass
   
    if teish:
        session_name = str(teish)
        print("String 23 Found")
        dav = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 23")
            await dav.start()
            botme = await dav.get_me()
            await dav(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await dav(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await dav(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await dav(functions.channels.JoinChannelRequest(channel="@EAGLE_SPAMMER"))
            await dav(functions.channels.JoinChannelRequest(channel="@BLACK_MAFIA_OP_BOLTE"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 23 not Found")
        session_name = "startup"
        dav = TelegramClient(session_name, a, b)
        try:
            await dav.start()
        except Exception as e:
            pass
   
    if tfour:
        session_name = str(tfour)
        print("String 24 Found")
        raj = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 24")
            await raj.start()
            botme = await raj.get_me()
            await raj(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await raj(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await raj(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await raj(functions.channels.JoinChannelRequest(channel="@EAGLE_SPAMMER"))
            await raj(functions.channels.JoinChannelRequest(channel="@BLACK_MAFIA_OP_BOLTE"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 24 not Found")
        session_name = "startup"
        raj = TelegramClient(session_name, a, b)
        try:
            await raj.start()
        except Exception as e:
            pass
   
    if tfive:
        session_name = str(tfive)
        print("String 25 Found")
        put = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 25")
            await put.start()
            botme = await put.get_me()
            await put(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await put(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await put(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await put(functions.channels.JoinChannelRequest(channel="@EAGLE_SPAMMER"))
            await put(functions.channels.JoinChannelRequest(channel="@BLACK_MAFIA_OP_BOLTE"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 25 not Found")
        session_name = "startup"
        put = TelegramClient(session_name, a, b)
        try:
            await put.start()
        except Exception as e:
            pass
   
    if tsix:
        session_name = str(tsix)
        print("String 26 Found")
        eag = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 26")
            await eah.start()
            botme = await eag.get_me()
            await eag(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await eag(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await eag(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await eag(functions.channels.JoinChannelRequest(channel="@EAGLE_SPAMMER"))
            await eag(functions.channels.JoinChannelRequest(channel="@BLACK_MAFIA_OP_BOLTE"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 26 not Found")
        session_name = "startup"
        eag = TelegramClient(session_name, a, b)
        try:
            await eag.start()
        except Exception as e:
            pass
   
    if tseven:
        session_name = str(tseven)
        print("String 27 Found")
        ydk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 27")
            await gle.start()
            await gle(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await gle(functions.channels.JoinChannelRequest(channel="@EAGLE_SPAMMER"))
            await gle(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await gle(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await gle(functions.channels.JoinChannelRequest(channel="@BLACK_MAFIA_OP_BOLTE"))
            botme = await gle.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 27 not Found")
        pass
        session_name = "startup"
        gle = TelegramClient(session_name, a, b)
        try:
            await gle.start()
        except Exception as e:
            pass

    if teight:
        session_name = str(teight)
        print("String 28 Found")
        wal = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 28")
            await  .start()
            await wal(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await wal(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await walfunctions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await wal(functions.channels.JoinChannelRequest(channel="@EAGLE_SPAMMER"))
            await wal(functions.channels.JoinChannelRequest(channel="@BLACK_MAFIA_OP_BOLTE"))
            botme = await wal.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 28 not Found")
        pass
        session_name = "startup"
        wal = TelegramClient(session_name, a, b)
        try:
            await wal.start()
        except Exception as e:
            pass

    if tnine:
        session_name = str(tnine)
        print("String 29 Found")
        aaa = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 29")
            await aaa.start()
            await aaa(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await aaa(functions.channels.JoinChannelRequest(channel="@EAGLE_SPAMMER"))
            await aaa(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await aaa(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await aaa(functions.channels.JoinChannelRequest(channel="@BLACK_MAFIA_OP_BOLTE"))
            botme = await aaa.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 29 not Found")
        pass
        session_name = "startup"
        aaa = TelegramClient(session_name, a, b)
        try:
            await aaa.start()
        except Exception as e:
            pass

    if thirty:
        session_name = str(thirty)
        print("String 30 Found")
        boy = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 30")
            await boy.start()
            await boy(functions.channels.JoinChannelRequest(channel="@RDX_OFFICIAL_BOT"))
            await boy(functions.channels.JoinChannelRequest(channel="@LOVE_LIFE_SI"))
            await boy(functions.channels.JoinChannelRequest(channel="@LOVE_FOREVER_WALA"))
            await boy(functions.channels.JoinChannelRequest(channel="@EAGLE_SPAMMER"))
            await boy(functions.channels.JoinChannelRequest(channel="@BLACK_MAFIA_OP_BOLTE"))
            botme = await boy.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 30 not Found")
        pass
        session_name = "startup"
        boy = TelegramClient(session_name, a, b)
        try:
            await boy.start()
        except Exception as e:
            pass
                  
   
loop = asyncio.get_event_loop()
loop.run_until_complete(start_yukki())       

async def gifspam(e, smex):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=sandy.media.document.id,
                    access_hash=smex.media.document.access_hash,
                    file_reference=smex.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception as e:
        pass


@idk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.bio"))

async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗕𝗶𝗼\n\nCommand:\n\n.bio <Message to set Bio of Userbot accounts>"
    if e.sender_id in SMEX_USERS:
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)     
        if len(e.text) > 5:
            bio = str(yukki[0])
            text = "Changing Bio"
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(functions.account.UpdateProfileRequest(about=bio))
                await event.edit("Succesfully Changed Bio By MULTI SPAMBOT")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
@idk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.join")) 
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.join")) 
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.join")) 
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.join")) 
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.join")) 
@sid.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.join"))


async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗝𝗼𝗶𝗻\n\nCommand:\n\n.join <Public Channel or Group Link/Username>"
    if e.sender_id in SMEX_USERS:
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 6:
            bc = yukki[0]
            text = "Joining..."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(functions.channels.JoinChannelRequest(channel=bc))
                await event.edit("Succesfully Joined")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
@idk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.pjoin")) 
@ake.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))



async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗣𝗿𝗶𝘃𝗮𝘁𝗲 𝗝𝗼𝗶𝗻\n\nCommand:\n\n.pjoin <Private Channel or Group's access hash>\n\nExample :\nLink = https://t.me/joinchat/HGYs1wvsPUplMmM1\n\n.pjoin HGYs1wvsPUplMmM1"
    if e.sender_id in SMEX_USERS:
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = yukki[0]
            text = "Joining...."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(ImportChatInviteRequest(bc))
                await event.edit("Succesfully Joined")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
        
@idk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.leave"))


async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗟𝗲𝗮𝘃𝗲\n\nCommand:\n\n.leave <Channel or Chat ID>"
    if e.sender_id in SMEX_USERS:
        yukki = ("".leave(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = yukki[0]
            bc = int(bc)
            text = "EAGLE BOT Leaving....."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("Succesfully Left")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
                
        
        
@idk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗦𝗽𝗮𝗺\n\nCommand:\n\n.spam <count> <message to spam>\n\n.spam <count> <reply to a message>\n\nCount must be a integer."
    error = "Spam Module can only be used till 100 count. For bigger spams use BigSpam."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(yukki) == 2:
            message = str(yukki[1])
            counter = int(yukki[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            await asyncio.wait([e.respond(message) for i in range(counter)])
        elif e.reply_to_msg_id and smex.media:  
            counter = int(yukki[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            for _ in range(counter):
                smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                await gifspam(e, smex)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(yukki[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            await asyncio.wait([e.respond(message) for i in range(counter)])
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            

@idk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))


async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗹𝗮𝘆𝗦𝗽𝗮𝗺\n\nCommand:\n\n.delayspam <sleep time> <count> <message to spam>\n\n.delayspam <sleep time> <count> <reply to a message>\n\nCount and Sleeptime must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        smex = await e.get_reply_message()
        yukki = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
        yukkisexy = yukki[1:]
        if len(yukkisexy) == 2:
            message = str(yukkisexy[1])
            counter = int(yukkisexy[0])
            sleeptime = float(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.media:  
            counter = int(yukkisexy[0])
            sleeptime = float(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex) 
                await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(yukkisexy[0])
            sleeptime = float(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@idk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))


async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗕𝗶𝗴𝗦𝗽𝗮𝗺\n\nCommand:\n\n.bigspam <count> <message to spam>\n\n.bigspam <count> <reply to a message>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(yukki) == 2:
            message = str(yukki[1])
            counter = int(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.1)
        elif e.reply_to_msg_id and smex.media:  
            counter = int(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex) 
                await asyncio.sleep(0.1)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@idk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗮𝗶𝗱\n\nCommand:\n\n.raid <count> <Username of User>\n\n.raid <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(yukki) == 2:
            message = str(yukki[1])
            print(message)
            a = await e.client.get_entity(message)
            g = a.id
            c = a.first_name
            username = f"[{c}](tg://user?id={g})"
            counter = int(yukki[0])
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            c = b.first_name
            counter = int(yukki[0])
            username = f"[{c}](tg://user?id={g})"
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )



@idk.on(events.NewMessage(incoming=True, pattern=r"\.sid"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.sid"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.sid"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.sid"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.sid"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.sid"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.sid"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.sid"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.sid"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.sid"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.sid"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.sid"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.sid"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.sid"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.sid"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.sid"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.sid"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.sid"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.sid"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.sid"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.sid"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.sid"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.sid"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.sid"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.sid"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.sid"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.sid"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.sid"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.sid"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.sid"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 =     eagle\n\nCommand:\n\n.eagle <count> <Username of User>\n\n.eagle <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(yukki) == 2:
            message = str(yukki[1])
            print(message)
            a = await e.client.get_entity(message)
            g = a.id
            c = a.first_name
            username = f"[{c}](tg://user?id={g})"
            counter = int(yukki[0])
            for _ in range(counter):
                reply = random.choice(EAGLE)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.2)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            c = b.first_name
            counter = int(yukki[0])
            username = f"[{c}](tg://user?id={g})"
            for _ in range(counter):
                reply = random.choice(EAGLE)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.2)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )




@idk.on(events.NewMessage(incoming=True))
@ydk.on(events.NewMessage(incoming=True))
@wdk.on(events.NewMessage(incoming=True))
@hdk.on(events.NewMessage(incoming=True))
@sdk.on(events.NewMessage(incoming=True))
@adk.on(events.NewMessage(incoming=True))
@bdk.on(events.NewMessage(incoming=True))
@cdk.on(events.NewMessage(incoming=True))
@edk.on(events.NewMessage(incoming=True))
@ddk.on(events.NewMessage(incoming=True))
@vkk.on(events.NewMessage(incoming=True))
@kkk.on(events.NewMessage(incoming=True))
@lkk.on(events.NewMessage(incoming=True))
@mkk.on(events.NewMessage(incoming=True))
@sid.on(events.NewMessage(incoming=True))
@shy.on(events.NewMessage(incoming=True))
@aan.on(events.NewMessage(incoming=True))
@ake.on(events.NewMessage(incoming=True))
@eel.on(events.NewMessage(incoming=True))
@khu.on(events.NewMessage(incoming=True))
@shi.on(events.NewMessage(incoming=True))
@yaa.on(events.NewMessage(incoming=True))
@dav.on(events.NewMessage(incoming=True))
@raj.on(events.NewMessage(incoming=True))
@put.on(events.NewMessage(incoming=True))
@eag.on(events.NewMessage(incoming=True))
@gle.on(events.NewMessage(incoming=True))
@wal.on(events.NewMessage(incoming=True))
@aaa.on(events.NewMessage(incoming=True))
@boy.on(events.NewMessage(incoming=True))


async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.2)
    async with event.client.action(event.chat_id, "typing"):
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(random.choice(RRAID)),
            reply_to=event.message.id,
        )           
            
            
@idk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))



async def _(e):
    global que
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱\n\nCommand:\n\n.replyraid <Username of User>\n\n.replyraid <reply to a User>"
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 11:
            message = str(yukki[0])
            a = await e.client.get_entity(message)
            g = a.id
            que[g] = []
            qeue = que.get(g)
            appendable = [g]
            qeue.append(appendable)
            text = "Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            que[g] = []
            qeue = que.get(g)
            appendable = [g]
            qeue.append(appendable)
            text = "Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

            
@idk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))


async def _(e):
    global que
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗮𝗰𝘁𝗶𝘃𝗮𝘁𝗲 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱\n\nCommand:\n\n.dreplyraid <Username of User>\n\n.dreplyraid <reply to a User>"
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 12:
            message = str(yukki[0])
            a = await e.client.get_entity(message)
            g = a.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "De-Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "De-Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
    
       

@idk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.ping"))

async def ping(e):
    if e.sender_id in SMEX_USERS:
        start = datetime.now()
        text = "Pong!"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f" PING !\n`{ms}` 𝗺𝘀")



        
        

@idk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
async def restart(e):
    if e.sender_id in SMEX_USERS:
        text = "𝙍𝙚𝙨𝙩𝙖𝙧𝙩𝙚𝙙\n\nPlease wait till it reboots..."
        await e.reply(text, parse_mode=None, link_preview=None )
        try:
            await idk.disconnect()
        except Exception as e:
            pass
        try:
            await ydk.disconnect()
        except Exception as e:
            pass
        try:
            await wdk.disconnect()
        except Exception as e:
            pass
        try:
            await hdk.disconnect()
        except Exception as e:
            pass
        try:
            await sdk.disconnect()
        except Exception as e:
            pass
        try:
            await adk.disconnect()
        except Exception as e:
            pass
        try:
            await bdk.disconnect()
        except Exception as e:
            pass
        try:
            await cdk.disconnect()
        except Exception as e:
            pass
        try:
            await ddk.disconnect()
        except Exception as e:
            pass
        try:
            await edk.disconnect()
        except Exception as e:
            pass
        try:
            await vkk.disconnect()
        except Exception as e:
            pass
        try:
            await kkk.disconnect()
        except Exception as e:
            pass
        try:
            await lkk.disconnect()
        except Exception as e:
            pass
        try:
            await mkk.disconnect()
        except Exception as e:
            pass
        try:
            await sid.disconnect()
        except Exception as e:
            pass
        try:
            await shy.disconnect()
        except Exception as e:
            pass
        try:
            await aan.disconnect()
        except Exception as e:
            pass
        try:
            await ake.disconnect()
        except Exception as e:
            pass
        try:
            await eel.disconnect()
        except Exception as e:
            pass
        try:
            await khu.disconnect()
        except Exception as e:
            pass
        try:
            await shi.disconnect()
        except Exception as e:
            pass
        try:
            await yaa.disconnect()
        except Exception as e:
            pass
        try:
            await dav.disconnect()
        except Exception as e:
            pass
        try:
            await raj.disconnect()
        except Exception as e:
            pass
        try:
            await put.disconnect()
        except Exception as e:
            pass
        try:
            await eag.disconnect()
        except Exception as e:
            pass
        try:
            await gle.disconnect()
        except Exception as e:
            pass
        try:
            await wal.disconnect()
        except Exception as e:
            pass
        try:
            await aaa.disconnect()
        except Exception as e:
            pass
        try:
            await boy.disconnect()
        except Exception as e:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()

        
        
        
        
        
@idk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.help"))

async def help(e):
    if e.sender_id in SMEX_USERS:
       text = "𝗔𝘃𝗮𝗶𝗹𝗮𝗯𝗹𝗲 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀\n\n𝙐𝙩𝙞𝙡𝙨 𝘾𝙤𝙢𝙢𝙖𝙣𝙙:\n.ping\n.restart\n\n𝙐𝙨𝙚𝙧𝙗𝙤𝙩 𝘾𝙤𝙢𝙢𝙖𝙣𝙙:\n.bio\n.join\n.pjoin\n.leave\n\n𝙎𝙥𝙖𝙢 𝘾𝙤𝙢𝙢𝙖𝙣𝙙:\n.spam\n.delayspam\n.bigspam\n.raid\n.replyraid\n.dreplyraid\n\n\nFor more help regarding usage of plugins type plugins name"
       await e.reply(text, parse_mode=None, link_preview=None )

        
import asyncio
import random
from userbot import bot as pandit
from . import *

NUMBER = ["0", "1"]

PANDIT = [
    "MADARCHOD TERI MAA KI CHUT ME GHUTKA KHAAKE THOOK DUNGA 馃ぃ馃ぃ",
    "TERE BEHEN K CHUT ME CHAKU DAAL KAR CHUT KA KHOON KAR DUGA",
    "TERI VAHEEN NHI HAI KYA? 9 MAHINE RUK SAGI VAHEEN DETA HU 馃ぃ馃ぃ馃ぉ",
    "TERI MAA K BHOSDE ME AEROPLANEPARK KARKE UDAAN BHAR DUGA 鉁堬笍馃洬",
    "TERI MAA KI CHUT ME SUTLI BOMB FOD DUNGA TERI MAA KI JHAATE JAL KE KHAAK HO JAYEGI馃挘",
    "TERI MAAKI CHUT ME SCOOTER DAAL DUGA馃憛",
    "TERE BEHEN K CHUT ME CHAKU DAAL KAR CHUT KA KHOON KAR DUGA",
    "TERE BEHEN K CHUT ME CHAKU DAAL KAR CHUT KA KHOON KAR DUGA",
    "TERI MAA KI CHUT KAKTE 馃け GALI KE KUTTO 馃Ξ ME BAAT DUNGA PHIR 馃崬 BREAD KI TARH KHAYENGE WO TERI MAA KI CHUT",
    "DUDH HILAAUNGA TERI VAHEEN KE UPR NICHE 馃啓馃啋馃槞",
    "TERI MAA KI CHUT ME 鉁� HATTH DALKE 馃懚 BACCHE NIKAL DUNGA 馃槏",
    "TERI BEHN KI CHUT ME KELE KE CHILKE 馃崒馃崒馃槏",
    "TERI BHEN KI CHUT ME USERBOT LAGAAUNGA SASTE SPAM KE CHODE",
    "TERI VAHEEN DHANDHE VAALI 馃構馃槢",
    "TERI MAA KE BHOSDE ME AC LAGA DUNGA SAARI GARMI NIKAL JAAYEGI",
    "TERI VAHEEN KO HORLICKS PEELAUNGA MADARCHOD馃槡",
    "TERI MAA KI GAAND ME SARIYA DAAL DUNGA MADARCHOD USI SARIYE PR TANG KE BACHE PAIDA HONGE 馃槺馃槺",
    "TERI MAA KO KOLKATA VAALE JITU BHAIYA KA LUND MUBARAK 馃ぉ馃ぉ",
    "TERI MUMMY KI FANTASY HU LAWDE, TU APNI BHEN KO SMBHAAL 馃槇馃槇",
    "TERA PEHLA BAAP HU MADARCHOD ",
    "TERI VAHEEN KE BHOSDE ME XVIDEOS.COM CHALA KE MUTH MAARUNGA 馃ぁ馃樄",
    "TERI MAA KA GROUP VAALON SAATH MILKE GANG BANG KRUNGA馃檶馃徎鈽狅笍 ",
    "TERI ITEM KI GAAND ME LUND DAALKE,TERE JAISA EK OR NIKAAL DUNGA MADARCHOD馃馃徎馃檶馃徎鈽狅笍 ",
    "AUKAAT ME REH VRNA GAAND ME DANDA DAAL KE MUH SE NIKAAL DUNGA SHARIR BHI DANDE JESA DIKHEGA 馃檮馃き馃き",
    "TERI MUMMY KE SAATH LUDO KHELTE KHELTE USKE MUH ME APNA LODA DE DUNGA鈽濔煆烩槤馃徎馃槵",
    "TERI VAHEEN KO APNE LUND PR ITNA JHULAAUNGA KI JHULTE JHULTE HI BACHA PAIDA KR DEGI馃憖馃懐 ",
    "TERI MAA KI CHUT MEI BATTERY LAGA KE POWERBANK BANA DUNGA 馃攱 馃敟馃ぉ",
    "TERI MAA KI CHUT MEI C++ STRING ENCRYPTION LAGA DUNGA BAHTI HUYI CHUT RUK JAYEGIIII馃槇馃敟馃槏",
    "TERI MAA KE GAAND MEI JHAADU DAL KE MOR 馃 BANA DUNGAA 馃ぉ馃サ馃槺",
    "TERI CHUT KI CHUT MEI SHOULDERING KAR DUNGAA HILATE HUYE BHI DARD HOGAAA馃槺馃ぎ馃懞",
    "TERI MAA KO REDI PE BAITHAL KE USSE USKI CHUT BILWAUNGAA 馃挵 馃樀馃ぉ",
    "BHOSDIKE TERI MAA KI CHUT MEI 4 HOLE HAI UNME MSEAL LAGA BAHUT BAHETI HAI BHOFDIKE馃憡馃ぎ馃あ馃あ",
    "TERI BAHEN KI CHUT MEI BARGAD KA PED UGA DUNGAA CORONA MEI SAB OXYGEN LEKAR JAYENGE馃あ馃ぉ馃コ",
    "TERI MAA KI CHUT MEI SUDO LAGA KE BIGSPAM LAGA KE 9999 FUCK LAGAA DU 馃ぉ馃コ馃敟",
    "TERI VAHEN KE BHOSDIKE MEI BESAN KE LADDU BHAR DUNGA馃ぉ馃コ馃敟馃槇",
    "TERI MAA KI CHUT KHOD KE USME CYLINDER 鉀斤笍 FIT KARKE USMEE DAL MAKHANI BANAUNGAAA馃ぉ馃憡馃敟",
    "TERI MAA KI CHUT MEI SHEESHA DAL DUNGAAA AUR CHAURAHE PE TAANG DUNGA BHOSDIKE馃槇馃槺馃ぉ",
    "TERI MAA KI CHUT MEI CREDIT CARD DAL KE AGE SE 500 KE KAARE KAARE NOTE NIKALUNGAA BHOSDIKE馃挵馃挵馃ぉ",
    "TERI MAA KE SATH SUAR KA SEX KARWA DUNGAA EK SATH 6-6 BACHE DEGI馃挵馃敟馃槺",
    "TERI BAHEN KI CHUT MEI APPLE KA 18W WALA CHARGER 馃敟馃ぉ",
    "TERI BAHEN KI GAAND MEI ONEPLUS KA WRAP CHARGER 30W HIGH POWER 馃挜馃槀馃槑",
    "TERI BAHEN KI CHUT KO AMAZON SE ORDER KARUNGA 10 rs MEI AUR FLIPKART PE 20 RS MEI BECH DUNGA馃ぎ馃懣馃槇馃",
    "TERI MAA KI BADI BHUND ME ZOMATO DAL KE SUBWAY KA BFF VEG SUB COMBO [15cm , 16 inches ] ORDER COD KRVAUNGA OR TERI MAA JAB DILIVERY DENE AYEGI TAB USPE JAADU KRUNGA OR FIR 9 MONTH BAAD VO EK OR FREE DILIVERY DEGI馃檧馃憤馃コ馃敟",
    "TERI BHEN KI CHUT KAALI馃檨馃ぃ馃挜",
    "TERI MAA KI CHUT ME CHANGES COMMIT KRUGA FIR TERI BHEEN KI CHUT AUTOMATICALLY UPDATE HOJAAYEGI馃馃檹馃",
    "TERI MAUSI KE BHOSDE MEI INDIAN RAILWAY 馃殏馃挜馃槀",
    "TU TERI BAHEN TERA KHANDAN SAB BAHEN KE LAWDE RANDI HAI RANDI 馃あ鉁咅煍�",
    "TERI BAHEN KI CHUT MEI IONIC BOND BANA KE VIRGINITY LOOSE KARWA DUNGA USKI 馃摎 馃槑馃ぉ",
    "TERI RANDI MAA SE PUCHNA BAAP KA NAAM BAHEN KE LODEEEEE 馃ぉ馃コ馃槼",
    "TU AUR TERI MAA DONO KI BHOSDE MEI METRO CHALWA DUNGA MADARXHOD 馃殗馃ぉ馃槺馃ザ",
    "TERI MAA KO ITNA CHODUNGA TERA BAAP BHI USKO PAHCHANANE SE MANA KAR DEGA馃槀馃懣馃ぉ",
    "TERI BAHEN KE BHOSDE MEI HAIR DRYER CHALA DUNGAA馃挜馃敟馃敟",
    "TERI MAA KI CHUT MEI TELEGRAM KI SARI RANDIYON KA RANDI KHANA KHOL DUNGAA馃懣馃ぎ馃槑",
    "TERI MAA KI CHUT ALEXA DAL KEE DJ BAJAUNGAAA 馃幎 猬嗭笍馃ぉ馃挜",
    "TERI MAA KE BHOSDE MEI GITHUB DAL KE APNA BOT HOST KARUNGAA 馃ぉ馃憡馃懁馃槏",
    "TERI BAHEN KA VPS BANA KE 24*7 BASH CHUDAI COMMAND DE DUNGAA 馃ぉ馃挜馃敟馃敟",
    "TERI MUMMY KI CHUT MEI TERE LAND KO DAL KE KAAT DUNGA MADARCHOD 馃敧馃槀馃敟",
    "SUN TERI MAA KA BHOSDA AUR TERI BAHEN KA BHI BHOSDA 馃懣馃槑馃憡",
    "TUJHE DEKH KE TERI RANDI BAHEN PE TARAS ATA HAI MUJHE BAHEN KE LODEEEE 馃懣馃挜馃ぉ馃敟",
    "SUN MADARCHOD JYADA NA UCHAL MAA CHOD DENGE EK MIN MEI 鉁咅煠ｐ煍ヰ煠�",
    "APNI AMMA SE PUCHNA USKO US KAALI RAAT MEI KAUN CHODNEE AYA THAAA! TERE IS PAPA KA NAAM LEGI 馃槀馃懣馃槼",
    "TOHAR BAHIN CHODU BBAHEN KE LAWDE USME MITTI DAL KE CEMENT SE BHAR DU 馃彔馃あ馃ぉ馃挜",
    "TUJHE AB TAK NAHI SMJH AYA KI MAI HI HU TUJHE PAIDA KARNE WALA BHOSDIKEE APNI MAA SE PUCH RANDI KE BACHEEEE 馃ぉ馃憡馃懁馃槏",
    "TERI MAA KE BHOSDE MEI SPOTIFY DAL KE LOFI BAJAUNGA DIN BHAR 馃槏馃幎馃幎馃挜",
    "TERI MAA KA NAYA RANDI KHANA KHOLUNGA CHINTA MAT KAR 馃憡馃ぃ馃ぃ馃槼",
    "TERA BAAP HU BHOSDIKE TERI MAA KO RANDI KHANE PE CHUDWA KE US PAISE KI DAARU PEETA HU 馃嵎馃ぉ馃敟",
    "TERI BAHEN KI CHUT MEI APNA BADA SA LODA GHUSSA DUNGAA KALLAAP KE MAR JAYEGI 馃ぉ馃槼馃槼馃敟",
    "TOHAR MUMMY KI CHUT MEI PURI KI PURI KINGFISHER KI BOTTLE DAL KE TOD DUNGA ANDER HI 馃槺馃槀馃ぉ",
    "TERI MAA KO ITNA CHODUNGA KI SAPNE MEI BHI MERI CHUDAI YAAD KAREGI RANDI 馃コ馃槏馃憡馃挜",
    "TERI MUMMY AUR BAHEN KO DAUDA DAUDA NE CHODUNGA UNKE NO BOLNE PE BHI LAND GHUSA DUNGA ANDER TAK 馃槑馃槑馃ぃ馃敟",
    "TERI MUMMY KI CHUT KO ONLINE OLX PE BECHUNGA AUR PAISE SE TERI BAHEN KA KOTHA KHOL DUNGA 馃槑馃ぉ馃槤馃槏",
    "TERI MAA KE BHOSDA ITNA CHODUNGA KI TU CAH KE BHI WO MAST CHUDAI SE DUR NHI JA PAYEGAA 馃槒馃槒馃ぉ馃槏",
    "SUN BE RANDI KI AULAAD TU APNI BAHEN SE SEEKH KUCH KAISE GAAND MARWATE HAI馃槒馃が馃敟馃挜",
    "TERI MAA KA YAAR HU MEI AUR TERI BAHEN KA PYAAR HU MEI AJA MERA LAND CHOOS LE 馃ぉ馃ぃ馃挜",
    "MADARCHOD",
    "BHOSDIKE",
    "LAAAWEEE KE BAAAAAL",
    "MAAAAR KI JHAAAAT KE BBBBBAAAAALLLLL",
    "MADRCHOD..",
    "TERI MA KI CHUT..",
    "LWDE KE BAAALLL.",
    "MACHAR KI JHAAT KE BAAALLLL",
    "TERI MA KI CHUT M DU TAPA TAP?",
    "TERI MA KA BHOSDAA",
    "TERI BHN SBSBE BDI RANDI.",
    "TERI MA OSSE BADI RANDDDDD",
    "TERA BAAP CHKAAAA",
    "KITNI CHODU TERI MA AB OR..",
    "TERI MA CHOD DI HM NE",
    "TERI MA KE STH REELS BNEGA ROAD PEE",
    "TERI MA KI CHUT EK DAM TOP SEXY",
    "MALUM NA PHR KESE LETA HU M TERI MA KI CHUT TAPA TAPPPPP",
    "LUND KE CHODE TU KEREGA TYPIN",
    "SPEED PKD LWDEEEE",
    "BAAP KI SPEED MTCH KRRR",
    "LWDEEE",
    "PAPA KI SPEED MTCH NHI HO RHI KYA",
    "ALE ALE MELA BCHAAAA",
    "CHUD GYA PAPA SEEE",
    "KISAN KO KHODNA OR",
    "SALE RAPEKL KRDKA TERA",
    "HAHAHAAAAA",
    "KIDSSSS",
    "TERI MA CHUD GYI AB FRAR MT HONA",
    "YE LDNGE BAPP SE",
    "KIDSSS FRAR HAHAHH",
    "BHEN KE LWDE SHRM KR",
    "KITNI GLIYA PDWEGA APNI MA KO",
    "NALLEE",
    "SHRM KR",
    "MERE LUND KE BAAAAALLLLL",
    "KITNI GLIYA PDWYGA APNI MA BHEN KO",
    "RNDI KE LDKEEEEEEEEE",
    "KIDSSSSSSSSSSSS",
    "Apni gaand mein muthi daal",
    "Apni lund choos",
    "Apni ma ko ja choos",
    "Bhen ke laude",
    "Bhen ke takke",
    "Abla TERA KHAN DAN CHODNE KI BARIII",
    "BETE TERI MA SBSE BDI RAND",
    "LUND KE BAAAL JHAT KE PISSSUUUUUUU",
    "LUND PE LTKIT MAAALLLL KI BOND H TUUU",
    "KASH OS DIN MUTH MRKE SOJTA M TUN PAIDA NA HOTAA",
    "GLTI KRDI TUJW PAIDA KRKE",
    "SPEED PKDDD",
    "Gaand main LWDA DAL LE APNI MERAAA",
    "Gaand mein bambu DEDUNGAAAAAA",
    "GAND FTI KE BALKKK",
    "Gote kitne bhi bade ho, lund ke niche hi rehte hai",
    "Hazaar lund teri gaand main",
    "Jhaant ke pissu-",
    "TERI MA KI KALI CHUT",
    "Khotey ki aulda",
    "Kutte ka awlat",
    "Kutte ki jat",
    "Kutte ke tatte",
    "TETI MA KI.CHUT , tERI MA RNDIIIIIIIIIIIIIIIIIIII",
    "Lavde ke bal",
    "muh mei lele",
    "Lund Ke Pasine",
    "MERE LWDE KE BAAAAALLL",
    "HAHAHAAAAAA",
    "CHUD GYAAAAA",
    "Randi khanE KI ULADDD",
    "Sadi hui gaand",
    "Teri gaand main kute ka lund",
    "Teri maa ka bhosda",
    "Teri maa ki chut",
    "Tere gaand mein keede paday",
    "Ullu ke pathe",
    "SUNN MADERCHOD",
    "TERI MAA KA BHOSDA",
    "BEHEN K LUND",
    "TERI MAA KA CHUT KI CHTNIIII",
    "MERA LAWDA LELE TU AGAR CHAIYE TOH",
    "GAANDU",
    "CHUTIYA",
    "TERI MAA KI CHUT PE JCB CHADHAA DUNGA",
    "SAMJHAA LAWDE",
    "YA DU TERE GAAND ME TAPAA TAP锟斤拷",
    "TERI BEHEN MERA ROZ LETI HAI",
    "TERI GF K SAATH MMS BANAA CHUKA HU锟斤拷锟戒笉锟戒笉",
    "TU CHUTIYA TERA KHANDAAN CHUTIYA",
    "AUR KITNA BOLU BEY MANN BHAR GAYA MERA锟戒笉",
    "TERIIIIII MAAAA KI CHUTTT ME ABCD LIKH DUNGA MAA KE LODE",
    "TERI MAA KO LEKAR MAI FARAR",
    "RANIDIII",
    "BACHEE",
    "CHODU",
    "RANDI",
    "RANDI KE PILLE",
    "TERIIIII MAAA KO BHEJJJ",
    "TERAA BAAAAP HU",
    "teri MAA KI CHUT ME HAAT DAALLKE BHAAG JAANUGA",
    "Teri maa KO SARAK PE LETAA DUNGA",
    "TERI MAA KO GB ROAD PE LEJAKE BECH DUNGA",
    "Teri maa KI CHUT M脡 KAALI MITCH",
    "TERI MAA SASTI RANDI HAI",
    "TERI MAA KI CHUT ME KABUTAR DAAL KE SOUP BANAUNGA MADARCHOD",
    "TERI MAAA RANDI HAI",
    "TERI MAAA KI CHUT ME DETOL DAAL DUNGA MADARCHOD",
    "TERI MAA KAAA BHOSDAA",
    "TERI MAA KI CHUT ME LAPTOP",
    "Teri maa RANDI HAI",
    "TERI MAA KO BISTAR PE LETAAKE CHODUNGA",
    "TERI MAA KO AMERICA GHUMAAUNGA MADARCHOD",
    "TERI MAA KI CHUT ME NAARIYAL PHOR DUNGA",
    "TERI MAA KE GAND ME DETOL DAAL DUNGA",
    "TERI MAAA KO HORLICKS PILAUNGA MADARCHOD",
    "TERI MAA KO SARAK PE LETAAA DUNGAAA",
    "TERI MAA KAA BHOSDA",
    "MERAAA LUND PAKAD LE MADARCHOD",
    "CHUP TERI MAA AKAA BHOSDAA",
    "TERIII MAA CHUF GEYII KYAAA LAWDEEE",
    "TERIII MAA KAA BJSODAAA",
    "MADARXHODDD",
    "TERIUUI MAAA KAA BHSODAAA",
    "TERIIIIII BEHENNNN KO CHODDDUUUU MADARXHODDDD",
    "NIKAL MADARCHOD",
    "RANDI KE BACHE",
    "TERA MAA MERI FAN",
    "TERI SEXY BAHEN KI CHUT OP",
]

que = {}


@pandit.on(admin_cmd(incoming=True))
@pandit.on(sudo_cmd(incoming=True, allow_sudo=True))
async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.3)
    async with event.client.action(event.chat_id, "typing"):
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(random.choice(PANDIT)),
            reply_to=event.message.id,
        )

@pandit.on(admin_cmd(pattern="raidop(?: |$)(.*)"))
@pandit.on(sudo_cmd(pattern="raidop(?: |$)(.*)", allow_sudo=True))
async def _(event):
    global que
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        a = await event.get_reply_message()
        b = await event.client.get_entity(a.sender_id)
        e = b.id
        c = b.first_name
        username = f"[{c}](tg://user?id={e})"
        event = await edit_or_reply(event, "TERI MA CHODUNGA AB DEKHTE JAA.")
        que[e] = []
        qeue = que.get(e)
        appendable = [e]
        qeue.append(appendable)
        await event.edit(f"TERI BHEN KI CHUT FADUNGA AB {username}")
    else:
        user = event.pattern_match.group(1)
        event = await edit_or_reply(event, "BCHE TERI MA KI CHUT SALE...")
        a = await event.client.get_entity(user)
        e = a.id
        c = a.first_name
        username = f"[{c}](tg://user?id={e})"
        que[e] = []
        qeue = que.get(e)
        appendable = [e]
        qeue.append(appendable)
        await event.edit(f"TERI BHEN CHODUNGA AB DEKHTE JA. {username}")


@pandit.on(admin_cmd(pattern="stopraid(?: |$)(.*)"))
@pandit.on(sudo_cmd(pattern="stopraid(?: |$)(.*)", allow_sudo=True))
async def _(event):
    global que
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        a = await event.get_reply_message()
        b = await event.client.get_entity(a.sender_id)
        e = b.id
        c = b.first_name
        username = f"[{c}](tg://user?id={e})"
        event = await edit_or_reply(event, "TERI MA CHOD DALI KUTTE KE SAMAN.")
        queue = que.get(e)
        queue.pop(0)
        await event.edit(f"TERI BHEN K RAPE KRDIA HAHA {username}")
    else:
        user = event.pattern_match.group(1)
        event = await edit_or_reply(event, "TERI MA KA RAPE KRDIAA")
        a = await event.client.get_entity(user)
        e = a.id
        c = a.first_name
        username = f"[{c}](tg://user?id={e})"
        queue = que.get(e)
        queue.pop(0)
        await event.edit(f"TERI BHEN KA BHOSDA CHOD KE RANGEEN KRDIAAA {username}")

    
        
text = """

💥💥EAGLE SUPER-30 BOT IS MODIFIED OF YUKKI 💥💥💥
💥💥💥💥💥💥 BY  SIDDHANT  & SIDDHARTH OP 💥💥💥💥💥💥"""

print(text)
print("")
print("SMEX! EAGLE SUPER-30 BOT STARTED SUCCESFULLY.")
if len(sys.argv) not in (1, 3, 4):
    try:
        idk.disconnect()
    except Exception as e:
        pass
    try:
        ydk.disconnect()
    except Exception as e:
        pass
    try:
        wdk.disconnect()
    except Exception as e:
        pass
    try:
        hdk.disconnect()
    except Exception as e:
        pass
    try:
        sdk.disconnect()
    except Exception as e:
        pass
    try:
        adk.disconnect()
    except Exception as e:
        pass
    try:
        bdk.disconnect()
    except Exception as e:
        pass
    try:
        cdk.disconnect()
    except Exception as e:
        pass
    try:
        edk.disconnect()
    except Exception as e:
        pass
    try:
        ddk.disconnect()
    except Exception as e:
        pass
    try:
        vkk.disconnect()
    except Exception as e:
        pass 
    try:
        kkk.disconnect()
    except Exception as e:
        pass
    try:
        lkk.disconnect()
    except Exception as e:
        pass 
    try:
        mkk.disconnect()
    except Exception as e:
        pass
    try:
        sid.disconnect()
    except Exception as e:
        pass
    try:
        shy.disconnect()
    except Exception as e:
        pass
    try:
        aan.disconnect()
    except Exception as e:
        pass
    try:
        ake.disconnect()
    except Exception as e:
        pass
    try:
        eel.disconnect()
    except Exception as e:
        pass
    try:
        khu.disconnect()
    except Exception as e:
        pass
    try:
        shi.disconnect()
    except Exception as e:
        pass
    try:
        yaa.disconnect()
    except Exception as e:
        pass
    try:
        dav.disconnect()
    except Exception as e:
        pass
    try:
        raj.disconnect()
    except Exception as e:
        pass
    try:
        put.disconnect()
    except Exception as e:
        pass
    try:
        eag.disconnect()
    except Exception as e:
        pass
    try:
        gle.disconnect()
    except Exception as e:
        pass
    try:
        wal.disconnect()
    except Exception as e:
        pass
    try:
        aaa.disconnect()
    except Exception as e:
        pass
    try:
        boy.disconnect()
    except Exception as e:
        pass
else:
    try:
        idk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        ydk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        wdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        hdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        sdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        adk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        cdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        edk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        ddk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        vkk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        kkk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        lkk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        mkk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        sid.run_until_disconnected()
    except Exception as e:
        pass
    try:
        shy.run_until_disconnected()
    except Exception as e:
        pass
    try:
        aan.run_until_disconnected()
    except Exception as e:
        pass
    try:
        ake.run_until_disconnected()
    except Exception as e:
        pass
    try:
        eel.run_until_disconnected()
    except Exception as e:
        pass
    try:
        khu.run_until_disconnected()
    except Exception as e:
        pass
    try:
        shi.run_until_disconnected()
    except Exception as e:
        pass
    try:
        yaa.run_until_disconnected()
    except Exception as e:
        pass
    try:
        dav.run_until_disconnected()
    except Exception as e:
        pass
    try:
        raj.run_until_disconnected()
    except Exception as e:
        pass
    try:
        put.run_until_disconnected()
    except Exception as e:
        pass
    try:
        eag.run_until_disconnected()
    except Exception as e:
        pass
    try:
        gle.run_until_disconnected()
    except Exception as e:
        pass
    try:
        wal.run_until_disconnected()
    except Exception as e:
        pass
    try:
        aaa.run_until_disconnected()
    except Exception as e:
        pass
    try:
        boy.run_until_disconnected()
    except Exception as e:
        pass
