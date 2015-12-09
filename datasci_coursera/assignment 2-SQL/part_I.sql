create view ks as
SELECT * FROM frequency
UNION
SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count;


select max(sim) 
from (select A.docid, B.docid, sum(A.count*B.count) as sim 
	from ks A inner join ks B on A.term=B.term 
	where A.docid='q' group by A.docid, B.docid);
