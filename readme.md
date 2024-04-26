# Installation

### Dependencies
Requires python 3.8+ or later

```bash
pip install -r requirements.txt
```

Setup environment variables

```bash
cp .env.example .env
```
You need to provide your own `API_KEY` in `.env` file

### Run
in root directory of project

```bash
$ scrapy crawl bds123 -O output.json
```

### Using Docker :whale:
```bash
$ docker build -t bds123 .
$ docker run -v $(pwd):/app/data bds123
```
The output will be saved in current directory

Example output

```json
[
  {
    "price": 4.0,
    "area": 35.0,
    "street": "Trương Định",
    "ward": "Tương Mai",
    "district": "Hoàng Mai",
    "post_date": "2024-04-06 14:50:00",
    "url": "https://bds123.vn/cho-thue-phong-o-duoc-4-ng-35m2-hoang-mai-full-do-pr803570.html",
    "description": "Phòng trọ khép kín, full nội thất. Diện tích 35M2 Hoàng Mai Ở được tối đa 4 người. Chỗ để xe rộng. Liên hệ trực tiếp chính chủ để biết thêm thông tin.",
    "num_bedroom": 0,
    "num_diningroom": 0,
    "num_kitchen": 0,
    "num_toilet": 0,
    "num_floor": 0,
    "current_floor": 0,
    "direction": "",
    "street_width": ""
  },
]
```