import pypyodbc
import csv
connection = pypyodbc.connect('Driver={SQL Server};Server=alphasql01;Database=Fandango;uid=scream;pwd=scream')
								
cursor = connection.cursor() 
SQLCommand = ("SELECT * FROM etl.tblConfig WHERE run=1 AND filename IN ('chain','tblAffiliate')")
                
cursor.execute(SQLCommand) 
for row in cursor.fetchall():
	print (row[4]+row[5]+"--"+row[11])
	cursor.execute(row[11]) 
	for sqlcmd in cursor.fetchall():
		with open (row[4]+row[5],'a') as csvfile:  
			csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
			csvwriter.writerow([str(sqlcmd)])				

connection.close()





