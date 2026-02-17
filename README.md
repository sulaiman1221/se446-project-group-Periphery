# se446-project-group-Periphery

Student names/IDs:  
- Suliman Alhammad 230103
- Saleh Alkhattaf
- Abdulrahman alghannam 


**Dataset (HDFS):**
- Sample: `/data/chicago_crimes_sample.csv`
- Full: `/data/chicago_crimes.csv`

This milestone implements **4 MapReduce jobs** using **Hadoop Streaming**:
1. Crime type distribution
2. Location hotspots
3. Crime trends by year
4. Arrest analysis

All jobs use a task-specific **mapper** and a shared **sum reducer** (`reducer_sum.py`).

All tasks were tested on the sample dataset before running on the full dataset.
Output directories are stored under: /user/ssalhammad/project/m1/

---

Task 2 — Crime Type Distribution
Sample Run

Command:
hdfs dfs -rm -r /user/ssalhammad/project/m1/task2_sample 2>/dev/null

mapred streaming \
  -files mapper_task2.py,reducer_sum.py \
  -mapper "python3 mapper_task2.py" \
  -reducer "python3 reducer_sum.py" \
  -input /data/chicago_crimes_sample.csv \
  -output /user/ssalhammad/project/m1/task2_sample


Key Counters

Map input records: 10001

Map output records: 10000

Reduce input groups: 29

Reduce output records: 29

Output (head)

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


Interpretation: Battery is the most frequent crime type in the sample dataset, followed by criminal damage and assault.

Full Run

Command:
hdfs dfs -rm -r /user/ssalhammad/project/m1/task2_full 2>/dev/null

mapred streaming \
  -files mapper_task2.py,reducer_sum.py \
  -mapper "python3 mapper_task2.py" \
  -reducer "python3 reducer_sum.py" \
  -input /data/chicago_crimes.csv \
  -output /user/ssalhammad/project/m1/task2_full


Key Counters

Map input records: 8,493,674

Reduce input groups: 34

Reduce output records: 34

Output (head)

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


Interpretation: Battery is the most frequent crime type in the full dataset (1,547,201), followed by criminal damage (965,727) and assault (570,382).
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Task 3 — Location Hotspots
Sample Run

Command:
hdfs dfs -rm -r /user/ssalhammad/project/m1/task3_sample 2>/dev/null

mapred streaming \
  -files mapper_task3.py,reducer_sum.py \
  -mapper "python3 mapper_task3.py" \
  -reducer "python3 reducer_sum.py" \
  -input /data/chicago_crimes_sample.csv \
  -output /user/ssalhammad/project/m1/task3_sample


Key Counters

Map input records: 10001

Map output records: 9907

Reduce input groups: 110

Reduce output records: 110

Output (head)

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


Interpretation: The sample shows crimes distributed across many location types (110 unique locations), indicating crimes occur across diverse environments.

Full Run

Command:
hdfs dfs -rm -r /user/ssalhammad/project/m1/task3_full 2>/dev/null

mapred streaming \
  -files mapper_task3.py,reducer_sum.py \
  -mapper "python3 mapper_task3.py" \
  -reducer "python3 reducer_sum.py" \
  -input /data/chicago_crimes.csv \
  -output /user/ssalhammad/project/m1/task3_full


Key Counters

Map input records: 8,493,674

Reduce input groups: 218

Reduce output records: 218

Output (head)

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


Interpretation: Crimes occur across a wide variety of locations (218 distinct types), with hotspots including abandoned buildings and major transportation infrastructure areas.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Task 4 — Crime Trends by Year
Sample Run

Command:
hdfs dfs -rm -r /user/ssalhammad/project/m1/task4_sample 2>/dev/null

mapred streaming \
  -files mapper_task4.py,reducer_sum.py \
  -mapper "python3 mapper_task4.py" \
  -reducer "python3 reducer_sum.py" \
  -input /data/chicago_crimes_sample.csv \
  -output /user/ssalhammad/project/m1/task4_sample


Key Counters

Map input records: 10001

Map output records: 10000

Reduce input groups: 24

Reduce output records: 24

Output (head)

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


Interpretation: The sample dataset contains incidents across multiple years with varying yearly counts.

Full Run

Command:
hdfs dfs -rm -r /user/ssalhammad/project/m1/task4_full 2>/dev/null

mapred streaming \
  -files mapper_task4.py,reducer_sum.py \
  -mapper "python3 mapper_task4.py" \
  -reducer "python3 reducer_sum.py" \
  -input /data/chicago_crimes.csv \
  -output /user/ssalhammad/project/m1/task4_full


Key Counters

Map input records: 8,493,674

Reduce input groups: 26

Reduce output records: 26

Output (head)

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


Interpretation: Crime volume shows a gradual decline over time (e.g., ~486k in 2001–2002 down to ~371k in 2010), indicating a long-term reduction in reported incidents.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Task 5 — Arrest Analysis
Sample Run

Command:
hdfs dfs -rm -r /user/ssalhammad/project/m1/task5_sample 2>/dev/null

mapred streaming \
  -files mapper_task5.py,reducer_sum.py \
  -mapper "python3 mapper_task5.py" \
  -reducer "python3 reducer_sum.py" \
  -input /data/chicago_crimes_sample.csv \
  -output /user/ssalhammad/project/m1/task5_sample


Key Counters

Map input records: 10001

Map output records: 10000

Reduce input groups: 2

Reduce output records: 2

Output

false   8717
true    1283


Interpretation: Most crimes in the sample did not result in an arrest, indicating a low arrest rate.

Full Run

Command:
hdfs dfs -rm -r /user/ssalhammad/project/m1/task5_full 2>/dev/null

mapred streaming \
  -files mapper_task5.py,reducer_sum.py \
  -mapper "python3 mapper_task5.py" \
  -reducer "python3 reducer_sum.py" \
  -input /data/chicago_crimes.csv \
  -output /user/ssalhammad/project/m1/task5_full


Key Counters

Map input records: 8,493,674

Reduce input groups: 2

Reduce output records: 2

Output

false   6357318
true    2136355


Interpretation: In the full dataset, arrests occur in about 25% of cases (2,136,355 out of 8,493,673 valid records), while ~75% do not result in arrest.





