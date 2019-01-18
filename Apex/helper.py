import requests, json
from Apex.settings import RE_CAPTCHA_SECRET

def checkReCaptcha(response):
    url = 'https://www.google.com/recaptcha/api/siteverify'
    data = {
        'secret': RE_CAPTCHA_SECRET,
        'response': response
    }
    r = requests.post(url, data)
    content = r.content.decode('utf-8')
    rdata = json.loads(content)
    success = rdata['success']
    return success
