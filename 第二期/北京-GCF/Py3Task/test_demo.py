# -*- coding:utf-8 -*-
import pytest
import time
from selenium import webdriver
__author__ = '米饭'

"""
    任务1：实现pytest-selenium输出HTML格式报告 ==》需要安装第三方插件pytest-html
    任务2：使用pytest -h了解pytest各命令行参数的含义，总结
    pytest-selenium使用
    1.安装pytest
    2.安装selenium最新版本
    3.安装pytest-selenium
    4.运行pytest：assert报错：打印出错结果，清晰的知道该测试为什么失败。
    5.打印driver日志
"""


# 初始化selenium通用配置
@pytest.fixture
def selenium(driver):
    driver.imlicitly_wait(10)
    driver.maximize_window()

    return driver


def test_baidu_search(driver):
    # 打开百度首页
    driver.get("http://www.baidu.com")

    # 定位输入框
    kw = driver.find_element_by_id("kw")
    su = driver.find_element_by_id("su")


    # 输入待搜索关键字
    kw.send_keys("开源测试1")
    su.click()

    # 强势等待
    time.sleep(5)

    # 断言pass,正常断言，子表达式最好是一个函数签名，这样就可以得到该函数的计算结果
    title = driver.title
    print(title)
    assert title == "开源测试_百度搜索", "pass"
    # 断言fail，异常断言，使用pytest.raise
    # assert title != "开源测试_百度搜索", "fail"
    with pytest.raises(False):
        title != "开源测试_百度搜索"