import re

import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        rows = response.css('section#numerical-index tbody tr')
        for row in rows:
            link = row.css('a::attr(href)').get()
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        pep_title = response.css('h1.page-title::text').get()
        title_pattern = r'PEP\s(?P<number>\d+)\W+(?P<name>.+)'
        match = re.match(title_pattern, pep_title)
        number, name = match.groups()
        status = response.css('dt:contains("Status") + dd abbr::text').get()
        data = {
            'number': number.split()[-1],
            'name': name.strip(),
            'status': status
        }
        yield PepParseItem(data)
