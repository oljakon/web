## 10000 запросов с балансировкой

### /api/v1/vacancy/
```
$ ab -c 10 -n 10000 http://127.0.0.1/api/v1/vacancy/
This is ApacheBench, Version 2.3 <$Revision: 1826891 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient)
Completed 1000 requests
Completed 2000 requests
Completed 3000 requests
Completed 4000 requests
Completed 5000 requests
Completed 6000 requests
Completed 7000 requests
Completed 8000 requests
Completed 9000 requests
Completed 10000 requests
Finished 10000 requests


Server Software:        Vacancy
Server Hostname:        127.0.0.1
Server Port:            80

Document Path:          /api/v1/vacancy/
Document Length:        169 bytes

Concurrency Level:      10
Time taken for tests:   1.432 seconds
Complete requests:      10000
Failed requests:        0
Non-2xx responses:      10000
Total transferred:      3750000 bytes
HTML transferred:       1690000 bytes
Requests per second:    6982.74 [#/sec] (mean)
Time per request:       1.432 [ms] (mean)
Time per request:       0.143 [ms] (mean, across all concurrent requests)
Transfer rate:          2557.16 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   5.9      0     414
Processing:     0    1  11.2      0     414
Waiting:        0    1   6.1      0     414
Total:          0    1  12.6      1     414

Percentage of the requests served within a certain time (ms)
  50%      1
  66%      1
  75%      1
  80%      1
  90%      1
  95%      2
  98%      2
  99%      3
 100%    414 (longest request)
```

### /api/v1/vacancy/1/
```
$ ab -c 10 -n 10000 http://127.0.0.1/api/v1/vacancy/1/
This is ApacheBench, Version 2.3 <$Revision: 1826891 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient)
Completed 1000 requests
Completed 2000 requests
Completed 3000 requests
Completed 4000 requests
Completed 5000 requests
Completed 6000 requests
Completed 7000 requests
Completed 8000 requests
Completed 9000 requests
Completed 10000 requests
Finished 10000 requests


Server Software:        Vacancy
Server Hostname:        127.0.0.1
Server Port:            80

Document Path:          /api/v1/vacancy/1/
Document Length:        169 bytes

Concurrency Level:      10
Time taken for tests:   0.983 seconds
Complete requests:      10000
Failed requests:        0
Non-2xx responses:      10000
Total transferred:      3770000 bytes
HTML transferred:       1690000 bytes
Requests per second:    10176.25 [#/sec] (mean)
Time per request:       0.983 [ms] (mean)
Time per request:       0.098 [ms] (mean, across all concurrent requests)
Transfer rate:          3746.53 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.3      0       6
Processing:     0    1   0.3      0       6
Waiting:        0    0   0.2      0       6
Total:          0    1   0.4      1       7
ERROR: The median and mean for the processing time are more than twice the standard
       deviation apart. These results are NOT reliable.

Percentage of the requests served within a certain time (ms)
  50%      1
  66%      1
  75%      1
  80%      1
  90%      1
  95%      2
  98%      2
  99%      3
 100%      7 (longest request)
```

## 10000 запросов без балансировки

### /api/v1/vacancy/
```
$ ab -c 10 -n 10000 http://127.0.0.1/api/v1/vacancy/
This is ApacheBench, Version 2.3 <$Revision: 1826891 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient)
Completed 1000 requests
Completed 2000 requests
Completed 3000 requests
Completed 4000 requests
Completed 5000 requests
Completed 6000 requests
Completed 7000 requests
Completed 8000 requests
Completed 9000 requests
Completed 10000 requests
Finished 10000 requests


Server Software:        Vacancy
Server Hostname:        127.0.0.1
Server Port:            80

Document Path:          /api/v1/vacancy/
Document Length:        169 bytes

Concurrency Level:      10
Time taken for tests:   1.675 seconds
Complete requests:      10000
Failed requests:        0
Non-2xx responses:      10000
Total transferred:      3750000 bytes
HTML transferred:       1690000 bytes
Requests per second:    5970.38 [#/sec] (mean)
Time per request:       1.675 [ms] (mean)
Time per request:       0.167 [ms] (mean, across all concurrent requests)
Transfer rate:          2186.42 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    1  11.2      0     650
Processing:     0    1  15.9      1     650
Waiting:        0    1  15.9      0     650
Total:          0    2  19.5      1     651

Percentage of the requests served within a certain time (ms)
  50%      1
  66%      1
  75%      1
  80%      1
  90%      1
  95%      2
  98%      2
  99%      3
 100%    651 (longest request)
```

### /api/v1/vacancy/1/
```
$ ab -c 10 -n 10000 http://127.0.0.1/api/v1/vacancy/1/
This is ApacheBench, Version 2.3 <$Revision: 1826891 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient)
Completed 1000 requests
Completed 2000 requests
Completed 3000 requests
Completed 4000 requests
Completed 5000 requests
Completed 6000 requests
Completed 7000 requests
Completed 8000 requests
Completed 9000 requests
Completed 10000 requests
Finished 10000 requests


Server Software:        Vacancy
Server Hostname:        127.0.0.1
Server Port:            80

Document Path:          /api/v1/vacancy/1/
Document Length:        169 bytes

Concurrency Level:      10
Time taken for tests:   14.077 seconds
Complete requests:      10000
Failed requests:        0
Non-2xx responses:      10000
Total transferred:      3770000 bytes
HTML transferred:       1690000 bytes
Requests per second:    710.36 [#/sec] (mean)
Time per request:       14.077 [ms] (mean)
Time per request:       1.408 [ms] (mean, across all concurrent requests)
Transfer rate:          261.53 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0   13 414.6      0   13116
Processing:     0    1   7.2      0     273
Waiting:        0    0   6.1      0     273
Total:          0   14 414.6      1   13117

Percentage of the requests served within a certain time (ms)
  50%      1
  66%      1
  75%      1
  80%      1
  90%      1
  95%      1
  98%      2
  99%      2
 100%  13117 (longest request)
```
