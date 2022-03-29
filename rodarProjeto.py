import os, platform

sistema = platform.system()
print("\n\n### Seu sistema:",sistema," ###\n")

if sistema == "Windows":
	print("\n\n### Criando a venv ###\n")
	os.system('python -m venv venv')
	
	print("\n\n### Ativando a venv ###\n")
	os.system('cd venv & cd Scripts & activate')

	print("\n\n### Instalando/atualizando o pip e instalando o requirements.txt ###\n")
	os.system('python -m pip install --upgrade pip & pip install -r requirements.txt')
	
	print("\n\n### Fazendo as migrations e migrate ###\n")
	os.system('cd app & cd main & python manage.py makemigrations & python manage.py migrate')

if sistema == "Linux":
	print("\n### Criando a venv ###\n")
	os.system('python3 -m venv venv')
	
	print("\n\n### Ativando a venv ###\n")
	os.system('source venv/bin/activate')
	
	print("\n\n### Instalando/atualizando o pip e instalando o requirements.txt ###\n")
	os.system('python -m pip install --upgrade pip | pip install -r requirements.txt')
	
	print("\n\n### Fazendo as migrations e migrate ###\n")
	os.system('cd app | cd main | python manage.py makemigrations | python manage.py migrate')
