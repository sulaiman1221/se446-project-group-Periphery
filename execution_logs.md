TASK 2 SAMPLE LOGS FROM TERMINAL:
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
>   -files mapper_task2.py,reducer_sum.py \
>   -mapper "python3 mapper_task2.py" \
>   -reducer "python3 reducer_sum.py" \
>   -input /data/chicago_crimes_sample.csv \
>   -output /user/ssalhammad/project/m1/task2_sample

packageJobJar: [] [/opt/hadoop-3.4.1/share/hadoop/tools/lib/hadoop-streaming-3.4.1.jar] /tmp/streamjob8403315720980474276.jar tmpDir=null
2026-02-17 19:41:45,691 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at master-node/134.209.172.50:8032
2026-02-17 19:41:46,053 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at master-node/134.209.172.50:8032
2026-02-17 19:41:46,550 INFO mapreduce.JobResourceUploader: Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/ssalhammad/.staging/job_1770991083092_0061
2026-02-17 19:41:47,410 INFO mapred.FileInputFormat: Total input files to process : 1
2026-02-17 19:41:47,583 INFO mapreduce.JobSubmitter: number of splits:2
2026-02-17 19:41:48,072 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1770991083092_0061
2026-02-17 19:41:48,072 INFO mapreduce.JobSubmitter: Executing with tokens: []
2026-02-17 19:41:48,449 INFO conf.Configuration: resource-types.xml not found
2026-02-17 19:41:48,450 INFO resource.ResourceUtils: Unable to find 'resource-types.xml'.
2026-02-17 19:41:48,568 INFO impl.YarnClientImpl: Submitted application application_1770991083092_0061
2026-02-17 19:41:48,630 INFO mapreduce.Job: The url to track the job: http://master-node:8088/proxy/application_1770991083092_0061/
2026-02-17 19:41:48,632 INFO mapreduce.Job: Running job: job_1770991083092_0061
2026-02-17 19:42:17,583 INFO mapreduce.Job: Job job_1770991083092_0061 running in uber mode : false
2026-02-17 19:42:17,585 INFO mapreduce.Job:  map 0% reduce 0%
2026-02-17 19:42:47,727 INFO mapreduce.Job:  map 100% reduce 0%
2026-02-17 19:43:05,118 INFO mapreduce.Job:  map 100% reduce 100%
2026-02-17 19:43:06,159 INFO mapreduce.Job: Job job_1770991083092_0061 completed successfully
2026-02-17 19:43:06,452 INFO mapreduce.Job: Counters: 54
        File System Counters
                FILE: Number of bytes read=159339
                FILE: Number of bytes written=1261928
                FILE: Number of read operations=0
                FILE: Number of large read operations=0
                FILE: Number of write operations=0
                HDFS: Number of bytes read=2391502
                HDFS: Number of bytes written=541
                HDFS: Number of read operations=11
                HDFS: Number of large read operations=0
                HDFS: Number of write operations=2
                HDFS: Number of bytes read erasure-coded=0
        Job Counters
                Launched map tasks=2
                Launched reduce tasks=1
                Data-local map tasks=2
                Total time spent by all maps in occupied slots (ms)=106054
                Total time spent by all reduces in occupied slots (ms)=30612
                Total time spent by all map tasks (ms)=53027
                Total time spent by all reduce tasks (ms)=15306
                Total vcore-milliseconds taken by all map tasks=53027
                Total vcore-milliseconds taken by all reduce tasks=15306
                Total megabyte-milliseconds taken by all map tasks=27149824
                Total megabyte-milliseconds taken by all reduce tasks=7836672
        Map-Reduce Framework
                Map input records=10001
                Map output records=10000
                Map output bytes=139333
                Map output materialized bytes=159345
                Input split bytes=212
                Combine input records=0
                Combine output records=0
                Reduce input groups=29
                Reduce shuffle bytes=159345
                Reduce input records=10000
                Reduce output records=29
                Spilled Records=20000
                Shuffled Maps =2
                Failed Shuffles=0
                Merged Map outputs=2
                GC time elapsed (ms)=1386
                CPU time spent (ms)=4570
                Physical memory (bytes) snapshot=658976768
                Virtual memory (bytes) snapshot=6556717056
                Total committed heap usage (bytes)=348168192
                Peak Map Physical memory (bytes)=258523136
                Peak Map Virtual memory (bytes)=2183454720
                Peak Reduce Physical memory (bytes)=151965696
                Peak Reduce Virtual memory (bytes)=2190479360
        Shuffle Errors
                BAD_ID=0
                CONNECTION=0
                IO_ERROR=0
                WRONG_LENGTH=0
                WRONG_MAP=0
                WRONG_REDUCE=0
        File Input Format Counters
                Bytes Read=2391290
        File Output Format Counters
                Bytes Written=541
2026-02-17 19:43:06,453 INFO streaming.StreamJob: Output directory: /user/ssalhammad/project/m1/task2_sample
ssalhammad@master-node:~$ 
ssalhammad@master-node:~$ hdfs dfs -cat /user/ssalhammad/project/m1/task2_sample/part-00000 | head

ARSON   21
ASSAULT 878
BATTERY 1728
BURGLARY        316
CONCEALED CARRY LICENSE VIOLATION       6
CRIM SEXUAL ASSAULT     4
CRIMINAL DAMAGE 1062
CRIMINAL SEXUAL ASSAULT 107
CRIMINAL TRESPASS       153
DECEPTIVE PRACTICE      799
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




TASK 2 FULL LOGS FROM TERMINAL:
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

