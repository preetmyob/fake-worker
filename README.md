# instructions

## running the program (directly)

### prerequisites
1. you need python installed - I used 3.12

### execution
```bash
# (optional) Creating a virtual evironment
python -m venv venv
source venv/bin/activate

# install program dependencies
pip install requests

# set input environment variable
export GET_WORK_URL=http://headers.jsontest.com

# run
python worker.py
GET_WORK_URL: http://headers.jsontest.com
{
   "X-Cloud-Trace-Context": "952f896a756000efa7c334011c0db4a6/12608285185932020282",
   "Accept": "*/*",
   "traceparent": "00-952f896a756000efa7c334011c0db4a6-aef9a093364c4a3a-00",
   "User-Agent": "python-requests/2.32.3",
   "X-Forwarded-For": "111.69.34.210",
   "Host": "headers.jsontest.com",
   "Via": "1.1 Umbrella_Proxy"
}

```

## running via docker (directly)

```bash
# create the image
docker buildx build --load  --tag workerimage .

# execute
export GET_WORK_URL=http://headers.jsontest.com
docker run -it --rm -e GET_WORK_URL="${GET_WORK_URL}" workerimage
GET_WORK_URL: http://headers.jsontest.com
{
   "X-Cloud-Trace-Context": "8ee30397c385d5cde689ab6f173f82eb/15422058868942071182",
   "Accept": "*/*",
   "traceparent": "00-8ee30397c385d5cde689ab6f173f82eb-d60628d4ec74658e-00",
   "User-Agent": "python-requests/2.32.3",
   "X-Forwarded-For": "111.69.34.210",
   "Host": "headers.jsontest.com",
   "Via": "1.1 Umbrella_Proxy"
}```

## running via docker-compose

```bash
export GET_WORK_URL=http://headers.jsontest.com
docker-compose up
[+] Running 1/0
 ✔ Container fake-worker-worker-1  Created                                                                                                                   0.0s
Attaching to worker-1
worker-1  | GET_WORK_URL: http://headers.jsontest.com
worker-1  | {
worker-1  |    "X-Cloud-Trace-Context": "af1b78b3799405d68314d18aa287a238/5633013972794099908",
worker-1  |    "Accept": "*/*",
worker-1  |    "traceparent": "00-af1b78b3799405d68314d18aa287a238-4e2c7c5cff3448c4-00",
worker-1  |    "User-Agent": "python-requests/2.31.0",
worker-1  |    "X-Forwarded-For": "111.69.34.210",
worker-1  |    "Host": "headers.jsontest.com",
worker-1  |    "Via": "1.1 Umbrella_Proxy"
worker-1  | }
worker-1  |
worker-1 exited with code 0
```

