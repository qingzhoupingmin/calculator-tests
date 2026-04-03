import pytest
import sys
import os
import yaml
from pathlib import Path

# 添加项目路径
def setup_module():
    """添加项目路径"""
    tests_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(tests_dir)
    if parent_dir not in sys.path:
        sys.path.insert(0, parent_dir)

# 自动执行setup_module，确保路径设置在测试开始前完成
@pytest.fixture(scope="session", autouse=True)
def setup_path():
    """自动配置路径"""
    setup_module()
@pytest.fixture(scope="session")
def test_data():
    # 从取测试数据文件中加载数据
    yaml_file = Path(__file__).parent / "fixtures" / "test_data.yaml"
    with open(yaml_file, "r" , encoding="utf-8") as f:
        return yaml.safe_load(f)

@pytest.fixture(scope="function")
def calculator():
    # 创建一个计算器实例，供测试函数使用
    from calculator.logic import Logic
    return Logic(5,3)

@pytest.fixture(scope="function")
def make_calculator():
    # 定义一个工厂函数，用于创建计算器实例
    from calculator.logic import Logic
    def _make(a,b):
        return Logic(a,b)
    return _make    

@pytest.fixture(scope="function")
def addition_data(test_data):
    # 从测试数据中提取加法测试数据
    return test_data["addition"]

@pytest.fixture(scope="function")
def subtraction_data(test_data):
    # 从测试数据中提取减法测试数据
    return test_data["subtraction"]

@pytest.fixture(scope="function")
def multiplication_data(test_data):
    # 从测试数据中提取乘法测试数据
    return test_data["multiplication"]

@pytest.fixture(scope="function")
def division_data(test_data):
    # 从测试数据中提取除法测试数据
    return test_data["division"]

@pytest.fixture(scope="function")
def exception_data(test_data):
    # 从测试数据中提取异常测试数据
    return test_data["exceptions"]
