#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2015-01-16 17:47:30
# Project: 39YaoPin

from pyspider.libs.base_handler import *


class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('http://ypk.39.net/', callback=self.fenlei_page)

    @config(age=10 * 24 * 60 * 60)
    def fenlei_page(self, response):
        for each in response.doc('a[href^="http://ypk.39.net/search/"]').items():        
            self.crawl(each.attr.href, callback=self.jutifenlei_page)

    @config(age=10 * 24 * 60 * 60)
    def jutifenlei_page(self, response):
        total_items = response.doc('DIV.search_tips>i').text()
        print repr(total_items)
        total_items = int(total_items)
        totalpage = int(total_items+int(16)-int(1))/int(16)

        for i in range(1, totalpage):

            i = repr(i)

            self.crawl(response.url + '--0-0-0-0-9-0-0-0-'+i, callback=self.yaopin_page)        

    @config(age=10 * 24 * 60 * 60)
    def yaopin_page(self, response):
        for each in response.doc('.search_right  .search_ul.search_ul_yb li a[href^="http://ypk.39.net/yaopin/"]').items():        
            self.crawl(each.attr.href, callback=self.brief_page)

    def brief_page(self, response):        
            detail = {
            "url": response.url,
            "title": response.doc('title').text()
        }
            for each in response.doc('HTML>BODY>DIV.page>DIV.yps_top>DIV.t4>UL>LI:eq(1)>A').items():        
                  self.crawl(each.attr.href, callback=self.detail_page, save= detail)


    def detail_page(self, response):    

        return {
            "url": response.url,
            "detail": response.save

}    
