## 10000 запросов с балансировкой

```
ab -c 10 -n 10000 http://127.0.0.1/api/v1/vacancy/
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
Time taken for tests:   1.283 seconds
Complete requests:      10000
Failed requests:        0
Non-2xx responses:      10000
Total transferred:      3750000 bytes
HTML transferred:       1690000 bytes
Requests per second:    7795.89 [#/sec] (mean)
Time per request:       1.283 [ms] (mean)
Time per request:       0.128 [ms] (mean, across all concurrent requests)
Transfer rate:          2854.94 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   2.4      0     140
Processing:     0    1   3.4      1     140
Waiting:        0    0   2.0      0     140
Total:          0    1   4.2      1     141

Percentage of the requests served within a certain time (ms)
  50%      1
  66%      1
  75%      1
  80%      1
  90%      2
  95%      2
  98%      3
  99%      4
 100%    141 (longest request)
```

```
ab -c 10 -n 10000 http://127.0.0.1/api/v1/vacancy/1/
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
Time taken for tests:   1.032 seconds
Complete requests:      10000
Failed requests:        0
Non-2xx responses:      10000
Total transferred:      3770000 bytes
HTML transferred:       1690000 bytes
Requests per second:    9692.72 [#/sec] (mean)
Time per request:       1.032 [ms] (mean)
Time per request:       0.103 [ms] (mean, across all concurrent requests)
Transfer rate:          3568.51 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   5.0      0     352
Processing:     0    1   9.9      0     352
Waiting:        0    1   9.3      0     352
Total:          0    1  11.1      1     352

Percentage of the requests served within a certain time (ms)
  50%      1
  66%      1
  75%      1
  80%      1
  90%      1
  95%      1
  98%      1
  99%      2
 100%    352 (longest request)
```

## 10000 запросов без балансировки

```
ab -c 10 -n 10000 http://127.0.0.1/api/v1/vacancy/
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
Time taken for tests:   0.841 seconds
Complete requests:      10000
Failed requests:        0
Non-2xx responses:      10000
Total transferred:      3750000 bytes
HTML transferred:       1690000 bytes
Requests per second:    11894.41 [#/sec] (mean)
Time per request:       0.841 [ms] (mean)
Time per request:       0.084 [ms] (mean, across all concurrent requests)
Transfer rate:          4355.86 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   1.5      0      86
Processing:     0    0   2.3      0      86
Waiting:        0    0   2.3      0      86
Total:          0    1   2.8      1      86

Percentage of the requests served within a certain time (ms)
  50%      1
  66%      1
  75%      1
  80%      1
  90%      1
  95%      1
  98%      2
  99%      3
 100%     86 (longest request)
```

```
ab -c 10 -n 10000 http://127.0.0.1/api/v1/vacancy/1/
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
Time taken for tests:   0.913 seconds
Complete requests:      10000
Failed requests:        0
Non-2xx responses:      10000
Total transferred:      3770000 bytes
HTML transferred:       1690000 bytes
Requests per second:    10957.86 [#/sec] (mean)
Time per request:       0.913 [ms] (mean)
Time per request:       0.091 [ms] (mean, across all concurrent requests)
Transfer rate:          4034.29 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.3      0       6
Processing:     0    1   0.6      0      15
Waiting:        0    0   0.5      0      14
Total:          0    1   0.7      1      18
WARNING: The median and mean for the processing time are not within a normal deviation
        These results are probably not that reliable.

Percentage of the requests served within a certain time (ms)
  50%      1
  66%      1
  75%      1
  80%      1
  90%      1
  95%      2
  98%      2
  99%      3
 100%     18 (longest request)
```
