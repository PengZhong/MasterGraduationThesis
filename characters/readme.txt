characters:
1. 作者前五年发表的论文数
2. 作者前五年的被引用次数


1.
author_paper_num.csv
author_paper_num.py
特征值1，统计学者前5年发表的论文数目

2.1
author_paper_5year.csv
author_paper_5year.py
生成选出的author_gt10.csv中的作者在学术生涯前5年发表的论文的列表，
存入(author, doi list)对应的二列csv文件中

2.2
author_citation_count.csv
author_citation_count.py
根据author_gt10.csv(获取作者以及学生生涯起始年份), doi_year.csv(获取论文发表年份), aps_full_info_citation.csv(获取引用关系)以及author_paper_5year.csv(获取作者前5年发表的论文doi),
生成author_citation_5year_dict(作者前五年被引用量)并将其存入author_citation_count.csv中。



