select count(*) from (select docid, sum(count) as cnt from Frequency group by docid having cnt>300);
