from sqlalchemy import inspect


def test_tables_exist(engine):
    inspector = inspect(engine)

    tables = set(inspector.get_table_names())

    assert "Analysis" in tables
    assert "Annotation" in tables
    assert "AudioFile" in tables
    assert "ImageFile" in tables
    assert "Languages" in tables
    assert "Speakers" in tables
    assert "TextFile" in tables
    assert "User" in tables
