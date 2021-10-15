import os

import mysql.connector

def db_connect():
    cnx = mysql.connector.connect(
        host=os.getenv('MYSQL_HOST'),
        user=os.getenv('MYSQL_USER'),
        port=os.getenv('MYSQL_PORT'),
        passwd=os.getenv('MYSQL_PW'),
        database=os.getenv('MYSQL_DATABASE')
    )
    cnx.set_charset_collation('utf8mb4', 'utf8mb4_general_ci')
    return cnx

def courses_by_startdate(startdate, course_type_refs):
    cnx = db_connect()
    cur = cnx.cursor()
    join_str = "','"

    query = (
        """
        SELECT count(b.id) num_bookings
        , c.start_date
        , GROUP_CONCAT(DISTINCT(t.course_ref)) as course_ref 
        , d.destination_ref
        , d.name 

        FROM booking_booking b
        LEFT JOIN booking_groupbooking gb on b.group_booking_id = gb.id
        LEFT JOIN booking_booktype bt on gb.book_type_id = bt.id
        LEFT JOIN booking_coursemarket cm on bt.course_market_id = cm.id
        LEFT JOIN booking_course c on cm.course_id = c.id
        LEFT JOIN booking_coursetype t on c.type_id = t.id
        LEFT JOIN booking_destination d on c.destination_id = d.id 
        WHERE start_date = '{}' 
        AND t.course_ref in ('{}')
        GROUP BY c.start_date, d.destination_ref
        HAVING count(b.id) > 0
        
        """.format(str(startdate), "','".join(course_type_refs))
    )

    cur.execute(query)
    res = cur.fetchall()
    cur.close()
    cnx.close()
    return res