ssalhammad@master-node:~$ mapred streaming \
>   -files mapper_task2.py,reducer_sum.py \
>   -mapper "python3 mapper_task2.py" \
>   -reducer "python3 reducer_sum.py" \
>   -input /data/chicago_crimes.csv \
>   -output /user/ssalhammad/project/m1/task2_full
packageJobJar: [] [/opt/hadoop-3.4.1/share/hadoop/tools/lib/hadoop-streaming-3.4.1.jar] /tmp/streamjob15969900299456328840.jar tmpDir=null
2026-02-17 19:45:13,798 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at master-node/134.209.172.50:8032
2026-02-17 19:45:14,174 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at master-node/134.209.172.50:8032
2026-02-17 19:45:14,707 INFO mapreduce.JobResourceUploader: Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/ssalhammad/.staging/job_1770991083092_0062
2026-02-17 19:45:15,493 INFO mapred.FileInputFormat: Total input files to process : 1
2026-02-17 19:45:15,642 INFO mapreduce.JobSubmitter: number of splits:15
2026-02-17 19:45:16,075 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1770991083092_0062
2026-02-17 19:45:16,075 INFO mapreduce.JobSubmitter: Executing with tokens: []
2026-02-17 19:45:16,482 INFO conf.Configuration: resource-types.xml not found
2026-02-17 19:45:16,483 INFO resource.ResourceUtils: Unable to find 'resource-types.xml'.
2026-02-17 19:45:16,620 INFO impl.YarnClientImpl: Submitted application application_1770991083092_0062
2026-02-17 19:45:16,691 INFO mapreduce.Job: The url to track the job: http://master-node:8088/proxy/application_1770991083092_0062/
2026-02-17 19:45:16,694 INFO mapreduce.Job: Running job: job_1770991083092_0062
2026-02-17 19:45:46,646 INFO mapreduce.Job: Job job_1770991083092_0062 running in uber mode : false
2026-02-17 19:45:46,648 INFO mapreduce.Job:  map 0% reduce 0%
2026-02-17 19:46:26,265 INFO mapreduce.Job:  map 3% reduce 0%
2026-02-17 19:46:28,336 INFO mapreduce.Job:  map 7% reduce 0%
2026-02-17 19:46:32,464 INFO mapreduce.Job:  map 9% reduce 0%
2026-02-17 19:46:34,516 INFO mapreduce.Job:  map 12% reduce 0%
2026-02-17 19:46:38,638 INFO mapreduce.Job:  map 15% reduce 0%
2026-02-17 19:46:40,696 INFO mapreduce.Job:  map 19% reduce 0%
2026-02-17 19:46:41,735 INFO mapreduce.Job:  map 21% reduce 0%
2026-02-17 19:46:42,805 INFO mapreduce.Job:  map 24% reduce 0%
2026-02-17 19:46:46,916 INFO mapreduce.Job:  map 27% reduce 0%
2026-02-17 19:46:50,035 INFO mapreduce.Job:  map 33% reduce 0%
2026-02-17 19:47:19,876 INFO mapreduce.Job:  map 37% reduce 0%
2026-02-17 19:47:26,010 INFO mapreduce.Job:  map 39% reduce 0%
2026-02-17 19:47:31,108 INFO mapreduce.Job:  map 42% reduce 0%
2026-02-17 19:47:32,139 INFO mapreduce.Job:  map 45% reduce 0%
2026-02-17 19:47:35,218 INFO mapreduce.Job:  map 48% reduce 0%
2026-02-17 19:47:36,232 INFO mapreduce.Job:  map 50% reduce 0%
2026-02-17 19:47:37,252 INFO mapreduce.Job:  map 53% reduce 0%
2026-02-17 19:47:43,390 INFO mapreduce.Job:  map 57% reduce 0%
2026-02-17 19:47:49,537 INFO mapreduce.Job:  map 60% reduce 0%
2026-02-17 19:47:53,635 INFO mapreduce.Job:  map 64% reduce 0%
2026-02-17 19:47:54,660 INFO mapreduce.Job:  map 67% reduce 0%
2026-02-17 19:48:13,000 INFO mapreduce.Job:  map 70% reduce 22%
2026-02-17 19:48:19,105 INFO mapreduce.Job:  map 73% reduce 22%
2026-02-17 19:48:25,232 INFO mapreduce.Job:  map 73% reduce 24%
2026-02-17 19:48:35,404 INFO mapreduce.Job:  map 74% reduce 24%
2026-02-17 19:48:37,431 INFO mapreduce.Job:  map 76% reduce 24%
2026-02-17 19:48:41,491 INFO mapreduce.Job:  map 77% reduce 24%
2026-02-17 19:48:43,517 INFO mapreduce.Job:  map 79% reduce 24%
2026-02-17 19:48:45,543 INFO mapreduce.Job:  map 82% reduce 24%
2026-02-17 19:48:47,568 INFO mapreduce.Job:  map 83% reduce 24%
2026-02-17 19:48:49,598 INFO mapreduce.Job:  map 85% reduce 24%
2026-02-17 19:48:50,607 INFO mapreduce.Job:  map 89% reduce 24%
2026-02-17 19:48:53,655 INFO mapreduce.Job:  map 90% reduce 24%
2026-02-17 19:48:55,685 INFO mapreduce.Job:  map 92% reduce 27%
2026-02-17 19:48:59,759 INFO mapreduce.Job:  map 93% reduce 27%
2026-02-17 19:49:02,082 INFO mapreduce.Job:  map 96% reduce 27%
2026-02-17 19:49:04,116 INFO mapreduce.Job:  map 100% reduce 27%
2026-02-17 19:49:08,177 INFO mapreduce.Job:  map 100% reduce 39%
2026-02-17 19:49:13,238 INFO mapreduce.Job:  map 100% reduce 63%
2026-02-17 19:49:19,323 INFO mapreduce.Job:  map 100% reduce 68%
2026-02-17 19:49:25,397 INFO mapreduce.Job:  map 100% reduce 73%
2026-02-17 19:49:31,480 INFO mapreduce.Job:  map 100% reduce 84%
2026-02-17 19:49:37,554 INFO mapreduce.Job:  map 100% reduce 90%
2026-02-17 19:49:43,635 INFO mapreduce.Job:  map 100% reduce 95%
2026-02-17 19:49:49,713 INFO mapreduce.Job:  map 100% reduce 100%
2026-02-17 19:49:50,745 INFO mapreduce.Job: Job job_1770991083092_0062 completed successfully
2026-02-17 19:49:51,017 INFO mapreduce.Job: Counters: 55
        File System Counters
                FILE: Number of bytes read=128121071
                FILE: Number of bytes written=261272992
                FILE: Number of read operations=0
                FILE: Number of large read operations=0
                FILE: Number of write operations=0
                HDFS: Number of bytes read=2007768170
                HDFS: Number of bytes written=725
                HDFS: Number of read operations=50
                HDFS: Number of large read operations=0
                HDFS: Number of write operations=2
                HDFS: Number of bytes read erasure-coded=0
        Job Counters
                Killed map tasks=2
                Launched map tasks=17
                Launched reduce tasks=1
                Data-local map tasks=17
                Total time spent by all maps in occupied slots (ms)=1729232
                Total time spent by all reduces in occupied slots (ms)=265010
                Total time spent by all map tasks (ms)=864616
                Total time spent by all reduce tasks (ms)=132505
                Total vcore-milliseconds taken by all map tasks=864616
                Total vcore-milliseconds taken by all reduce tasks=132505
                Total megabyte-milliseconds taken by all map tasks=442683392
                Total megabyte-milliseconds taken by all reduce tasks=67842560
        Map-Reduce Framework
                Map input records=8493674
                Map output records=8493673
                Map output bytes=111133719
                Map output materialized bytes=128121155
                Input split bytes=1485
                Combine input records=0
                Combine output records=0
                Reduce input groups=34
                Reduce shuffle bytes=128121155
                Reduce input records=8493673
                Reduce output records=34
                Spilled Records=16987346
                Shuffled Maps =15
                Failed Shuffles=0
                Merged Map outputs=15
                GC time elapsed (ms)=9425
                CPU time spent (ms)=156710
                Physical memory (bytes) snapshot=4138422272
                Virtual memory (bytes) snapshot=34972311552
                Total committed heap usage (bytes)=2567798784
                Peak Map Physical memory (bytes)=276926464
                Peak Map Virtual memory (bytes)=2205978624
                Peak Reduce Physical memory (bytes)=362758144
                Peak Reduce Virtual memory (bytes)=2206646272
        Shuffle Errors
                BAD_ID=0
                CONNECTION=0
                IO_ERROR=0
                WRONG_LENGTH=0
                WRONG_MAP=0
                WRONG_REDUCE=0
        File Input Format Counters
                Bytes Read=2007766685
        File Output Format Counters
                Bytes Written=725
2026-02-17 19:49:51,018 INFO streaming.StreamJob: Output directory: /user/ssalhammad/project/m1/task2_full
ssalhammad@master-node:~$ hdfs dfs -cat /user/ssalhammad/project/m1/task2_full/part-00000 | head

ARSON   14508
ASSAULT 570382
BATTERY 1547201
BURGLARY        448674
CONCEALED CARRY LICENSE VIOLATION       1709
CRIM SEXUAL ASSAULT     27257
CRIMINAL DAMAGE 965727
CRIMINAL SEXUAL ASSAULT 12088
CRIMINAL TRESPASS       228367
DECEPTIVE PRACTICE      392829
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





