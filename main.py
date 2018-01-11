#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" soccer bet main function file """

import spider
import portfoliomodel
import time

m_match_ids = spider.crawl_match_list()

for m_match_id in m_match_ids:
    m_match = spider.get_match(m_match_id)
    portfolio = portfoliomodel.best_portfolio(m_match)
    # m_match.display()
    portfolio.display(102)
    time.sleep(4)