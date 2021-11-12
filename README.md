## <font size="7">**Kanvas**</font>

### Features

- [x] Cadastro de usuário
- [x] Cadastro de Instrutor
- [x] Cadastro de Facilitador
- [x] Faz a autenticação do usuário
- [x] Cria um curso
- [x] Lista os cursos e os alunos matriculados 
- [x] Retorna o curso com o id informado
- [x] Vincula os alunos ao curso
- [x] Cria uma nova atividade 
- [x] Lista todas as atividades com suas respectivas submissões
- [x] Editando uma atividade
- [x] Faz a submissão de uma atividade
- [x] Altera a nota de uma submissão
- [x] Lista as submissões. 

## <font size="6">Routes</font>

### <font color="purple"> POST </font> Sign up *****


```json
/api/accounts/
```

```json
{
    "username": "Instrutor Carlos",
    "password": "1234",
    "is_superuser": true,
    "is_staff": true
}
```

<font color="yellow"> _Response_ </font>
​
```json
 

{
    "id":1,
    "username": "Instrutor Carlos",
    "is_superuser": true,
    "is_staff": true
}
```

### <font color="purple"> POST </font> Sign in *****


```json
/api/accounts/
```

```json
{
    "username": "Instrutor Carlos",
    "password": "1234",
}
```

<font color="yellow"> _Response_ </font>
​
```json
{
  "token": "24ddba949356013921cee84e957897d5390eb2b2"
}
```



### <font color="purple"> POST </font> Create a Course *****


```json
/api/accounts/
```

```json
{
    "name": "Front-end",
}
```

