# Escola
Projeto para homologação dos plugins de estudos de aceleramento de desenvolvimento de api

## USUÁRIO

  > Um usuario pertence a um grupo de DIRETOR, PROFESSOR OU ALUNO
 
  > O usuario é obrigado a preencher o cadastro.

###### ROTAS
  - [ ] GET
  - [ ] Registro
  - [ ] Login
  - [ ] Recuperação de conta
  - [ ] Edição de perfil



## GRUPO 
  > Haverá 4 Grupos, ADM, DIRETOR, PROFESSOR e ALUNO

  > ADM - Será o responsavel pelo sistema e terá total liberdade.
  
  > DIRETOR - Será responsavel por uma ou mais escolas e terá total liberdade dentro dela.

  > PROFESSOR - Será responsavel por uma ou mais salas de aula e tera total liberdade dentro dela.

  > ALUNO - Sera um membro de uma ou mais escolas e fará parte de uma ou mais salas de aula

###### ROTAS
  - [ ] GET
  - [ ] POST
  - [ ] PUT 
  - [ ] DELETE

## TESTE
  > Será os modelos e "provas" aplicadas
  
  > Tera questoes de multipla escolhas ou de escrita
  
  > ESCRITA - As questoes de escrita esperará a avaliação do professor para concluir a "prova"

###### ROTAS
  - [ ] CLOSE
  - [ ] GET
  - [ ] POST
  - [ ] PUT
  - [ ] DELETE

## PROVA
  > Terá as informações do "teste" aplicado justo com as informações do alunos
  
###### ROTAS
  - [ ] GET
  - [ ] POST
  - [ ] DELETE
  - [ ] PUT

## SALA
  > Terá as informações de alunos e professor e provas aplicadas
  
###### ROTAS
  - [ ] GET
  - [ ] POST
  - [ ] PUT
  - [ ] DELETE

## SOCKET AULA
  > Será o sistema pricipal de aplicação de provas
  
  > Deverá da uma serie de informações sobre a prova aplicada como, % de acerto ate o momento, e tempo medio de cada aluno nas questões

###### EMIT
  - [ ] SINCRONIZAÇÃO
  - [ ] START
  - [ ] PAUSA
  - [ ] SET OFFLINE
 
