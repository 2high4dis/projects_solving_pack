from datetime import datetime, date
import urllib
import re
import webbrowser
import sched
import time

sec_between_checks = 60

days = [("2013-07-26", "day-nineteen"),
        ("2013-07-27", "day-twenty"), ("2013-07-28", "day-twentyone"),
        ("2013-07-29", "day-twentytwo"), ("2013-07-30", "day-twentythree"),
        ("2013-07-31", "day-twentyfour"), ("2013-08-01", "day-twentyfive"),
        ("2013-08-02", "day-twentysix"), ("2013-08-03", "day-twentyseven"),
        ("2013-08-04", "day-twentyeight"), ("2013-08-05", "day-twentynine"),
        ("2013-08-06", "day-thirty"), ("2013-08-07", "day-thirtyone"),
        ("2013-08-08", "day-thirtytwo"), ("2013-08-09", "day-thirtythree"),
        ("2013-08-10", "day-thirtyfour"), ("2013-08-11", "day-thirtyfive"),
        ("2013-08-12", "day-thirtysix"), ("2013-08-13", "day-thirtyseven"),
        ("2013-08-14", "day-thirtyeight"), ("2013-08-15", "day-thirtynine"),
        ("2013-08-16", "day-forty")
        ]
