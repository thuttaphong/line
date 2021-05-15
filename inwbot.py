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
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
#==============================================================================#
botStart = time.time()
#==============================================================================#
from qr import QRLogin
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
#open json file and give it to data variable as a dictionary
with open("db.json") as data_file:
	data = json.load(data_file)

#Defining a HTTP request Handler class
class ServiceHandler(BaseHTTPRequestHandler):
	qrv2 = QRLogin()
	result = qrv2.loginWithQrCode("ipad")
	APP = "IOSIPAD\t10.1.1\tiPhone 8\t11.2.5"
	line = LINE(result.accessToken,appName=APP)
	print(line.authToken)
	print ("Login Succes")
	line.log("Auth Token : " + str(line.authToken))
	line.log("Timeline Token : " + str(line.tl.channelAccessToken))
	print ("Login Succes")

	lineMID = line.profile.mid
	lineProfile = line.getProfile()
	lineSettings = line.getSettings()
	# sets basic headers for the server
	def _set_headers(self):
		self.send_response(200)
		self.send_header('Content-type','text/json')
		#reads the length of the Headers
		length = int(self.headers['Content-Length'])
		#reads the contents of the request
		content = self.rfile.read(length)
		temp = str(content).strip('b\'')
		self.end_headers()
		return temp
		
    	######
	#LIST#
	######
	#GET Method Defination
	def do_GET(self):
		#defining all the headers
		self.send_response(200)
		self.send_header('Content-type','text/json')
		self.end_headers()
		self.line.getGroupsV2('','')
		#prints all the keys and values of the json file
		self.wfile.write(json.dumps(data).encode())
		
    	######
    	#VIEW#
    	######
    	#VIEW method defination
	def do_VIEW(self):
		#dict var. for pretty print
		display = {}
		temp = self._set_headers()
		#check if the key is present in the dictionary
		if temp in data:
			display[temp] = data[temp]
			#print the keys required from the json file
			self.wfile.write(json.dumps(display).encode())
		else:
			error = "NOT FOUND!"
			self.wfile.write(bytes(error,'utf-8'))
			self.send_response(404)
			
    ########
    #CREATE#
    ########
    #POST method defination
	def do_POST(self):
		temp = self._set_headers()
		key=0
		#getting key and value of the data dictionary
		for key,value in data.items():
			pass
		index = int(key)+1
		data[str(index)]=str(temp)
		#write the changes to the json file
		with open("db.json",'w+') as file_data:
			json.dump(data,file_data)
		#self.wfile.write(json.dumps(data[str(index)]).encode())
	
	########
	#UPDATE#
	########
	#PUT method Defination
	def do_PUT(self):
		temp = self._set_headers()
		#seprating input into key and value
		x = temp[:1]
		y = temp[2:]
		#check if key is in data
		if x in data:
			data[x] = y
			#write the changes to file
			with open("db.json",'w+') as file_data:
				json.dump(data,file_data)
			#self.wfile.write(json.dumps(data[str(x)]).encode())
		else:
			error = "NOT FOUND!"
			self.wfile.write(bytes(error,'utf-8'))
			self.send_response(404)
			
	########
	#DELETE#
	########
	#DELETE method defination	
	def do_DELETE(self):
		temp = self._set_headers()
		#check if the key is present in the dictionary
		if temp in data:
			del data[temp]
			#write the changes to json file
			with open("db.json",'w+') as file_data:
				json.dump(data,file_data)
		else:
			error = "NOT FOUND!"
			self.wfile.write(bytes(error,'utf-8'))
			self.send_response(404)
			
#Server Initialization
server = HTTPServer(('127.0.0.1',8081), ServiceHandler)
server.serve_forever()