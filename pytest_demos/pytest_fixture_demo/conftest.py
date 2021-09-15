import pytest

@pytest.fixture()
def login():
    print("这是一个登陆方法")

def pytest_configure(config):
    mark_list = ["search", "login"]
    for markers in mark_list:
        config.addinivalue_line(
            "markers", markers
        )