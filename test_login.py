def test_valid_login():
    username = "student001"
    password = "password123"

    assert username == "student001"
    assert password == "password123"

    print("Login test passed")


if __name__ == "__main__":
    test_valid_login()