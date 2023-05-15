import datetime

from pathlib import Path
import json
import jsonpickle
jsonpickle

# Ajout au projet de la classe "Personne"
class Personne:
    def __init__(self, nom: str, prenom: str):
        self.setnom(nom)
        self.setprenom(prenom)

    # Méthodes d'accès get/set pour "nom"
    def getnom(self) -> str:
        return self._nom

    def setnom(self, value: str) -> None:
        self._nom = value

    # Méthodes d'accès get/set pour "prenom"
    def getprenom(self) -> str:
        return self._prenom

    def setprenom(self, value: str) -> None:
        self._prenom = value

    # Méthode "__str__" qui retourne les propriétés en format string
    def __str__(self) -> str:
        return f"Nom : {self.getnom}\t Prenom : {self.getprenom}"


# Ajout au projet de la classe "Employe" qui hérite de la classe "Personne"
class Employe(Personne):
    def __init__(self, code: int, fonction: str, nom: str, prenom: str):
        # Méthode "super" pour effectuer l'héritage de la classe "Personne"
        super().__init__(nom, prenom)
        self.setcode(code)
        self.setfonction(fonction)

    # Méthodes d'accès get/set pour "code"
    def getcode(self) -> int:
        return self._code

    def setcode(self, value: int) -> None:
        self._code = value

    # Méthodes d'accès pour "fonction"
    def getfonction(self) -> str:
        return self._fonction

    def setfonction(self, value: str) -> None:
        self._fonction = value

    # Méthode "__str__" qui retourne les propriétés en format string
    def __str__(self) -> str:
        return f"Code : {self.getcode}\t Fonction : {self.getfonction}\t Nom : {self.getnom}\t Prenom : {self.getprenom}"


# Ajout au projet de la classe "Client"
class Client(Personne):
    def __init__(self, telephone: str, courriel: str, nom: str, prenom: str):
        # Méthode "super" pour effectuer l'héritage de la classe "Personne
        super().__init__(nom, prenom)
        self.settelephone(telephone)
        self.setcourriel(courriel)

    # Méthodes d'accès get/set pour "telephone"
    def gettelephone(self) -> str:
        return self._telephone

    def settelephone(self, value: str) -> None:
        self._telephone = value

    # Méthodes d'accès get/set pour "courriel"
    def getcourriel(self) -> str:
        return self._courriel

    def setcourriel(self, value: str) -> None:
        self._courriel = value

    # Méthode "__str__" qui retourne les propriétés en format string
    def __str__(self) -> str:
        return f"Telephone : {self.gettelephone}\t Client : {self.getcourriel}\t Nom : {self.getnom}\t Prenom : {self.getprenom}"


# Ajout au projet de la classe "Reparation"
class Reparation:
    def __init__(self, code: int, description: str, montant: float, datereparation: datetime, codeemploye: int):
        self.setcode(code)
        self.setdescription(description)
        self.setmontant(montant)
        self.setdatereparation(datereparation)
        self.setcodeemploye(codeemploye)

    # Méthodes d'accès get/set pour "code"
    def getcode(self) -> int:
        return self._code

    def setcode(self, value: int) -> None:
        self._code = value

    # Méthodes d'accès get/set pour "description"
    def getdescription(self) -> str:
        return self._description

    def setdescription(self, value: str) -> None:
        self._description = value

    # Méthodes d'accès pour "montant"
    def getmontant(self) -> float:
        return self._montant

    def setmontant(self, value: float) -> None:
        self._montant = value

    # Méthodes d'accès get/set pour "datereparation"
    def getdatereparation(self) -> datetime:
        return self._datereparation

    def setdatereparation(self, value: datetime):
        self._datereparation = value

    # Méthodes d'accès get/set pour "codeemploye"
    def getcodeemploye(self) -> int:
        return self._codeemploye

    def setcodeemploye(self, value: int) -> None:
        self._codeemploye = value


