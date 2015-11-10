import requests

def submit_form(form_id, responses):
    url = 'https://docs.google.com/forms/d/{0}/formResponse'.format(form_id)
    form_data = {
            'draftResponse':[],
            'pageHistory':0
        }
    form_data.update(responses)
    headers = {
            'Referer':'https://docs.google.com/forms/d/{0}/viewform'.format(form_id),
            'User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36"
        }
    req = requests.post(url, data=form_data, headers=headers)
    return req.ok
