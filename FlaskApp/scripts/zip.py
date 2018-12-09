import urllib, json
import http.client

api_key =  "AIzaSyCU8pm4K5Es8KqVqk4ojzY-G4IwsJPghX0" 

def get_pincode(city):
	try:
		url = "https://maps.googleapis.com/maps/api/geocode/json?address=+"+str(city)+"&key="+str(api_key)
		response = urllib.urlopen(url)
		data = json.loads(response.read())
		location_details =[json.dumps(data['results'][0]['address_components'][0]['long_name']).strip('"'),\
			json.dumps(data['results'][0]['formatted_address']).strip('"')] 
		return location_details
	except:
		print "Error in get_pincode"
		location_details = []
		return location_details

if __name__ == '__main__':
	print __name__