TASK 3 SAMPLE LOGS FROM TERMINAL:
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
ssalhammad@master-node:~$ mapred streaming \
>   -files mapper_task3.py,reducer_sum.py \ 
>   -mapper "python3 mapper_task3.py" \     
>   -reducer "python3 reducer_sum.py" \
>   -input /data/chicago_crimes_sample.csv \        
>   -output /user/ssalhammad/project/m1/task3_sample

packageJobJar: [] [/opt/hadoop-3.4.1/share/hadoop/tools/lib/hadoop-streaming-3.4.1.jar] /tmp/streamjob13726192675068490526.jar tmpDir=null
2026-02-17 19:20:07,583 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at master-node/134.209.172.50:8032
2026-02-17 19:20:07,941 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at master-node/134.209.172.50:8032
2026-02-17 19:20:08,439 INFO mapreduce.JobResourceUploader: Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/ssalhammad/.staging/job_1770991083092_0058
2026-02-17 19:20:09,287 INFO mapred.FileInputFormat: Total input files to process : 1
2026-02-17 19:20:09,500 INFO mapreduce.JobSubmitter: number of splits:2
2026-02-17 19:20:09,991 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1770991083092_0058
2026-02-17 19:20:09,991 INFO mapreduce.JobSubmitter: Executing with tokens: []
2026-02-17 19:20:10,416 INFO conf.Configuration: resource-types.xml not found
2026-02-17 19:20:10,417 INFO resource.ResourceUtils: Unable to find 'resource-types.xml'.
2026-02-17 19:20:10,562 INFO impl.YarnClientImpl: Submitted application application_1770991083092_0058
2026-02-17 19:20:10,646 INFO mapreduce.Job: The url to track the job: http://master-node:8088/proxy/application_1770991083092_0058/
2026-02-17 19:20:10,648 INFO mapreduce.Job: Running job: job_1770991083092_0058
2026-02-17 19:20:39,567 INFO mapreduce.Job: Job job_1770991083092_0058 running in uber mode : false
2026-02-17 19:20:39,569 INFO mapreduce.Job:  map 0% reduce 0%
2026-02-17 19:21:09,488 INFO mapreduce.Job:  map 100% reduce 0%
2026-02-17 19:21:26,716 INFO mapreduce.Job:  map 100% reduce 100%
2026-02-17 19:21:27,747 INFO mapreduce.Job: Job job_1770991083092_0058 completed successfully
2026-02-17 19:21:28,221 INFO mapreduce.Job: Counters: 54
        File System Counters
                FILE: Number of bytes read=166942       
                FILE: Number of bytes written=1277137   
                FILE: Number of read operations=0       
                FILE: Number of large read operations=0 
                FILE: Number of write operations=0      
                HDFS: Number of bytes read=2391502
                HDFS: Number of bytes written=2628
                HDFS: Number of read operations=11
                HDFS: Number of large read operations=0
                HDFS: Number of write operations=2
                HDFS: Number of bytes read erasure-coded=0
        Job Counters
                Launched map tasks=2
                Launched reduce tasks=1
                Data-local map tasks=2
                Total time spent by all maps in occupied slots (ms)=105850
                Total time spent by all reduces in occupied slots (ms)=29456
                Total time spent by all map tasks (ms)=52925
                Total time spent by all reduce tasks (ms)=14728
                Total vcore-milliseconds taken by all map tasks=52925
                Total vcore-milliseconds taken by all reduce tasks=14728
                Total megabyte-milliseconds taken by all map tasks=27097600
                Total megabyte-milliseconds taken by all reduce tasks=7540736
        Map-Reduce Framework
                Map input records=10001
                Map output records=9907
                Map output bytes=147122
                Map output materialized bytes=166948
                Input split bytes=212
                Combine input records=0
                Combine output records=0
                Reduce input groups=110
                Reduce shuffle bytes=166948
                Reduce input records=9907
                Reduce output records=110
                Spilled Records=19814
                Shuffled Maps =2
                Failed Shuffles=0
                Merged Map outputs=2
                GC time elapsed (ms)=1071
                CPU time spent (ms)=4970
                Physical memory (bytes) snapshot=655745024
                Virtual memory (bytes) snapshot=6563913728
                Total committed heap usage (bytes)=348135424
                Peak Map Physical memory (bytes)=256126976
                Peak Map Virtual memory (bytes)=2188664832
                Peak Reduce Physical memory (bytes)=147025920
                Peak Reduce Virtual memory (bytes)=2190446592
        Shuffle Errors
                BAD_ID=0
                CONNECTION=0
                IO_ERROR=0
                WRONG_LENGTH=0
                WRONG_MAP=0
                WRONG_REDUCE=0
        File Input Format Counters
                Bytes Read=2391290
        File Output Format Counters
                Bytes Written=2628
2026-02-17 19:21:28,221 INFO streaming.StreamJob: Output directory: /user/ssalhammad/project/m1/task3_sample
ssalhammad@master-node:~$ 
ssalhammad@master-node:~$ hdfs dfs -cat /user/ssalhammad/project/m1/task3_sample/part-00000 | head

ABANDONED BUILDING      2
AIRCRAFT        1
AIRPORT BUILDING NON-TERMINAL - NON-SECURE AREA 2
AIRPORT EXTERIOR - NON-SECURE AREA      2
AIRPORT EXTERIOR - SECURE AREA  3
AIRPORT PARKING LOT     8
AIRPORT TERMINAL LOWER LEVEL - NON-SECURE AREA  5
AIRPORT TERMINAL LOWER LEVEL - SECURE AREA      5
AIRPORT TERMINAL UPPER LEVEL - NON-SECURE AREA  4
AIRPORT TERMINAL UPPER LEVEL - SECURE AREA      11
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


TASK 3 FULL LOGS FROM TERMINAL:
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
ssalhammad@master-node:~$ mapred streaming \
>   -files mapper_task3.py,reducer_sum.py \
>   -mapper "python3 mapper_task3.py" \
>   -reducer "python3 reducer_sum.py" \
>   -input /data/chicago_crimes.csv \
>   -output /user/ssalhammad/project/m1/task3_full

