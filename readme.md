# Installation

### Dependencies
Requires python 3.8+ or later

```bash
pip install Scrapy
```

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
    "price": 1.2,
    "area": 14.0,
    "street": "25/59 Phố Vũ Ngọc Phan",
    "ward": "Phường Láng Hạ",
    "district": "Đống Đa",
    "post_date": "2024-04-03 10:20:00",
    "url": "https://bds123.vn/cho-thue-phong-o-gia-re-tai-lang-ha-pr802246.html",
    "description": "Diện tích 14m2. Giá thuê chỉ 1.2 triệu/ tháng. Điện nước tính riêng. Có khóa cổng an toàn. Giao thông thuận tiện, gần trạm xe buýt. Gần chợ Láng Hạ, trường ĐH Lao động Xã hội. Liên hệ A Hien: 0913238557.",
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