#!/bin/bash
current_date_time=$(date +'%Y-%m-%d_%H-%M-%S')
scrapy crawl bds123 -O "${current_date_time}_bds123_output.json"
