
# Résultats
* When adding a new product, the user should not have to enter a product name

J'ai supprimé de la liste 'name'.


* When adding a new product, the user should only be able to enter a 13 digits reference in the Gtin field

J'ai ajouté un fichier 'validator.py' pour écrire une fonction qui renvoit une erreur si le Gtin n'a pas exactement 13 digits. 

* When adding a new product, the site should send a request to OpenFoodFact to gather the product name and an image url. The api documentation can be found here: https://world.openfoodfacts.org/data

Pour cette partie j'ai crée une fonction pour faire un get request avec l'URL complétée par le numéro du code barre. J'ai aussi crée deux fonctions pour extraire le nom et l'url de la photo du fichier json. Il y a sûrement une manière plus 'jolie' d'écrire ces fonctions mais je n'ai pas réussi à trouver de librairies ou fonctions qui me permettraient de faire ceci.

* On the home page, in the list of products, the photo from Open Food Facts, along with the name, should be displayed

J'ai réussi à afficher le nom mais pas la photo. J'ai essayé d'ajouter l'url comme élement de la classe Inventory (url_photo = models.TextField(default=None)) mais j'ai eu un bug au niveau du fichier index.html que je n'ai pas su résoudre dans le temps imparti.
