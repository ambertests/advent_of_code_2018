import requests, sys
from datetime import datetime
from collections import OrderedDict

# Grab the session cookie from the https://adventofcode.com/2018 site:
# right-click, Inspect, Application tab, Cookies, session.
# Call from command line with "python3 aoc_day01.py <session>"
session = sys.argv[1]

url = "https://adventofcode.com/2018/day/4/input"
headers = {
	'cookie': "session=" + session
	}

input = requests.request("GET", url, headers=headers)
# cut off the last value because it is an empty string
record_list = input.text.split('\n')[:-1]


records = [(r[1:17],r[19:]) for r in record_list]
ordered = OrderedDict(sorted(records, key=lambda t: t[0]))
guards = {}
current_guard = ''
asleep = -1
for record in ordered:
    activity = ordered.get(record)
    dt = datetime.strptime(record, '%Y-%m-%d %H:%M')
    if activity.startswith('Guard'):
        guard_id = activity[6:activity.index(' begins')]
        if guard_id != current_guard:
            current_guard = guard_id
            asleep = -1
        if guard_id not in guards:
            guards[guard_id] = [0 for i in range(60)]
    if activity == 'falls asleep':
        asleep = dt.minute
    if activity == 'wakes up':
        for i in range(asleep, dt.minute):
            guards[current_guard][i] = guards[current_guard][i] + 1

max_total_sleep = 0
sleepiest_guard = ''
max_sleep_in_minute = 0
guard_with_max_sleep_minute = ''
for guard in guards:
    minutes = guards[guard]
    total_sleep = sum(minutes)
    if total_sleep > max_total_sleep:
        sleepiest_guard = guard
        max_total_sleep = total_sleep

    max_minute = max(minutes)    
    if max_minute > max_sleep_in_minute:
        max_sleep_in_minute = max_minute
        guard_with_max_sleep_minute = guard
    

print('Sleepiest guard is', sleepiest_guard)
sleep_minutes = guards[sleepiest_guard]
sleepiest_minute = sleep_minutes.index(max(sleep_minutes))
print('Sleepiest minute is', sleepiest_minute)

print('Solution 4.1:', int(sleepiest_guard[1:])*sleepiest_minute)
max_sleep_minute = guards[guard_with_max_sleep_minute].index(max_sleep_in_minute)
print('Max sleep in minute is', max_sleep_in_minute, 'by', guard_with_max_sleep_minute, 'at minute', max_sleep_minute)
print('Solution 4.2:', max_sleep_minute*int(guard_with_max_sleep_minute[1:]))

    
        
        
            

