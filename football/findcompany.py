#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" find best return rate company """

import time

import spider

match_all_ids = []

for day in range(13, 20, 1):
    match_ids = spider.crawl_match_list_by_date("2016-07-" + str(day))

    match_all_ids += match_ids

item_list = []

seq = 0


company_map = {}

for match_id in match_all_ids:
    seq += 1
    print(seq, match_id)

    match = spider.get_match(match_id)

    for item in match.item_arr:
        if item.company in company_map:
            cur_company = company_map[item.company]
            cur_company.back_ratio = \
                (cur_company.back_ratio * cur_company.count + item.back_ratio) / \
                (cur_company.count + 1)
            cur_company.count += 1
        else:
            company_map[item.company] = item

    time.sleep(5)

companies = []
for company in company_map.values():
    companies.append(company)

companies.sort(lambda x, y: cmp(x.back_ratio, y.back_ratio))

seq = 0
for company in companies:
    seq += 1
    print(seq, company.id, company.company, company.back_ratio)