packageJobJar: [] [/opt/hadoop-3.4.1/share/hadoop/tools/lib/hadoop-streaming-3.4.1.jar] /tmp/streamjob12225127851772971247.jar tmpDir=null
2026-02-17 19:51:25,279 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at master-node/134.209.172.50:8032
2026-02-17 19:51:25,548 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at master-node/134.209.172.50:8032
2026-02-17 19:51:25,942 INFO mapreduce.JobResourceUploader: Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/ssalhammad/.staging/job_1770991083092_0063
2026-02-17 19:51:26,634 INFO mapred.FileInputFormat: Total input files to process : 1
2026-02-17 19:51:26,771 INFO mapreduce.JobSubmitter: number of splits:15
2026-02-17 19:51:27,095 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1770991083092_0063
2026-02-17 19:51:27,096 INFO mapreduce.JobSubmitter: Executing with tokens: []
2026-02-17 19:51:27,415 INFO conf.Configuration: resource-types.xml not found
2026-02-17 19:51:27,415 INFO resource.ResourceUtils: Unable to find 'resource-types.xml'.
2026-02-17 19:51:27,522 INFO impl.YarnClientImpl: Submitted application application_1770991083092_0063
2026-02-17 19:51:27,585 INFO mapreduce.Job: The url to track the job: http://master-node:8088/proxy/application_1770991083092_0063/
2026-02-17 19:51:27,587 INFO mapreduce.Job: Running job: job_1770991083092_0063
2026-02-17 19:51:57,472 INFO mapreduce.Job: Job job_1770991083092_0063 running in uber mode : false
2026-02-17 19:51:57,474 INFO mapreduce.Job:  map 0% reduce 0%
2026-02-17 19:52:36,226 INFO mapreduce.Job:  map 3% reduce 0%
2026-02-17 19:52:42,297 INFO mapreduce.Job:  map 6% reduce 0%
2026-02-17 19:52:43,305 INFO mapreduce.Job:  map 7% reduce 0%
2026-02-17 19:52:44,314 INFO mapreduce.Job:  map 9% reduce 0%
2026-02-17 19:52:48,357 INFO mapreduce.Job:  map 11% reduce 0%
2026-02-17 19:52:50,385 INFO mapreduce.Job:  map 14% reduce 0%
2026-02-17 19:52:51,421 INFO mapreduce.Job:  map 19% reduce 0%
2026-02-17 19:52:56,486 INFO mapreduce.Job:  map 22% reduce 0%
2026-02-17 19:53:02,582 INFO mapreduce.Job:  map 26% reduce 0%
2026-02-17 19:53:08,657 INFO mapreduce.Job:  map 27% reduce 0%
2026-02-17 19:53:09,680 INFO mapreduce.Job:  map 33% reduce 0%
2026-02-17 19:53:27,957 INFO mapreduce.Job:  map 36% reduce 0%
2026-02-17 19:53:34,018 INFO mapreduce.Job:  map 39% reduce 0%
2026-02-17 19:53:40,100 INFO mapreduce.Job:  map 42% reduce 0%
2026-02-17 19:53:45,142 INFO mapreduce.Job:  map 47% reduce 0%
2026-02-17 19:53:53,216 INFO mapreduce.Job:  map 50% reduce 0%
2026-02-17 19:53:59,282 INFO mapreduce.Job:  map 53% reduce 0%
2026-02-17 19:54:05,335 INFO mapreduce.Job:  map 55% reduce 0%
2026-02-17 19:54:06,344 INFO mapreduce.Job:  map 56% reduce 0%
2026-02-17 19:54:11,422 INFO mapreduce.Job:  map 58% reduce 0%
2026-02-17 19:54:12,431 INFO mapreduce.Job:  map 59% reduce 0%
2026-02-17 19:54:17,472 INFO mapreduce.Job:  map 60% reduce 0%
2026-02-17 19:54:18,487 INFO mapreduce.Job:  map 67% reduce 0%
2026-02-17 19:54:20,504 INFO mapreduce.Job:  map 70% reduce 22%
2026-02-17 19:54:26,551 INFO mapreduce.Job:  map 73% reduce 22%
2026-02-17 19:54:32,615 INFO mapreduce.Job:  map 73% reduce 24%
2026-02-17 19:54:52,818 INFO mapreduce.Job:  map 77% reduce 24%
2026-02-17 19:54:56,867 INFO mapreduce.Job:  map 80% reduce 24%
2026-02-17 19:55:02,915 INFO mapreduce.Job:  map 80% reduce 27%
2026-02-17 19:55:04,935 INFO mapreduce.Job:  map 83% reduce 27%
2026-02-17 19:55:10,990 INFO mapreduce.Job:  map 85% reduce 27%
2026-02-17 19:55:17,038 INFO mapreduce.Job:  map 87% reduce 27%
2026-02-17 19:55:18,045 INFO mapreduce.Job:  map 88% reduce 27%
2026-02-17 19:55:23,079 INFO mapreduce.Job:  map 91% reduce 27%
2026-02-17 19:55:24,090 INFO mapreduce.Job:  map 92% reduce 27%
2026-02-17 19:55:27,247 INFO mapreduce.Job:  map 94% reduce 27%
2026-02-17 19:55:29,261 INFO mapreduce.Job:  map 95% reduce 27%
2026-02-17 19:55:30,270 INFO mapreduce.Job:  map 96% reduce 27%
2026-02-17 19:55:32,287 INFO mapreduce.Job:  map 100% reduce 27%
2026-02-17 19:55:34,305 INFO mapreduce.Job:  map 100% reduce 34%
2026-02-17 19:55:40,351 INFO mapreduce.Job:  map 100% reduce 57%
2026-02-17 19:55:46,395 INFO mapreduce.Job:  map 100% reduce 67%
2026-02-17 19:55:52,436 INFO mapreduce.Job:  map 100% reduce 75%
2026-02-17 19:55:58,482 INFO mapreduce.Job:  map 100% reduce 80%
2026-02-17 19:56:04,530 INFO mapreduce.Job:  map 100% reduce 89%
2026-02-17 19:56:10,586 INFO mapreduce.Job:  map 100% reduce 93%
2026-02-17 19:56:14,615 INFO mapreduce.Job:  map 100% reduce 100%
2026-02-17 19:56:14,631 INFO mapreduce.Job: Job job_1770991083092_0063 completed successfully
2026-02-17 19:56:14,914 INFO mapreduce.Job: Counters: 55
        File System Counters
                FILE: Number of bytes read=137941496
                FILE: Number of bytes written=280913842
                FILE: Number of read operations=0
                FILE: Number of large read operations=0
                FILE: Number of write operations=0
                HDFS: Number of bytes read=2007768170
                HDFS: Number of bytes written=5125
                HDFS: Number of read operations=50
                HDFS: Number of large read operations=0
                HDFS: Number of write operations=2
                HDFS: Number of bytes read erasure-coded=0
        Job Counters
                Killed map tasks=2
                Launched map tasks=17
                Launched reduce tasks=1
                Data-local map tasks=17
                Total time spent by all maps in occupied slots (ms)=1864904
                Total time spent by all reduces in occupied slots (ms)=296356
                Total time spent by all map tasks (ms)=932452
                Total time spent by all reduce tasks (ms)=148178
                Total vcore-milliseconds taken by all map tasks=932452
                Total vcore-milliseconds taken by all reduce tasks=148178
                Total megabyte-milliseconds taken by all map tasks=477415424
                Total megabyte-milliseconds taken by all reduce tasks=75867136
        Map-Reduce Framework
                Map input records=8493674
                Map output records=8478108
                Map output bytes=120985274
                Map output materialized bytes=137941580
                Input split bytes=1485
                Combine input records=0
                Combine output records=0
                Reduce input groups=218
                Reduce shuffle bytes=137941580
                Reduce input records=8478108
                Reduce output records=218
                Spilled Records=16956216
                Shuffled Maps =15
                Failed Shuffles=0
                Merged Map outputs=15
                GC time elapsed (ms)=10841
                CPU time spent (ms)=160930
                Physical memory (bytes) snapshot=4195790848
                Virtual memory (bytes) snapshot=34979389440
                Total committed heap usage (bytes)=2585530368
                Peak Map Physical memory (bytes)=282071040
                Peak Map Virtual memory (bytes)=2208104448
                Peak Reduce Physical memory (bytes)=374673408
                Peak Reduce Virtual memory (bytes)=2206728192
        Shuffle Errors
                BAD_ID=0
                CONNECTION=0
                IO_ERROR=0
                WRONG_LENGTH=0
                WRONG_MAP=0
                WRONG_REDUCE=0
        File Input Format Counters
                Bytes Read=2007766685
        File Output Format Counters
                Bytes Written=5125
