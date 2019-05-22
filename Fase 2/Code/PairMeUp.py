##  Universidad del Valle de Guatemala
##  1CC2003 Algoritmos y Estructuras de Datos
##  Proyecto 2 - Pair Me Up
##  Andrés Berthet - 171504
##  José Block - 18935
##  Luis Pedro Cuéllar - 18220

##  ----------------------------

##  This program is supposed to emulate the famous app Tinder, but in a different
##  way. It uses the database in graphs Neo4J to do the recommendations to the users
##  about their matches with other users. The algorithm works by making some questions
##  to a new user, later it compares their answers with the other users and makes a percentage.
##  All the users that have a higher percentage than 75% are "compatible".


user = "user"
password = "password"
isLoggedIn = False
wantsToContinue = True
option = 0
menu = "\n --- BIENVENIDO --- \n \n1. Ver personas compatibles \n2. Cerrar Sesión\n"

## Print menu for the log in o user registration

while wantsToContinue == True:
    print("\n *** PAIR ME UP *** \n1. Registrarse\n2. Iniciar Sesión\n3. Salir \n")
    option = input("Ingrese la opción que desea realizar: ")

    try:
        val = int(option)

        if (val == 1):
            user = input("Ingrese su correo:")
            password = input("Ingrese su contraseña: ")

            ##  Guardar esta información en la base de datos!

            ##  Empezar a hacer las preguntas y guardar las respuestas en una base de datos!
            print("Ingrese el número de la respuesta de las siguientes preguntas: \n")

            ##  Con cada preginta verificar que la respuesta esté en el rango de las respuestas, sinó, tirar error y repetir la pregunta, si sí
            ##  hacer la siguiente pregunta

            print("¿Cuál es su sexo? \n1. Masculino \n2. Femenino \n")
            sexualGender = input("Respuesta: ")
            print(" ")

            print("¿Cuál es su comida favorita? \n1. Italiana \n2. China \n3. Marisocs \n4. Típica Guatemalteca \n5. Mexicana \n6. Norte Americana \n")
            typeFood = input("Respuesta: ")
            print(" ")

            print("¿Cuál es género musical favorito? \n1. Pop \n2. Rock \n3. Electrónica \n4. Country \n5. Reggaeton \n6. Hip Hop")
            musicalGenre = input("Respuesta: ")
            print(" ")

            print("¿Cuál es su tipo de clima preferido? \n1. Tropical \n2. Verano \n3. Invierno \n4. Lluvioso")
            typeWeather = input("Respuesta: ")
            print(" ")

            print("¿Cual es su red social favorita? \n1. Instagram \n2. Snapchat \n3. Facebook \n4. Twitter \n5. WhatsApp \n6. YouTube\n")
            favSocialNetwork = input("Respuesta: ")
            print(" ")

            print("¿Cuál es su género de películas preferido? \n1. Acción \n2. Comedia \n3. Romance \n4. Suspenso \n5. Aventura \n6. Sci-Fi \n7. Fantasía \n8. Documental \n")
            movieGenre = input("Respuesta: ")
            print(" ")

            print("¿Habla un segundo idioma? \n1. Inglés \n2. Alemán \n3. Italiano \n4. Francés \n5. Portugués \n6. Mandarín \n7. Solo Español \n")
            secondLanguage = input("Respuesta: ")
            print(" ")

            print("¿Cuál es su bebida preferida? \n1. Frutales \n2. Naturales \n3. Carbonatadas \n4. Alcohólicas \n5. Café \n6. Té \n")
            beverage = input("Respuesta: ")
            print(" ")

            print("¿Cuál es su deporte favorito? \n1. Fútbol  \n2. Fútbol Americano \n3. Voleibol \n4. Baloncesto \n5. Hockey \n6. Golf \n7. Ninguno \n")
            favSport = input("Respuesta: ")
            print(" ")

            print("¿Cuál es su forma favorita de entretenimiento? \n1. Jugar videojuegos \n2. Ver Series \n3. Ver Películs \n4. Ir al teatro \n5. Hacer deporte \n6. Practicar arte \n7. Leer \n8. Salidas sociales \n")
            favEntertainment = input("Respuesta: ")
            print(" ")

            print("¿Cuál es su preferencia sexual? \n1. Sexo masculino \n2. Sexo femenino \n3. Ambos \n")
            sexPreference = input("Respuesta: ")
            print(" ")

            ##  Una vez ya se hayan respondido las preguntas de forma correcta, imprimir el mismo menú que les aparecerá a los usuarios que hayan iniciado sesión.
            print(menu)
            action = input("Ingrese la opción que desea realizar: ")

        elif (val == 2):
            ##  Pedir los datos para el log in
            user = input("Ingrese su correo:")
            password = input("Ingrese su contraseña: ")

            ##  Verificar si esta información existe, si existe presentar menú, y si no existe mostrar error y volver a preguntar datos

            isLoggedIn = True

            while (isLoggedIn == True):
                print(menu)
                action = input("Ingrese la opción que desea realizar: ")

                try:
                    num = int(action)

                    if (action == "1"):
                        print("sus matches son mi nepe!")

                    elif (action == "2"):
                        isLoggedIn = False
                        print("Se ha cerrado sesión")

                    else:
                        print("Por favor ingrese una opción válida \n")

                except ValueError:
                    print("Por favor ingrese números! \n")

        elif (val == 3):
            wantsToContinue = False

        else:
            print("Por favor ingrese una opción válida\n")

    except ValueError:
        print("Por favor ingrese números!\n")

print("\nGRACIAS POR USAR PAIR ME UP <3\n")