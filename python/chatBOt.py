def chatbot():
    respuestas = {
        "hola": "¡Hola! ¿En qué puedo ayudarte?",
        "adios": "¡Adiós! Que tengas un buen día.",
        "como estas": "Estoy aquí para ayudarte, gracias por preguntar.",
    }

    while True:
        pregunta = input("Tú: ").lower()
        if pregunta in respuestas:
            print(f"Chatbot: {respuestas[pregunta]}")
        elif pregunta == "salir":
            break
        else:
            print("Chatbot: Lo siento, no entiendo esa pregunta.")

chatbot()