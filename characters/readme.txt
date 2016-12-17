characters:
1. 作者前五年发表的论文数
2. 作者前五年的被引用次数
3. 作者前五年论文的平均被引用次数
4. 作者前五年合作者数量
5. 作者前五年合作者的平均被引用次数


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
根据author_gt10.csv(获取作者以及学生生涯起始年份), doi_year.csv(获取论文发表年份), 
aps_full_info_citation.csv(获取引用关系)以及author_paper_5year.csv(获取作者前5年发表的论文doi),
生成author_citation_5year_dict(作者前五年被引用量)并将其存入author_citation_count.csv中。

3.
author_avg_citation_count.csv
author_avg_citation_count.py
根据author_citation_count.csv(作者前五年总被引用次数), author_paper_num.csv(获取作者论文数)，
生成author_avg_citation_dict(作者前五年每篇论文平均被引用次数)存入author_avg_citation_count.csv。

4.
author_coauthor_count.csv
author_coauthor_count.py
根据author_paper_5year.csv中作者对应的发表的论文到metadata中找到合作者，
将作者合作者数量对应的关系存入author_coauthor_count_dict中，最后写入author_coauthor_count.csv中。

5.
coauthor_avg_citation_num.csv
coauthor_avg_citation_num.py
主要过程写入了../aps/CoauthorAvgCitation.py中，根据每个作者单独求解，
即多少个作者就运行多少次程序求解


