1.1
paper_all_author_all.csv
paper_all_author_all.py
根据APS原始的metadata中全部json数据，提取出论文doi和作者对应的信息，存入csv中，
无作者信息的第二列为空字符串，其中名字中含有\n的未进行处理。

1.4
paper_all_author_all_format1.csv
paper_all_author_all_format1.py
根据paper_all_author_all.csv生成论文doi，作者列表（字符串形式）对应的csv文件，
其中作者名字中含有的"\n"全部替换成了空格

1.3
paper_all_author_all_format2.csv
paper_all_author_all_format2.py
根据APS原始数据集的metadata中全部json数据，提取出论文doi和作者对于那个的信息，
每行一名作者，每个doi有一行至多行，无作者信息的第二列为空字符串，已处理名字中的"\n"

1.2
paper_all_author_all_format3.csv
paper_all_author_all_format3.py
根据paper_all_author_all.csv生成论文doi，作者对应的csv文件，每个作者占一列，
已处理作者名字中的"\n"

2.
author_all_paper_li_all.csv
author_all_paper_li_all.py
根据paper_all_author_all_format3.csv生成作者的与其发表的全部论文doi列表对应的文件，
两列，第一列为作者名，第二列为doi列表（字符串形式）

3.
author_all_year_list.csv
author_all_year_list.py
根据author_all_paper_li_all.csv生成的文件，包含两列：作者名 和 作者发表论文的年份列表，
遗憾的是，由于原始数据集本身的缺陷，部分人名没有区分开

4.
author_start_end_year.csv
author_start_end_year.py
根据3中生成的author_all_year_list.csv找出作者发表的第一篇和左后一篇论文的时间，
生成 作者名， 起始年份，结束年份 三列格式的csv文件

5.
author_gt10.csv
author_gt10.py
根据author_start_end_year.csv选取第一篇论文发表时间在1993年以后（包含1993年）且
学术生涯时间至少是10年的学者名单，该文件共有三列，作者名，学术生涯起始年份，学术生涯结束年份

6.
author_gt10_paper_li.csv
author_gt10_paper_li.py
根据author_gt10.csv和author_all_paper_li_all.csv生成学术生涯大于10年，
且起始生涯在1993年之后（包含1993年）的学者的学者姓名和论文doi列表对应的csv文件

7.
doi_year.csv
存储doi与year对应的信息, 其中的doi只包含出现在原始citation文件中
且信息完整(包含作者信息和发表年份信息)的论文
aps_full_info_citation.csv
aps_full_info_citation.py
根据aps原始数据集中的原始引用数据, 筛选掉引用和被引用论文doi中信息不全的数据行
(作者信息和发表年份信息)

