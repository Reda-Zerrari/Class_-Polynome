# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 20:57:40 2021

@author: Razer Blade
"""

from monome import Monome

class Polynome:
    def __init__(self, tete=None):
        """
        constructeur permet d'initialiser l'objet de type Polynome       
        Attributs
        ----------
        tete : Monome

        Returns
        -------
        None.

        """
        self.tete = tete # est de type Monome
        
    def getTete(self):
        """
        retourne le monome tete
        Returns
        -------
        Monome

        """
        return self.tete
    
    def setTete(self, t):
        """
        permet de modifier le monome tete
        Parameters
        ----------
        t : Monome

        Returns
        -------
        Polynome

        """
        self.tete = t
        return self
    
    def est_vide(self):
        """
        permet de verifier si le polynome est vide ou non
        Returns
        -------
        bool
        Retourne True si le polynome est vide
        Retourne False sinon

        """
        return self.getTete() == None
    
    def localiser(self, m):
        """
        localiser où situer convenablement un monome de même degré que m dans le polynome courant.
        Parameters
        ----------
        m : Monome
            monome à situer dans le polynome appelant.
        Returns
        -------
        Monome.
        """
        p = self.getTete()
        while p :
            suivant = p.getSuivant()
            if suivant != None and suivant.getDeg() <= m.getDeg():
                return p
            p = p.getSuivant()
        return self
    
    def dernier(self):
        """
        retourner le dernier Monome du Polynome
        Returns
        -------
        p : Monome

        """
        p = self.getTete()
        while p.getSuivant() != None:
            p = p.getSuivant()
        return p
    
    def ajouter(self, m):
        """
        inserer un nouveau monome convenablement dans le polynome courant.
        Parameters
        ----------
        m : Monome
            monome à inserer dans le polynome appelant.  
        """
        x= self.localiser(m)  
        m.suivant , x.suivant = x.suivant , m
        
    
        
        
        
    
        