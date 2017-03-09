from urllib.request import urlopen
import json


def get_data():

	country = input("Enter country name")

	url='https://restcountries.eu/rest/v2/name/'+country+'?fullText=true'

	req=urlopen(url)

	data=req.read().decode('utf')

	json_parse=json.loads(data)[0]
	#print(json_parse)

	Region = json_parse["region"]

	capital = json_parse["capital"]

	zip_code = json_parse["callingCodes"][0]

	time_zone = json_parse["timezones"][0]

	print("%s is in %s region and its capital is %s and its zip code is %s in time zone %s" %(country,Region,capital,zip_code,time_zone))

get_data()