import os  # Linterに検知させるための不要なインポート

def check_even_odd(number):
    """偶数か奇数かを判定する関数"""
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

def multiply(a, b):
    return a * b