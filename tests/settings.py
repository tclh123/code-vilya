import os
import tempfile

WTF_CSRF_SECRET_KEY = "[REPLACE THIS WITH REAL KEY]"
SECRET_KEY = "[REPLACE THIS WITH REAL KEY]"

DATABASE = {
    'name': 'vilya-tests',
    'engine': 'peewee.MySQLDatabase',
    'user': 'root',
    'passwd': '',
}

CACHE_TYPE = 'simple'
MIGRATIONS_DIR = 'vilya/migrations'

TESTING = True

GIT_REPO_ROOT = os.path.join(tempfile.gettempdir(), 'vilya-testing-repos')
GIT_TEMP_REPO_ROOT = os.path.join(tempfile.gettempdir(), 'vilya-testing-temp-repos')
