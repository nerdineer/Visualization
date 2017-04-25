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

cursor.execute("SELECT * FROM message")
message = []
for i in cursor:
    try: 
        message.append({'id': int(i[0]), 'channelid': int(i[1]), 'userid': int(i[2]), 'message': i[3].encode('utf-8').strip(), 'timestamp': int(i[4])})
    except:
        #ill formatted messages.
        continue 
#print message

mariadb_connection.close()

json_dump = [channel, user, message]
print json.dumps(json_dump)