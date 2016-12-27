#-*-coding:utf-8-*-

from urllib2 import Request, urlopen
from urllib import urlencode, quote_plus

#from xml.etree.ElementTree import Element, SubElement, dump, fromstring # for xml parsing
import xml.etree.ElementTree as ET

import requests

	
url = ['http://openapi.airport.co.kr/service/rest/wjuParkingLiveService/getParkingLive',  #Wonju
	'http://openapi.airport.co.kr/service/rest/usnParkingLiveService/getParkingLive', #Ulsan
	'http://openapi.airport.co.kr/service/rest/rsuParkingLiveService/getParkingLive', #Yeosu
	'http://openapi.airport.co.kr/service/rest/taeParkingLiveService/getParkingLive', #Daegu
	'http://openapi.airport.co.kr/service/rest/kwjParkingLiveService/getParkingLive', #Gwangju
	'http://openapi.airport.co.kr/service/rest/kuvParkingLiveService/getParkingLive', #Gunsan
	'http://openapi.airport.co.kr/service/rest/cjuParkingLiveService/getParkingLive', #Jeju
	'http://openapi.airport.co.kr/service/rest/pusParkingLiveService/getParkingLive', #Gimhae
	'http://openapi.airport.co.kr/service/rest/gmpParkingLiveService/getParkingLive'  #Gimpo
	]
	
airport_list = ['Wonju', 'urn:epc:id:sgln:0352630.12757.0', # 강원도 횡성군 횡성읍 횡성로 38 / 지리적위치 : 북위 35˚26´30˝ 동경 127˚57´48˝ 해발 99.7~101m
	'Ulsan', 'urn:epc:id:sgln:0353536.12921.0', # 울산광역시 북구 산업로 1103 / 지리적위치 : 북위 35˚35´36˝ 동경 129˚21´38˝
	'Yeosu', 'urn:epc:id:sgln:0345024.12736.0', # 전남 여수시 여순로 386 / 지리적위치 : 북위 34˚50´24˝ 동경 127˚36´57˝ 해발 4m
	'Daegu', 'urn:epc:id:sgln:0355327.12839.0', # 대구광역시 동구 공항로 221 / 지리적위치 : 북위 35˚53´27˝ 동경 128˚39´40˝ 해발 35.4m
	'Gwangju', 'urn:epc:id:sgln:0350730.12648.0', # 광주광역시 광산구 상무대로 420-25 / 지리적위치 : 북위 35˚07´30˝ 동경 126˚48´42˝ 해발 128m
	'Gunsan', 'urn:epc:id:sgln:0354006.12637.0', # 전북 군산시 옥셔면 산동길 2 / 지리적위치 : 북위 35˚40´06˝ 동경 126˚37´06˝ 해발 20m
	'Jeju', 'urn:epc:id:sgln:0335065.12649.0', # 제주특별자치도 제주시 공항로 2 / 지리적위치 :  북위 33˚50´65˝ 동경 126˚49´52˝
	'Gimhae', 'urn:epc:id:sgln:0351728.12894.0', # 부산광역시 강서구 공항진입로 108 / 지리적위치 : 북위 35˚17´28˝ 동경 128˚94´57˝
	'Gimpo', 'urn:epc:id:sgln:0375557.12680.0', # 서울특별시 강서구 하늘길 112 / 지리적위치 : 북위 37˚55´57˝ 동경 126˚80´66˝
	]
parking_list = ['Wonju', u'주차장', 'urn:epc:id:sgln:0352630.12757.1', 
	'Ulsan', u'여객주차장', 'urn:epc:id:sgln:0353536.12921.1',
	'Yeosu', u'여객주차장', 'urn:epc:id:sgln:0345024.12736.1',
	'Daegu', u'여객주차장', 'urn:epc:id:sgln:0355327.12839.1',
	'Daegu', u'화물주차장', 'urn:epc:id:sgln:0355327.12839.2',
	'Gwangju', u'여객주차장', 'urn:epc:id:sgln:0350730.12648.1',
	'Gwangju', u'화물주차장', 'urn:epc:id:sgln:0350730.12648.2',
	'Gunsan', u'여객주차장', 'urn:epc:id:sgln:0354006.12637.1',
	'Jeju', u'화물주차장', 'urn:epc:id:sgln:0335065.12649.1',
	'Jeju', u'여객주차장', 'urn:epc:id:sgln:0335065.12649.2',
	'Gimhae', u'국제화물(장기)', 'urn:epc:id:sgln:0351728.12894.1',
	'Gimhae', u'여객(국내,국제)', 'urn:epc:id:sgln:0351728.12894.2',
	'Gimhae', u'국내화물', 'urn:epc:id:sgln:0351728.12894.3',
	'Gimpo', u'국제선주차장', 'urn:epc:id:sgln:0375557.12680.1',
	'Gimpo', u'국내선 제1주차장', 'urn:epc:id:sgln:0375557.12680.2',
	'Gimpo', u'국내선 제2주차장', 'urn:epc:id:sgln:0375557.12680.3',
	'Gimpo', u'화물청사 주차장', 'urn:epc:id:sgln:0375557.12680.4',
	]

