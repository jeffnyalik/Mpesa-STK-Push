from django.http import HttpResponse
import requests
import json
from requests.auth import HTTPBasicAuth
from datetime import datetime
import base64

class Mpesac2bCredentials:
    consumer_key = '' ##Enter your Consumer Key here...
    consumer_secret = '' ##Enter your Consumer Secret Key here
    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

class MpesaAccessToken:
    r = requests.get(Mpesac2bCredentials.api_URL, auth=HTTPBasicAuth( Mpesac2bCredentials.consumer_key,
    Mpesac2bCredentials.consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validate_mpesa_access_token = mpesa_access_token['access_token']

class LipaNaMpesapassword:
    mpesa_time = datetime.now().strftime('%Y%m%d%H%M%S')
    Business_short_code = '174379'
    passKey = '' #Enter Passkey 
    data_to_encode = Business_short_code + passKey + mpesa_time
    online_password = base64.b64encode(data_to_encode.encode())
    decode_password = online_password.decode('utf-8')