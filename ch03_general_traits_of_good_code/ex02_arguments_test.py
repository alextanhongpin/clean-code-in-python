from .ex02_arguments import bad_users_from_rows, users_from_rows, USERS, User


def test_users_from_rows():
    users = bad_users_from_rows(USERS)
    user = users[0]
    assert user.user_id == 0
    assert user.first_name == "first_name_0"
    assert user.last_name == "last_name_0"

    users = users_from_rows(USERS)
    user = users[0]
    assert user.user_id == 0
    assert user.first_name == "first_name_0"
    assert user.last_name == "last_name_0"
