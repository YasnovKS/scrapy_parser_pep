from datetime import datetime as dt

from pep_parse.settings import BASE_DIR


class PepParsePipeline:

    def open_spider(self, spider):
        self.statuses = dict()

    def process_item(self, item, spider):
        status = item['status']
        self.statuses[status] = self.statuses.get(status, 0) + 1
        return item

    def close_spider(self, spider):
        result_dir = BASE_DIR / 'results'
        result_dir.mkdir(exist_ok=True)
        time_pattern = ('%Y-%m-%d_%H-%M-%S')
        time_now = dt.now().strftime(time_pattern)
        filename = f'{result_dir}/status_summary_{time_now}.csv'

        with open(filename, mode='w', encoding='utf-8') as file:
            file.write('Статус,Количество\n')
            total = 0
            for status, amount in self.statuses.items():
                file.write(f'{status},{amount}\n')
                total += amount
            file.write(f'Total,{total}\n')
