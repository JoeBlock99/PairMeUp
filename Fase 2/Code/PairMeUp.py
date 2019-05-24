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

from neo4j import GraphDatabase

driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "admin"))

def crearUsuario(tx, user, age, sexualGender, typeFood, sexPreference, musicalGenre, favEntertainment, religion, movieGenre, ocupation, faq):
    tx.run("""CREATE
            ($user)-[:TIENE]->($age),
            ($user)-[:ES]->($sexoEs),
            ($user)-[:COME]->($comida),
            ($user)-[:BUSCA]->($sexoBusca),
            ($user)-[:ESCUCHA]->($musica),
            ($user)-[:HACE]->($algo),
            ($user)-[:CREE]->($creencia),
            ($user)-[:VE]->($genero),
            ($user)-[:LABOR]->($EstudianteTrabajador),
            ($user)-[:ESTUDIA]->($faq)
            ($user)-[:ESPERA]->($tipoRelacion),
            ($user)-[:HABLA]->($idioma),""", user= user, age=age, sexoEs=sexualGender, comida=typeFood, sexoBusca=sexPreference, musica = musicalGenre, algo = favEntertainment, creencia = religion, genero = movieGenre, EstudianteTrabajador = ocupation, faq = faq, tipoRelacion = beverage, idioma = secondLanguage)


def getMatch(tx, user):
    for usuarioMatch in tx.run("""
        match (user:Persona) Where user.Correo = $correo
        match (user) -[:BUSCA]-> (:Sexo) <-[:ES]- (algunUsuario: Persona)
        match (algunUsuario)-[:BUSCA]->(:Sexo)<-[:ES]-(user)
        optional match (user)-[:ESPERA]-> (:Buscando)<-[:ESPERA]-(algunUsuario)
        return algunUsuario.Correo
        """, correo = user):
        print("----------------------")
        print(usuarioMatch["algunUsuario.Correo"])




user = "user"
#password = "password"
isLoggedIn = False
wantsTocontinuar = True
continuar = False
option = 0
menu = "\n --- BIENVENIDO --- \n \n1. Ver personas compatibles \n2. Cerrar Sesión\n"

## Print menu for the log in o user registration

