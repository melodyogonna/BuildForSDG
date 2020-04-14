import unittest

from src.estimator import sample_input_data, estimator



class TestEstimationOutput(unittest.TestCase):

    def setUp(self):
        self.estimator = estimator(sample_input_data)

    def test_estimator_returns_currently_infected(self):
        self.assertIn('currentlyInfected', self.estimator['impact'])
        self.assertIn('currentlyInfected', self.estimator['severeImpact'])

        self.assertIsInstance(
            self.estimator['impact']['currentlyInfected'], int)
        self.assertIsInstance(
            self.estimator['severeImpact']['currentlyInfected'], int)

    def test_estimator_returns_cases_by_requsted_time(self):
        self.assertIn('infectionsByRequestedTime', self.estimator['impact'])
        self.assertIn('infectionsByRequestedTime',
                      self.estimator['severeImpact'])

        self.assertIsInstance(
            self.estimator['impact']['infectionsByRequestedTime'], int)
        self.assertIsInstance(
            self.estimator['severeImpact']['infectionsByRequestedTime'], int)

    def test_estimator_returns_severe_cases(self):
        self.assertIn('severeCasesByRequestedTime', self.estimator['impact'])
        self.assertIn('severeCasesByRequestedTime',
                      self.estimator['severeImpact'])

        self.assertIsInstance(
            self.estimator['impact']['severeCasesByRequestedTime'], int)
        self.assertIsInstance(
            self.estimator['severeImpact']['severeCasesByRequestedTime'], int)

    def test_estimator_returns_available_beds(self):
        self.assertIn('hospitalBedsByRequestedTime', self.estimator['impact'])
        self.assertIn('hospitalBedsByRequestedTime',
                      self.estimator['severeImpact'])

        self.assertIsInstance(
            self.estimator['impact']['hospitalBedsByRequestedTime'], int)
        self.assertIsInstance(
            self.estimator['severeImpact']['hospitalBedsByRequestedTime'], int)

    def test_estimator_returns_ICU_cases(self):
        self.assertIn('casesForICUByRequestedTime', self.estimator['impact'])
        self.assertIn('casesForICUByRequestedTime',
                      self.estimator['severeImpact'])

        self.assertIsInstance(
            self.estimator['impact']['casesForICUByRequestedTime'], int)
        self.assertIsInstance(
            self.estimator['severeImpact']['casesForICUByRequestedTime'], int)

    def test_estimator_returns_cases_that_requires_ventilation(self):
        self.assertIn('casesForVentilatorsByRequestedTime',
                      self.estimator['impact'])
        self.assertIn('casesForVentilatorsByRequestedTime',
                      self.estimator['severeImpact'])

        self.assertIsInstance(
            self.estimator['impact']['casesForVentilatorsByRequestedTime'], int)
        self.assertIsInstance(
            self.estimator['severeImpact']['casesForVentilatorsByRequestedTime'], int)

    def test_estimator_returns_money_lost(self):
        self.assertIn('dollarsInFlight',
                      self.estimator['impact'])
        self.assertIn('dollarsInFlight',
                      self.estimator['severeImpact'])


if __name__ == '__main__':
    unittest.main()
