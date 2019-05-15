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


def lbsToKgs(users_weight):
    weightInKgs = users_weight * one_kilo
    return weightInKgs


# CHANGE FEET TO INCHES

def feetToInches(users_feet):
    users_height = users_feet * one_foot
    return users_height

# INCHES TO METERS


def inchesToMeter(users_feet, users_inches):
    total_user_height = ((feetToInches(users_feet) + users_inches) * one_meter)
    return total_user_height

# BMI CALCULATOR


def bmiCalc(weight, height):
    user_bmi = weight/height
    return user_bmi


# check for age
user_age = int(input('How old are you ? '))

# SPECIAL MESSAGE


def diagnosisMessage(size, bmi):
    return f'Based off the weigth and the height you provided, your BMI is {bmi} ({size})'

# RETURN MESSAGE


def quickDiagnosis(bmi):
    if bmi < 18.5:
        return diagnosisMessage(small, bmi)
    if bmi > 18.5 and bmi < 24.9:
        return diagnosisMessage(medium, bmi)
    if bmi > 25.0 and bmi < 29.9:
        return diagnosisMessage(large, bmi)
    if bmi > 30.0:
        return diagnosisMessage(xlarge, bmi)


if user_age >= age_bracket:
    users_weight = int(input('Enter you weight in lbs: '))
    users_feet = int(input('Enter you height in feet: '))
    users_inches = int(input('Enter your height in inches : '))
    actual_user_weight = lbsToKgs(users_weight)
    actual_user_height = pow((inchesToMeter(users_feet, users_inches)), 2)
    your_body_mass = round(bmiCalc(actual_user_weight, actual_user_height), 1)
    print('HERE IS YOUR BMI', your_body_mass)
    message = quickDiagnosis(your_body_mass)
    print(message)
else:
    print('Sorry this will not work you\'re under age')
