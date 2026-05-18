import json
try:    
    with open("alunos.json", "r") as arquivo:
        alunos = json.load(arquivo)
except:
    alunos = []
cods = 1001
qnt = int(input('Qual a quantidade de alunos a serem informados? '))
for r in range(1, qnt+1):
    matricula = {'nome':0, 'idade': 0, 'curso': 0, 'cod': 0, 'sala': 0}
    while True:
        nome = input(f'Qual o nome do {r}o aluno: ')
        confirm = input(f'O nome do aluno é {nome}, você confirma? [s] ou [n]')
        while confirm.upper() not in ['S', 'N']:
           confirm = input(f'Resposta inválida. O nome do aluno é {nome}, você confirma? [s] ou [n]')
        if confirm.upper() == 'S':
            break
        else:
            print('Retornando')
    matricula['nome'] = nome.upper()
    idade = int(input(f'Qual a idade do {r}o: '))
    while idade < 0 or idade > 18:
        idade = int(input('Idade inválida ou superior ao permitido. Qual é a idade?'))
    matricula['idade'] = idade
    if 0<idade<=5:
        matricula['curso'] = 'jardim de infância'
    elif 5<idade<=14:
        matricula['curso'] = 'ensino fundamental'
    else: 
        matricula['curso'] = 'ensino médio'
    matricula['cod'] = cods
    if cods % 2 == 0:
        matricula['sala'] = 'B'
    else:
        matricula['sala'] = 'A'
    cods += 1
    alunos.append(matricula)
while True:
    quest = input('Você gostaria de visualizar [NOMES], [MATRICULAS], [PROCURAR ALUNO], [REMOVER] uma matrícula,  [TROCAR] informações ou [SAIR]? ')
    quest_upper = quest.upper()
    if quest_upper == 'MATRICULAS':
        for a in alunos:
            print(a)
    elif quest_upper == 'NOMES':
        for a in alunos:
            print(a['nome'])
    elif quest_upper == 'PROCURAR ALUNO':
        valid = False
        proc = input('Qual aluno você procura? ')
        for n in alunos:
            if proc.upper() == n['nome']:
                valid = True
                inf = input('Você gostaria de ver [IDADE], [COD], [SALA] ou [MATRICULA] completa? ')
                inf_upper = inf.upper()
                if inf_upper == 'IDADE':
                    print(f"A idade do aluno é {n['idade']} anos.")
                    break
                elif inf_upper == 'COD':
                    print(f"O código do aluno é {n['cod']}.")
                    break
                elif inf_upper == 'SALA':
                    print(f"O aluno está na sala {n['sala']} do {n['curso']}.")
                else:
                    print(n)
                    break
            else:
                continue
        if valid == False:
            print('Aluno não encontrado.')
    elif quest_upper == 'REMOVER':
        remov = input('Qual matrícula deve ser removida?')
        remov_cond = False
        for mat in alunos:
            if remov.upper() == mat.get('nome'):
                alunos.remove(mat)
                print(f'Matrícula de {remov} removida.')
                remov_cond = True
                break
        if remov_cond == False:
            print('A matrícula não pode ser encontrada')
    elif quest_upper == 'SAIR':
        with open("alunos.json", "w") as arquivo:
            json.dump(alunos, arquivo)
        break
    else:
        print('Inválido, tente novamente.')
        continue
    cont = input('Você quer procurar outra informação? [s] ou [n] ')
    cont_upper = cont.upper()
    if cont_upper == 'S':
        continue
    elif cont_upper == 'N':
        break
print('Programa encerrado')

#Adicionar código que contabiliza quantos alunos tem na sala/ no ano
#Transformar partes repetitivas em funções (ex.: confirmação de nome, validação de idade, cadastro)
#Tratar possíveis erros de entrada (ex.: usuário digitar letra em idade)
#Melhorar a legibilidade e manutenção do código, como evitar muitos loops aninhados
