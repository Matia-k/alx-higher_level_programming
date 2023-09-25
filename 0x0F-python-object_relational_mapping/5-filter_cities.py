#!/usr/bin/python3
"""script that takes in the name of a state as an argument and lists all
cities of that state, using the given database.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
                FROM `cities` \
                INNER JOIN `states` ON cities.state_id=states.id")
    _cities = cur.fetchall()
    for city in _cities:
        if city[2] == sys.argv[4]:
            print(city[1], end=', ')
    print()
