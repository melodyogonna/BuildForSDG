from application.main import CovidEstimator, convert_month_to_days, convert_week_to_days


sample_input_data = {
    'region': {
        'name': "Africa",
        'avgAge': 19.7,
        'avgDailyIncomeInUSD': 5,
        'avgDailyIncomePopulation': 0.71
    },
    'periodType': "days",
    'timeToElapse': 58,
    'reportedCases': 674,
    'population': 66622705,
    'totalHospitalBeds': 1380614
}


def estimator(data: dict) -> dict:

    output_data = {
        'data': data,
        'impact': {},
        'severeImpact': {}
    }

    if data['periodType'] == 'days':
        requested_days = data.get('timeToElapse', 1)
    elif data['periodType'] == 'weeks':
        requested_days = convert_week_to_days(data.get('timeToElapse', 1))
    elif data['periodType'] == 'months':
        requested_days = convert_month_to_days(data.get('timeToElapse', 1))

    covid_estimator = CovidEstimator(days=requested_days)
    covid_estimator.set_currently_infected(data.get('reportedCases', 0))

    output_data['impact']['currentlyInfected'] = covid_estimator.get_currently_infected()
    output_data['severeImpact']['currentlyInfected'] = covid_estimator.get_currently_infected(
        severe=True)

    output_data['impact']['infectionsByRequestedTime'] = covid_estimator.get_estimated_infections_for_days()
    output_data['severeImpact']['infectionsByRequestedTime'] = covid_estimator.get_estimated_infections_for_days(
        severe=True)

    output_data['impact']['severeCasesByRequestedTime'] = covid_estimator.estimate_cases_requires_hospital()
    output_data['severeImpact']['severeCasesByRequestedTime'] = covid_estimator.estimate_cases_requires_hospital(
        severe=True)

    output_data['impact']['hospitalBedsByRequestedTime'] = covid_estimator.get_available_hospital_beds(
        data.get('totalHospitalBeds', 1))
    output_data['severeImpact']['hospitalBedsByRequestedTime'] = covid_estimator.get_available_hospital_beds(
        data.get('totalHospitalBeds', 1), severe=True)

    output_data['impact']['casesForICUByRequestedTime'] = covid_estimator.get_estimated_ICU_cases()
    output_data['severeImpact']['casesForICUByRequestedTime'] = covid_estimator.get_estimated_ICU_cases(
        severe=True)

    output_data['impact']['casesForVentilatorsByRequestedTime'] = covid_estimator.get_estimated_ventilator_cases()
    output_data['severeImpact']['casesForVentilatorsByRequestedTime'] = covid_estimator.get_estimated_ventilator_cases(
        severe=True)

    average_income = data['region'].get('avgDailyIncomeInUSD', 1)
    average_income_population = data['region'].get(
        'avgDailyIncomePopulation', .00)
    output_data['impact']['dollarsInFlight'] = covid_estimator.estimated_economic_money_loss(
        average_income, average_income_population)
    output_data['severeImpact']['dollarsInFlight'] = covid_estimator.estimated_economic_money_loss(
        average_income, average_income_population, severe=True)

    return output_data
