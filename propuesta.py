import os


def main():
    nombre = os.getenv("USERNAME")
    print(f"Hola esta es la propuesta de {nombre} desde GitHub!")


if __name__ == "__main__":
    main()