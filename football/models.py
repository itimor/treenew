# -*- coding: utf-8 -*-
# author: itimor

from django.db import models


class duqiu(models.Model):
    profit = models.CharField(max_length=5, verbose_name=u'最低毛利率')

    win_item_id = models.CharField(max_length=5, verbose_name=u'win公司id')
    win_item_company = models.CharField(max_length=20, verbose_name=u'win公司')
    win_item_cw_odds = models.CharField(max_length=5, verbose_name=u'win赔率')
    win_percentage = models.CharField(max_length=5, verbose_name=u'win资金占比')

    draw_item_id = models.CharField(max_length=5, verbose_name=u'draw公司id')
    draw_item_company = models.CharField(max_length=20, verbose_name=u'draw公司')
    draw_item_cw_odds = models.CharField(max_length=5, verbose_name=u'draw赔率')
    draw_percentage = models.CharField(max_length=5, verbose_name=u'draw资金占比')

    lose_item_id = models.CharField(max_length=5, verbose_name=u'lose公司id')
    lose_item_company = models.CharField(max_length=20, verbose_name=u'lose公司')
    lose_item_cw_odds = models.CharField(max_length=5, verbose_name=u'lose赔率')
    lose_percentage = models.CharField(max_length=5, verbose_name=u'lose资金占比')
