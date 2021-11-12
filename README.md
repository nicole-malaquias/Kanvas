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

### <font color="purple"> POST </font> Create a user *****



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
​
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



### <font color="purple"> POST </font> sign in *****

```json
/api/login/
```

```json
{
    "username": "Facilitador Fabio",
    "password": "1234"
}
```
<font color="yellow"> _Response_ </font>
​

```json
{
  "token": "4a18f48640e97cadf32137e480be3ec8d0b230b8"
}
```



### <font color="purple"> POST </font> Create a course *****

```json
/api/courses/
```


```json
{
    "name": "Django Rest Framework"
}
```
<font color="yellow"> _Response_ </font>
​

```json
{
  "id": 3,
  "name": "Django Rest Framework",
  "users": []
}

```

### <font color="purple"> GET </font> List all courses and students *****

```json
/api/courses/
```

```json
[
  {
    "id": 1,
    "name": "Django 3.22",
    "users": [
      {
        "id": 17,
        "username": "Studente Joanne"
      }
    ]
  },
  {
    "id": 2,
    "name": "Node.JS 3.2.8",
    "users": []
  }
]
```


### <font color="purple"> GET </font> get course by id *****

```json
/api/courses/2/
```

```json
{
  "id": 2,
  "name": "Node.JS 3.2.8",
  "users": []
}
```


### <font color="purple"> PUT </font> Add student in course by id *****

```json
/api/courses/1/registrations/
```

```json
{
    "user_ids": [17]
}
```
<font color="yellow"> _Response_ </font>
​
```json
{
  "id": 1,
  "name": "Django 3.2",
  "users": [
    {
      "id": 17,
      "username": "Studente Rafael"
    }
  ]
}
```

### <font color="purple"> PUT </font> Change course  *****

```json
	/api/courses/<int:course_id>/
```

```json
{
    "name": "Django 3.2",
}
```
<font color="yellow"> _Response_ </font>
​
```json
{
  "id": 1,
  "name": "Django 3.2",
  "users": []
}
```

### <font color="purple"> DELETE </font> Delete course  *****

```json
	/api/courses/1/
```


### <font color="purple"> POST </font> Create a activity *****

```json
/api/activities/
```

```json
{
    "title": "Kenzie Club 1.5",
    "points": 10
}
```
<font color="yellow"> _Response_ </font>
​
```json
{
  "id": 4,
  "title": "Kenzie Club 1.5",
  "points": 10.0,
  "submissions": []
}
```

### <font color="purple"> GET </font> Get all activities and their submissions *****

```json
/api/activities/
```


```json
[
  {
    "id": 1,
    "title": "Kenzie Club 1.3",
    "points": 80.0,
    "submissions": [
      {
        "id": 1,
        "repo": "repositório do github 2",
        "user_id": 15,
        "grade": 8.0,
        "activity_id": 1
      }
    ]
  },
  {
    "id": 2,
    "title": "Kenzie Club 1.4",
    "points": 10.0,
    "submissions": []
  },
]
```

### <font color="purple"> PUT </font> Edit a specific activity  *****

```json
/api/activities/1/
```

```json
  {
    "title": "Kenzie Club 1.3",
  }
```
<font color="yellow"> _Response_ </font>
​
```json
  {
    "id": 1,
    "title": "Kenzie Club 1.3",
    "points": 80.0,
    "submissions": []
  },
```
### <font color="purple"> PUT </font>Make a submission activity  *****

```json
	/api/activities/<int:activity_id>/submissions/
```

```json
{
    "grade":10,
    "repo": "http://gitlab.com/kenzie_pet",
}
```

<font color="yellow"> _Response_ </font>
​
```json
	/api/activities/<int:activity_id>/submissions/
```

```json
{
    "id": 7,
    "grade": null,
    "repo": "http://gitlab.com/kenzie_pet",
    "user_id": 3,
    "activity_id": 1
}
      
```





### <font color="purple"> PUT </font> Change grade  *****

```json
	/api/submissions/1/
```

```json
  {
    "grade": 8,
  }
```
<font color="yellow"> _Response_ </font>


```json
{
  "id": 1,
  "repo": "http://gitlab.com/kenzie_pet",
  "user_id": 15,
  "grade": 8.0,
  "activity_id": 1
}
```



