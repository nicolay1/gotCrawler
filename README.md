# Context

Ce projet est basé sur la proposition de créer un notificateur de série. Un processus en V à été utilisé lors de sa création, de par une volonté que tout le monde touche à toute les parties du code. Nous avons essayé de respecter PEP 8 et typer au maximum le code afin d'améliorer et l'autocomplete durant le dévelopement.

Il a au départ été défini un UML [https://ibb.co/cebO0V](https://ibb.co/cebO0V), cet UML a été utilisé comme base du model M(V)C que nous avons tenté d'implémenter. 

Taches effectuées dans l'ordre : 
- Modèles et la base de donnée en parallèle : `src/db`, `src/models`
- Contrôlleurs : `src/controllers`
- Routes appelant les contrôlleurs : `src/ressources` + `src/app.py`
- Front : `front`

Cette méthode non agile a eu pour effet de ne pas nous rendre compte du travail restant à faire (notamment pour le front), ce qui nous a obligé à finir rapidement le projet.

# Installation du Notificateur de Série
Prérequis : 
Python3, npm

Dans le dossier principal :

* `./install.sh` => installe les modules nécessaires et la base de données
* `./launch.sh` => lance le serveur sur localhost:5000

Passer dans le dossier du front : `cd front`
 * `npm install` => installation de l'ensemble des packages nécessaires 
 * `npm run dev ` => lance l'application sur [http://localhost:8080/](http://localhost:8080/)

User par defaut :

- nicolas/mymdp
- amelie/mymdp
- rachel/mymdp

# Fonctionnement

On peut voir ce projet comme un wrapper de l'application TMDB : https://www.themoviedb.org/.

L'application permet ainsi de naviguer au travers des différentes séries de TMDB et les mettre en favori. Une fois qu'elles sont en favori, l'utilisateur reçoit des notifications lorsqu'un nouveau prochain épisode arrive.

L'idée a été d'une part de généraliser les données reçues par TMDB en les utilisant pour générer nos propres objets et d'autre part de minimiser les call API sur TMDB.

# Points d'intention

## Piliers de la POOA

### Encapsulation

Surtout présente nos models : `src/models`

- Utilisation au maximum d'attributs privés.
- Utilisations de class pour définir nos controlleurs qui ne sont pourtant qu'une librairie de fonctions.

### Héritage

Un peu plus compliqué dans le cadre de ce projet étant donné que son utilisation ne nous a pas semblé évidente dans le cadre de ce projet.

- Actor et Author heritent de Person (dans `src/models`)
- ApiHelperTMDB implémente ApiHelper (dans `src/api_helper`), ce dernier étant une classe que nous avons voulu abstraite. Cet héritage était un peu forcé mais permetai d'avoir plusieurs plusieurs sources d'API.
- les erreurs custom héritent de GCErrorException (dans `src/errors`)

### Polymorphisme

Un peu compliqué à utiliser aussi mais à la base de l'utilisation de classe abstraites en python.

Reste utilisé par NotificationManager vu qu'il hérite de Thread et que la method \_\_init\_\_ semble être un polymorphisme du \_\_init\_\_ de Thread (vu que ce dernier est appelé.)

## Gestion d'erreur

Les erreurs de fonctionnalités détecté dans les routes (utilisateur existant déjà lors de la création, recherche d'une série qui n'existe pas...), sont décrite par le model `src/errors` dans le \_\_init\_\_ de ce dernier.

La détection de l'errer peut être vu au niveau des routes `src/ressources`.

*Une classe par erreur aurait pu être utilisée mais le manque de temps a conduit à cette solution et à l'heritage utilisé*

## Thread

Le thread s'occuper de gérer l'update des notifications tout en essayer de se limiter aux quotas. L'idée est de maximiser le temps entre chaque mise à jour tout en s'accordant une fréquence de mise à jour raisonnable. Il se trouve dans `src/notification_manager`
