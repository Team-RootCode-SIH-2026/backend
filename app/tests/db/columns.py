from sqlalchemy import inspect


def test_users_columns(engine):
    inspector = inspect(engine)
    cols = inspector.get_columns("User")
    colnames = {column["name"] for column in cols}
    assert colnames == {"pk_id", "k_email", "k_username", "hashed_pwd", "is_active", "is_superuser", "created_at"}

def test_analysis_columns(engine):
    inspector = inspect(engine)
    cols = inspector.get_columns("Analysis")
    colnames = {column["name"] for column in cols}
    assert colnames == {"pk_analysis_id", "subject_type", "pipeline", "model_name", "model_version", "analysis_result", "confidence_score", "analysis_date"}

def test_annotations_columns(engine):
    inspector = inspect(engine)
    cols = inspector.get_columns("Annotation")
    colnames = {column["name"] for column in cols}
    assert colnames == {"pk_annotation_id", "researcher_id", "analysis_corrected", "corrections"}

def test_audio_columns(engine):
    inspector = inspect(engine)
    cols = inspector.get_columns("AudioFile")
    colnames = {column["name"] for column in cols}
    assert colnames == {"pk_id", "fk_owner_id", "original_filename", "stored_filename", "size_bytes", "created_at", "file_type", "language_name"}

def test_images_columns(engine):
    inspector = inspect(engine)
    cols = inspector.get_columns("ImageFile")
    colnames = {column["name"] for column in cols}
    assert colnames == {"pk_id", "fk_owner_id", "original_filename", "stored_filename", "size_bytes", "created_at", "file_type", "language_name"}

def test_languages_columns(engine):
    inspector = inspect(engine)
    cols = inspector.get_columns("Languages")
    colnames = {column["name"] for column in cols}
    assert colnames == {"k_name", "pk_code", "family", "region", "status"}

def test_speakers_columns(engine):
    inspector = inspect(engine)
    cols = inspector.get_columns("Speakers")
    colnames = {column["name"] for column in cols}
    assert colnames == {"pk_speaker_id", "age_range", "dialect", "community"}

def test_text_columns(engine):
    inspector = inspect(engine)
    cols = inspector.get_columns("TextFile")
    colnames = {column["name"] for column in cols}
    assert colnames == {"pk_id", "fk_owner_id", "original_filename", "stored_filename", "size_bytes", "created_at", "file_type", "language_name"}
