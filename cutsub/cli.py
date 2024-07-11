import click
from cutsub.subtitle_cutter import cut_subtitle_file, parse_time


@click.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.argument('output_file', type=click.Path())
@click.argument('start_time')
@click.argument('end_time')
def cut_subtitle(input_file, output_file, start_time, end_time):
    """
    Cut a subtitle file (SSA/ASS) given start and end times.

    INPUT_FILE: Path to the input subtitle file.
    OUTPUT_FILE: Path to the output subtitle file.
    START_TIME: Start time in HH:MM:SS.MS format.
    END_TIME: End time in HH:MM:SS.MS format.
    """
    try:
        start_time_dict = parse_time(start_time)
        end_time_dict = parse_time(end_time)
        cut_subtitle_file(input_file, output_file, start_time_dict, end_time_dict)
        click.echo('Subtitle file successfully cut.')
    except Exception as e:
        click.echo(f'Error cutting subtitle file: {str(e)}', err=True)
        raise click.Abort()


if __name__ == '__main__':
    cut_subtitle()
