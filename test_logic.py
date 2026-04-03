import pytest

def test_addition(make_calculator, addition_data):
    # 测试加法功能
    print("测试加法")
    for case in addition_data:
        a , b , expected = case["a"], case["b"], case["expected"]
        calc = make_calculator(case["a"], case["b"])
        result = calc.add()
        print(f"测试数据: {a} + {b} = {expected}, 计算结果: {result}")
        assert result == case["expected"]
def test_subtraction(make_calculator, subtraction_data):
    # 测试减法功能
    print("测试减法")
    for case in subtraction_data:
        a , b , expected = case["a"], case["b"], case["expected"]
        calc = make_calculator(case["a"], case["b"])
        result = calc.sub()
        print(f"测试数据: {a} - {b} = {expected}, 计算结果: {result}")
        assert result == case["expected"]
def test_multiplication(make_calculator, multiplication_data):
    # 测试乘法功能
    print("测试乘法")
    for case in multiplication_data:
        a , b , expected = case["a"], case["b"], case["expected"]
        calc = make_calculator(case["a"], case["b"])
        result = calc.mul()
        print(f"测试数据: {a} * {b} = {expected}, 计算结果: {result}")
        assert result == case["expected"]
def test_division(make_calculator, division_data):
    # 测试除法功能
    print("测试除法")
    for case in division_data:
        a , b , expected = case["a"], case["b"], case["expected"]
        calc = make_calculator(case["a"], case["b"])
        result = calc.div()
        print(f"测试数据: {a} / {b} = {expected}, 计算结果: {result}")
        assert result == case["expected"]
def test_division_by_zero(make_calculator, exception_data):
    # 测试除数为零的情况
    print("测试除数为零的情况")
    for case in exception_data:
        a , b = case["a"], case["b"]
        calc = make_calculator(case["a"], case["b"])
        with pytest.raises(ValueError) as exc_info:
            calc.div()
        print(f"测试数据: {a} / {b}, 捕获异常: {exc_info.value}")
        assert "除数不能为零" in str(exc_info.value)  # ✅ 使用包含判断
