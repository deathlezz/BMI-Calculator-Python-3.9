# BMI calculator
# Python 3.9.1
# Created by deathlezz
# Date 24.01.2021


# Say hi
print('')
print('* Welcome to BMI Calculator *')
print('')

# Create infinite loop
while True:

   # Create gender input
   gender = input('Enter your gender: ')

   if gender == 'male':

      # Create age input
      try:
         age = int(input('Enter your age: '))

      except ValueError:
         print('# Enter value 18 - 99')
         print('')
         continue

      if age < 18:
         print('# You must be over 18')
         print('')

      elif age >= 18 and age <= 24:

         try:
            height = float(input('Enter your height: '))

         except ValueError:
            print('# Enter numbers only')
            print('')
            continue

         try:
            weight = float(input('Enter your weight: '))

         except ValueError:
            print('# Enter numbers only')
            print('')
            continue

         heightM = height * 0.01
         BMI = round((weight / (heightM * heightM)), 2)

         if BMI < 20:
            print('Your BMI is', BMI, 'so, you are underweight!')
            print('')

         elif BMI >= 20 and BMI <= 25:
            print('Your BMI is', BMI, 'so, you are healthy!')
            print('')

         elif BMI > 25 and BMI < 31:
            print('Your BMI is', BMI, 'so, you are overweight!')
            print('')

         elif BMI >= 31 and BMI <= 40:
            print('Your BMI is', BMI, 'so, you are obese!')
            print('')

         elif BMI > 40:
            print('Your BMI is', BMI, 'so, you are severely obese!')
            print('')

      elif age >= 25 and age <= 34:

         try:
            height = float(input('Enter your height: '))

         except ValueError:
            print('# Enter numbers only')
            print('')
            continue

         try:
            weight = float(input('Enter your weight: '))

         except ValueError:
            print('# Enter numbers only')
            print('')
            continue

         heightM = height * 0.01
         BMI = round((weight / (heightM * heightM)), 2)

         if BMI < 21:
            print('Your BMI is', BMI, 'so, you are underweight!')
            print('')

         elif BMI >= 21 and BMI <= 26:
            print('Your BMI is', BMI, 'so, you are healthy!')
            print('')

         elif BMI > 26 and BMI < 32:
            print('Your BMI is', BMI, 'so, you are overweight!')
            print('')

         elif BMI >= 32 and BMI <= 41:
            print('Your BMI is', BMI, 'so, you are obese!')
            print('')

         elif BMI > 41:
            print('Your BMI is', BMI, 'so, you are severely obese!')
            print('')

      elif age >= 35 and age <= 44:

         try:
            height = float(input('Enter your height: '))

         except ValueError:
            print('# Enter numbers only')
            print('')
            continue

         try:
            weight = float(input('Enter your weight: '))

         except ValueError:
            print('# Enter numbers only')
            print('')
            continue

         heightM = height * 0.01
         BMI = round((weight / (heightM * heightM)), 2)

         if BMI < 22:
            print('Your BMI is', BMI, 'so, you are underweight!')
            print('')

         elif BMI >= 22 and BMI <= 27:
            print('Your BMI is', BMI, 'so, you are healthy!')
            print('')

         elif BMI > 27 and BMI < 33:
            print('Your BMI is', BMI, 'so, you are overweight!')
            print('')

         elif BMI >= 33 and BMI <= 42:
            print('Your BMI is', BMI, 'so, you are obese!')
            print('')

         elif BMI > 42:
            print('Your BMI is', BMI, 'so, you are severely obese!')
            print('')

      elif age >= 45 and age <= 54:

         try:
            height = float(input('Enter your height: '))

         except ValueError:
            print('# Enter numbers only')
            print('')
            continue

         try:
            weight = float(input('Enter your weight: '))

         except ValueError:
            print('# Enter numbers only')
            print('')
            continue

         heightM = height * 0.01
         BMI = round((weight / (heightM * heightM)), 2)

         if BMI < 23:
            print('Your BMI is', BMI, 'so, you are underweight!')
            print('')

         elif BMI >= 23 and BMI <= 28:
            print('Your BMI is', BMI, 'so, you are healthy!')
            print('')

         elif BMI > 28 and BMI < 34:
            print('Your BMI is', BMI, 'so, you are overweight!')
            print('')

         elif BMI >= 34 and BMI <= 43:
            print('Your BMI is', BMI, 'so, you are obese!')
            print('')

         elif BMI > 43:
            print('Your BMI is', BMI, 'so, you are severely obese!')
            print('')

      elif age >= 55 and age <= 65:

         try:
            height = float(input('Enter your height: '))

         except ValueError:
            print('# Enter numbers only')
            print('')
            continue

         try:
            weight = float(input('Enter your weight: '))

         except ValueError:
            print('# Enter numbers only')
            print('')
            continue

         heightM = height * 0.01
         BMI = round((weight / (heightM * heightM)), 2)

         if BMI < 24:
            print('Your BMI is', BMI, 'so, you are underweight!')
            print('')

         elif BMI >= 24 and BMI <= 29:
            print('Your BMI is', BMI, 'so, you are healthy!')
            print('')

         elif BMI > 29 and BMI < 35:
            print('Your BMI is', BMI, 'so, you are overweight!')
            print('')

         elif BMI >= 35 and BMI <= 44:
            print('Your BMI is', BMI, 'so, you are obese!')
            print('')

         elif BMI > 44:
            print('Your BMI is', BMI, 'so, you are severely obese!')
            print('')

      elif age > 65 and age < 100:

         try:
            height = float(input('Enter your height: '))

         except ValueError:
            print('# Enter numbers only')
            print('')
            continue

         try:
            weight = float(input('Enter your weight: '))

         except ValueError:
            print('# Enter numbers only')
            print('')
            continue

         heightM = height * 0.01
         BMI = round((weight / (heightM * heightM)), 2)

         if BMI < 25:
            print('Your BMI is', BMI, 'so, you are underweight!')
            print('')

         elif BMI >= 25 and BMI <= 30:
            print('Your BMI is', BMI, 'so, you are healthy!')
            print('')

         elif BMI > 30 and BMI < 36:
            print('Your BMI is', BMI, 'so, you are overweight!')
            print('')

         elif BMI >= 36 and BMI <= 45:
            print('Your BMI is', BMI, 'so, you are obese!')
            print('')

         elif BMI > 45:
            print('Your BMI is', BMI, 'so, you are severely obese!')
            print('')

      else:
         print('# Enter value 18 - 99')
         print('')

      continue

   if gender == 'female':

      # Create age input
      try:
         age = int(input('Enter your age: '))

      except ValueError:
         print('# Enter value 18 - 99')
         print('')
         continue

      if age < 18:
         print('# You must be over 18')
         print('')

      elif age >= 18 and age <= 24:

         try:
            height = float(input('Enter your height: '))

         except ValueError:
            print('# Enter numbers only')
            print('')
            continue

         try:
            weight = float(input('Enter your weight: '))

         except ValueError:
            print('# Enter numbers only')
            print('')
            continue

         heightM = height * 0.01
         BMI = round((weight / (heightM * heightM)), 2)

         if BMI < 19:
            print('Your BMI is', BMI, 'so, you are underweight!')
            print('')

         elif BMI >= 19 and BMI <= 24:
            print('Your BMI is', BMI, 'so, you are healthy!')
            print('')

         elif BMI >= 25 and BMI < 30:
            print('Your BMI is', BMI, 'so, you are overweight!')
            print('')

         elif BMI >= 30 and BMI <= 39:
            print('Your BMI is', BMI, 'so, you are obese!')
            print('')

         elif BMI > 39:
            print('Your BMI is', BMI, 'so, you are severely obese!')
            print('')

      elif age >= 25 and age <= 34:

         try:
            height = float(input('Enter your height: '))

         except ValueError:
            print('# Enter numbers only')
            print('')
            continue

         try:
            weight = float(input('Enter your weight: '))

         except ValueError:
            print('# Enter numbers only')
            print('')
            continue

         heightM = height * 0.01
         BMI = round((weight / (heightM * heightM)), 2)

         if BMI < 20:
            print('Your BMI is', BMI, 'so, you are underweight!')
            print('')

         elif BMI >= 20 and BMI <= 25:
            print('Your BMI is', BMI, 'so, you are healthy!')
            print('')

         elif BMI > 25 and BMI < 31:
            print('Your BMI is', BMI, 'so, you are overweight!')
            print('')

         elif BMI >= 31 and BMI <= 40:
            print('Your BMI is', BMI, 'so, you are obese!')
            print('')

         elif BMI > 40:
            print('Your BMI is', BMI, 'so, you are severely obese!')
            print('')

      elif age >= 35 and age <= 44:

         try:
            height = float(input('Enter your height: '))

         except ValueError:
            print('# Enter numbers only')
            print('')
            continue

         try:
            weight = float(input('Enter your weight: '))

         except ValueError:
            print('# Enter numbers only')
            print('')
            continue

         heightM = height * 0.01
         BMI = round((weight / (heightM * heightM)), 2)

         if BMI < 21:
            print('Your BMI is', BMI, 'so, you are underweight!')
            print('')

         elif BMI >= 21 and BMI <= 26:
            print('Your BMI is', BMI, 'so, you are healthy!')
            print('')

         elif BMI > 26 and BMI < 32:
            print('Your BMI is', BMI, 'so, you are overweight!')
            print('')

         elif BMI >= 32 and BMI <= 41:
            print('Your BMI is', BMI, 'so, you are obese!')
            print('')

         elif BMI > 41:
            print('Your BMI is', BMI, 'so, you are severely obese!')
            print('')

      elif age >= 45 and age <= 54:

         try:
            height = float(input('Enter your height: '))

         except ValueError:
            print('# Enter numbers only')
            print('')
            continue

         try:
            weight = float(input('Enter your weight: '))

         except ValueError:
            print('# Enter numbers only')
            print('')
            continue

         heightM = height * 0.01
         BMI = round((weight / (heightM * heightM)), 2)

         if BMI < 22:
            print('Your BMI is', BMI, 'so, you are underweight!')
            print('')

         elif BMI >= 22 and BMI <= 27:
            print('Your BMI is', BMI, 'so, you are healthy!')
            print('')

         elif BMI > 27 and BMI < 33:
            print('Your BMI is', BMI, 'so, you are overweight!')
            print('')

         elif BMI >= 33 and BMI <= 42:
            print('Your BMI is', BMI, 'so, you are obese!')
            print('')

         elif BMI > 42:
            print('Your BMI is', BMI, 'so, you are severely obese!')
            print('')

      elif age >= 55 and age <= 64:

         try:
            height = float(input('Enter your height: '))

         except ValueError:
            print('# Enter numbers only')
            print('')
            continue

         try:
            weight = float(input('Enter your weight: '))

         except ValueError:
            print('# Enter numbers only')
            print('')
            continue

         heightM = height * 0.01
         BMI = round((weight / (heightM * heightM)), 2)

         if BMI < 23:
            print('Your BMI is', BMI, 'so, you are underweight!')
            print('')

         elif BMI >= 23 and BMI <= 28:
            print('Your BMI is', BMI, 'so, you are healthy!')
            print('')

         elif BMI > 28 and BMI < 34:
            print('Your BMI is', BMI, 'so, you are overweight!')
            print('')

         elif BMI >= 35 and BMI <= 43:
            print('Your BMI is', BMI, 'so, you are obese!')
            print('')

         elif BMI > 43:
            print('Your BMI is', BMI, 'so, you are severely obese!')
            print('')

      elif age > 65 and age < 100:

         try:
            height = float(input('Enter your height: '))

         except ValueError:
            print('# Enter numbers only')
            print('')
            continue

         try:
            weight = float(input('Enter your weight: '))

         except ValueError:
            print('# Enter numbers only')
            print('')
            continue

         heightM = height * 0.01
         BMI = round((weight / (heightM * heightM)), 2)

         if BMI < 24:
            print('Your BMI is', BMI, 'so, you are underweight!')
            print('')

         elif BMI >= 24 and BMI <= 29:
            print('Your BMI is', BMI, 'so, you are healthy!')
            print('')

         elif BMI > 29 and BMI < 35:
            print('Your BMI is', BMI, 'so, you are overweight!')
            print('')

         elif BMI >= 35 and BMI <= 44:
            print('Your BMI is', BMI, 'so, you are obese!')
            print('')

         elif BMI > 44:
            print('Your BMI is', BMI, 'so, you are severely obese!')
            print('')

      else:
         print('# Enter value 18 - 99')
         print('')

      continue

   else:
      print('# Enter "male" or "female"')
      print('')