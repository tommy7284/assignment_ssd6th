import pytest

# srcフォルダにあるlogic.pyから関数をインポートします
from src.logic import check_even_odd, multiply

# テスト関数名は必ず "test_" で始める必要があります


def test_check_even_odd():
    """偶数・奇数判定の基本的なテスト"""
    assert check_even_odd(2) == "Even"
    assert check_even_odd(3) == "Odd"
    assert check_even_odd(0) == "Even"


def test_multiply():
    """掛け算の基本的なテスト"""
    assert multiply(3, 4) == 12
    assert multiply(-1, 5) == -5
    assert multiply(0, 100) == 0


# --- 以下はレポートのネタになる少し高度なテスト（任意） ---


# パラメータ化テスト（一度に複数のデータをテストする書き方）
@pytest.mark.parametrize("number, expected", [(10, "Even"), (7, "Odd"), (-2, "Even")])
def test_check_even_odd_advanced(number, expected):
    assert check_even_odd(number) == expected
