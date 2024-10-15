import requests
import os

def worker():
    # get url from environment variable 
    url = os.getenv('GET_WORK_URL')
    print(f'GET_WORK_URL: {url}')


    # create a client and call the url
    client = requests.session()
    response = client.get(url)

    print(response.text)

if __name__ == '__main__':
    worker()