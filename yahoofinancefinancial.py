

import bs4 as bs
import urllib.request
from urllib.request import Request, urlopen
from selenium import webdriver
import time


import bs4 as bs
import urllib.request
from urllib.request import Request, urlopen


import json
import csv
import tweepy
import re
import time
from datetime import datetime
import lxml
from lxml import html
import requests
import numpy as np
import pandas as pd
import bs4 as bs
import urllib.request
from urllib.request import Request, urlopen
from selenium import webdriver


consumer_key = 'GwDiU2tiYgqsWZWcfGm3WdNcr'#input('Consumer Key ')
consumer_secret = 'ojU61L0SRNMgwVuWaAPOW9WDULWMjM1dUzAC3fStFZjR4lqy2Y'#input('Consumer Secret ')
access_token = '1258195865266782209-vFLC6HS57iza6F3DBFkk12ZoyZtT0t'#input('Access Token ')
access_token_secret = 'LAhbLa4caH5bkjimYutpjd0WY3gdOwRi6cpaIjvD8alDk'#input('Access Token Secret ')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)


tweets = []
context = []
username = '' #MrZackMorris #Biotech_SD #Hugh_Henne
count = 400
try: 
# Pulling individual tweets from query
	for tweet in api.user_timeline(id=username, count=count):
# Adding to list that contains all tweets
  		tweets.append(tweet.text+'created at ' +str(tweet.created_at)) #(tweet.created_at,tweet.id,)
  		

except BaseException as e:
      print('failed on_status,',str(e))
      time.sleep(3)


filtered = []
for i in tweets:
	if "$" in str(i):
		filtered.append(str(i))
		context.append(str(i))


#for i in filtered:
	#print(i)

'''for i in filtered:
	print(i)
print(filtered[0])
print(list(filtered[0]))

for i in list(filtered[0]):
	if i == "$":
		print(type(list(filtered[0]).index('$')))
		print(list(filtered[0])[list(filtered[0]).index('$')]+list(filtered[0])[list(filtered[0]).index('$')+1]+list(filtered[0])[list(filtered[0]).index('$')+2]+list(filtered[0])[list(filtered[0]).index('$')+3]+list(filtered[0])[list(filtered[0]).index('$')+4])

lis=[]

def repeat(string):
	for i in list(string):
		if i == '$':
			lis.append('$')
	if len(lis)>1:
		True'''
listed = []
for q in filtered:
#	if repeat(q)==True:
#		print('yo!')
#	else:	
	for i in list(q):
		if i == '$':
			try:
				listed.append(list(q)[list(q).index('$')]+list(q)[list(q).index('$')+1]+list(q)[list(q).index('$')+2]+list(q)[list(q).index('$')+3]+list(q)[list(q).index('$')+4])
			except Exception:
				pass
listed = list(dict.fromkeys(listed))



for q in range(10):
	for i in listed:
		if list(i)[1]==str(q):
			listed.remove(i)

for i in listed:
	if list(i)[1]==' ':
		listed.remove(i)

for i in listed:
	if list(i)[4]==' ':
		listed[listed.index(i)] = i[1:4]
	else:
		listed[listed.index(i)] = i[1:5]







ticker = listed

ticker = ['tif']
print(ticker)



for i in ticker:
	try:
		print("                             "+i+'                             ')
		url = 'https://www.marketwatch.com/investing/stock/'+i+'/financials/balance-sheet/quarter'
		url2 = 'https://finance.yahoo.com/quote/'+i+'/'
		req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
		webpage = urlopen(req).read()

		soup = bs.BeautifulSoup(webpage, 'lxml')

		browser = webdriver.Chrome('C:\\Users\\sam\\Documents\\chromedriver_win32\\chromedriver.exe')
		browser.get(url2)

		sauce= browser.execute_script('return document.documentElement.outerHTML')
		browser.quit()

		soupy = bs.BeautifulSoup(sauce, 'lxml')

		

		cash1 = soup.find_all('tr', class_='mainRow')


#DATA1 = BIGGER DROPDOWNS, MORE GENERAL
		data1 = []
		for i in cash1:
			opend = str(i).index('[')
			close = str(i).index(']')
			#for a in range(int(close)-int(opend)):
				#print(str(i)[opend+a])
			lis = str(i)[int(opend):int(close)]+']'
			empty = lis[lis.rfind(',')+1:-1]
			data1.append(empty)

		for n, i in enumerate(data1):
			if i == 'null':
				data1[n] = '0'

		data1 = list(map(int, data1))

		CASH_N_SHORT_TERM=data1[0]
		TOTAL_ACCNT_RECEIVABLE=data1[1]
		INVENTORIES=data1[2]
		OTHER_CURRENT_ASSETS=data1[3]
		NET_PROP_EQUIP = data1[4]
		TOTAL_INVEST = data1[5]
		LONG_TERM_NOTE = data1[6]
		INTANGIBLE_ASSET = data1[7]
		OTHER_ASSET=data1[8]
		ST_DEBT_CURRENT_LT=data1[9]
		ACCOUNTS_PAYABLE=data1[10]
		OTHER_CURRENT_LIAB = data1[12]
		LT_DEBT = data1[13]
		DEF_TAX=data1[15]
		OTHER_LIAB = data1[16]

