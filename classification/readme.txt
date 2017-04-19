1.
total_citation_by_year.csv
total_citation_by_year.py
根据aps_full_info_citation.csv生成每年产生的总引用数量存入total_citation_by_year.csv中
每行包括两列, 第一列年份, 第二列总引用数

2.
year_citation_num.csv
year_citation_num.py
根据原始引用文件计算每年产生的引用量存入csv中

3.
year_author_paper.py
根据../result/AuthorCitationNetwork中的年份文件生成每年的作者及其对应的论文的文件
存入到../result/AuthorCitationByYear文件夹下

4.
year_author_citation.py
根据year_author_paper.py产生的年份作者csv文件, 统计按照年份这些作者在当年的被引用次数, 
并存入../result/AuthorCitationByYear/下的按年份命名的csv文件中

5.
rank_author.py
根据论文引用百分比, 把所有学者按照百分比大小排序
