'''
Created on 1 janv. 2019

@author: rachid
'''
import datetime

class Personne(object):
    '''
    Une personne.
    '''


    def __init__(self, nom = "", prenom = "", dateNaissance = datetime.date.today()):
        '''
        Constructor
        '''
        self.nom = nom
        self.prenom = prenom
        self.dateNaissance = dateNaissance
    
    def obtenirAge(self, dateReference = datetime.date.today()):
        jours = dateReference - self.dateNaissance
        resultat = jours.days / 365
        return round(resultat, 1)