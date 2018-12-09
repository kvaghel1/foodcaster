from flask import Flask,render_template,request,url_for
from scripts.zip import get_pincode
from scripts.yahoo_weather import get_weather
from scripts.nut import get_nutritions
# from wtforms import Form, BooleanField, StringField, PasswordField, validators


app = Flask(__name__)

# class RegistrationForm(Form):
#     username = StringField('Username', [validators.Length(min=4, max=25)])
#     email = StringField('Email Address', [validators.Length(min=6, max=35)])
#     password = PasswordField('New Password', [
#         validators.DataRequired(),
#         validators.EqualTo('confirm', message='Passwords must match')
#     ])
#     confirm = PasswordField('Repeat Password')
#     accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])

@app.route("/")#,methods=['GET','POST']
#@app.route("/")
def main():
	print "Main"
	
	if request.method == "POST":
		print "Main Post"

	if request.method == "GET":
		print "Main Get"

	# text = request.form['seach_food']
	# print text
	return render_template('index.html',show_details = False)

@app.route("/index",methods=['POST'])
def index():
	print "Index"
	if request.method == "POST":
		print "Index Post Method"
		print "Food--->",request.form['search_food']
		print "Details Entered--->",request.form['search_pincode']
		#bool_condition= (str(request.form['search_food']) and str(request.form['search_pincode']))
		bool_condition = bool( (str(request.form['search_food'])) and (str(request.form['search_food'])) )
		print bool_condition
		if bool_condition:
			json_data = {}
			#Location Details
			try:
				address_list = get_pincode(request.form['search_pincode'])
				print "Pincode",address_list[0]
				print "Address",address_list[1]
				json_data["Pincode"] = address_list[0]
				json_data["Address"] = address_list[1]
			except:
				print "Error in Address"
				address_list = [[],"No data found"]
				json_data["Pincode"] = ""
				json_data["Address"] = ""
			
			#Weather Details
			try:
				weather = get_weather(str(address_list[1]))
				print "Full weather:",weather
				print "CC:",weather[0]
				icon_no = 3
				if "cloudy" in weather[0].lower():
					icon_no = 2
				elif "rain" in weather[0].lower() or "thunder" in weather[0].lower():
					icon_no = 1
				print "weather forecast:", weather[2]
			except:
				print "Error in Weather"
				weather = [[],[],[[0,0],[0,0],[0,0],[0,0]]]
				icon_no = 3

			#Nutrition Details
			try:
				nutrition = get_nutritions(request.form['search_food'])
				print "Total Cal -->",nutrition[0]
				print "Time -->",nutrition[1]
				print "Serving --> ",nutrition[2]
				print "Details -->", nutrition[3]
			except:
				print "Error in Nutrition"
				nutrition = [[],[],[],[]]

			return render_template('details.html',temp=address_list[1],current_condition=weather[0],\
					current_temperature=weather[1],weather_forecast=weather[2],calories = nutrition[0],\
					list_time = nutrition[1],weight = nutrition[2],detail_item = nutrition[3],\
					icon_no= str(icon_no), show_details = True) #,detail_item = nutrition[3]
		else:
			pass


	if request.method == "GET":
		print "Index Get Method"

	return render_template('index.html')

if __name__ == "__main__":
    app.run()