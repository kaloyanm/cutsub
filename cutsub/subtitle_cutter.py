from pysubs2 import SSAFile, make_time


def parse_time(time_str):
    hours, minutes, seconds = map(int, time_str.split(":"))
    seconds, milliseconds = divmod(seconds, 1)

    return {"h": hours, "m": minutes, "s": seconds}


def cut_subtitle_file(input_file, output_file, start_time, end_time):
    subs = SSAFile.load(input_file)
    # Convert start_time and end_time to milliseconds
    start_ms = make_time(**start_time)
    end_ms = make_time(**end_time)

    # Filter subtitles based on start and end time
    filtered_events = [
        event for event in subs.events if start_ms <= event.start < end_ms
    ]

    if not filtered_events:
        # If there are no events in the given time range, save an empty subtitle file
        SSAFile().save(output_file)
        return

    # Calculate the offset to adjust all subtitle start times to begin from 0
    offset = filtered_events[0].start

    # Adjust the start and end times of each subtitle
    for event in filtered_events:
        event.start -= offset
        event.end -= offset

    # Create a new SSAFile object and add adjusted events
    new_subs = SSAFile()
    new_subs.events.extend(filtered_events)

    # Save the adjusted subtitles to the output file
    new_subs.save(output_file)
