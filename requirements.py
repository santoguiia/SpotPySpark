import importlib
import subprocess

def check_and_install_requirements():
    required_libraries = [
        ('pyspark', '3.5.0'),
        ('py4j', '>=0.10.9.7'),
        ('pandas', '>=1.0.5'),
        ('pyarrow', '>=4.0.0'),
        ('numpy', '>=1.15'),
        ('grpcio', '>=1.48, <1.57'),
        ('grpcio-status', '>=1.48, <1.57'),
        ('googleapis-common-protos', '==1.56.4'),
        ('hvplot', '>==0.9.0'),
        ('panel', '>=0.12.6'),
    ]

    missing_libraries = []

    for library, version in required_libraries:
        try:
            importlib.import_module(library)
        except ImportError:
            missing_libraries.append((library, version))

    if missing_libraries:
        print("Missing libraries: ", missing_libraries)
        print("Installing missing libraries via pip...")
        for library, version in missing_libraries:
            subprocess.run(['pip', 'install', f'{library}{version}'])

        print("Libraries installed successfully.")
    else:
        print("All required libraries are already installed.")

check_and_install_requirements()