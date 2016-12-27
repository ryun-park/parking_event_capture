#-*-coding:utf-8-*-

from urllib2 import Request, urlopen
from urllib import urlencode, quote_plus

#from xml.etree.ElementTree import Element, SubElement, dump, fromstring # for xml parsing
import xml.etree.ElementTree as ET

import requests

	
url = ['http://openapi.bisco.or.kr/open-api/service/rest/ParkingInfoService/getParkingList',  #Parking list
	'http://openapi.bisco.or.kr/open-api/service/rest/ParkingInfoService/getParkingInfo', #Parking Info
	]
	
parking_list = ['A01', u'명륜역', 'urn:epc:id:sgln:0352137.12908.0', #35.213735, 129.080503
	'A02', u'사상역', 'urn:epc:id:sgln:0351622.12898.0', #35.162266, 128.988617
	'A03', u'동래역', 'urn:epc:id:sgln:0352074.12907.0', #35.207438, 129.078484
	'A04', u'온천장역', 'urn:epc:id:sgln:0352135.12908.0', #35.213530, 129.080126
	'A05', u'부산대남측', 'urn:epc:id:sgln:0352282.12908.0', #35.228230, 129.089236
	'A06', u'부산대북측', 'urn:epc:id:sgln:0352316.12908.0', #35.231672, 129.089029
	'A07', u'장전역', 'urn:epc:id:sgln:0352391.12908.0', #35.239197, 129.088424
	'A08', u'구서역', 'urn:epc:id:sgln:0352455.12909.0', #35.245587, 129.091250
	'A09', u'남산역', 'urn:epc:id:sgln:0352654.12909.0', #35.265426, 129.092845
	'A10', u'노포역', 'urn:epc:id:sgln:0352832.12909.0', #35.283269, 129.095090
	'A11', u'하단역', 'urn:epc:id:sgln:0351046.12896.0', #35.104601, 128.964474
	'A12', u'학장천', 'urn:epc:id:sgln:0351486.12900.0', #35.148666, 129.001273
	'A14', u'장산역2', 'urn:epc:id:sgln:0351691.12917.0', #35.169152, 129.177358
	'A15', u'장산역', 'urn:epc:id:sgln:0351704.12917.0', #35.170445, 129.175992
	'A16', u'해운대광장', 'urn:epc:id:sgln:0351590.12915.0', #35.159073, 129.159332
	'A17', u'수변공원', 'urn:epc:id:sgln:0351548.12913.0', #35.154869, 129.131358
	'A18', u'광안해수월드옆', 'urn:epc:id:sgln:0351563.12913.0', #35.156325, 129.134126
	'A22', u'중동역 주차장', 'urn:epc:id:sgln:0351670.12917.0', #35.167051, 129.170377
	'A23', u'동백사거리 주차장', 'urn:epc:id:sgln:0351575.12915.0', #35.157585, 129.151627
	]

EPCIS_list = ['A01', u'명륜역', 	'http://143.248.53.173:10024/epcis/Service/EventCapture', 
	'A02', u'사상역', 		'http://143.248.53.173:10024/epcis/Service/EventCapture',
	'A03', u'동래역', 		'http://143.248.53.173:10024/epcis/Service/EventCapture',
	'A04', u'온천장역',		'http://143.248.53.173:10024/epcis/Service/EventCapture',
	'A05', u'부산대남측', 		'http://143.248.53.173:10024/epcis/Service/EventCapture',
	'A06', u'부산대북측', 		'http://143.248.53.173:10024/epcis/Service/EventCapture',
	'A07', u'장전역', 		'http://143.248.53.173:10024/epcis/Service/EventCapture',
	'A08', u'구서역', 		'http://143.248.53.173:10024/epcis/Service/EventCapture',
	'A09', u'남산역', 		'http://143.248.53.173:10024/epcis/Service/EventCapture',
	'A10', u'노포역', 		'http://143.248.53.173:10024/epcis/Service/EventCapture',
	'A11', u'하단역', 		'http://143.248.53.173:10024/epcis/Service/EventCapture',
	'A12', u'학장천', 		'http://143.248.53.173:10024/epcis/Service/EventCapture',
	'A14', u'장산역2', 		'http://143.248.53.173:10024/epcis/Service/EventCapture',
	'A15', u'장산역',		'http://143.248.53.173:10024/epcis/Service/EventCapture',
	'A16', u'해운대광장',		'http://143.248.53.173:10024/epcis/Service/EventCapture',
	'A17', u'수변공원',		'http://143.248.53.173:10024/epcis/Service/EventCapture',
	'A18', u'광안해수월드옆',	'http://143.248.53.173:10024/epcis/Service/EventCapture',	
	'A22', u'중동역 주차장',		'http://143.248.53.173:10024/epcis/Service/EventCapture',
	'A23', u'동백사거리 주차장',	'http://143.248.53.173:10024/epcis/Service/EventCapture',	
	]


