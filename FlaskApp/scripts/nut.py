#UPC Database
from nutritionix import Nutritionix
import json
from bs4 import BeautifulSoup
import requests

nix = Nutritionix(app_id="66cb7ae9", api_key="0cede6486dc6177929d950a7f593d406")

def get_nutritions(food_item):
	print "Food Item -->",food_item
	search_entity = nix.search(str(food_item))
	results = search_entity.json()

	#print json.dumps(results)
	search_results = []
	for result in results['hits']:
		#print json.dumps(result)
		search_results.append(str(result['_id']))
		#a = raw_input("is this the list?")
	print search_results
	if len(search_results) < 1:
		total_calories = None
		burn_time = None
		serving = None
		detail = None
	else:
		for item_id in search_results:
			#nix.item(id=item_id).json
			#print json.dumps(nix.item(id=str(item_id)).json())
			html_format = ""
			json_item = nix.item(id=str(item_id)).json()
			#print json_item 
			# for i in json_item:
			# 	html_format += "<li> " str(i["nf_serving_weight_grams"]) + " g" + \
			# 						str(i["usda_fields"]["VITA_IU"]['desc']) + " " + str(i["usda_fields"]["VITA_IU"]['value']) +\
			# 						str(i["usda_fields"]["VITB12"]['desc']) + " " + str(i["usda_fields"]["VITB12"]['value']) +\
			# 						str(i["usda_fields"]["FE"]['desc']) + " " + str(i["usda_fields"]["FE"]['value']) +\
			# 						str(i["usda_fields"]["PROCTN"]['desc']) + " " + str(i["usda_fields"]["PROCTN"]['value']) +\
			# 						str(i["usda_fields"]["FAT"]['desc']) + " " + str(i["usda_fields"]["FAT"]['value']) +\
			detail = [str(json_item['item_name']),str(json_item['nf_cholesterol']),str(json_item['nf_total_carbohydrate']),str(json_item['nf_protein']),\
						str(json_item['nf_total_fat']),str(json_item['nf_sugars'])]
			total_calories = float(json_item['nf_calories'])
			serving = str(json_item['nf_serving_weight_grams']) + str(" g")
			burn_time = compute_time(total_calories)
			break
		#a = raw_input("Pause...")
	return [total_calories,burn_time,serving,detail]


def compute_time(calories):
	walking_time = int(0.27 * calories)
	running_time = int(0.0975 * calories)
	cycling_time = int(0.14 * calories)

	return [walking_time,running_time,cycling_time]


if __name__ == '__main__':
	print __name__
	print get_nutritions("Chocolate Cake")
	