import pytest
from pysubs2 import SSAFile, SSAEvent


@pytest.fixture
def sample_srt_path(tmp_path_factory):
    # Create a sample input SRT file with known content for testing
    sample_srt = tmp_path_factory.mktemp('data') / 'sample.srt'

    event = SSAEvent(
        start=0,
        end=10000,
        text='Sample subtitle'
    )

    subs = SSAFile()
    subs.events.append(event)

    with open(sample_srt, 'w') as f:
        f.write(subs.to_string('srt'))

    return str(sample_srt)
