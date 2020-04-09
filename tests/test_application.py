# Standard library
import unittest

# Third-party module


# Local dependencies
from application.main import CovidEstimator


class TestApplication(unittest.TestCase):

    def setUp(self):
        self.est = CovidEstimator(days=30)
        self.est.set_currently_infected(reported_cases=100)

    def test_set_currently_infected(self):
        self.est.set_currently_infected(reported_cases=200)

        currently_infected = self.est.currently_infected
        currently_infected_worst_case = self.est.currently_infected_worst_case

        self.assertEqual(currently_infected, 2000)
        self.assertEqual(currently_infected_worst_case, 10000)

    def test_get_currently_infected(self):
        currently_infected = self.est.get_currently_infected
        self.assertEqual(currently_infected(), self.est.currently_infected)
        self.assertEqual(currently_infected(severe=True),
                         self.est.currently_infected_worst_case)

    def test_get_estimated_infections_in_days(self):
        es = self.est.get_estimated_infections_for_days

        self.assertIsInstance(es(), int)
        self.assertEqual(
            es(), self.est.currently_infected * (2 ** (30 // 3)))
        self.assertEqual(
            es(severe=True), self.est.currently_infected_worst_case * (2 ** (30 // 3)))

    def test_cases_that_require_hospitalization(self):
        requires_hospitalization = self.est.estimate_cases_requires_hospital

        self.assertEqual(requires_hospitalization(),
                         self.est.get_estimated_infections_for_days() * 0.15)
        self.assertEqual(requires_hospitalization(severe=True),
                         self.est.get_estimated_infections_for_days(severe=True) * 0.15)

    def test_available_hospital_beds(self):
        available_beds = self.est.get_available_hospital_beds

        self.assertEqual(available_beds(100), 35 -
                         self.est.estimate_cases_requires_hospital())
        self.assertEqual(available_beds(100, severe=True),
                         35 - self.est.estimate_cases_requires_hospital(severe=True))

    def test_ICU_cases(self):

        ICU_cases = self.est.get_estimated_ICU_cases

        self.assertEqual(
            ICU_cases(), self.est.get_estimated_infections_for_days() * 0.05)
        self.assertEqual(ICU_cases(severe=True),
                         self.est.get_estimated_infections_for_days(severe=True) * 0.05)

    def test_ventilator_cases(self):
        ventilator_cases = self.est.get_estimated_ventilator_cases

        self.assertEqual(ventilator_cases(),
                         self.est.get_estimated_infections_for_days() * 0.02)
        self.assertEqual(ventilator_cases(severe=True),
                         self.est.get_estimated_infections_for_days(severe=True) * 0.02)

    def test_estimated_economic_loss(self):
        economic_loss = self.est.estimated_economic_money_loss

        self.assertEqual(economic_loss(
            1.5), self.est.get_estimated_infections_for_days() * 0.65 * 1.5*self.est.request_period)
        self.assertEqual(economic_loss(
            1.5, severe=True), self.est.get_estimated_infections_for_days(severe=True)*0.65*1.5*self.est.request_period)


if __name__ == '__main__':
    unittest.main()
