from datetime import datetime
from enum import Enum

# MARK: - Задание №1

class PublisherDateFormat(Enum):
    # MARK: case
    TheMoscowTimes = ("The Moscow Times", "%A, %B %d, %Y")
    TheGuardian = ("The Guardian", "%A, %d.%m.%y")
    DailyNews = ("Daily News", "%A, %d %B %Y")
    
    # MARK: Public properties
    @property
    def name_publisher(self):
        return self.value[0]

    @property
    def format(self):
        return self.value[1]
    


class DateFormatter:
    # MARK: Public methods
    def get_date_from_str_for_publisher(self, date_str: str, for_publisher: PublisherDateFormat):     
        return datetime.strptime(date_str, for_publisher.format).date()


dict_publishers_and_date_formats = {
     PublisherDateFormat.TheMoscowTimes: "Wednesday, October 2, 2002",
     PublisherDateFormat.TheGuardian: "Friday, 11.10.13",
     PublisherDateFormat.DailyNews: "Thursday, 18 August 1977"
}

date_formatter = DateFormatter()


for publisher, date_str in dict_publishers_and_date_formats.items():
    date = date_formatter.get_date_from_str_for_publisher(date_str, publisher)

    print(f'Дата для "{date_str}" y издателя "{publisher.name_publisher}" равна: {date}')
