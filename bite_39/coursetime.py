from datetime import datetime, timedelta
import os
import re
import urllib.request

# getting the data
COURSE_TIMES = os.path.join(os.getenv("TMP", "/tmp"), "course_timings")
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/course_timings", COURSE_TIMES
)


def get_all_timestamps(file=COURSE_TIMES):
    """Read in the COURSE_TIMES and extract all MM:SS timestamps.
    Here is a snippet of the input file:

    Start  What is Practical JavaScript? (3:47)
    Start  The voice in your ear (4:41)
    Start  Is this course right for you? (1:21)
    ...

     Return a list of MM:SS timestamps
    """
    with open(file, "r") as f:
        text = f.read()

    return re.findall(r"(\d{1,2}:\d{2,})", text)


def calc_total_course_duration(timestamps):
    """Takes timestamps list as returned by get_all_timestamps
    and calculates the total duration as HH:MM:SS"""
    total_time = timedelta(0, 0)
    for timestamp in timestamps:
        minutes, seconds = timestamp.split(":")
        seconds = int(minutes) * 60 + int(seconds)
        total_time += timedelta(0, seconds)
    return str(total_time)


if __name__ == "__main__":
    print(calc_total_course_duration(get_all_timestamps()))
