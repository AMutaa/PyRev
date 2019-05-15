# BMI CALCULATOR

age_bracket = 20

# SIZES

small = 'Underweight'
medium = 'Normal or Healthy Weight'
large = 'Overweight'
xlarge = 'Obese'

weight_in_kilos = 68
height_metres = 1.65

one_kilo = 0.453592
one_foot = 12
one_meter = 0.0254

# CHANGE WEIGHT TO KGS


def lbstokgs(user_weight):
    weightInKgs = user_weight * one_kilo
    return weightInKgs


# CHANGE FEET TO INCHES

def feetToInches(users_feet):
    users_height = users_feet * one_foot
    return users_height

# INCHES TO METERS


def inchesToMeters(users_feet, users_inches):
    total_user_height = ((feetToInches(users_feet) + users_inches) * one_meter)
    return total_user_height

# BMI CALCULATOR


def bmiCalc(weight, height):
    user_bmi = weight/height
    return user_bmi