# Ajout au projet de la classe "Voiture"
class Voiture:
    def __init__(self, numeroplaque: str, marque: str, modele: str, couleur: str, annee: int, proprietaire: Client,
                 reparations: list[Reparation]):
        self.setnumeroplaque(numeroplaque)
        self.setmarque(marque)
        self.setmodele(modele)
        self.setcouleur(couleur)
        self.setannee(annee)
        self.setproprietaire(proprietaire)
        self.setreparations(reparations)

    # Méthodes d'accès get/set pour "numeroplaque"
    def getnumeroplaque(self) -> str:
        return self._numeroplaque

    def setnumeroplaque(self, value: str) -> None:
        self._numeroplaque = value

    # Méthodes d'accès get/set pour "marque"
    def getmarque(self) -> str:
        return self._marque

    def setmarque(self, value: str) -> None:
        self._marque = value

    # Méthodes d'accès get/set pour "modele"
    def getmodele(self) -> str:
        return self._modele

    def setmodele(self, value: str) -> None:
        self._modele = value

    # Méthodes d'accès get/set pour "couleur"
    def getcouleur(self) -> str:
        return self._couleur

    def setcouleur(self, value: str) -> None:
        self._couleur = value

    # Méthodes d'accès get/set pour "annee"
    def getannee(self) -> int:
        return self._annee

    def setannee(self, value: int) -> None:
        self._annee = value

    # Méthodes d'accès get/set pour "proprietaire"
    def getproprietaire(self) -> Client:
        return self._proprietaire

    def setproprietaire(self, value: Client) -> None:
        self._proprietaire = value

    # Méthodes d'accès get/set pour "reparations"
    def getreparations(self) -> list[Reparation]:
        return self._reparations

    def setreparations(self, value: list[Reparation]) -> None:
        self._reparations = value

        # Méthode nommée "ajouterreparation"
        self.reparations = {}

    def ajouterreparation(self, element: Reparation) -> None:
        self.reparations[element] = {}


# Ajout au projet de la classe "Garage"
class Garage:
    def __init__(self, nom: str, adresse: str, telephone: str, employes: list[Employe], voitures: list[Voiture]):
        self.setnom(nom)
        self.setadresse(adresse)
        self.settelephone(telephone)
        self.setemployes(employes)
        self.setvoitures(voitures)

    # Méthodes d'accès get/set pour "nom"
    def getnom(self) -> str:
        return self._nom

    def setnom(self, value: str) -> None:
        self._nom = value

    # Méthodes d'accès get/set pour "adresse"
    def getadresse(self) -> str:
        return self._adresse

    def setadresse(self, value: str) -> None:
        self._adresse = value

    # Méthodes d'accès get/set pour "telephone"
    def gettelephone(self) -> str:
        return self._telephone

    def settelephone(self, value: str) -> None:
        self._telephone = value

    # Méthodes d'accès get/set pour "employes"
    def getemployes(self) -> list[Employe]:
        return self._employes

    def setemployes(self, value: list[Employe]) -> {}:
        self._employes = value

    # Méthodes d'accès get/set pour "voitures"
    def getvoitures(self) -> list[Voiture]:
        return self._voitures

    def setvoitures(self, value: list[Voiture]) -> {}:
        self._voitures = value


# Méthode de classe pour la sérialisation

### Je n'ai pas réussi à coder correctement mes sérialiser/désérialiser, pourrais-je avoir quelques points d'effort ? ###

def serialisergarage(cls, element: Garage, fichier: str) -> None:
    @property
    def filename(self) -> str:
        return self.__filename

    @filename.setter
    def filename(self, value: str):
        self.__filename = value

    # Ouvrir le fichier (création du stream)
    path: Path = Path(cls.fichier)
    if path.is_file():
        stream = path.open('w')
        # Serialiser la valeur vers le fichier
        json.dump(element, stream, indent=4, separators=(',', ':'), default=Garage.converttodict)
        # Fermer le stream
        stream.flush()
        stream.close()
    else:
        raise Exception('fichier incorrect')


def deserialisergarage(cls, fichier: str) -> Garage:
    # Ouvrir le fichier (creer le stream)
    path: Path = Path(cls.filename)
    if path.exists():
        stream = path.open('r')
        # deserialiser le fichier vers un objet liste de compte
        listeemploye: list[Employe] = json.load(stream, object_hook=Garage.createfromdict)

        # fermer le stream
        stream.close()
        # retourner le resultat
        return listeemploye
    else:
        raise Exception('fichier inexistant')


def ajoutervoiture(self, element: Voiture) -> None:
    self.voitures[element] = {}

def getvoiture(self, numvoiture: str) -> Voiture:
    pass

def ajouterreparation(self, numvoiture: str, reparation: Reparation) -> None:
    self.objet[Reparation] = {}

def getreparation(self, numvoiture: str) -> list[Reparation]:
    return self.numvoiture
