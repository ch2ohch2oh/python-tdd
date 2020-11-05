import os
import tempfile

import pytest

from blog.models import Article


@pytest.fixture(autouse=True)
def database():
    # Create a temporary db before the test
    _, file_name = tempfile.mkstemp()
    os.environ['DATABASE_NAME'] = file_name
    Article.create_table(database_name=file_name)
    yield
    # Delete the temporary db after the test
    os.unlink(file_name)