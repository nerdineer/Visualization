#!/usr/bin/python
import MySQLdb as mariadb
import json
mariadb_connection = mariadb.connect(host='localhost', port=3306, user='root', passwd='root', db='twitch_chat') 
cursor = mariadb_connection.cursor()

cursor.execute("SELECT * FROM channel")
channel = {}
for i in cursor:
    if int(i[0]) not in channel:
        channel[int(i[0])] = i[1]
#print channel

cursor.execute("SELECT * FROM user")
user = {}
for i in cursor:
    if int(i[0]) not in user:
        user[int(i[0])] = i[1]
#print user

cursor.execute("select * from message where timestamp between  1492214400 and 1492300800")
message = []
for i in cursor:
    try: 
        message.append({'id': int(i[0]), 'channelid': int(i[1]), 'userid': int(i[2]), 'message': i[3].encode('utf-8').strip(), 'timestamp': int(i[4])})
    except:
        #ill formatted messages.
        continue 
#print message

mariadb_connection.close()

real_users = {}
real_channels = {}
for j in message:
    if j['userid'] in user:
        real_users[j['userid']] = user[j['userid']]
    if j['channelid'] in channel:
        real_channels[j['channelid']] = channel[j['channelid']]
        
#print "New vs. Old User count: ", len(real_users), len(user)
#print "New vs. Old Channel count: ", len(real_channels), len(channel)
json_dump = [real_channels, real_users, message]
print json.dumps(json_dump)