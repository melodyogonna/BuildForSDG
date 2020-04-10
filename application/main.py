
def convert_month_to_days(number_of_months: int) -> int:
    return number_of_months * 30


def convert_week_to_days(number_of_weeks: int) -> int:
    return number_of_weeks * 7


class CovidEstimator:

    def __init__(self, **kwargs):
        self.currently_infected: int = 0
        self.currently_infected_worst_case: int = 0
        self.request_period = kwargs.get('days', 1)

    def set_currently_infected(self, reported_cases: int = 0):

        self.currently_infected_worst_case = reported_cases * 50
        self.currently_infected = reported_cases * 10

    def get_currently_infected(self, severe: bool = False):
        if severe:
            return self.currently_infected_worst_case
        return self.currently_infected

    def get_estimated_infections_for_days(self, severe: bool = False) -> int:
        'return the estimated number of infections after a given days, infection doubles every three days'

        days = self.request_period
        three_day_set: int = days // 3

        if severe:
            return self.currently_infected_worst_case * (2 ** three_day_set)
        return self.currently_infected * (2 ** three_day_set)

    def estimate_cases_requires_hospital(self, severe: bool = False) -> int:
        'Return the estimated number of infected people that needs hospitalization'

        if severe:
            requires_hospitalization = self.get_estimated_infections_for_days(
                severe=True) * 0.15
        else:
            requires_hospitalization = self.get_estimated_infections_for_days() * 0.15

        return int(requires_hospitalization)

    def get_available_hospital_beds(self, total_beds: int = 1, severe: bool = False):
        if total_beds < 1:
            total_beds = 1
        estimated_beds_available = total_beds * 0.35

        if severe:
            return int(estimated_beds_available - self.estimate_cases_requires_hospital(severe=True))

        return int(estimated_beds_available - self.estimate_cases_requires_hospital())

    def get_estimated_ICU_cases(self, severe: bool = False):
        '''Return estimated number of cases that will require ICU'''

        if severe:
            ICU_cases = self.get_estimated_infections_for_days(
                severe=True) * 0.05
        else:
            ICU_cases = self.get_estimated_infections_for_days() * 0.05

        return int(ICU_cases)

    def get_estimated_ventilator_cases(self, severe: bool = False):
        '''Return estimated number of cases that will require ventilators'''

        if severe:
            ventilator_cases = self.get_estimated_infections_for_days(
                severe=True) * 0.02
        else:
            ventilator_cases = self.get_estimated_infections_for_days() * 0.02

        return int(ventilator_cases)

    def estimated_economic_money_loss(self, average_income, average_income_population, severe: bool = False):
        if severe:
            economic_loss = ((self.get_estimated_infections_for_days(
                severe=True) * average_income*average_income_population)/self.request_period)
        else:
            economic_loss = ((self.get_estimated_infections_for_days()
                              * average_income*average_income_population)/self.request_period)

        return int(economic_loss)
