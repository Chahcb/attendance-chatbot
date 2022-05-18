# Chatbot pour la présence à la cantine

développé en python 3.9 et déployé sur heroku

### Installation

* installation de python (de préférence la version 3.9 pour éviter les erreurs d'encoding)
* installation des modules fastapi et uvicorn avec les commandes suivantes (pip ou pip3, ça dépend de votre version):
    * `pip install fastapi` ou `pip3 install fastapi`
    * `pip install "uvicorn[standard]"` ou `pip3 install "uvicorn[standard]"`
* lancer l'app avec la commande `uvicorn AttendanceChatbotController:app --reload`
* lancer les tests: `python -m unittest AttendanceChatbotTest.AttendanceTest`

### Informations sur le chatbot

* [Chatbot](https://attendance-chatbot.herokuapp.com/)
* [Documentation du Chatbot](https://attendance-chatbot.herokuapp.com/documentation)

### Liens utiles

* [Introduction à FastApi](https://dev.to/ericlecodeur/introduction-a-fastapi-python-5mf)
* [Documentation FastApi](https://fastapi.tiangolo.com/)
* [Tests unitaires en Python](https://docs.python.org/3/library/unittest.html)