2026-02-17 19:56:14,921 INFO streaming.StreamJob: Output directory: /user/ssalhammad/project/m1/task3_full
ssalhammad@master-node:~$ 
ssalhammad@master-node:~$ hdfs dfs -cat /user/ssalhammad/project/m1/task3_full/part-00000 | head

ABANDONED BUILDING      12234
AIRCRAFT        1009
AIRPORT BUILDING NON-TERMINAL - NON-SECURE AREA 1585
AIRPORT BUILDING NON-TERMINAL - SECURE AREA     938
AIRPORT EXTERIOR - NON-SECURE AREA      1337
AIRPORT EXTERIOR - SECURE AREA  633
AIRPORT PARKING LOT     1934
AIRPORT TERMINAL LOWER LEVEL - NON-SECURE AREA  2752
AIRPORT TERMINAL LOWER LEVEL - SECURE AREA      1189
AIRPORT TERMINAL MEZZANINE - NON-SECURE AREA    157
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




TASK 4 SAMPLE LOGS FROM TERMINAL:
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
ssalhammad@master-node:~$ mapred streaming \
>   -files mapper_task4.py,reducer_sum.py \
>   -mapper "python3 mapper_task4.py" \
>   -reducer "python3 reducer_sum.py" \
>   -input /data/chicago_crimes_sample.csv \
>   -output /user/ssalhammad/project/m1/task4_sample

packageJobJar: [] [/opt/hadoop-3.4.1/share/hadoop/tools/lib/hadoop-streaming-3.4.1.jar] /tmp/streamjob15589794351446124258.jar tmpDir=null
2026-02-17 19:29:12,975 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at master-node/134.209.172.50:8032
2026-02-17 19:29:13,333 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at master-node/134.209.172.50:8032
2026-02-17 19:29:13,853 INFO mapreduce.JobResourceUploader: Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/ssalhammad/.staging/job_1770991083092_0059
2026-02-17 19:29:14,713 INFO mapred.FileInputFormat: Total input files to process : 1
2026-02-17 19:29:14,865 INFO mapreduce.JobSubmitter: number of splits:2
2026-02-17 19:29:15,380 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1770991083092_0059
2026-02-17 19:29:15,380 INFO mapreduce.JobSubmitter: Executing with tokens: []
2026-02-17 19:29:15,747 INFO conf.Configuration: resource-types.xml not found
2026-02-17 19:29:15,748 INFO resource.ResourceUtils: Unable to find 'resource-types.xml'.
2026-02-17 19:29:15,876 INFO impl.YarnClientImpl: Submitted application application_1770991083092_0059
2026-02-17 19:29:15,923 INFO mapreduce.Job: The url to track the job: http://master-node:8088/proxy/application_1770991083092_0059/
2026-02-17 19:29:15,925 INFO mapreduce.Job: Running job: job_1770991083092_0059
2026-02-17 19:29:44,090 INFO mapreduce.Job: Job job_1770991083092_0059 running in uber mode : false
2026-02-17 19:29:44,092 INFO mapreduce.Job:  map 0% reduce 0%
2026-02-17 19:30:15,673 INFO mapreduce.Job:  map 100% reduce 0%
2026-02-17 19:30:35,254 INFO mapreduce.Job:  map 100% reduce 100%
2026-02-17 19:30:36,302 INFO mapreduce.Job: Job job_1770991083092_0059 completed successfully
2026-02-17 19:30:36,566 INFO mapreduce.Job: Counters: 54
        File System Counters
                FILE: Number of bytes read=90006
                FILE: Number of bytes written=1123265
                FILE: Number of read operations=0
                FILE: Number of large read operations=0
                FILE: Number of write operations=0
                HDFS: Number of bytes read=2391502
                HDFS: Number of bytes written=185
                HDFS: Number of read operations=11
                HDFS: Number of large read operations=0
                HDFS: Number of write operations=2
                HDFS: Number of bytes read erasure-coded=0
        Job Counters
                Launched map tasks=2
                Launched reduce tasks=1
                Data-local map tasks=2
                Total time spent by all maps in occupied slots (ms)=110554
                Total time spent by all reduces in occupied slots (ms)=35456
                Total time spent by all map tasks (ms)=55277
                Total time spent by all reduce tasks (ms)=17728
                Total vcore-milliseconds taken by all map tasks=55277
                Total vcore-milliseconds taken by all reduce tasks=17728
                Total megabyte-milliseconds taken by all map tasks=28301824
                Total megabyte-milliseconds taken by all reduce tasks=9076736
        Map-Reduce Framework
                Map input records=10001
                Map output records=10000
                Map output bytes=70000
                Map output materialized bytes=90012
                Input split bytes=212
                Combine input records=0
                Combine output records=0
                Reduce input groups=24
                Reduce shuffle bytes=90012
                Reduce input records=10000
                Reduce output records=24
                Spilled Records=20000
                Shuffled Maps =2
                Failed Shuffles=0
                Merged Map outputs=2
                GC time elapsed (ms)=1515
                CPU time spent (ms)=5070
                Physical memory (bytes) snapshot=639451136
                Virtual memory (bytes) snapshot=6557147136
                Total committed heap usage (bytes)=348164096
                Peak Map Physical memory (bytes)=247341056
                Peak Map Virtual memory (bytes)=2184556544
                Peak Reduce Physical memory (bytes)=145498112
                Peak Reduce Virtual memory (bytes)=2190262272
        Shuffle Errors
                BAD_ID=0
                CONNECTION=0
                IO_ERROR=0
                WRONG_LENGTH=0
                WRONG_MAP=0
                WRONG_REDUCE=0
        File Input Format Counters
                Bytes Read=2391290
        File Output Format Counters
                Bytes Written=185
2026-02-17 19:30:36,566 INFO streaming.StreamJob: Output directory: /user/ssalhammad/project/m1/task4_sample
ssalhammad@master-node:~$ 
ssalhammad@master-node:~$ hdfs dfs -cat /user/ssalhammad/project/m1/task4_sample/part-00000 | head

2001    4
2002    2
2003    1
2004    6
2005    19
2006    4
2007    7
2008    16
2009    5
2010    5
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


