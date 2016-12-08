# -*- coding: utf-8 -*-
import os


# APS-DATA metadata absolute path
base_path_posix = r"/media/zhongpeng/Datas/APS-DATA/aps-dataset-metadata-2013"
base_path_nt = r"E:/APS-DATA/aps-dataset-metadata-2013"


def get_base_path():
    if os.name == "posix":
        return base_path_posix
    elif os.name == "nt":
        return base_path_nt
    else:
        print "base_path init error, exit"
        exit(0)
