#Faça um algoritimo que converte uma dada temperatura, fornecida pelo usuário entre as escalas Celsius(C), Fahrenheit(F) e Kelvin(K)
# 1 - Se o usuário fornecer a temperatura em °C  converta para °F e °K.
# 2 - Se o usuário fornecer a temperatura em °F  converta para °C e °K.
# 3 - Se o usuário fornecer a temperatura em °K  converta para °C e °F.

#Aluno: Jhonatan Aragão Costa
#Curso: Ciências da computação
#Instituição: AESPI - FAPI

while True:
    options_menu = ("1. Celsius (°C)\n2. Fahrenheit (°F)\n3. Kelvin (°K)")
    print(options_menu)
    try:
        userChoice = int(input("Escolha uma das opções equivalente à escala de temperatura que deseja converter:\n"))
    except:
        print("Digite apenas números!\nTry again :)\n")
    else:
        if userChoice < 1 or userChoice > 3:
            print("erro404\nEscolha apenas opções entre 1 e 3!\nTry again :)\n")
        elif userChoice == 1:
            temperatureValue = float(input("Digite o valor da temperatura em °C:\n"))
            temperatureKelvin = temperatureValue + 273
            temperatureFahrenheit = (temperatureValue * 9 + 160) / 5
            print(f"{temperatureValue:.0f}°C corresponde à:\n{temperatureKelvin:.0f}°K\n{temperatureFahrenheit:.1f}°F\n")
        elif userChoice == 2:
            temperatureValue = float(input("Digite o valor da temperatura em °F:\n"))
            temperatureCelsius = (temperatureValue * 5 - 160) / 9
            temperatureKelvin = temperatureCelsius + 273
            print(f"{temperatureValue:.1f}°F corresponde à:\n{temperatureCelsius:.0f}°C\n{temperatureKelvin:.0f}°K\n")
        elif userChoice == 3:
            temperatureValue = float(input("Digite o valor da temperatura em °K:\n"))
            temperatureCelsius = temperatureValue - 273
            temperatureFahrenheit = (temperatureCelsius * 9) / 5 + 32
            print(f"{temperatureValue:.0f}°K corresponde à:\n{temperatureCelsius:.0f}°C\n{temperatureFahrenheit:.1f}°F\n")
        else:
            print("\nEncerrando o programa...\n")
            break