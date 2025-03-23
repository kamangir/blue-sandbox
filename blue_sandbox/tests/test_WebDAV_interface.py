import pytest

from blue_objects import objects

from blue_sandbox.WebDAV import WebDAVInterface


@pytest.mark.parametrize(
    ["filename"],
    [
        ["giza.pdf"],
    ],
)
@pytest.mark.parametrize(
    ["source_object_name"],
    [
        ["giza-v1"],
    ],
)
def test_WebDAV_interface(
    filename: str,
    source_object_name: str,
):
    destination_object_name = objects.unique_object("test_WebDAV_interface")

    assert objects.download(source_object_name)

    interface = WebDAVInterface()

    assert interface.upload(
        objects.path_of(filename, source_object_name),
        f"{destination_object_name}/{filename}",
    )

    assert interface.download(
        f"{destination_object_name}/{filename}",
        objects.path_of(filename, destination_object_name),
    )
