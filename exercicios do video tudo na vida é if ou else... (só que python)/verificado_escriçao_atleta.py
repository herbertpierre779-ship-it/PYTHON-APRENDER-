# video do professor: https://www.youtube.com/watch?v=gZBV7FlHDtg&t=1279s minuto:20:14

# Crie um programa Vai vai dar entrada de atletas em uma competição olímpica 
# para entrar o atleta deverá dentre 18 e 25 anos
#  Ele também precisa ter um bom condicionamento físico ou permissão médica
#  As condições devem ser feitas em uma única estrutura if

condicionamento =int(input("qual e o condicionameto do atleta? (1 para ruim | 2 para bom)"))
idade_atleta = int(input("qual e a idade edo atleta? "))
permiçao_medica = "s"

if 18 <= idade_atleta <= 25 and (condicionamento == 2 or permiçao_medica == "s"):
    print("Atleta pode participar")
else:
    print("Atleta nao pode participar!!")