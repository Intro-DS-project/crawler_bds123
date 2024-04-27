from datetime import datetime
import os
from dotenv import load_dotenv
from pathlib import Path

import google.generativeai as genai

dotenv_path = Path('./.env')
load_dotenv(dotenv_path=dotenv_path)

GEMINI_API_KEY = os.getenv('API_KEY')
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel('gemini-pro')


def extract_description(description):
    prompt = f"bạn là chuyên gia phân tích dữ liệu từ dữ liệu thô. Ta có thông tin cho thuê nhà trọ bằng tiếng Việt như sau: \
        {description} \n \
        Hãy trích xuất thông tin trên và chuyển về csv gồm các trường thông tin dưới đây. \
        Mỗi trường thông tin ứng với 1 cột trong csv. \
        Trường nào không trích xuất được giá trị thì giá trị mặc định là 0. \
        Danh sách các trường: num_bedroom (số lượng phòng ngủ), \
        num_diningroom (số lượng phòng khách), num_kitchen (số lượng phòng bếp), num_toilet (số lượng nhà vệ sinh), num_floor (nếu là nhà trọ thì có mấy tầng), \
        current_floor (phòng trọ ở tầng mấy), direction (hướng nhà, 1 trong 4 giá trị Đông/Tây/Nam/Bắc), \
        street_width (số thực, theo mét). \
        Vui lòng chỉ trả lại thông tin csv, không sử dụng markdown.\
        Giá trị mặc định của các trường luôn là 0.\
        Ví dụ: 0,0,1,0,0,0,0,0 \
        "

    response = model.generate_content(prompt)
    print(response.text)

    return response.text


def format_date(post_date_str):
    date_time_str = post_date_str.split(', ')[1]
    input_format = "%H:%M %d/%m/%Y"
    post_date_obj = datetime.strptime(date_time_str, input_format)
    return post_date_obj.strftime("%Y-%m-%d %H:%M:%S")


def format_location(address: str, pattern: list):
    res = address
    for p in pattern:
        if p in address:
            res = address.split(p)[1].strip()
            break

    res = res.strip()
    return res
