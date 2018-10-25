# Disponibilizando uma API REST de um modelo de análise de sentimentos

Esse pequeno exemplo mostra como fazer a análise de sentimentos usando ``Naive bayes`` do ``sklearn`` e disponibilizar o modelo em uma API REST. Bibliotecas usadas no projeto:

- [Sklearn](http://scikit-learn.org/stable/)
- [Flask](http://flask.pocoo.org/) - mini web framework
- [Connexion](https://github.com/zalando/connexion) - handles HTTP requests based on Swagger spec
- [Pickle](https://docs.python.org/3/library/pickle.html) - serializing and de-serializing objects

Para rodar, basta executar ``python app.py``. Para acessar a página do Swagger digite: ``localhost:5000/api/ui``. Resultados ``1 = Positivo`` e ``0 = Negativo``.

Para acessar o app no Heroku, acesse: https://marco-binary-class.herokuapp.com/api/ui/

Acessando a UI do Swagger, é possível ver o padrão de envio e recebimento das mensagens.
