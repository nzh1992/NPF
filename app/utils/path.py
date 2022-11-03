# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2022/11/4
Last Modified: 2022/11/4
Description: 获取所有路径相关信息
"""
import os


class PathUtil:

    @staticmethod
    def get_project_root_path():
        """
        获取项目根目录的绝对路径
        :return: path.
        """
        return os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))