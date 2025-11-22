# desafios-codigo-cyber
🚀 Desafios de Código 

Este repositório contém a resolução dos desafios de Python concluídos durante os módulos do Bootcamp Santander Cibersegurança.

📋 Desafios Implementados
🔐 1. Sistema de Verificação de Tentativas de Login
Desenvolvi um sistema que analisa uma lista de tentativas de login para identificar possíveis acessos não autorizados. O programa determina se uma conta deve ser bloqueada com base em um limite máximo de tentativas falhas consecutivas.

🕵️ 2. Analisador de Comandos do Usuário
Implementei um analisador que avalia comandos digitados por um usuário para classificar o comportamento como "suspeito" ou "seguro". O sistema identifica padrões e palavras-chave que possam indicar atividades maliciosas.

🔐 3. Simulando um Ransomware em Ambiente Controlado

Este projeto é uma simulação acadêmica de ransomware criada para fins de estudo em segurança da informação. Ele foi desenvolvido em ambiente controlado e não representa uma ameaça real, servindo apenas como demonstração de como esse tipo de ataque funciona.

O programa atua sobre dois arquivos de texto — dados-confidenciais.txt e senhas.txt — localizados na mesma pasta do executável. Ele lê o conteúdo, criptografa os dados, gera a chave necessária para a descriptografia e, em seguida, cria um novo arquivo simulando uma mensagem de infecção.

O objetivo é mostrar de forma prática como ocorre a criptografia de dados em ataques de ransomware e conscientizar sobre os riscos digitais. Por isso, o uso é restrito a ambientes de teste e estudo, não devendo ser aplicado em máquinas pessoais ou sistemas de produção.

🕵️ 4. Simulando um Keylogger em Ambiente Controlado

Este projeto é uma simulação de keylogger desenvolvida para fins educacionais e de conscientização em segurança da informação. Ele demonstra como softwares maliciosos podem capturar informações digitadas pelo usuário, mas foi criado apenas para estudo em ambiente controlado, sem representar uma ameaça real.

O programa registra todas as teclas pressionadas no teclado, porém ignora atalhos comuns e padrões do sistema para evitar que o log gerado seja poluído com informações irrelevantes. Paralelamente, o módulo chamado keylogger_email é responsável por coletar esse log e simular o envio dos dados a um endereço de e-mail a cada dois minutos, conforme definido no algoritmo.

O objetivo é mostrar de forma prática como funcionam ataques baseados em captura de teclado e exfiltração de dados, reforçando a importância da proteção contra esse tipo de ameaça. Por isso, o uso é restrito a ambientes de teste e estudo, não devendo ser aplicado em sistemas pessoais ou de produção.