while wantsTocontinuar == True:
    print("\n *** PAIR ME UP *** \n1. Registrarse\n2. Iniciar Sesión\n3. Salir \n")
    option = input("Ingrese la opción que desea realizar: ")

    try:
        val = int(option)

        if (val == 1):
            user = input("Ingrese su correo: ")
            #password = input("Ingrese su contraseña: ")



            ##  Guardar esta información en la base de datos!

            ##  Empezar a hacer las preguntas y guardar las respuestas en una base de datos!
            print("Ingrese el número de la respuesta de las siguientes preguntas: \n")

            ##  Con cada preginta verificar que la respuesta esté en el rango de las respuestas, sinó, tirar error y repetir la pregunta, si sí
            ##  hacer la siguiente pregunta

            while continuar == False :
                print("¿Cuál es su sexo? \n1. Masculino \n2. Femenino \n")
                sexualGender = input("Respuesta: ")
                print(" ")

                if sexualGender == "1":
                    sexualGender = "Masculino"
                    continuar = True

                elif sexualGender == "2":
                    sexualGender = "Femenino"
                    continuar = True

                else:
                    print("Ingrese unas opci[on valida!")


            continuar = False
            while continuar == False:
                print("¿Qué sexo le atrae? \n1. Masculino \n2. Femenino \n3. Ambos \n")
                sexPreference = input("Respuesta: ")
                print(" ")

                if sexPreference == "1":
                    sexPreference = "Masculino"
                    continuar = True

                elif sexPreference == "2":
                    sexPreference = "Femenino"
                    continuar = True

                elif sexPreference == "3":
                    sexPreference = "Ambos"

                else:
                    print("Ingrese unas opci[on valida!")

            continuar = False
            while continuar == False:
                print("¿En qué rango de edades se encuentra su edad? \n1. 18-21 \n2. 21-25 \n3. 25+")
                age = input("Respuesta: ")
                print(" ")

                if age == "1":
                    age = "adadA"
                    continuar = True

                elif age == "2":
                    age = "edadB"
                    continuar = True

                elif age == "3":
                    age = "edadC"
                    continuar = True

                else:
                    print("Ingrese unas opci[on valida!")


            continuar = False
            while continuar == False:
                print("¿Cuál es su comida favorita? \n1. Italiana \n2. China \n3. Mariscos \n4. Típica Guatemalteca \n5. Mexicana \n")
                typeFood = input("Respuesta: ")
                print(" ")

                if typeFood == "1":
                    typeFood = "Italiana"
                    continuar = True

                elif typeFood == "2":
                    typeFood = "China"
                    continuar = True

                elif typeFood == "3":
                    typeFood = "Mariscos"
                    continuar = True

                elif typeFood == "4":
                    typeFood = "TipicaGuatemala"
                    continuar = True

                elif typeFood == "5":
                    typeFood = "Mexicana"
                    continuar = True

                else:
                    print("Ingrese unas opci[on valida!")


            continuar = False
            while continuar == False:
                print("¿Cuál es género musical favorito? \n1. Pop \n2. Rock \n3. Electrónica \n4. Country \n5. Reggaeton \n6. Hip Hop \n7. Rap \n8. R&B \n9. Ninguna \n")
                musicalGenre = input("Respuesta: ")
                print(" ")

                if musicalGenre =="1":
                    musicalGenre = "Pop"
                    continuar = True

                elif musicalGenre =="2":
                    musicalGenre = "Rock"
                    continuar = True

                elif musicalGenre =="3":
                    musicalGenre = "Electronica"
                    continuar = True

                elif musicalGenre =="4":
                    musicalGenre = "Country"
                    continuar = True

                elif musicalGenre =="5":
                    musicalGenre = "Reggaeton"
                    continuar = True

                elif musicalGenre =="6":
                    musicalGenre = "HipHop0"
                    continuar = True

                elif musicalGenre =="7":
                    musicalGenre = "Rap"
                    continuar = True

                elif musicalGenre =="8":
                    musicalGenre = "RyB"
                    continuar = True

                elif musicalGenre =="9":
                    musicalGenre = "Ninguna"
                    continuar = True

                else:
                    print("Ingrese unas opci[on valida!")


            continuar = False
            while continuar == False:
                print("¿Cuál es su género de películas preferido? \n1. Acción \n2. Comedia \n3. Romance \n4. Suspenso \n5. Aventura \n6. Sci-Fi \n7. Fantasía \n8. Documental \n")
                movieGenre = input("Respuesta: ")
                print(" ")

                if movieGenre =="1":
                    movieGenre = "Accion"
                    continuar = True

                elif movieGenre =="2":
                    movieGenre = "Comedia"
                    continuar = True

                elif movieGenre =="3":
                    movieGenre = "Romance"
                    continuar = True

                elif movieGenre =="4":
                    movieGenre = "Suspenso"
                    continuar = True

                elif movieGenre =="5":
                    movieGenre = "Aventura"
                    continuar = True

                elif movieGenre =="6":
                    movieGenre = "SciFi"
                    continuar = True

                elif movieGenre =="7":
                    movieGenre = "Fantasia"
                    continuar = True

                elif movieGenre =="8":
                    movieGenre = "Documental"
                    continuar = True

                else:
                    print("Ingrese unas opci[on valida!")

            continuar = False
            while continuar == False:
                print("¿Habla un segundo idioma? \n1. Inglés \n2. Alemán \n3. Italiano \n4. Francés \n5. Portugués \n6. Mandarín \n7. Solo Español \n")
                secondLanguage = input("Respuesta: ")
                print(" ")

                if secondLanguage == "1":
                    secondLanguage = "Ingles"
                    continuar = True

                elif secondLanguage == "2":
                    secondLanguage = "Aleman"
                    continuar = True

                elif secondLanguage == "3":
                    secondLanguage = "Italiano"
                    continuar = True

                elif secondLanguage == "4":
                    secondLanguage = "Frances"
                    continuar = True

                elif secondLanguage == "5":
                    secondLanguage = "Portugues"
                    continuar = True

                elif secondLanguage == "6":
                    secondLanguage = "Mandarin"
                    continuar = True

                elif secondLanguage == "7":
                    secondLanguage = "Espanol"
                    continuar = True

                else:
                    print("Ingrese unas opci[on valida!")


            continuar = False
            while continuar == False:
                print("¿Qué quiere llegar a ser con su match? \n1. Relación \n2. Conocer \n3. Ambos \n")
                beverage = input("Respuesta: ")
                print(" ")

                if beverage == "1":
                    beverage = "Relacion"
                    continuar = True

                elif beverage == "2":
                    beverage = "Conocer"
                    continuar = True

                elif beverage == "3":
                    beverage = "Ambo"
                    continuar = True

                else:
                    print("Ingrese unas opci[on valida!")


            continuar == False
            while continuar == False:
                print("¿Cuál es la actividad que más hace en su tiempo libre? \n1. Jugar videojuegos \n2. Ver television \n3. Leer \n4. Arte \n5. Hacer deporte \n6. Salir con amigos y amigas \n")
                favEntertainment = input("Respuesta: ")
                print(" ")

                if favEntertainment == "1":
                    favEntertainment = "Videojuegos"
                    continuar = True

                elif favEntertainment == "2":
                    favEntertainment = "Television"
                    continuar = True

                elif favEntertainment == "3":
                    favEntertainment = "Leer"
                    continuar = True

                elif favEntertainment == "4":
                    favEntertainment = "Arte"
                    continuar = True

                elif favEntertainment == "5":
                    favEntertainment = "Deporte"
                    continuar = True

                elif favEntertainment == "6":
                    favEntertainment = "Amistades"
                    continuar = True

                else:
                    print("Ingrese unas opci[on valida!")


            continuar = False
            while continuar == False:
                print("¿En qué se ocupa en cuestiones de labor? \n1. Estudio \n2. Trabajo \n3. Ambos \n")
                ocupation = input("Respuesta: ")
                print(" ")

                if ocupation == "1":
                    ocupation = "Estudiante"
                    continuar = True

                elif ocupation == "2":
                    ocupation = "Trabajador"
                    continuar = True

                elif ocupation == "3":
                    ocupation = "EstudianteTrabajador"
                    continuar = True

                else:
                    print("Ingrese unas opci[on valida!")


            continuar = False
            while continuar == False:
                print("¿En qué facultad esta? \n1. Ingeniería \n2. Humanidades \n3. Ciencias Sociales \n4. Ciencias Esonómicas \n5. Ciencias de salud \n6. Ciencias Jurídicas \n")
                faq = input("Respuesta: ")
                print(" ")

                if faq == "1":
                    faq = "Ingenieria"
                    continuar = True

                elif faq == "2":
                    faq = "Humanidades"
                    continuar = True

                elif faq == "3":
                    faq = "CienciasSociales"
                    continuar = True

                elif faq == "4":
                    faq = "CienciasEconomicas"
                    continuar = True

                elif faq == "5":
                    faq = "CienciasSalud"
                    continuar = True

                elif faq == "6":
                    faq = "CienciasJuridicas"
                    continuar = True

                else:
                    print("Ingrese unas opci[on valida!")

            continuar = False
            while continuar == False:
                print("¿Cual es su religion? \n1. CatólicoCristiano \n2. Evangélico \n3. Judio \n4. Mormón \n5. Musulman \n6. SinPreferencia \n")
                religion = input("Respuesta: ")
                print(" ")

                if religion == "1":
                    religion = "CatolicoCristiano"
                    continuar = True

                elif religion == "2":
                    religion = "Evangelico"
                    continuar = True

                elif religion == "3":
                    religion = "Judio"
                    continuar = True

                elif religion == "4":
                    religion = "Mormon"
                    continuar = True

                elif religion == "5":
                    religion = "Musulman"
                    continuar = True

                elif religion == "6":
                    religion = "SinPreferencia"
                    continuar = True

                else:
                    print("Ingrese unas opci[on valida!")


            driver.session().write_transaction(crearUsuario, user, age, sexualGender, typeFood, sexPreference, musicalGenre, favEntertainment, religion, movieGenre, ocupation, faq)


            ##  Una vez ya se hayan respondido las preguntas de forma correcta, imprimir el mismo menú que les aparecerá a los usuarios que hayan iniciado sesión.
            print(menu)
            action = input("Ingrese la opción que desea realizar: ")

            #
            #

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
                        print("Sus matches son: ")
                        # LOGICA DE RECOMEDACION:


                        driver.session().read_transaction(getMatch, user)



                    elif (action == "2"):
                        isLoggedIn = False
                        print("Se ha cerrado sesión")

                    else:
                        print("Por favor ingrese una opción válida \n")

                except ValueError:
                    print("Por favor ingrese números! \n")

        elif (val == "3"):
            wantsTocontinuar = False

        else:
            print("Por favor ingrese una opción válida\n")
    except ValueError:
        print("Por favor ingrese números!\n")

print("\nGRACIAS POR USAR PAIR ME UP <3\n")
