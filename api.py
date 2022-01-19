import flask
import requests




url = "http://www.boredapi.com/api/activity/"



def find_activity(activity_type):

    parameters = {
        'type': activity_type,
        'participants': 1
    }

    headers = {
        'Accepts':'application/json'
    }

    response = requests.get(url,params= parameters, headers=headers)
    return response.json().get('activity')


#  activitey types: education,recreational,social, diy, charity, cooking, relaxation, music, busywork]

print(find_activity("education"))