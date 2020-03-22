"""TEST - Write
Test writing the mashup of ideologies
"""

# # Native # #
from uuid import uuid4

# # Project # #
from ideology_mashup.methods import write_strings


def test_write_strings(tmp_path, mashed_ideologies):
    file_path = (tmp_path / str(uuid4())).as_posix()

    write_strings(list(mashed_ideologies), file_path=file_path)

    with open(file_path, "r") as file:
        write_result = file.read()

    assert write_result == "\n".join([*mashed_ideologies, ""])
