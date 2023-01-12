# bmi_calculator

This python package is for calculation of BMI (body mass index), and some more computations based on weight loss goals. The package provides simple answers to a user's weight loss goals in terms of how much weight loss/gain and calorie deficit/increase should be aimed for with a target weight and time frame in mind.  The package also provides helpful visualizations about BMI and calorie intake change trajectory leading to the target.

## Functions

The package contains the following functions

- `calculate_bmi`: computes user's BMI based on weight and height. Also creates a visual of the BMI on scale
- `project_bmi`: computes how much average change in BMI should be achieved per day given a targeted weight and the timeframe to reach the goal. Also presents a visual trajectory for BMI
- `project_calories`: computes how much average calorie intake is ideal per day given a targeted weight and the timeframe to reach the goal. Also presents a visual trajectory for calories
- `exercise_plan`: suggests possible exercise plans to achieve the targeted weight


## Installation

```bash
$ pip install bmi_calculator
```

## Usage

- TODO

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`bmi_calculator` was created by Qurat-ul-Ain Azim, Natalie Cho, HanChen Wang, Kelvin Wong. It is licensed under the terms of the MIT license.

## Credits

`bmi_calculator` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
