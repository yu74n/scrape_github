# -*- coding: utf-8 -*-
import scrapy
from scrapy.utils.python import to_unicode
import json
from urllib.parse import urljoin

class GithubSpider(scrapy.Spider):
    name = "github"
    allowed_domains = ["api.github.com"]
    base_url = 'https://api.github.com/'

    def start_requests(self):
        user = self.user
        # TODO Return error message if 'user' command line parameter is not passed
        urls = ["users/%s/events/public" % user, "/users/%s/starred" % user, "/users/%s/repos" % user, "/users/%s/followers" % user, "/users/%s/following" % user]
        for path in urls:
            url = urljoin(self.base_url, path)
            yield scrapy.Request(url, self.parse)

    def parse(self, response):
        key = response.url.split("/")[-1]
        yield json.loads("{ \"%s\": %s }" % (key, to_unicode(response.body)))
