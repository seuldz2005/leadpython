import mysql.connector
import schedule
import time

def do():
    print("Updating... ", end="")
    conn = mysql.connector.connect(host="localhost", port="3306",user="root",password="",database="thesieutoc")
    cursor=conn.cursor()
    slectquery="select name, menhgia from napthe_log WHERE note ='thanh cong' ORDER BY name"
    cursor.execute(slectquery)

    records=cursor.fetchall()
    d = dict()

    for row in records:
        values = list(row)
        d[values[0]] = d.get(values[0], 0) + int(values[1])

    cursor.close()
    conn.close()

    # lay tu ưeb

    conn = mysql.connector.connect(host="localhost", port="3306",user="root",password="",database="authme")
    cursor=conn.cursor()
    
    slectquery="select user_id, amount from topup_history WHERE status=1"
    cursor.execute(slectquery)
    records=cursor.fetchall()

    for row in records:
        values = list(row)
        user_id = row[0]

        slectquery2 = "select realname from authme WHERE id='" + str(user_id) + "'"
        cursor.execute(slectquery2)

        r = cursor.fetchall()

        if len(list(r)):
            name = list(r)[0][0]
            d[name] = d.get(name, 0) + int(values[1])

    cursor.close()
    conn.close()

    d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

    leaderboard=mysql.connector.connect(host="localhost", port="3306",user="root",password="",database="leaderboard_napthe")
    mycursor=leaderboard.cursor()
    mycursor.execute("DELETE FROM top;")

    i = 0

    for k, v in d.items():
        mycursor.execute("INSERT INTO top (name, money) VALUES (%s, %s)", (k, v))
        i = i + 1
        if i == 10:
            break

    leaderboard.commit()
    mycursor.close()
    leaderboard.close()

    print("OK")


do()

schedule.every().hour.do(do)
while True:
    schedule.run_pending()
    time.sleep(1)