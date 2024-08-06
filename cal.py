from project import calculator

def main():
    test_one()
    test_two()
    test_three()

def test_one () :
    assert calculator("12+2") == "14"
    assert calculator("12/2") == "6"
    assert calculator("12*2") == "24"
    assert calculator("12-2") == "10"
    assert calculator("123456789") == "123456789"

def test_two():
    assert calculator("aaa") == "Error..."
    assert calculator("sssssss") == "Error..."

def test_three():
    assert calculator("1/10") == "Error..."
    assert calculator("12(12)") == "Error..."

if __name__ == "__main__":
    main()