class Dates:
    def __init__(self, initialDate, untilDate):
        if initialDate['year'] > untilDate['year']:
            raise Exception('The initial date cannnot be larger than the until date.')

        self.initialDate = initialDate
        self.untilDate = untilDate

        self.daysInMonth = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if self.isLeapYear(self.initialDate['year']):
            self.daysInMonth[2] = 29

    def isLeapYear(self, year):
        return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

    def daysUntilDate(self):
        firstMonth = self.initialDate['month']
        firstYear = self.initialDate['year']

        lastMonth = self.untilDate['month']
        lastYear = self.untilDate['year']

        restMonth = self.daysInMonth[firstMonth] - self.initialDate['day']
        restYear = 0

        for i in range(firstMonth + 1, 13):
            restYear += self.daysInMonth[i]

        firstYearDays = restMonth + restYear

        middleYearDays = 0

        for i in range(firstYear + 1, lastYear):
            daysYear = 365 if not self.isLeapYear(i) else 366
            middleYearDays += daysYear

        if not self.isLeapYear(lastYear):
            self.daysInMonth[2] = 28

        lastYearDays = 0

        for i in range(lastMonth):
            lastYearDays += self.daysInMonth[i]

        lastYearDays += self.untilDate['day']

        return firstYearDays + middleYearDays + lastYearDays

initialDate = {
    'day': 9,
    'month': 2,
    'year': 1978
}

untilDate = {
    'day': 6,
    'month': 3,
    'year': 2019
}

dates = Dates(initialDate, untilDate)
dates.daysUntilDate()
