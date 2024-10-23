from django.db import models

# Create your models here.
class Alcool():

    def __init__(self, nom=None, degre=None, quantite= None) -> None:
        self._nom = nom
        self._degre = degre
        self._quantite = quantite
    
    def __str__(self) -> str:
        return f"{self._nom} - {self._degre}°"
    
    def mix(self, alcool, dosage):
        self._degre = (self._degre + alcool._degre * dosage) / (1 + dosage)

    def getDegre(self):
        return self._degre
    
    def setDegre(self, degre):
        self._degre = degre

    def getNom(self):
        return self._nom
    
    def setNom(self, nom):
        self._nom = nom

class Humain():

    def __init__(self, nom=None, taille=None, masse=None, sexe=None, age= None) -> None:
        self._alcoolemie = 0
        self._nom = nom
        self._taille = taille
        self._masse = None
        self._sexe = None
        self._age = None
        self._imc = self.setIMC()

    def __str__(self) -> str:
        return f"{self._nom} - {self._masse}kg - {self._taille}m"
    
    def setIMC(self):
        self._imc = self._masse / self._taille ** 2

    def picole(self, alcool: Alcool, quantite=None):
        if quantite is None:
            quantite = alcool._quantite
        self._alcoolemie += alcool._degre #TODO trouver formule qtté