TASK 4 FULL LOGS FROM TERMINAL:
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
ssalhammad@master-node:~$ mapred streaming \
>   -files mapper_task4.py,reducer_sum.py \
>   -mapper "python3 mapper_task4.py" \
>   -reducer "python3 reducer_sum.py" \
>   -input /data/chicago_crimes.csv \
>   -output /user/ssalhammad/project/m1/task4_full
packageJobJar: [] [/opt/hadoop-3.4.1/share/hadoop/tools/lib/hadoop-streaming-3.4.1.jar] /tmp/streamjob6751765559408225126.jar tmpDir=null
2026-02-17 20:08:11,490 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at master-node/134.209.172.50:8032
2026-02-17 20:08:11,856 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at master-node/134.209.172.50:8032
2026-02-17 20:08:12,413 INFO mapreduce.JobResourceUploader: Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/ssalhammad/.staging/job_1770991083092_0064
2026-02-17 20:08:13,231 INFO mapred.FileInputFormat: Total input files to process : 1
2026-02-17 20:08:13,397 INFO mapreduce.JobSubmitter: number of splits:15
2026-02-17 20:08:13,737 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1770991083092_0064
2026-02-17 20:08:13,738 INFO mapreduce.JobSubmitter: Executing with tokens: []
2026-02-17 20:08:14,031 INFO conf.Configuration: resource-types.xml not found
2026-02-17 20:08:14,031 INFO resource.ResourceUtils: Unable to find 'resource-types.xml'.
2026-02-17 20:08:14,159 INFO impl.YarnClientImpl: Submitted application application_1770991083092_0064
2026-02-17 20:08:14,218 INFO mapreduce.Job: The url to track the job: http://master-node:8088/proxy/application_1770991083092_0064/
2026-02-17 20:08:14,221 INFO mapreduce.Job: Running job: job_1770991083092_0064
2026-02-17 20:08:40,157 INFO mapreduce.Job: Job job_1770991083092_0064 running in uber mode : false
2026-02-17 20:08:40,159 INFO mapreduce.Job:  map 0% reduce 0%
2026-02-17 20:09:17,067 INFO mapreduce.Job:  map 3% reduce 0%
2026-02-17 20:09:23,139 INFO mapreduce.Job:  map 6% reduce 0%
2026-02-17 20:09:29,202 INFO mapreduce.Job:  map 10% reduce 0%
2026-02-17 20:09:30,211 INFO mapreduce.Job:  map 11% reduce 0%
2026-02-17 20:09:31,268 INFO mapreduce.Job:  map 16% reduce 0%
2026-02-17 20:09:35,323 INFO mapreduce.Job:  map 17% reduce 0%
2026-02-17 20:09:36,335 INFO mapreduce.Job:  map 18% reduce 0%
2026-02-17 20:09:42,412 INFO mapreduce.Job:  map 21% reduce 0%
2026-02-17 20:09:48,471 INFO mapreduce.Job:  map 24% reduce 0%
2026-02-17 20:09:54,535 INFO mapreduce.Job:  map 27% reduce 0%
2026-02-17 20:09:58,583 INFO mapreduce.Job:  map 33% reduce 0%
2026-02-17 20:10:02,635 INFO mapreduce.Job:  map 37% reduce 0%
2026-02-17 20:10:08,721 INFO mapreduce.Job:  map 39% reduce 0%
2026-02-17 20:10:14,816 INFO mapreduce.Job:  map 42% reduce 0%
2026-02-17 20:10:18,869 INFO mapreduce.Job:  map 47% reduce 0%
2026-02-17 20:10:47,197 INFO mapreduce.Job:  map 50% reduce 0%
2026-02-17 20:10:50,223 INFO mapreduce.Job:  map 54% reduce 16%
2026-02-17 20:10:53,268 INFO mapreduce.Job:  map 56% reduce 16%
2026-02-17 20:10:54,276 INFO mapreduce.Job:  map 59% reduce 16%
2026-02-17 20:10:56,296 INFO mapreduce.Job:  map 59% reduce 18%
2026-02-17 20:10:59,329 INFO mapreduce.Job:  map 62% reduce 18%
2026-02-17 20:11:05,383 INFO mapreduce.Job:  map 65% reduce 18%
2026-02-17 20:11:11,437 INFO mapreduce.Job:  map 67% reduce 18%
2026-02-17 20:11:12,444 INFO mapreduce.Job:  map 71% reduce 18%
2026-02-17 20:11:13,452 INFO mapreduce.Job:  map 73% reduce 18%
2026-02-17 20:11:14,465 INFO mapreduce.Job:  map 73% reduce 24%
2026-02-17 20:11:19,530 INFO mapreduce.Job:  map 77% reduce 24%
2026-02-17 20:11:22,562 INFO mapreduce.Job:  map 80% reduce 24%
2026-02-17 20:11:26,596 INFO mapreduce.Job:  map 80% reduce 27%
2026-02-17 20:11:49,786 INFO mapreduce.Job:  map 83% reduce 27%
2026-02-17 20:11:53,821 INFO mapreduce.Job:  map 87% reduce 27%
2026-02-17 20:11:56,842 INFO mapreduce.Job:  map 88% reduce 29%
2026-02-17 20:12:02,891 INFO mapreduce.Job:  map 90% reduce 29%
2026-02-17 20:12:09,947 INFO mapreduce.Job:  map 91% reduce 29%
2026-02-17 20:12:14,984 INFO mapreduce.Job:  map 92% reduce 29%
2026-02-17 20:12:15,993 INFO mapreduce.Job:  map 93% reduce 29%
2026-02-17 20:12:21,037 INFO mapreduce.Job:  map 94% reduce 29%
2026-02-17 20:12:22,046 INFO mapreduce.Job:  map 95% reduce 29%
2026-02-17 20:12:23,055 INFO mapreduce.Job:  map 97% reduce 29%
2026-02-17 20:12:27,104 INFO mapreduce.Job:  map 98% reduce 29%
2026-02-17 20:12:28,114 INFO mapreduce.Job:  map 100% reduce 31%
2026-02-17 20:12:34,160 INFO mapreduce.Job:  map 100% reduce 56%
2026-02-17 20:12:40,209 INFO mapreduce.Job:  map 100% reduce 69%
2026-02-17 20:12:46,252 INFO mapreduce.Job:  map 100% reduce 76%
2026-02-17 20:12:52,290 INFO mapreduce.Job:  map 100% reduce 83%
2026-02-17 20:12:58,335 INFO mapreduce.Job:  map 100% reduce 91%
2026-02-17 20:13:04,394 INFO mapreduce.Job:  map 100% reduce 98%
2026-02-17 20:13:06,411 INFO mapreduce.Job:  map 100% reduce 100%
2026-02-17 20:13:07,431 INFO mapreduce.Job: Job job_1770991083092_0064 completed successfully
2026-02-17 20:13:07,753 INFO mapreduce.Job: Counters: 55
        File System Counters
                FILE: Number of bytes read=76443063
                FILE: Number of bytes written=157916960
                FILE: Number of read operations=0
                FILE: Number of large read operations=0
                FILE: Number of write operations=0
                HDFS: Number of bytes read=2007768170
                HDFS: Number of bytes written=311
                HDFS: Number of read operations=50
                HDFS: Number of large read operations=0
                HDFS: Number of write operations=2
                HDFS: Number of bytes read erasure-coded=0
        Job Counters
                Killed map tasks=3
                Launched map tasks=18
                Launched reduce tasks=1
                Data-local map tasks=18
                Total time spent by all maps in occupied slots (ms)=1926698
                Total time spent by all reduces in occupied slots (ms)=332528
                Total time spent by all map tasks (ms)=963349
                Total time spent by all reduce tasks (ms)=166264
                Total vcore-milliseconds taken by all map tasks=963349
                Total vcore-milliseconds taken by all reduce tasks=166264
                Total megabyte-milliseconds taken by all map tasks=493234688
                Total megabyte-milliseconds taken by all reduce tasks=85127168
        Map-Reduce Framework
                Map input records=8493674
                Map output records=8493673
                Map output bytes=59455711
                Map output materialized bytes=76443147
                Input split bytes=1485
                Combine input records=0
                Combine output records=0
                Reduce input groups=26
                Reduce shuffle bytes=76443147
                Reduce input records=8493673
                Reduce output records=26
                Spilled Records=16987346
                Shuffled Maps =15
                Failed Shuffles=0
                Merged Map outputs=15
                GC time elapsed (ms)=9440
                CPU time spent (ms)=162130
                Physical memory (bytes) snapshot=4134522880
                Virtual memory (bytes) snapshot=34967822336
                Total committed heap usage (bytes)=2458251264
                Peak Map Physical memory (bytes)=282877952
                Peak Map Virtual memory (bytes)=2205982720
                Peak Reduce Physical memory (bytes)=275607552
                Peak Reduce Virtual memory (bytes)=2206027776
        Shuffle Errors
                BAD_ID=0
                CONNECTION=0
                IO_ERROR=0
                WRONG_LENGTH=0
                WRONG_MAP=0
                WRONG_REDUCE=0
        File Input Format Counters
                Bytes Read=2007766685
        File Output Format Counters
                Bytes Written=311
