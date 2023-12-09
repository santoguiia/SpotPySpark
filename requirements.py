import importlib
import subprocess

def check_and_install_requirements():
    required_libraries = [
        'excel',
        'pyspark'
    ]

    missing_libraries = []

    for library in required_libraries:
        try:
            importlib.import_module(library)
        except ImportError:
            missing_libraries.append(library)

    if missing_libraries:
        print("Bibliotecas ausentes: ", missing_libraries)
        print("Instalando bibliotecas ausentes via pip...")
        for library in missing_libraries:
            subprocess.run(['pip', 'install', library])

        print("Bibliotecas instaladas com sucesso.")
    else:
        print("Todas as bibliotecas necessárias estão instaladas.")

check_and_install_requirements()
