# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class FindWatchesPipeline:
    def __init__(self):
        self.create_connection()
        self.create_table_watch()

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def create_connection(self):
        self.conn = sqlite3.connect("database.db")
        self.curr = self.conn.cursor()

    def create_table_watch(self):
        self.curr.execute("""
        CREATE TABLE IF NOT EXISTS WATCH (
        id_watch INTEGER PRIMARY KEY UNIQUE ,
        name text, 
        brand text,
        price text,
        link text UNIQUE,
        img  text,
        status text, 
        website text
        )
        """)

    def store_db(self, item):
        self.curr.execute("""
        INSERT INTO WATCH VALUES (?,?,?,?,?,?,?,?)
        """, (
            None,
            item['name'],
            item['brand'],
            item['price'],
            item['link'],
            item['img'],
            item['status'],
            item['website']
        ))
        self.conn.commit()
