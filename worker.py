import requests
import os

def worker():
    # get url from environment variable 
    url = os.getenv('GET_WORK_URL')
    print(f'GET_WORK_URL: {url}')


    # create a client and call the url
    client = requests.session()
    response = client.get(url)

    operation = response.operation
    dbConnectionString = response.dbConnectionString
    statusUrl = response.statusUrl

    # ..... do work .... 
    


    # ..... do work .... 
    


    client.post(statusUrl, json={"status": "done"})
    
    print(response.text)

if __name__ == '__main__':
    worker()