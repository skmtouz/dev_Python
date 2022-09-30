# Um "jogo" de perguntas e respostas referente a Certificação do Exame Az-900: Microsoft Azure Fundamentals

from time import sleep

print('=' * 46)
print('   Bem vindo ao Quiz da certificação AZ-900')
print('=' * 46)

analisando = 'Analisando sua resposta...'
pontos = 0

start = input("Deseja começar o Quiz? (S/N) ")

if start != "S":
    quit()
else:
    sleep(1)
    print('Ok, Vamos começar!')
    sleep(2)

print('=' * 20)
questão1 = ('PRIMEIRA PERGUNTA: \nQual das opções a seguir fornece um conjunto de ferramentas para monitorar, '
            'alocar e otimizar seus custos do Azure?')
print(questão1)
sleep(1)
alternativas1 = '(A) Azure Cost Management \n(B) Azure Pricing Calculator \n(C) Total Cost of Ownership Calculator'
print(alternativas1)

resposta1 = input('Digite a Alternativa Correta: ')

print(analisando)
sleep(1)


if resposta1 == 'A':
    print('Você Acertou!!')
    sleep(1)
    print('Azure Cost Management é um produto do Azure que fornece um conjunto de ferramentas para monitorar, '
          'alocar e otimizar seus custos do Azure.')
    pontos = pontos + 20
else:
    print('Você errou, vamos para a próxima pergunta')

print('=' * 20)

questão2 = 'SEGUNDA PERGUNTA: \nQual das opções a seguir pode ser usada para gerenciar a governança em várias ' \
           'assinaturas do Azure? '
print(questão2)
sleep(1)
alternativas2 = '(A) Azure Initiatives \n(B) Management Groups \n(C) Resource Groups'
print(alternativas2)

resposta2 = input('Digite a Alternativa Correta: ')

print(analisando)
sleep(1)

if resposta2 == 'B':
    print('Você Acertou!!')
    sleep(1)
    print('Os grupos de gerenciamento facilitam a ordenação hierárquica dos recursos do Azure em coleções, '
          'em um nível de escopo acima das assinaturas.\nCondições de governança distintas podem ser aplicadas a cada '
          'grupo de gerenciamento com a Política do Azure e RBACs do Azure,\npara gerenciar as assinaturas do Azure '
          'de forma eficaz.\nOs recursos e assinaturas atribuídos a um grupo de gerenciamento herdam automaticamente '
          'as condições aplicadas ao grupo de gerenciamento.')
    pontos = pontos + 20
else:
    print('Você errou, vamos para a próxima pergunta')

print('=' * 20)

questão3 = 'TERCEIRA PERGUNTA: \nQual das opções a seguir define metas de desempenho, como tempo de atividade, ' \
           'para um produto ou serviço do Azure? '
print(questão3)
sleep(1)
alternativas3 = '(A) Service Level Agreements \n(B) Support Plans \n(C) Usage Meters'
print(alternativas3)

resposta3 = input('Digite a Alternativa Correta: ')

print(analisando)
sleep(1)

if resposta3 == 'A':
    print('Você Acertou!!')
    sleep(1)
    print('Service Level Agreement (SLA). O SLA define metas de desempenho para um produto ou serviço do Azure.')
    pontos = pontos + 20
else:
    print('Você errou, vamos para a próxima pergunta')

print('=' * 20)

questão4 = 'QUARTA PERGUNTA: \nQual das opções a seguir é uma unidade lógica de serviços do Azure vinculada a uma ' \
           'conta do Azure? '
print(questão4)
sleep(1)
alternativas4 = '(A) Azure Subscription \n(B) Management Group \n(C) Resource Group'
print(alternativas4)

resposta4 = input('Digite a Alternativa Correta: ')

print(analisando)
sleep(1)

if resposta4 == 'A':
    print('Você Acertou!!')
    sleep(1)
    print('A Azure Subscription é a unidade lógica de serviços do Azure que se vincula a uma conta do Azure.')
    pontos = pontos + 20
else:
    print('Você errou, vamos para a próxima pergunta')

print('=' * 20)

questão5 = 'QUINTA PERGUNTA: \nQual plano de suporte do Azure é o melhor para cargas de trabalho business-critical?'
print(questão5)
sleep(1)
alternativas5 = '(A) Azure Developer \n(B) Azure Professional Direct \n(C) Azure Standard'
print(alternativas5)

resposta5 = input('Digite a Alternativa Correta: ')

print(analisando)
sleep(1)

if resposta5 == 'B':
    print('Você Acertou!!')
    sleep(1)
    print('Azure Professional Direct é a melhor maneira de garantir que suas soluções funcionem quase o tempo todo.')
    pontos = pontos + 20
else:
    print('Você errou, vamos para a próxima pergunta')

print('=' * 20)