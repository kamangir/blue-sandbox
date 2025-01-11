from abcli.tests.test_env import test_abcli_env
from blue_objects.tests.test_env import test_blue_objects_env

from blue_sandbox import env


def test_required_env():
    test_abcli_env()
    test_blue_objects_env()


def test_blue_sandbox_env():
    assert env.DAMAGES_TEST_DATASET_OBJECT_NAME
    assert env.ENCODED_BLOB_SAS_TOKEN
