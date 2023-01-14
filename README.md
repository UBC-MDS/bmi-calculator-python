# bmi_calculator

This python package is for calculation of BMI (body mass index), and some more computations based on weight loss goals. The package provides simple answers to a user's weight loss goals in terms of how much weight loss/gain and calorie deficit/increase should be aimed for with a target weight and time frame in mind.  The package also provides helpful visualizations about BMI and calorie intake change trajectory leading to the target.

## Functions

The package contains the following functions

- `calculate_bmi`: computes user's BMI based on weight and height. Also creates a visual of the BMI on scale
- `project_bmi`: computes how much average change in BMI should be achieved per day given a targeted weight and the timeframe to reach the goal. Also presents a visual trajectory for BMI
- `project_calories`: computes how much average calorie intake is ideal per day given a targeted weight and the timeframe to reach the goal. Also presents a visual trajectory for calories
- `exercise_plan`: suggests possible exercise plans to achieve the targeted weight. Also gives a graph showing how much exercise of each kind is needed per day

## Suitability within Python Ecosystem

Our BMI calculator is unique in the sense that it provides easy and instantly understandable visuals to quickly get the gist of how healthy a person is. The package does not rely on any historical data of a person's weights, and hence needs no dataset files to be provided. The only arguments needed for the functions of this calculator are current weight and height, and target weight with timeframe in case weight change is desired. It also recommends simple figures for weight gain/loss goals. There are many BMI calculators in the Python ecosystem. Some of the examples can be found [here](https://pypi.org/project/body-mass-index/) and [here](https://pypi.org/project/Py-bmi/). Both these offer limited visual aid in understanding one's health metrics and targets related to BMI.


## Installation

```bash
$ pip install bmi_calculator
```

## Usage

The package is under active work for now, and the package functions need updating with appropriate functionality. The usage will be updated with details as the functions are updated.

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a [Code of Conduct](https://github.com/UBC-MDS/bmi-calculator-python/blob/master/CONDUCT.md). You can follow guidelines outlined [here](https://github.com/UBC-MDS/bmi-calculator-python/blob/master/CONTRIBUTING.md) in case you want to contribute to the project. By contributing to this project, you agree to abide by its terms.

The list of contributors to the original project can be found [here](https://github.com/UBC-MDS/bmi-calculator-python/blob/master/CONTRIBUTORS.md).

## License

`bmi_calculator` was created by Qurat-ul-Ain Azim, Natalie Cho, HanChen Wang, Kelvin Wong. It is licensed under the terms of the MIT license.

## Credits

`bmi_calculator` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
