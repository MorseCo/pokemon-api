
import json
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def main():
    appUrl = "http://127.0.0.1:5000/pokemon/random"
    requestCount = 20
    successfulCalls = 0
    failedCalls = 0
    
    for i in range(requestCount):
        response = requests.request("GET", appUrl, auth=("ash", "pikachu"))
        print(response.status_code)
        if response.status_code == 200:
            successfulCalls += 1
        elif response.status_code >= 400 or response.status_code < 200:
            failedCalls += 1
        else:
            print(response)
    print(f"Success Rate: {successfulCalls}/{requestCount}")
    print(f"Failure Rate: {failedCalls}/{requestCount}")

if __name__ == '__main__':
    main()