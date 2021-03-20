# !usr/bin/env python
# -*- coding: GBK -*-
"""
@author: T5610
@software: PyCharm
@file: Delete_NameSpace.py
@time: 2021/3/20 14:20
"""
import sys

reload(sys)
sys.setdefaultencoding("GBK")

import maya.cmds as cmds
cmds.sphere(r=10)