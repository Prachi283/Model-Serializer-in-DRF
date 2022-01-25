import requests
import json

URL= "http://127.0.0.1:8000/employeeapi/"

# Read Data
def get_data(id=None):
	data={}
	if id is not None:
		data={'id':id}
	json_data=json.dumps(data)
	r= requests.get(url= URL,data=json_data)
	data=r.json()
	print(data)
# get_data()

# Create Data
def post_data():
	data= {
		'name':'Menaka',
		'emp':900,
		'email':'meni@gmail.com',
		'post':'HR Executive'
		}

	json_data=json.dumps(data)
	r=requests.post(url=URL , data= json_data)
	data=r.json()
	print(data)
post_data()

# Update Data
def update_data():
	data= {
		'id': 3 ,
		'name':'ranchi',
		'emp':700,
		'post':'Python Developer'
		}
	json_data=json.dumps(data)
	r=requests.put(url=URL , data= json_data)
	data=r.json()
	print(data)
# update_data()

def delete_data():
	data= {
		'id': 2 
		}
	json_data=json.dumps(data)
	r=requests.delete(url=URL , data= json_data)
	data=r.json()
	print(data)
# delete_data()