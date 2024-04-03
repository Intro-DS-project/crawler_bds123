from datetime import datetime


def format_date(post_date_str):
    date_time_str = post_date_str.split(', ')[1]
    input_format = "%H:%M %d/%m/%Y"
    post_date_obj = datetime.strptime(date_time_str, input_format)
    return post_date_obj.strftime("%Y-%m-%d %H:%M:%S")
