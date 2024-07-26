#!/usr/bin/env python3
# Student ID: [seneca_id]

class Time:
    """Simple object type for time of the day.
    data attributes: hour, minute, second
    function attributes: __init__, __str__, __repr__,
                         time_to_sec, format_time,
                         change_time, sum_times
    """
    def __init__(self, hour=12, minute=0, second=0):
        """Constructor for time object"""
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        """String representation for the time object"""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def __repr__(self):
        """Official string representation for the time object"""
        return f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}'

    def format_time(self):
        """Return time object as a formatted string"""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def time_to_sec(self):
        """Convert a time object to a single integer representing the number of seconds from mid-night"""
        return self.hour * 3600 + self.minute * 60 + self.second

    def change_time(self, seconds):
        """Change the time by a certain number of seconds"""
        total_seconds = self.time_to_sec() + seconds
        new_time = sec_to_time(total_seconds)
        self.hour, self.minute, self.second = new_time.hour, new_time.minute, new_time.second
        return None

    def sum_times(self, t2):
        """Add two time objects and return the sum."""
        total_seconds = self.time_to_sec() + t2.time_to_sec()
        return sec_to_time(total_seconds)

    def valid_time(self):
        """Check for the validity of the time object attributes:
        0 <= hour < 24, 0 <= minute < 60, 0 <= second < 60
        """
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.minute >= 60 or self.second >= 60 or self.hour >= 24:
            return False
        return True

def sec_to_time(seconds):
    """Convert a given number of seconds to a time object in hour, minute, second format"""
    seconds = seconds % 86400  # Ensure the time is within the range of 0-86399 seconds
    time = Time()
    time.hour, remainder = divmod(seconds, 3600)
    time.minute, time.second = divmod(remainder, 60)
    return time
