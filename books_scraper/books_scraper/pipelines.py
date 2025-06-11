# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import re

class CleanBookDataPipeline:
    def process_item(self, item, spider):
        # Convert price (e.g., "£51.77") to float
        if item.get('price'):
            item['price'] = float(item['price'].replace('£', '').strip())

        # Convert rating string to integer
        rating_map = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
        item['rating'] = rating_map.get(item.get('rating', '').strip(), 0)

        # Fill missing category
        if not item.get('category'):
            item['category'] = 'Unknown'

        # Fill missing description
        if not item.get('description'):
            item['description'] = 'No description available'

        return item