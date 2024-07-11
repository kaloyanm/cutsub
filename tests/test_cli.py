import pytest

from click.testing import CliRunner
from cutsub.cli import cut_subtitle


@pytest.fixture
def runner():
    return CliRunner()


def test_cutsub_command(runner, sample_srt_path):
    output_file = "output.srt"
    result = runner.invoke(
        cut_subtitle, [str(sample_srt_path), output_file, "00:00:00", "00:00:05"]
    )
    assert result.exit_code == 0
    assert "Subtitle file successfully cut." in result.output
