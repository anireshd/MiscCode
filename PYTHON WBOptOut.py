import pyodbc
import sys

conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};Server=10.64.116.16;Database=Fandango;Uid=admin;Pwd=gr34g00s3;')

email_tx = str(sys.argv[1])

email_list = email_tx.split(",")



SQL = ''

for i in range(len(email_list)):
    print(email_list[i]+"\n")

    SQL = "select subscriber_guid from dbo.tblSubscriber where Email_nm  = '"+ email_list[i]+"'"

    print(SQL+"\n")

    cur = conn.cursor()

    cur.execute(SQL)

    res = cur.fetchone()

    if res is None:
        print('Email not found')

        SQL = "insert into dbo.tblSubscriber (subscriber_guid,email_nm,create_dm) values (newid(),'"+email_list[i]+"',getutcdate())"

        cur.execute(SQL)

        conn.commit()

        SQL = "select subscriber_guid from dbo.tblSubscriber where Email_nm  = '"+ email_list[i]+"'"

        cur.execute(SQL)

        res = cur.fetchone()

    subscriber_guid = str(res[0])


    SQL = "insert into dbo.tblSubscription (subscriberlist_id,subscriber_guid,create_dm) values (16,'"+subscriber_guid+"',getutcdate())"
    print(SQL+"\n")

    try:
        cur.execute(SQL)
        conn.commit()
    except () as e:
        print(e)
        conn.rollback()

    cur.close()

cur = conn.cursor()

cur.execute("EXEC ETL.WB_OptOut_Update")

conn.commit()

conn.close()