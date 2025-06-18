from datetime import datetime
import pytz

def convert_timezone(ist_datetime_str, to_timezone):
    """
    Convert a datetime string in IST to the requested timezone.
    Format expected: 'YYYY-MM-DD HH:MM'
    """
    try:
        # Parse the input time assuming IST
        ist = pytz.timezone("Asia/Kolkata")
        naive_dt = datetime.strptime(ist_datetime_str, "%Y-%m-%d %H:%M")
        ist_dt = ist.localize(naive_dt)

        # Convert to requested timezone
        target = pytz.timezone(to_timezone)
        converted = ist_dt.astimezone(target)

        return converted.strftime("%Y-%m-%d %H:%M %Z")
    except Exception as e:
        # If timezone is invalid or conversion fails, return original IST
        return ist_datetime_str + " IST"
