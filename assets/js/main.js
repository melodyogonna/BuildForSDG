const vue = new Vue({
    el: '#app',
    data: {
        returnedOutput: null,
        loading: false,

        regionName: '',
        avgDailyIncome: '',
        averageIncomePopulation: '',
        reportedCases: '',
        periodType: 'days',
        periodValue: '',
        totalHospitalBeds: '',
        population: ''
    },
    methods: {
        submit() {
            this.loading = true;
            const data = {
                region: {
                    name: this.regionName,
                    avgDailyIncomeInUSD: parseInt(this.avgDailyIncome) || 0,
                    avgDailyIncomePopulation: this.averageIncomePopulation / 100
                },
                periodType: this.periodType,
                timeToElapse: parseInt(this.periodValue) || 0,
                reportedCases: parseInt(this.reportedCases) || 0,
                population: parseInt(this.population) || 0,
                totalHospitalBeds: parseInt(this.totalHospitalBeds) || 0
            }

            fetch('http://127.0.0.1:8080/api/v1/on-covid-19/', {
                method: 'post',
                mode: 'cors',
                body: JSON.stringify(data),
                headers: new Headers({
                    'Content-Type': 'application/json'
                })
            }).then(
                response => response.json()
            ).then(
                data => {
                    this.returnedOutput = data;
                    this.loading = false;
                    console.log(data)
                }
            ).catch(
                err => {
                    this.loading = false;
                    this.returnedOutput = null;
                    console.log(err)
                }
            );

        }
    },
})