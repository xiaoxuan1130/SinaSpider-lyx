# encoding=utf-8

class NewsPipeline(object):

    def process_item(self, item, spider):
        print("business logic -----------")
        return item
