'''
Q4. Create a Temperature class. Make two methods :
      a. convertFahrenheit - It will take Celsius and will print it into Fahrenheit.
      b. convertCelsius - It will take Fahrenheit and will convert it into Celsius.
'''

class Temperature(object):
    def convertFahrenheit(celcius):
        print("Celcius = {}\nFahrenhiet = {}".format(celcius, 1.8 * celcius + 32))


    def convertCelcius(fahn):
        print("Fahrenheit = {}\nCelcius = {}".format(fahn, (fahn - 32) / 1.8))


temp = Temperature
temp.convertFahrenheit(34)
temp.convertCelcius(65)