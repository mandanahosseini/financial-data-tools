from datetime import datetime
import jdatetime

def shamsi_to_gregorian(shamsi_date: str) -> datetime:
    year, month, day = map(int, shamsi_date.split("/"))
    return jdatetime.date(year, month, day).togregorian()

def gregorian_to_shamsi(gregorian_date: datetime) -> str:
    jdate = jdatetime.date.fromgregorian(date=gregorian_date)
    return f"{jdate.year}/{jdate.month:02d}/{jdate.day:02d}"