#DATA = MORE PRECISE DROP DOWNS
		cash = soup.find_all('tr', class_='rowLevel-2')


		data = []
		for i in cash:
			opend = str(i).index('[')
			close = str(i).index(']')
			#for a in range(int(close)-int(opend)):
				#print(str(i)[opend+a])
			lis = str(i)[int(opend):int(close)]+']'
			empty = lis[lis.rfind(',')+1:-1]
			data.append(empty)

		for n, i in enumerate(data):
			if i == 'null':
				data[n] = '0'

		data = list(map(int, data))

		
		cash_only = data[0]
		short_term_invest = data[1]
		accnt_receiv_net = data[2]
		other_receiv = data[3]
		finished_goods = data[4]
		work_inprogress = data[5]
		raw_materials = data[6]
		progress_payment_other = data[7]
		misc_current_assets = data[8]
		property_plant_equip = data[9]
		accumulated_depreciation = data[10]
		long_term_invest = data[11]
		net_goodwill = data[12]
		intangible_asset = data[13]
		tangible_asset = data[14]
		short_debt = data[15]
		current_long_debt = data[16]
		dividends = data[17]
		acc_payroll = data[18]
		misc_current_liab = data[19]
		long_term_debt_excl_cap_leases = data[20]
		cap_lease_oblig = data[21]
		#def_tax = data[22]+data[23]
		other_liab = data[24]
		def_income = data[25]

		
		inventory= finished_goods+work_inprogress+raw_materials+progress_payment_other
		receivables =accnt_receiv_net+other_receiv 
		cashmoney = cash_only+short_term_invest
		misc_current_a=misc_current_assets
		property_plant=property_plant_equip
		net_other_int=intangible_asset+net_goodwill

		if CASH_N_SHORT_TERM>cash_only+short_term_invest:
			cashmoney = CASH_N_SHORT_TERM
		if TOTAL_ACCNT_RECEIVABLE> accnt_receiv_net+other_receiv:
			receivables = TOTAL_ACCNT_RECEIVABLE
		if INVENTORIES>finished_goods+work_inprogress+raw_materials+progress_payment_other:
			inventory=INVENTORIES
		if OTHER_CURRENT_ASSETS>misc_current_assets:
			misc_current_a=OTHER_CURRENT_ASSETS 
		if NET_PROP_EQUIP>property_plant_equip:
			property_plant=NET_PROP_EQUIP
		if INTANGIBLE_ASSET>intangible_asset+net_goodwill:
			net_other_int=INTANGIBLE_ASSET


		assets = cashmoney +receivables*0.8+inventory*0.5+(property_plant+tangible_asset)*0.6+(net_other_int)*0.6+long_term_invest+misc_current_a+LONG_TERM_NOTE
		print("THE ASSETS ARE $" +str(assets))
		print('\n', '	The cash only is: $'+ str(cash_only))
		print(' 	The property/equipment is: $'+ str(NET_PROP_EQUIP))
		print(' 	The finished goods are: $'+str(finished_goods))
		print(' 	The raw materials are: $'+str(raw_materials))
		print('  	The Goodwill is: $'+str(net_goodwill), '\n')


		liabilities = short_debt + dividends + long_term_debt_excl_cap_leases + other_liab+misc_current_liab+ACCOUNTS_PAYABLE
		print("THE LIABILITIES ARE $" +str(liabilities))
		print('\n', ' 	The short term debt is: $'+str(short_debt))
		print(' 	The current long term debt is: $'+str(current_long_debt), '\n')

		liq_value = assets - liabilities

		print("THE LIQUIDATION VALUE IS $" +str(liq_value))

		price = soupy.find_all('span', class_='Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)')
		
		price1=''
		for i in price:
			current_price=price1+i.text
		

		div = soupy.find_all('td', class_='Ta(end) Fw(600) Lh(14px)')

		listy=[]

		for i in div:
			listy.append(i.text)


		day_range = listy[4]
		year_range = listy[5]
		volume = listy[6]
		avg_volume = listy[7]
		marketcap= listy[8]
		beta = listy[9]
		pe_ratio = listy[10]
		eps = listy[11]
		earnings = listy[12]
		
		def conversion():
			print('THE MARKET CAP IS $' +str(a))
			print('THE MARKET CAP IS '+str(a/liq_value)+'x THAT OF LIQUIDATION')
			print('THE CURRENT PRICE IS $'+current_price)
			print('$'+str(liq_value/(a/float(current_price)))+' SHOULD BE PRICE')

			if ((liq_value)*1.35)>a:
				print("       -----------------------------                  ALERT                  ------------------------------------            ")
				#print('$'+str(liq_value/(a/float(current_price)))+' SHOULD BE PRICE')

		if 'M' in marketcap:
			a=(float(marketcap[:marketcap.index('M')]))*1000000
			'''a =marketcap.replace('M', "")
			float(a)*float(1000000)'''
			conversion()

		if 'B' in marketcap:
			a=(float(marketcap[:marketcap.index('B')]))*1000000000
			'''a =marketcap.replace('B', ' ')
			float(a)*float(1000000000)'''
			conversion()
			
		
		if 'T' in marketcap:
			a=(float(marketcap[:marketcap.index('T')]))*1000000000000
			'''a =marketcap.replace('T', ' ')
			float(a)*float(1000000000000)'''
			conversion()


	except Exception as e:
		print(e)

