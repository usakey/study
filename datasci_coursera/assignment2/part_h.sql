select sum(A.count*B.count) from Frequency A inner join Frequency B on A.term=B.term where A.docid='10080_txt_crude' and b.docid='17035_txt_earn';