EPCIS_list = ['Wonju', u'주차장', 'http://143.248.53.173:10022/epcis/Service/EventCapture', 
	'Ulsan', u'여객주차장', 'http://143.248.53.173:10022/epcis/Service/EventCapture',
	'Yeosu', u'여객주차장', 'http://143.248.53.173:10022/epcis/Service/EventCapture',
	'Daegu', u'여객주차장', 'http://143.248.53.173:10022/epcis/Service/EventCapture',
	'Daegu', u'화물주차장', 'http://143.248.53.173:10022/epcis/Service/EventCapture',
	'Gwangju', u'여객주차장', 'http://143.248.53.173:10022/epcis/Service/EventCapture',
	'Gwangju', u'화물주차장', 'http://143.248.53.173:10022/epcis/Service/EventCapture',
	'Gunsan', u'여객주차장', 'http://143.248.53.173:10022/epcis/Service/EventCapture',
	'Jeju', u'화물주차장', 'http://143.248.53.173:10022/epcis/Service/EventCapture',
	'Jeju', u'여객주차장', 'http://143.248.53.173:10022/epcis/Service/EventCapture',
	'Gimhae', u'국제화물(장기)', 'http://143.248.53.173:10022/epcis/Service/EventCapture',
	'Gimhae', u'여객(국내,국제)', 'http://143.248.53.173:10022/epcis/Service/EventCapture',
	'Gimhae', u'국내화물', 'http://143.248.53.173:10022/epcis/Service/EventCapture',
	'Gimpo', u'국제선주차장', 'http://143.248.53.173:10022/epcis/Service/EventCapture',
	'Gimpo', u'국내선 제1주차장', 'http://143.248.53.173:10022/epcis/Service/EventCapture',
	'Gimpo', u'국내선 제2주차장', 'http://143.248.53.173:10022/epcis/Service/EventCapture',
	'Gimpo', u'화물청사 주차장', 'http://143.248.53.173:10022/epcis/Service/EventCapture',
	]

