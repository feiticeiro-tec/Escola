# Escola

Projeto para homologação de **plugins** [Fet-UI](https://github.com/feiticeiro-tec/fet-ui).

- [MaskForm](https://github.com/feiticeiro-tec/fet-ui/tree/master/Scripts/MaskForm) *- Mascara aplicada em type*  
- [ValidateForm](https://github.com/feiticeiro-tec/fet-ui/tree/master/Scripts/ValidateForm) *- Validação de formulario por type(PreventDefault)*
- [FeedbackForm](https://github.com/feiticeiro-tec/fet-ui/tree/master/Scripts/FeedbackForm) *- Detaque de mensagem abaixo do input*

Além da homologação, tambem será testado um method de **aceleração de desenvolvimento**.  
O method é uma total presunção minha e sem conhecimento previo da existencia de ferramenta ou algo do tipo.  

## Súmario
- [*Usuario*](https://github.com/feiticeiro-tec/Escola#usu%C3%A1rio)
- [*Grupo*](https://github.com/feiticeiro-tec/Escola#grupo)
- [*Teste*](https://github.com/feiticeiro-tec/Escola#teste)
- [*Prova*](https://github.com/feiticeiro-tec/Escola#prova)
- [*Sala*](https://github.com/feiticeiro-tec/Escola#sala)
- [*Socket*](https://github.com/feiticeiro-tec/Escola#socket-aula)
- [*Grupo Alvo*](https://github.com/feiticeiro-tec/Escola#grupo-alvo)
- [*Noticia*](https://github.com/feiticeiro-tec/Escola#not%C3%ADcia)
- [*Check-in*](https://github.com/feiticeiro-tec/Escola#check---in)

## *USUÁRIO*

> Um **usuario** pertence a um grupo de *ADM*, *DIRETOR*, *PROFESSOR* OU *ALUNO*.  
> O usuario é **obrigado** a preencher o cadastro.

###### **ROTAS**

- [ ] GET
- [ ] Registro
- [ ] Login
- [ ] Recuperação de conta
- [ ] Edição de perfil

## *GRUPO*

> Haverá **4 Grupos**, ADM, DIRETOR, PROFESSOR e ALUNO.
> **ADM** - *Será o responsavel pelo sistema e terá total liberdade.*  
> **DIRETOR** - *Será responsavel por uma ou mais escolas e terá total liberdade dentro dela.*  
> **PROFESSOR** - *Será responsavel por uma ou mais salas de aula e tera total liberdade dentro dela.*  
> **ALUNO** - *Sera um membro de uma ou mais escolas e fará parte de uma ou mais salas de aula.*

###### **ROTAS**

- [ ] GET
- [ ] POST
- [ ] PUT 
- [ ] DELETE

## *TESTE*

> Será os modelos e "*provas*" aplicadas.  
> Tera questoes de **multipla** escolhas ou de **escrita**.  
> ESCRITA - *As questoes de escrita esperará a avaliação do professor para concluir a "prova".*  

###### **ROTAS**

- [ ] CLOSE
- [ ] GET
- [ ] POST
- [ ] PUT
- [ ] DELETE

## *PROVA*

> Terá as informações do "*teste*" aplicado justo com as informações do alunos
  
###### **ROTAS**

- [ ] GET
- [ ] POST
- [ ] DELETE
- [ ] PUT

## *SALA*

> Terá as informações de alunos e professor e provas aplicadas
  
###### **ROTAS**

- [ ] GET
- [ ] POST
- [ ] PUT
- [ ] DELETE

## *SOCKET AULA*

> Será o sistema pricipal de aplicação de provas.  
> Deverá da uma serie de **informações** sobre a prova aplicada como, **%** de acerto ate o momento, e **tempo medio** de cada aluno nas questões

###### EMIT

- [ ] SINCRONIZAÇÃO
- [ ] START
- [ ] PAUSA
- [ ] SET OFFLINE

## *GRUPO ALVO*

> Será os grupos de **exibição** das noticias.  
> Terá os grupos basicos porém tambem será possivel criar grupos expecificos de forma **dinamica**.  
> Os grupos base são imutaveis.  

- [ ] GET
- [ ] POST
- [ ] PUT
- [ ] DELETE

## *NOTÍCIA*

> A **noticia** terá um grupo de exibição podendo ser **filtrada** para cada tipo.  
> Texto Rico.

- [ ] GET
- [ ] POST
- [ ] PUT
- [ ] DELETE

## *CHECK - IN*
> Analisar melhor forma de fazer check-in e check-out