2026-02-17 20:13:07,755 INFO streaming.StreamJob: Output directory: /user/ssalhammad/project/m1/task4_full
ssalhammad@master-node:~$ hdfs dfs -cat /user/ssalhammad/project/m1/task4_full/part-00000 | head

2001    485958
2002    486831
2003    475998
2004    469443
2005    453788
2006    448198
2007    437108
2008    427216
2009    392866
2010    370564
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



TASK 5 SAMPLE LOGS FROM TERMINAL:
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
ssalhammad@master-node:~$ mapred streaming \
>   -files mapper_task5.py,reducer_sum.py \
>   -mapper "python3 mapper_task5.py" \
>   -reducer "python3 reducer_sum.py" \
>   -input /data/chicago_crimes_sample.csv \
>   -output /user/ssalhammad/project/m1/task5_sample

packageJobJar: [] [/opt/hadoop-3.4.1/share/hadoop/tools/lib/hadoop-streaming-3.4.1.jar] /tmp/streamjob10373479405919738689.jar tmpDir=null
2026-02-17 19:34:54,081 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at master-node/134.209.172.50:8032
2026-02-17 19:34:54,415 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at master-node/134.209.172.50:8032
2026-02-17 19:34:54,825 INFO mapreduce.JobResourceUploader: Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/ssalhammad/.staging/job_1770991083092_0060
2026-02-17 19:34:55,493 INFO mapred.FileInputFormat: Total input files to process : 1
2026-02-17 19:34:55,659 INFO mapreduce.JobSubmitter: number of splits:2
2026-02-17 19:34:56,024 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1770991083092_0060
2026-02-17 19:34:56,024 INFO mapreduce.JobSubmitter: Executing with tokens: []
2026-02-17 19:34:56,308 INFO conf.Configuration: resource-types.xml not found
2026-02-17 19:34:56,309 INFO resource.ResourceUtils: Unable to find 'resource-types.xml'.
2026-02-17 19:34:56,496 INFO impl.YarnClientImpl: Submitted application application_1770991083092_0060
2026-02-17 19:34:56,622 INFO mapreduce.Job: The url to track the job: http://master-node:8088/proxy/application_1770991083092_0060/
2026-02-17 19:34:56,637 INFO mapreduce.Job: Running job: job_1770991083092_0060
2026-02-17 19:35:27,513 INFO mapreduce.Job: Job job_1770991083092_0060 running in uber mode : false
2026-02-17 19:35:27,515 INFO mapreduce.Job:  map 0% reduce 0%
2026-02-17 19:35:53,234 INFO mapreduce.Job:  map 100% reduce 0%
2026-02-17 19:36:10,661 INFO mapreduce.Job:  map 100% reduce 100%
2026-02-17 19:36:11,704 INFO mapreduce.Job: Job job_1770991083092_0060 completed successfully
2026-02-17 19:36:11,995 INFO mapreduce.Job: Counters: 54
        File System Counters
                FILE: Number of bytes read=98723
                FILE: Number of bytes written=1140699
                FILE: Number of read operations=0
                FILE: Number of large read operations=0
                FILE: Number of write operations=0
                HDFS: Number of bytes read=2391502
                HDFS: Number of bytes written=21
                HDFS: Number of read operations=11
                HDFS: Number of large read operations=0
                HDFS: Number of write operations=2
                HDFS: Number of bytes read erasure-coded=0
        Job Counters
                Launched map tasks=2
                Launched reduce tasks=1
                Data-local map tasks=2
                Total time spent by all maps in occupied slots (ms)=88374
                Total time spent by all reduces in occupied slots (ms)=29460
                Total time spent by all map tasks (ms)=44187
                Total time spent by all reduce tasks (ms)=14730
                Total vcore-milliseconds taken by all map tasks=44187
                Total vcore-milliseconds taken by all reduce tasks=14730
                Total megabyte-milliseconds taken by all map tasks=22623744
                Total megabyte-milliseconds taken by all reduce tasks=7541760
        Map-Reduce Framework
                Map input records=10001
                Map output records=10000
                Map output bytes=78717
                Map output materialized bytes=98729
                Input split bytes=212
                Combine input records=0
                Combine output records=0
                Reduce input groups=2
                Reduce shuffle bytes=98729
                Reduce input records=10000
                Reduce output records=2
                Spilled Records=20000
                Shuffled Maps =2
                Failed Shuffles=0
                Merged Map outputs=2
                GC time elapsed (ms)=978
                CPU time spent (ms)=3820
                Physical memory (bytes) snapshot=661147648
                Virtual memory (bytes) snapshot=6561939456
                Total committed heap usage (bytes)=348049408
                Peak Map Physical memory (bytes)=257953792
                Peak Map Virtual memory (bytes)=2185900032
                Peak Reduce Physical memory (bytes)=146100224
                Peak Reduce Virtual memory (bytes)=2191020032
        Shuffle Errors
                BAD_ID=0
                CONNECTION=0
                IO_ERROR=0
                WRONG_LENGTH=0
                WRONG_MAP=0
                WRONG_REDUCE=0
        File Input Format Counters
                Bytes Read=2391290
        File Output Format Counters
                Bytes Written=21
2026-02-17 19:36:12,005 INFO streaming.StreamJob: Output directory: /user/ssalhammad/project/m1/task5_sample
ssalhammad@master-node:~$ 
ssalhammad@master-node:~$ hdfs dfs -cat /user/ssalhammad/project/m1/task5_sample/part-00000

false   8717
true    1283
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



