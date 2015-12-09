select sum(a.value*b.value) from a inner join b on a.col_num=b.row_num where a.row_num=2 and b.col_num=3;
