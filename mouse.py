# -*- coding: utf-8 -*-
import time
import sys
from mouse_library import MouseAutomation


def main(duration: int) -> None:
    """
    Runs the application for a specified duration in seconds.
    """
    print('Press Ctrl-C to quit.')
    start_time = time.time()
    end_time = start_time + duration;
    mouse = MouseAutomation()

    try:
        if duration != 0:
            print('\bStop at ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(end_time)))
        while time.time() < end_time or duration == 0:
            mouse.switch_screens()
            mouse.wiggle_mouse()
            sys.stdout.flush()
    except KeyboardInterrupt:
        print("\nApplication stopped by user.")


if len(sys.argv) > 2:
    print("Usage: python mouse.py <duration_in_seconds>")
    sys.exit(1)  
try:
    duration = int(sys.argv[1]) if len(sys.argv) == 2 else 0
    main(duration)
except ValueError:
    print("Please provide a valid integer for the duration.")
    sys.exit(1)