key = '5xpZRJbVjGb2voi2U0mwHbeekEwkITBJx%2FWfGHf7EYtKzYU4WbQda0Yy6aD7CQlouN3TGZsigaHSiQxIrzITNg%3D%3D'
numOfRows = 999
pageNo = 1

# time stamp
def get_currenttime(): 
#	print "================"
	import datetime
	now = datetime.datetime.now()
	current_time = now.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
#	print current_time
	return current_time

# UTC offset
def get_utcoffset(): 
	import time
	tz = time.timezone
	utc_offset = "%02d:00" % ((-time.timezone/60)/60)
	if (tz < 0):
		utc_offset = '+' + utc_offset
#	print utc_offset
	return utc_offset

# gln of parking lot
def get_parking_gln(parking_name):
	pos = 0

	while (parking_name.encode('utf8') !=  parking_list[pos+1].encode('utf8')):
		pos += 3 #
		if(pos>len(parking_list)):
			print "ERROR: can't find parking lot name"
			break

	return parking_list[pos+2]


# EPCIS server of parking lot
def get_EPCIS_server(parking_name):
	pos = 0

	while (parking_name.encode('utf8') !=  EPCIS_list[pos+1].encode('utf8')):
		pos += 3 #
		if(pos>len(EPCIS_list)):
			print "ERROR: can't find parking lot name"
			break

	return EPCIS_list[pos+2]


def get_parking_data_from_api(parking_num):
	queryParams = '?ServiceKey='+key+'&numOfRows='+str(numOfRows)+'&pageNo='+str(pageNo)+'&pParkGCd='+parking_list[parking_num*3]
	
	request = Request(url[1] + queryParams)
	request.get_method = lambda: 'GET'
	response_body = urlopen(request).read()

	response_url = urlopen(request).geturl() # for debugging

	# print 'query=' + queryParams
	# print '======================'
	# print response_body
	# print '======================'
	# print response_url
	# print '======================'

	parking_info = ET.ElementTree(ET.fromstring(response_body))

	ET.dump(parking_info)
	return parking_info


parking_num = 0

namespaces = {'epcis': 'urn:epcglobal:epcis:xsd:1',
		'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
		'smartparking': 'http://www.tta.or.kr/epcis/schema/smartparking.xsd#'}

def update_parking_data(parking_info, parking_num):
	root = parking_info.getroot()

	#element_body = root.find("body")

	#for element in root.findall("item"):
#	for element in root.iter("item"):
#		for item in element.iter():
#			print item.tag
	#read information from API
	for element in root.iter("item"):
		print "================"
		parking_name = element.findtext("parknm")	
		print element.findtext("curravacnt")
		print element.findtext("lastupdatetime")
		print element.findtext("maxcnt")
		print element.findtext("parkgcd")
		print element.findtext("parkingcnt")
		parking_free_space = int(element.findtext("curravacnt"))
		print parking_free_space
		print "================"
	
		# read template xml file
		ET.register_namespace('epcis', 'urn:epcglobal:epcis:xsd:1')
		ET.register_namespace('xsi', "http://www.w3.org/2001/XMLSchema-instance")
		ET.register_namespace('smartparking', 'http://www.tta.or.kr/epcis/schema/smartparking.xsd#')

		parking_event = ET.parse("event_template.xml")
#		ET.dump(parking_event)
		event_root = parking_event.getroot()


		#update file
		for element in event_root.iter("ObjectEvent"):
			element.find("eventTime").text = get_currenttime()
			print element.findtext("eventTime")
	
			element.find("eventTimeZoneOffset").text = get_utcoffset()
			print element.findtext("eventTimeZoneOffset")
	
			element.find("bizLocation").find("id").text = get_parking_gln(parking_name)
			print element.find("bizLocation").findtext("id")

			element.find("smartparking:available_space", namespaces).text = str(parking_free_space)

		# save result xml for debugging. 
		parking_event.write("output-"+str(parking_num)+".xml", encoding="utf-8", xml_declaration=True)
		
		
		#url = 'http://143.248.56.130:8080/epcis/Service/EventCapture' #ryun
		#url = 'http://143.248.53.173:10024/epcis/Service/EventCapture' #yeji
		#url = 'http://127.0.0.1:8080/epcis/Service/EventCapture' #localhost
		url = get_EPCIS_server(parking_name)
		
		#data = ET.tostring(event_root, encoding='UTF-8', method='xml')
		data = ET.tostring(event_root, method='xml')
		#print "======"
		print data
		#print "======"
		headers = {'Content-Type': 'application/xml'} # set what your server accepts
		#print requests.post(url, data=data, headers=headers).text
		print requests.post(url, data=data, headers=headers).text
		
		parking_num+=1

def main():
	
	for parking_num in range(len(parking_list)/3):
		print "==================" + str(parking_num) + "=================="
		parking_info = get_parking_data_from_api(parking_num)
		update_parking_data(parking_info, parking_num)


main()
