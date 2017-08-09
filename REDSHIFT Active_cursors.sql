select u.text,u.starttime,u.endtime,c.userid,c.name,c.row_count,c.byte_count,c.fetched_rows 
from STV_ACTIVE_CURSORS c
inner join 
stl_utilitytext u
on c.pid = u.pid