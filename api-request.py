from requests import post,get
from time import sleep
from ast import literal_eval

headers =  {'X-Api-Key':'KX55MEJ8DLXN3DVCRVTE'}
data = '{ "studentId": "Tia", "currentBandwidth": 923, "newShaper": 1100, "attemptNumber": 1 }'

url_check = 'https://nxvw9ddm19.execute-api.ap-southeast-2.amazonaws.com/dev/currentBandwidth'
url_update = 'https://nxvw9ddm19.execute-api.ap-southeast-2.amazonaws.com/dev/updateShaper'

attempt = 1
student = "Tia"

def build_data(id,bw,ns,an):

	return '{ "studentId": "'+id+'", "currentBandwidth": '+str(bw)+', "newShaper": '+str(ns)+', "attemptNumber": '+str(an)+' }'


def function_one(delay):

	global attempt

	while(attempt < 5):
		
		response = get(url_check, headers=headers)
		print(response.text)

		current_values = literal_eval(response.text)
		function_two(current_values['shaper'],current_values['currentBandwidth'])

		sleep(delay)



def function_two(shaper_value, shaper_bandwidth):

	global attempt
	new_shaper_value = 0

	max_bandwidth = 0.9*shaper_value
	min_bandwidth = 0.8*shaper_bandwidth

	if (shaper_bandwidth >= max_bandwidth):
		new_shaper_value = function_three('increase', shaper_value)
	elif (shaper_bandwidth < min_bandwidth):
		new_shaper_value =  function_three('decrease', shaper_value)

	if(new_shaper_value):
		response = post(url_update, headers=headers, data=build_data(student,shaper_bandwidth,new_shaper_value,attempt))
		print(response.text)
		attempt += 1



def function_three(function, shaper_value):

	new_shaper_value = shaper_value

	if(function == 'increase'):
		new_shaper_value = 1.1*shaper_value
	elif (function == 'decrease'):
		new_shaper_value = 0.8*shaper_value

	return new_shaper_value


	print(response.text)


delay_s = input ("Enter time interval (s):") 
function_one(int(delay_s))

