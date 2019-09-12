# Python Developer Test - Backend

A ong doghouse precisa de um backend para o seu ecommerce. A ong quer encontrar pessoas que desejam adotar cachorros e gatos e as pessoas precisam visualizar os gatos e os cachorros que estão esperando adoção.

O desenvolvedor deve construir o backend que suporte a operação da ONG.

### Instruções   

* Criar virtual enviroment e ativá-lo:   
`$ python -m venv env`   
`$ source env/Scripts/activate`   

* Instalar dependências:   
`$ pip install -r requirements.txt`   

* Criar usuário administrador:   
`$ cd src`   
`$ python manage.py createsuperuser --email admin@example.com --username admin`   

* Rodar aplicação:   
`$ python -m manage.py runserver`   

### Testar   

* Para a interface admin, digitar no navegador:   
`127.0.0.1:8000/admin/`   

* Para a API (lista todos pets - GET, POST):   
`127.0.0.1:8000/api/v1/pets`   

* Ou para listar um pet específico (PUT, DELETE):   
`127.0.0.1:8000/api/v1/pets/<id>`   

* Rodar testes automáticos (tests.py):   
`$ python -m manage.py test`   

### License   
[MIT](https://choosealicense.com/licenses/mit/)
