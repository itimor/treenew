#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" soccer bet main function file """

import time

import spider
import portfoliomodel

m_match_ids = spider.crawl_match_list()

for m_match_id in m_match_ids:
    m_match = spider.get_match(m_match_id)
    portfolio = portfoliomodel.best_portfolio(m_match)
    # m_match.display()
    portfolio.display(110)
    time.sleep(4)