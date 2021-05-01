# BMI calculator
# Python 3.9.1
# Created by deathlezz
# Date 24.01.2021


# Say hi
print()
print('* Welcome to BMI Calculator *')
print()

# Create infinite loop
while True:

   # Create gender input
   gender = input('Enter your gender: ')

   if gender == 'male':

      # Create age input
      try:
         age = int(input('Enter your age: '))

      except ValueError:
         print('* Enter numbers only *')
         print()
         continue

      # You can also use: "if age > 0 and age < 18:"
      if 0 < age < 18:
         print('* You must be over 18 *')
         print()

      elif 18 <= age <= 24:

         try:
            # Create height input
            height = float(input('Enter your height: '))

         except ValueError:
            print('* Enter numbers only *')
            print()
            continue

         if 50 <= height <= 280:

            try:
               # Create weight input
               weight = float(input('Enter your weight: '))

            except ValueError:
               print('* Enter numbers only *')
               print()
               continue

            if 20 <= weight <= 300:

               # Change height unit (m -> cm)
               heightM = height * 0.01
               # BMI standard formula with rounding to 1 decimal point
               BMI = round((weight / (heightM * heightM)), 1)

               if BMI < 20:
                  print(f'Your BMI is {BMI}, so you are underweight!')
                  print()

               elif 20 <= BMI <= 25:
                  print(f'Your BMI is {BMI}, so you are healthy!')
                  print()

               elif 25 < BMI < 31:
                  print(f'Your BMI is {BMI}, so you are overweight!')
                  print()

               elif 31 <= BMI <= 40:
                  print(f'Your BMI is {BMI}, so you are obese!')
                  print()

               elif BMI > 40:
                  print(f'Your BMI is {BMI}, so you are severely obese!')
                  print()

            else:
               print('* Enter value 20 - 300 *')
               print()

         else:
            print('* Enter value 50 - 280 *')
            print()

      elif 25 <= age <= 34:

         try:
            height = float(input('Enter your height: '))

         except ValueError:
            print('* Enter numbers only *')
            print()
            continue

         if 50 <= height <= 280:

            try:
               weight = float(input('Enter your weight: '))

            except ValueError:
               print('* Enter numbers only *')
               print()
               continue

            if 20 <= weight <= 300:

               heightM = height * 0.01
               BMI = round((weight / (heightM * heightM)), 1)

               if BMI < 21:
                  print(f'Your BMI is {BMI}, so you are underweight!')
                  print()

               elif 21 <= BMI <= 26:
                  print(f'Your BMI is {BMI}, so you are healthy!')
                  print()

               elif 26 < BMI < 32:
                  print(f'Your BMI is {BMI}, so you are overweight!')
                  print()

               elif 32 <= BMI <= 41:
                  print(f'Your BMI is {BMI}, so you are obese!')
                  print()

               elif BMI > 41:
                  print(f'Your BMI is {BMI}, so you are severely obese!')
                  print()

            else:
               print('* Enter value 20 - 300 *')
               print()

         else:
            print('* Enter value 50 - 280 *')
            print()

      elif 35 <= age <= 44:

         try:
            height = float(input('Enter your height: '))

         except ValueError:
            print('* Enter numbers only *')
            print()
            continue

         if 50 <= height <= 280:

            try:
               weight = float(input('Enter your weight: '))

            except ValueError:
               print('* Enter numbers only *')
               print()
               continue

            if 20 <= weight <= 300:

               heightM = height * 0.01
               BMI = round((weight / (heightM * heightM)), 1)

               if BMI < 22:
                  print(f'Your BMI is {BMI}, so you are underweight!')
                  print()

               elif 22 <= BMI <= 27:
                  print(f'Your BMI is {BMI}, so you are healthy!')
                  print()

               elif 27 < BMI < 33:
                  print(f'Your BMI is {BMI}, so you are overweight!')
                  print()

               elif 33 <= BMI <= 42:
                  print(f'Your BMI is {BMI}, so you are obese!')
                  print()

               elif BMI > 42:
                  print(f'Your BMI is {BMI}, so you are severely obese!')
                  print()

            else:
               print('* Enter value 20 - 300 *')
               print()

         else:
            print('* Enter value 50 - 280 *')
            print()

      elif 45 <= age <= 54:

         try:
            height = float(input('Enter your height: '))

         except ValueError:
            print('* Enter numbers only *')
            print()
            continue

         if 50 <= height <= 280:

            try:
               weight = float(input('Enter your weight: '))

            except ValueError:
               print('* Enter numbers only *')
               print()
               continue

            if 20 <= weight <= 300:

               heightM = height * 0.01
               BMI = round((weight / (heightM * heightM)), 1)

               if BMI < 23:
                  print(f'Your BMI is {BMI}, so you are underweight!')
                  print()

               elif 23 <= BMI <= 28:
                  print(f'Your BMI is {BMI}, so you are healthy!')
                  print()

               elif 28 < BMI < 34:
                  print(f'Your BMI is {BMI}, so you are overweight!')
                  print()

               elif 34 <= BMI <= 43:
                  print(f'Your BMI is {BMI}, so you are obese!')
                  print()

               elif BMI > 43:
                  print(f'Your BMI is {BMI}, so you are severely obese!')
                  print()

            else:
               print('* Enter value 20 - 300 *')
               print()

         else:
            print('* Enter value 50 - 280 *')
            print()

      elif 55 <= age <= 65:

         try:
            height = float(input('Enter your height: '))

         except ValueError:
            print('# Enter numbers only')
            print()
            continue

         if 50 <= height <= 280:

            try:
               weight = float(input('Enter your weight: '))

            except ValueError:
               print('* Enter numbers only *')
               print()
               continue

            if 20 <= weight <= 300:

               heightM = height * 0.01
               BMI = round((weight / (heightM * heightM)), 1)

               if BMI < 24:
                  print(f'Your BMI is {BMI}, so you are underweight!')
                  print()

               elif 24 <= BMI <= 29:
                  print(f'Your BMI is {BMI}, so you are healthy!')
                  print()

               elif 29 < BMI < 35:
                  print(f'Your BMI is {BMI}, so you are overweight!')
                  print()

               elif 35 <= BMI <= 44:
                  print(f'Your BMI is {BMI}, so you are obese!')
                  print()

               elif BMI > 44:
                  print(f'Your BMI is {BMI}, so you are severely obese!')
                  print()

            else:
               print('* Enter value 20 - 300 *')
               print()

         else:
            print('* Enter value 50 - 280 *')
            print()

      elif 65 < age < 100:

         try:
            height = float(input('Enter your height: '))

         except ValueError:
            print('* Enter numbers only *')
            print()
            continue

         if 50 <= height <= 280:

            try:
               weight = float(input('Enter your weight: '))

            except ValueError:
               print('* Enter numbers only *')
               print()
               continue

            if 20 <= weight <= 300:

               heightM = height * 0.01
               BMI = round((weight / (heightM * heightM)), 1)

               if BMI < 25:
                  print(f'Your BMI is {BMI}, so you are underweight!')
                  print()

               elif 25 <= BMI <= 30:
                  print(f'Your BMI is {BMI}, so you are healthy!')
                  print()

               elif 30 < BMI < 36:
                  print(f'Your BMI is {BMI}, so you are overweight!')
                  print()

               elif 36 <= BMI <= 45:
                  print(f'Your BMI is {BMI}, so you are obese!')
                  print()

               elif BMI > 45:
                  print(f'Your BMI is {BMI}, so you are severely obese!')
                  print()

            else:
               print('* Enter value 20 - 300 *')
               print()

         else:
            print('* Enter value 50 - 280 *')
            print()

      else:
         print('* Enter value 18 - 99 *')
         print()

      continue

   if gender == 'female':

      # Create age input
      try:
         age = int(input('Enter your age: '))

      except ValueError:
         print('* Enter numbers only *')
         print()
         continue

      if 0 < age < 18:
         print('* You must be over 18 *')
         print()

      elif 18 <= age <= 24:

         try:
            height = float(input('Enter your height: '))

         except ValueError:
            print('* Enter numbers only *')
            print()
            continue

         if 50 <= height <= 280:

            try:
               weight = float(input('Enter your weight: '))

            except ValueError:
               print('* Enter numbers only *')
               print()
               continue

            if 20 <= weight <= 300:

               heightM = height * 0.01
               BMI = round((weight / (heightM * heightM)), 1)

               if BMI < 19:
                  print(f'Your BMI is {BMI}, so you are underweight!')
                  print()

               elif 19 <= BMI <= 24:
                  print(f'Your BMI is {BMI}, so you are healthy!')
                  print()

               elif 25 <= BMI < 30:
                  print(f'Your BMI is {BMI}, so you are overweight!')
                  print()

               elif 30 <= BMI <= 39:
                  print(f'Your BMI is {BMI}, so you are obese!')
                  print()

               elif BMI > 39:
                  print(f'Your BMI is {BMI}, so you are severely obese!')
                  print()

            else:
               print('* Enter value 20 - 300 *')
               print()

         else:
            print('* Enter value 50 - 280 *')
            print()

      elif 25 <= age <= 34:

         try:
            height = float(input('Enter your height: '))

         except ValueError:
            print('* Enter numbers only *')
            print()
            continue

         if 50 <= height <= 280:

            try:
               weight = float(input('Enter your weight: '))

            except ValueError:
               print('* Enter numbers only *')
               print()
               continue

            if 20 <= weight <= 300:

               heightM = height * 0.01
               BMI = round((weight / (heightM * heightM)), 1)

               if BMI < 20:
                  print(f'Your BMI is {BMI}, so you are underweight!')
                  print()

               elif 20 <= BMI <= 25:
                  print(f'Your BMI is {BMI}, so you are healthy!')
                  print()

               elif 25 < BMI < 31:
                  print(f'Your BMI is {BMI}, so you are overweight!')
                  print()

               elif 31 <= BMI <= 40:
                  print(f'Your BMI is {BMI}, so you are obese!')
                  print()

               elif BMI > 40:
                  print(f'Your BMI is {BMI}, so you are severely obese!')
                  print()

            else:
               print('* Enter value 20 - 300 *')
               print()

         else:
            print('* Enter value 50 - 280 *')
            print()

      elif 35 <= age <= 44:

         try:
            height = float(input('Enter your height: '))

         except ValueError:
            print('* Enter numbers only *')
            print()
            continue

         if 50 <= height <= 280:

            try:
               weight = float(input('Enter your weight: '))

            except ValueError:
               print('* Enter numbers only *')
               print()
               continue

            if 20 <= weight <= 300:

               heightM = height * 0.01
               BMI = round((weight / (heightM * heightM)), 1)

               if BMI < 21:
                  print(f'Your BMI is {BMI}, so you are underweight!')
                  print()

               elif 21 <= BMI <= 26:
                  print(f'Your BMI is {BMI}, so you are healthy!')
                  print()

               elif 26 < BMI < 32:
                  print(f'Your BMI is {BMI}, so you are overweight!')
                  print()

               elif 32 <= BMI <= 41:
                  print(f'Your BMI is {BMI}, so you are obese!')
                  print()

               elif BMI > 41:
                  print(f'Your BMI is {BMI}, so you are severely obese!')
                  print()

            else:
               print('* Enter value 20 - 300 *')
               print()

         else:
            print('* Enter value 50 - 280 *')
            print()

      elif 45 <= age <= 54:

         try:
            height = float(input('Enter your height: '))

         except ValueError:
            print('* Enter numbers only *')
            print()
            continue

         if 50 <= height <= 280:

            try:
               weight = float(input('Enter your weight: '))

            except ValueError:
               print('* Enter numbers only *')
               print()
               continue

            if 20 <= weight <= 300:

               heightM = height * 0.01
               BMI = round((weight / (heightM * heightM)), 1)

               if BMI < 22:
                  print(f'Your BMI is {BMI}, so you are underweight!')
                  print()

               elif 22 <= BMI <= 27:
                  print(f'Your BMI is {BMI}, so you are healthy!')
                  print()

               elif 27 < BMI < 33:
                  print(f'Your BMI is {BMI}, so you are overweight!')
                  print()

               elif 33 <= BMI <= 42:
                  print(f'Your BMI is {BMI}, so you are obese!')
                  print()

               elif BMI > 42:
                  print(f'Your BMI is {BMI}, so you are severely obese!')
                  print()

            else:
               print('* Enter value 20 - 300 *')
               print()

         else:
            print('* Enter value 50 - 280 *')
            print()

      elif 55 <= age <= 65:

         try:
            height = float(input('Enter your height: '))

         except ValueError:
            print('* Enter numbers only *')
            print()
            continue

         if 50 <= height <= 280:

            try:
               weight = float(input('Enter your weight: '))

            except ValueError:
               print('* Enter numbers only *')
               print()
               continue

            if 20 <= weight <= 300:

               heightM = height * 0.01
               BMI = round((weight / (heightM * heightM)), 1)

               if BMI < 23:
                  print(f'Your BMI is {BMI}, so you are underweight!')
                  print()

               elif 23 <= BMI <= 28:
                  print(f'Your BMI is {BMI}, so you are healthy!')
                  print()

               elif 28 < BMI < 34:
                  print(f'Your BMI is {BMI}, so you are overweight!')
                  print()

               elif 35 <= BMI <= 43:
                  print(f'Your BMI is {BMI}, so you are obese!')
                  print()

               elif BMI > 43:
                  print(f'Your BMI is {BMI}, so you are severely obese!')
                  print()

            else:
               print('* Enter value 20 - 300 *')
               print()

         else:
            print('* Enter value 50 - 280 *')
            print()

      elif 65 < age < 100:

         try:
            height = float(input('Enter your height: '))

         except ValueError:
            print('* Enter numbers only *')
            print()
            continue

         if 50 <= height <= 280:

            try:
               weight = float(input('Enter your weight: '))

            except ValueError:
               print('* Enter numbers only *')
               print()
               continue

            if 20 <= weight <= 300:

               heightM = height * 0.01
               BMI = round((weight / (heightM * heightM)), 1)

               if BMI < 24:
                  print(f'Your BMI is {BMI}, so you are underweight!')
                  print()

               elif 24 <= BMI <= 29:
                  print(f'Your BMI is {BMI}, so you are healthy!')
                  print()

               elif 29 < BMI < 35:
                  print(f'Your BMI is {BMI}, so you are overweight!')
                  print()

               elif 35 <= BMI <= 44:
                  print(f'Your BMI is {BMI}, so you are obese!')
                  print()

               elif BMI > 44:
                  print(f'Your BMI is {BMI}, so you are severely obese!')
                  print()

            else:
               print('* Enter value 20 - 300 *')
               print()

         else:
            print('* Enter value 50 - 280 *')
            print()

      else:
         print('* Enter value 18 - 99 *')
         print()

      continue

   else:
      print('* Enter "male" or "female" *')
      print()