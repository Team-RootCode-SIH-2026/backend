from ..models.user import User


def test_create_user(session):
    user = User(
        k_email="alice@example.com",
        k_username="alice",
        hashed_pwd="aliceAliceHeartAndSoul",
        is_active=True,
        is_superuser=False
    )
    session.add(user)
    session.commit()

    assert user.pk_id is not None

    result = session.get(User, user.pk_id)
    assert result is not None
    assert result.k_username == "alice"
