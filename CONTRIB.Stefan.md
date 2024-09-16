# Propositions de structuration du projet

## Paramétrage (settings.py)
Pour un projet d'une telle envergure, je propose que les différentes configurations soient regroupées en fonction de leur catégporie. Par exemple, si une variable (constante) est exclusivement réservée au package `django-tenants`, il serait préférable les regrouper dans une section avec des commentaires bien explicites permettant de se retrouver plus tard si l'on reprend le projet un bon moment plus tard. Voici un exemple de ce dont je parle:

```python
#############################################################
#############################################################
#############################################################
#######                                             #########
#######                                             #########
#######                  ROOT CONFIGS               #########
#######                                             #########
#######                                             #########
#############################################################
#############################################################
#############################################################
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# All subdomains from the main domain are accepted. So accept everything (commentaire ajouté)
ALLOWED_HOSTS = ["*"]
...




#############################################################
#############################################################
#############################################################
#######                                             #########
#######                                             #########
#######       INSTALLED APPLICATIONS DEFINITION     #########
#######                                             #########
#######                                             #########
#############################################################
#############################################################
#############################################################
# Shared apps (means all apps declared in this section aren't tenant based apps)
SHARED_APPS = [...]

# Tenant's apps (all data/models from these apps are available only in the current tenant)
TENANT_APPS = [...]

# Loading project's apps. Django needs this to work properly.
INSTALLED_APPS = SHARED_APPS + [app for app in TENANT_APPS if app not in SHARED_APPS]
...



#############################################################
#############################################################
#############################################################
#######                                             #########
#######                                             #########
#######           3rd PARTY APPS CONFIGS            #########
##### (Means that coming configs are for 3rd        #########
#####            party apps. Not Django)            #########
#######                                             #########
#######                                             #########
#############################################################
#############################################################
#############################################################



#############################################################
#############################################################
########            REST FRAMEWORK CONFIGS       ############
#############################################################
#############################################################
REST_FRAMEWORK = {...}
...

```

Tu as sûrement compris là où je veux en venir, ainsi, on sait que chaque section n'est destinée qu'à un usage bien précis et surtout, on explique pourquoi on a besoin de telle ou telle config.


## Variables d'environnement
Tu as déjà opté pour des variables d'environnement au lieu de déclarer en dur les données sensibles dans le fichier de configuration. C'est déjà une très bonne idée. Je pourrais ajouter qu'il faudrait créer un fichier de configuration avec les variables (sans les valeurs) pour dire aux contributeurs quelles configurations sont requises pour lancer proprement ce projet.
J'ai mis des exemples dans cette branche à travers le fichier `.env-sample`. Je déclare les variables uniquement et donne des détails si possible afin que l'on sache quel type de valeurs est autorisé. Quiconque voudra donc lancer ce projet n'aura qu'à voir dans ce fichier et configurer son environnement en fonction des variables qui y sont.
À chaque nouvel ajout de variables d'environnement, il faut l'ajouter dans ce fichier et donner des détails possible. Les contributeurs n'auront qu'à y jeter un coup d'oeil et c'est bon.


## Middlewares & Context processors & Backends ou autres changements
Je préconise que les middlewares soit à l'intérieur du dossier principal du projet. Ici, dans notre cas, ça devrait être dans le dossier *Dreametrix_backend*. Après changement, il faudrait naturellement les chemins d'accès à ces différents fichiers (en tenant compte de la nouvelle structure des dossiers). Ou peut-être, s'il y a des middlewares spécifiques à chaque application, tu pourrais créer un fichier `middlewares.py` dans chaque application (chose que je conseille pas; il est mieux de centraliser les middlewares dans un seul et même fichier). De mêmes que les services (si besoin) qui serviront à envoyer des mails ou des SMS.


## Structuration des models et des applications
Pour un souci lisibilité et pour suivre le concept `DRY: Don't Repeat Yourself`, il vaudrait mieux changer la structure des models ainsi que des managers.
Voici donc ce que je propose:
<ul>
    <li>Une application centrale (shared app) <b>schools</b> pour les models  <i>Tenant</i> & <i>Domain</i> </li>
    <li>Une application interne (tenant app) <b>students</b> pour les models en rapport avec les élèves </li>
    <li>Une application interne (tenant app) <b>teachers</b> pour les models en rapport avec les enseignants </li>
    <li>Une application interne (tenant app) <b>courses</b> pour les models en rapport avec les cours </li>
    <li>...</li>
</ul>
Tu auras compris là où je veux en venir, il vaudrait structurer les applications et les models comme il faut. Chaque application devra être plus ou moins autonome facilitant ainsi une quelconque collaboration. On pourrait même demander à un développeur annexe de développer tel ou tel truc et nous, on ne récupère que l'application parce qu'elle serait autonome.

En ce concerner les managers, il devrait y avoir un fichier dans chaque application contenant les managers de tous les models de ladite application. Example:
```python
# dans teachers/models.py
from teachers.managers import TeacherManager
class Teacher(...):
    ...
    objects = TeacherManager()


# dans teachers/managers.py
class TeacherManager(...):
    pass
```


## Notes
D'autres détails suivront plus tard. C'est ce que j'ai pu notifier de notable. Quant au contenu et l'algo, je ne vais pas me prononcer là-dessus pour l'instant. Il me faut regarder de plus près avant de faire des suggestions et/ou remarques.
