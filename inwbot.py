# -*- coding: utf-8 -*-

from linepy import *
from akad.ttypes import Message
from akad.ttypes import ContentType as Type
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib.request, urllib.parse, urllib.error, urllib.parse
from gtts import gTTS
import html5lib,shutil
import wikipedia,goslate
import youtube_dl, pafy, asyncio
from multiprocessing import Pool, Process
from googletrans import Translator
#==============================================================================#
botStart = time.time()
#==============================================================================#


from qr import QRLogin
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
qrv2 = QRLogin()
result = qrv2.loginWithQrCode("ipad")

APP = "IOSIPAD\t10.1.1\tiPhone 8\t11.2.5"
line = LINE(result.accessToken,appName=APP)
print(line.authToken)
print ("Login Succes")
#line = LINE()
#line = LINE("Email","Passwd")
# line = LINE('')
line.log("Auth Token : " + str(line.authToken))
line.log("Timeline Token : " + str(line.tl.channelAccessToken))

print ("Login Succes")

lineMID = line.profile.mid
lineProfile = line.getProfile()
lineSettings = line.getSettings()

oepoll = OEPoll(line)

def lineBot(op):
    try:

        if op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            print(msg)
            print(text)
            print(msg_id)
            print(receiver)
            print(sender)
            if msg.toType == 0:
                if sender != line.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
    except Exception as error:
         logError(error)                

while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
         logError(e)