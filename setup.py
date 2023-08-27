import subprocess

def install_requirements(file_path):
    with open(file_path, 'r') as file:
        requirements = file.readlines()
        
    for requirement in requirements:
        package_name = requirement.strip()
        if package_name:
            subprocess.run(['pip', 'install', package_name])

if __name__ == "__main__":
    requirements_file = "requirements.txt"
    install_requirements(requirements_file)
    print("Các thư viện đã được cài đặt từ file requirements.txt")
