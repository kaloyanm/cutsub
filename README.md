# cutsub

`cutsub` is a Python CLI tool that allows you to cut subtitle files (SRT format) based on specified start and end times.

## Installation

You can install cutsub using pip:

```bash
>>> pip install cutsub
```

## Usage

To cut a subtitle file, use the cutsub command followed by the input file, output file, start time, and end time:

```bash
>>> cutsub input.srt output.srt 00:01:00 00:02:00
```

## Parameters

| Parameter    | Description                                                 | Example        |
|--------------|-------------------------------------------------------------|----------------|
| `input_file` | Path to the input subtitle file                             | `input.srt`    |
| `output_file`| Path to the output subtitle file                            | `output.srt`   |
| `start_time` | Start time in the format `HH:MM:SS`                         | `00:01:00`     |
| `end_time`   | End time in the format `HH:MM:SS`                           | `00:02:00`     |

## License

This project is licensed under the MIT License - see the LICENSE file for details.
