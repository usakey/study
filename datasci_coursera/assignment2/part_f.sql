select count(*) from 
(select distinct docid from Frequency where term='transactions'
intersect
select distinct docid from Frequency where term='world');