TASK 5 FULL LOGS FROM TERMINAL:
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
ssalhammad@master-node:~$ mapred streaming \
>   -files mapper_task5.py,reducer_sum.py \
>   -mapper "python3 mapper_task5.py" \
er "pyt>   -reducer "python3 reducer_sum.py" \
>   -input /data/chicago_crimes.csv \
>   -output /user/ssalhammad/project/m1/task5_full
packageJobJar: [] [/opt/hadoop-3.4.1/share/hadoop/tools/lib/hadoop-streaming-3.4.1.jar] /tmp/streamjob10613274252047208707.jar tmpDir=null
2026-02-17 20:14:33,909 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at master-node/134.209.172.50:8032
2026-02-17 20:14:34,197 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at master-node/134.209.172.50:8032
2026-02-17 20:14:34,658 INFO mapreduce.JobResourceUploader: Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/ssalhammad/.staging/job_1770991083092_0065
2026-02-17 20:14:35,464 INFO mapred.FileInputFormat: Total input files to process : 1
2026-02-17 20:14:35,643 INFO mapreduce.JobSubmitter: number of splits:15
2026-02-17 20:14:36,048 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1770991083092_0065
2026-02-17 20:14:36,048 INFO mapreduce.JobSubmitter: Executing with tokens: []
2026-02-17 20:14:36,339 INFO conf.Configuration: resource-types.xml not found
2026-02-17 20:14:36,340 INFO resource.ResourceUtils: Unable to find 'resource-types.xml'.
2026-02-17 20:14:36,457 INFO impl.YarnClientImpl: Submitted application application_1770991083092_0065
2026-02-17 20:14:36,515 INFO mapreduce.Job: The url to track the job: http://master-node:8088/proxy/application_1770991083092_0065/
2026-02-17 20:14:36,518 INFO mapreduce.Job: Running job: job_1770991083092_0065
2026-02-17 20:15:08,788 INFO mapreduce.Job: Job job_1770991083092_0065 running in uber mode : false
2026-02-17 20:15:08,791 INFO mapreduce.Job:  map 0% reduce 0%
2026-02-17 20:15:49,382 INFO mapreduce.Job:  map 4% reduce 0%
2026-02-17 20:15:50,407 INFO mapreduce.Job:  map 5% reduce 0%
2026-02-17 20:15:51,432 INFO mapreduce.Job:  map 7% reduce 0%
2026-02-17 20:15:55,535 INFO mapreduce.Job:  map 10% reduce 0%
2026-02-17 20:15:56,551 INFO mapreduce.Job:  map 11% reduce 0%
2026-02-17 20:15:57,576 INFO mapreduce.Job:  map 13% reduce 0%
2026-02-17 20:16:01,711 INFO mapreduce.Job:  map 17% reduce 0%
2026-02-17 20:16:02,726 INFO mapreduce.Job:  map 20% reduce 0%
2026-02-17 20:16:03,761 INFO mapreduce.Job:  map 23% reduce 0%
2026-02-17 20:16:08,945 INFO mapreduce.Job:  map 25% reduce 0%
2026-02-17 20:16:15,140 INFO mapreduce.Job:  map 33% reduce 0%
2026-02-17 20:16:38,676 INFO mapreduce.Job:  map 37% reduce 0%
2026-02-17 20:16:44,832 INFO mapreduce.Job:  map 39% reduce 0%
2026-02-17 20:16:50,952 INFO mapreduce.Job:  map 42% reduce 0%
2026-02-17 20:16:54,003 INFO mapreduce.Job:  map 48% reduce 0%
2026-02-17 20:16:55,043 INFO mapreduce.Job:  map 49% reduce 0%
2026-02-17 20:17:00,162 INFO mapreduce.Job:  map 51% reduce 0%
2026-02-17 20:17:01,197 INFO mapreduce.Job:  map 53% reduce 0%
2026-02-17 20:17:06,329 INFO mapreduce.Job:  map 54% reduce 0%
2026-02-17 20:17:07,352 INFO mapreduce.Job:  map 56% reduce 0%
2026-02-17 20:17:12,466 INFO mapreduce.Job:  map 57% reduce 0%
2026-02-17 20:17:13,499 INFO mapreduce.Job:  map 59% reduce 0%
2026-02-17 20:17:17,600 INFO mapreduce.Job:  map 67% reduce 0%
2026-02-17 20:17:31,832 INFO mapreduce.Job:  map 70% reduce 22%
2026-02-17 20:17:37,924 INFO mapreduce.Job:  map 73% reduce 22%
2026-02-17 20:17:44,030 INFO mapreduce.Job:  map 73% reduce 24%
2026-02-17 20:17:57,268 INFO mapreduce.Job:  map 76% reduce 24%
2026-02-17 20:18:03,372 INFO mapreduce.Job:  map 78% reduce 24%
2026-02-17 20:18:04,386 INFO mapreduce.Job:  map 83% reduce 24%
2026-02-17 20:18:08,440 INFO mapreduce.Job:  map 86% reduce 24%
2026-02-17 20:18:09,449 INFO mapreduce.Job:  map 88% reduce 24%
2026-02-17 20:18:10,467 INFO mapreduce.Job:  map 89% reduce 24%
2026-02-17 20:18:14,523 INFO mapreduce.Job:  map 89% reduce 27%
2026-02-17 20:18:15,536 INFO mapreduce.Job:  map 90% reduce 27%
2026-02-17 20:18:16,553 INFO mapreduce.Job:  map 92% reduce 27%
2026-02-17 20:18:21,650 INFO mapreduce.Job:  map 100% reduce 27%
2026-02-17 20:18:26,714 INFO mapreduce.Job:  map 100% reduce 50%
2026-02-17 20:18:32,819 INFO mapreduce.Job:  map 100% reduce 67%
2026-02-17 20:18:57,129 INFO mapreduce.Job:  map 100% reduce 92%
2026-02-17 20:19:03,216 INFO mapreduce.Job:  map 100% reduce 100%
2026-02-17 20:19:05,274 INFO mapreduce.Job: Job job_1770991083092_0065 completed successfully
2026-02-17 20:19:05,628 INFO mapreduce.Job: Counters: 55
        File System Counters
                FILE: Number of bytes read=82800381
                FILE: Number of bytes written=170631612
                FILE: Number of read operations=0
                FILE: Number of large read operations=0
                FILE: Number of write operations=0
                HDFS: Number of bytes read=2007768170
                HDFS: Number of bytes written=27
                HDFS: Number of read operations=50
                HDFS: Number of large read operations=0
                HDFS: Number of write operations=2
                HDFS: Number of bytes read erasure-coded=0
        Job Counters
                Killed map tasks=2
                Launched map tasks=16
                Launched reduce tasks=1
                Data-local map tasks=16
                Total time spent by all maps in occupied slots (ms)=1681218
                Total time spent by all reduces in occupied slots (ms)=257256
                Total time spent by all map tasks (ms)=840609
                Total time spent by all reduce tasks (ms)=128628
                Total vcore-milliseconds taken by all map tasks=840609
                Total vcore-milliseconds taken by all reduce tasks=128628
                Total megabyte-milliseconds taken by all map tasks=430391808
                Total megabyte-milliseconds taken by all reduce tasks=65857536
        Map-Reduce Framework
                Map input records=8493674
                Map output records=8493673
                Map output bytes=65813029
                Map output materialized bytes=82800465
                Input split bytes=1485
                Combine input records=0
                Combine output records=0
                Reduce input groups=2
                Reduce shuffle bytes=82800465
                Reduce input records=8493673
                Reduce output records=2
                Spilled Records=16987346
                Shuffled Maps =15
                Failed Shuffles=0
                Merged Map outputs=15
                GC time elapsed (ms)=8726
                CPU time spent (ms)=153590
                Physical memory (bytes) snapshot=4100706304
                Virtual memory (bytes) snapshot=34971422720
                Total committed heap usage (bytes)=2469249024
                Peak Map Physical memory (bytes)=279887872
                Peak Map Virtual memory (bytes)=2205409280
                Peak Reduce Physical memory (bytes)=285421568
                Peak Reduce Virtual memory (bytes)=2208112640
        Shuffle Errors
                BAD_ID=0
                CONNECTION=0
                IO_ERROR=0
                WRONG_LENGTH=0
                WRONG_MAP=0
                WRONG_REDUCE=0
        File Input Format Counters
                Bytes Read=2007766685
        File Output Format Counters
                Bytes Written=27
2026-02-17 20:19:05,634 INFO streaming.StreamJob: Output directory: /user/ssalhammad/project/m1/task5_full
ssalhammad@master-node:~$ hdfs dfs -cat /user/ssalhammad/project/m1/task5_full/part-00000

false   6357318
true    2136355
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


