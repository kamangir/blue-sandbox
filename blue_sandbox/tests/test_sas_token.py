import pytest

from blue_options import string

from blue_sandbox.microsoft_building_damage_assessment.sas_token import (
    encode_token,
    decode_token,
)


@pytest.mark.parametrize(
    ["token"],
    [
        [string.random()],
    ],
)
def test_sas_token_encoding(token: str):
    assert decode_token(encode_token(token)) == token
