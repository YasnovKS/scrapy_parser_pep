from datetime import datetime as dt

from pep_parse.settings import BASE_DIR


class PepParsePipeline:

    def __init__(self):
        self.result_dir = BASE_DIR / 'results'
        self.result_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.statuses = dict()

    def process_item(self, item, spider):
        status = item['status']
        self.statuses[status] = self.statuses.get(status, 0) + 1
        return item

    def close_spider(self, spider):
        time_pattern = ('%Y-%m-%d_%H-%M-%S')
        time_now = dt.now().strftime(time_pattern)
        filename = BASE_DIR / f'results/status_summary_{time_now}.csv'

        with open(filename, mode='w', encoding='utf-8') as file:
            file.write('Статус,Количество\n')
            total = 0
            for status, amount in self.statuses.items():
                file.write(f'{status},{amount}\n')
                total += amount
            file.write(f'Total,{total}\n')
