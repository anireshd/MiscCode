import pyodbc
import sys

conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};Server=10.64.116.16;Database=Fandango;Uid=adevchoudhury;Pwd=N0te$ma1l;')

stubsnum = str(sys.argv[1])



SQL = "select t.email_nm from tbltransaction t (nolock) "
SQL = SQL + "inner join tbltransactioncommitted tc (nolock) "
SQL = SQL + "on t.transaction_guid = tc.transaction_guid "
SQL = SQL + "where tc.loyalty_cd = '"+stubsnum+"' "
SQL = SQL + "union "
SQL = SQL + "select c.email_nm from tblcustomer c (nolock) "
SQL = SQL + "join tblcustomermembershipcard cm (nolock) on c.customer_guid = cm.customer_guid "
SQL = SQL + "where cm.loyalty_cd = '"+ stubsnum+"'"

print(SQL)

dest_dir = "\\\\colfsrp01\DataExports\\DB_Requests\\AMC Stubs\\"

file_name = "AMC_"+ stubsnum+".txt"

print(file_name)
f = open(dest_dir+file_name,'w')

cur = conn.cursor()
cur.execute(SQL)

results = cur.fetchone()
while results:
    #print(str(results[0]))
    f.write(str(results[0])+'\n')
    results = cur.fetchone()

f.close()
cur.close()
conn.close()
print("Results here:"+ dest_dir+file_name)