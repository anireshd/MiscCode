select usesysid, usename, groname from pg_user u 
left join pg_group g on ','||array_to_string(grolist,',')||','
  like '%,'||cast(usesysid as varchar(10))||',%';