parking_address = ['Wonju', u'주차장', u'강원도 횡성군 횡성읍 곡교리 112-1', 
	'Ulsan', u'여객주차장', u'울산광역시 북구 송정동 522',
	'Yeosu', u'여객주차장', u'전라남도 여수시 율촌면 신풍리 983-1',
	'Daegu', u'여객주차장', u'대구광역시 동구 지저동 454-7',
	'Daegu', u'화물주차장', u'대구광역시 동구 지저동 465-1',
	'Gwangju', u'여객주차장', u'광주광역시 광산구 신촌동 698-9',
	'Gwangju', u'화물주차장', u'광주광역시 광산구 신촌동 701-8',
	'Gunsan', u'여객주차장', u'전라북도 군산시 옥서면 선연리 387',
	'Jeju', u'화물주차장', u'제주특별자치도 제주시 용담2동 731-3',
	'Jeju', u'여객주차장', u'제주특별자치도 제주시 용담2동 1462-1',
	'Gimhae', u'국제화물(장기)', u'부산광역시 강서구 대저2동 2148',
	'Gimhae', u'여객(국내,국제)', u'부산광역시 강서구 대저2동 2764',
	'Gimhae', u'국내화물', u'부산광역시 강서구 대저2동 2778-5',
	'Gimpo', u'국제선주차장', u'서울특별시 강서구 방화2동 7',
	'Gimpo', u'국내선 제1주차장', u'서울특별시 강서구 공항동 7',
	'Gimpo', u'국내선 제2주차장', u'서울특별시 강서구 공항동 80-7',
	'Gimpo', u'화물청사 주차장', u'서울특별시 강서구 공항동 281-7',
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
def get_parking_gln(airport, parking_name):
	pos = 0
	airport_name = airport_list[airport*2].encode('utf8')

	while (airport_name !=  parking_list[pos].encode('utf8')):
		pos += 3 #
		if(pos>len(parking_list)):
			print "ERROR: can't find airport name"
			break

	while (parking_name.encode('utf8') !=  parking_list[pos+1].encode('utf8')):
		pos += 3 #
		if(pos>len(parking_list)):
			print "ERROR: can't find parking lot name"
			break

	return parking_list[pos+2]

# address of parking lot
def get_parking_address(airport, parking_name):
	pos = 0
	airport_name = airport_list[airport*2].encode('utf8')

	while (airport_name !=  parking_address[pos].encode('utf8')):
		pos += 3 #
		if(pos>len(parking_address)):
			print "ERROR: can't find airport name"
			break

	while (parking_name.encode('utf8') !=  parking_address[pos+1].encode('utf8')):
		pos += 3 #
		if(pos>len(parking_address)):
			print "ERROR: can't find parking lot name"
			break

	return parking_address[pos+2]	

# EPCIS server of parking lot
def get_EPCIS_server(airport, parking_name):
	pos = 0
	airport_name = airport_list[airport*2].encode('utf8')

	while (airport_name !=  EPCIS_list[pos].encode('utf8')):
		pos += 3 #
		if(pos>len(EPCIS_list)):
			print "ERROR: can't find airport name"
			break

	while (parking_name.encode('utf8') !=  EPCIS_list[pos+1].encode('utf8')):
		pos += 3 #
		if(pos>len(EPCIS_list)):
			print "ERROR: can't find parking lot name"
			break

	return EPCIS_list[pos+2]


queryParams = '?ServiceKey='+key+'&numOfRows='+str(numOfRows)+'&pageNo='+str(pageNo)

def get_parking_data_from_api(airport_num, parking_num):
	request = Request(url[airport_num] + queryParams)
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


airport_num = 0 
parking_num = 0

namespaces = {'epcis': 'urn:epcglobal:epcis:xsd:1',
		'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
		'smartparking': 'http://www.tta.or.kr/epcis/schema/smartparking.xsd#'}

def update_parking_data(parking_info, airport_num, parking_num):
	root = parking_info.getroot()

	#element_body = root.find("body")

	#for element in root.findall("item"):
#	for element in root.iter("item"):
#		for item in element.iter():
#			print item.tag
	#read information from API
	for element in root.iter("item"):
		print "================"
		parking_name = element.findtext("parkingAirportCodeName")	
		print element.findtext("parkingAirportCodeName")
		print element.findtext("parkingGetdate")
		print element.findtext("parkingIincnt")
		print element.findtext("parkingIoutcnt")
		print element.findtext("parkingIstay")
		print element.findtext("parkingPullSpace")
		max_capacity = element.findtext("parkingPullSpace")
		parking_free_space = int(element.findtext("parkingPullSpace")) - int(element.findtext("parkingIstay"))
		print parking_free_space
		print "================"
	
		# read template xml file
		ET.register_namespace('epcis', 'urn:epcglobal:epcis:xsd:1')
		ET.register_namespace('p', 'http://www.unece.org/cefact/namespaces/StandardBusinessDocumentHeader')
		ET.register_namespace('xsi', "http://www.w3.org/2001/XMLSchema-instance")

		parking_event = ET.parse("master_template.xml")
#		ET.dump(parking_event)
		event_root = parking_event.getroot()


		#update file
		for element in event_root.iter("VocabularyElement"):
			element.attrib["id"] = get_parking_gln(airport_num, parking_name)
			for sub_element in event_root.iter("attribute"):
				if (sub_element.attrib["id"] == "http://epcis.example.com/airport/name"):
					sub_element.text = airport_list[airport_num*2] + " airport " + parking_name
				if (sub_element.attrib["id"] == "http://epcis.example.com/airport/address"):
					sub_element.text = get_parking_address(airport_num, parking_name)
				if (sub_element.attrib["id"] == "http://epcis.example.com/airport/max_capacity"):
					sub_element.text = max_capacity

		parking_event.write("output-master"+str(airport_num)+"-"+str(parking_num)+".xml", encoding="utf-8", xml_declaration=True)
		
		
		#url = 'http://143.248.56.130:8080/epcis/Service/EventCapture' #ryun
		#url = 'http://143.248.53.173:10022/epcis/Service/EventCapture' #yeji
		#url = 'http://127.0.0.1:8080/epcis/Service/EventCapture' #localhost
		url = get_EPCIS_server(airport_num, parking_name)
		
		#data = ET.tostring(event_root, encoding='utf-8', method='xml')
		data = ET.tostring(event_root, method='xml')
		#print "======"
		#print data
		#print "======"
		headers = {'Content-Type': 'application/xml'} # set what your server accepts
		#print requests.post(url, data=data, headers=headers).text
		print requests.post(url, data=data, headers=headers).text
		
		parking_num+=1

def main():
	for airport_num in range(len(airport_list)/2):
		parking_num = 0
		print "==================" + str(airport_num) + "=================="
		parking_info = get_parking_data_from_api(airport_num, parking_num)
		update_parking_data(parking_info, airport_num, parking_num)
	

main()

