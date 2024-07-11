import pytest

from pysubs2 import SSAFile
from cutsub.subtitle_cutter import cut_subtitle_file, parse_time


def test_cut_subtitle_file(sample_srt_path, tmp_path):
    output_file = tmp_path / 'output.srt'
    start_time = parse_time('00:00:00')
    end_time = parse_time('00:00:10')

    cut_subtitle_file(sample_srt_path, str(output_file), start_time, end_time)

    output_subs = SSAFile.load(str(output_file))
    assert len(output_subs.events) == 1
    assert output_subs.events[0].text == 'Sample subtitle'


def test_parse_time():
    test_cases = [
        ("00:01:00", {'h': 0, 'm': 1, 's': 0}),
        ("01:02:03", {'h': 1, 'm': 2, 's': 3}),
        ("10:20:30", {'h': 10, 'm': 20, 's': 30}),
        ("00:00:00", {'h': 0, 'm': 0, 's': 0}),
    ]

    for input_str, expected_output in test_cases:
        assert parse_time(input_str) == expected_output


def test_parse_time_invalid_format():
    with pytest.raises(ValueError):
        parse_time("invalid_time_format")
