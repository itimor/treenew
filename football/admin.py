# -*- coding: utf-8 -*-
# author: itimor

from django.contrib import admin
from football.models import Duqiu

@admin.register(Duqiu)
class DuqiuAdmin(admin.ModelAdmin):
    # 显示在管理页面的字段
    list_display = ('name', 'profit', 'win_item_company', 'win_item_cw_odds', 'win_percentage', 'draw_item_company', 'draw_item_cw_odds', 'draw_percentage', 'lose_item_company', 'lose_item_cw_odds', 'lose_percentage')
    # 定制过滤器
    list_filter = ('win_item_company','draw_item_company','lose_item_company')
    # 可查询字段
    search_fields = ('name',)
    # 可以修改内容的链接
    list_display_links = ['name']
    # 排序
    ordering = ('profit',)