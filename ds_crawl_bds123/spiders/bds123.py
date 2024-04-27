from datetime import datetime
import scrapy
from hanoikovoidcdau import standardize

from ds_crawl_bds123.items import DsCrawlBds123Item
from ds_crawl_bds123.utils import format_date, format_location, extract_description


class Bds123Spider(scrapy.Spider):
    name = "bds123"
    allowed_domains = ["bds123.vn"]
    start_urls = ["https://bds123.vn/cho-thue-phong-tro-nha-tro-ha-noi.html"]

    def start_requests(self):
        pages = []
        for i in range(1, 5):
            pages.append(
                f"https://bds123.vn/cho-thue-phong-tro-nha-tro-ha-noi.html?page={i}")

        for page in pages:
            yield scrapy.Request(url=page, callback=self.parse_link)

    def parse_link(self, response):
        for i in range(1, 20):
            str = "div.post-listing > li:nth-child({}) > a::attr(href)".format(
                i)
            link = response.css(str).extract_first()
            link = "https://bds123.vn" + link
            yield scrapy.Request(url=link, callback=self.parse)
        pass

    def parse(self, response):
        # check expired post
        if response.css("div.alrt_post_expired_date"):
            return

        item = DsCrawlBds123Item()
        # example: " 3.2" -> 3.2
        item["price"] = response.css(".post-price::text").get()
        item["price"] = float(item["price"].strip())
        # example: "20 m" -> 20
        item["area"] = response.css(".post-acreage::text").get()
        item["area"] = float(item["area"].strip().split(" ")[0])

        # example: 'Địa chỉ: 25/59 Phố Vũ Ngọc Phan, Phường Láng Hạ, Đống Đa, Hà Nội'
        address = response.css(".item.post-address .address+span::text").get()
        item["street"] = address.split(",")[0].split(":")[1].strip()

        # street may have house_number before partern "Phố", "Đường", "phố", "đường", cut it
        street_pattern = ["Phố", "Đường", "phố", "đường"]
        item["street"] = format_location(item["street"], street_pattern)
        item["street"] = standardize.standardize_street_name(item["street"])

        item["ward"] = address.split(",")[1].strip()
        ward_pattern = ["Phường", "phường", "xã", "Xã"]
        item["ward"] = format_location(item["ward"], ward_pattern)
        item["ward"] = standardize.standardize_ward_name(item["ward"])

        item["district"] = address.split(",")[2].strip()
        discrict_pattern = ["Quận", "Huyện", "quận", "huyện"]
        item["district"] = format_location(item["district"], discrict_pattern)
        item["district"] = standardize.standardize_district_name(
            item["district"])

        # example: 'Thứ 4, 10:20 03/04/2024'
        post_date = response.css(".d-inline-flex::attr(title)").get()
        # format post_date to like 2024-03-31 20:37:21
        item["post_date"] = format_date(post_date)
        item["url"] = response.url

        description = response.css(
            ".margin-bottom-30+ .margin-bottom-30 div p::text").getall()
        item["description"] = " ".join(description)
        num_bedroom, num_diningroom, num_kitchen, num_toilet, num_floor, current_floor, direction, street_width = extract_description(
            description).split(",")

        # field don't have value
        item["num_bedroom"] = num_bedroom
        item["num_diningroom"] = num_diningroom
        item["num_kitchen"] = num_kitchen
        item["num_toilet"] = num_toilet
        item["num_floor"] = num_floor
        item["current_floor"] = current_floor
        item["direction"] = direction
        item["street_width"] = street_width

        yield item

    def format_date(str):
        date_time_str = str.split(', ')[1]
        input_format = "%H:%M %d/%m/%Y"
        post_date_obj = datetime.strptime(date_time_str, input_format)
        return post_date_obj.strftime("%Y-%m-%d %H:%M:%S")
