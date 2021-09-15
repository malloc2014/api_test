import pytest
import  yaml

class TestData:
    @pytest.mark.parametrize("x, y", yaml.safe_load(open("./test_data.yaml")))
    def test_multi(self, x, y):
        print(f"yaml 的数据是{x + y}")


if  __name__ == "__main__":
    pytest.main()
