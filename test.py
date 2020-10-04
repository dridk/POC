from PySide2.QtWidgets import *
from PySide2.QtCore import *
import pandas as pd
from math import pi
import sys


fichier_coupe = pd.read_csv("parametre_coupe.csv", sep=";") # 

app = QApplication(sys.argv)

w = QWidget()  					# création d'une fenêtre
w.isMaximized() True

layout = QVBoxLayout()  		# création conteneur de widgets

resultat = QLabel()				# création zone de texte
l_matiere = QLabel()
l_diametre = QLabel()
l_revetement = QLabel()
l_nb_dent = QLabel()

box_matiere = QComboBox()  		# création menu déroulant
box_revetement = QComboBox()
box_diametre = QComboBox()
box_dent = QComboBox()

box_matiere.addItems(fichier_coupe["matiere"].unique())  # Ajoute à la liste déroulante les occurance uniques de la colonne matière
box_revetement.addItems(fichier_coupe["revetement"].unique())  # Ajoute à la liste déroulante les occurance uniques de la colonne revetement
box_diametre.addItems(fichier_coupe["diametre"].astype(str).unique())
box_dent.addItems(fichier_coupe["nb_dent"].astype(str).unique())

btn = QPushButton("Calculer")  			# crétaion bouton

layout.addWidget(l_matiere)			# Ajout du menu déroulant à la fenêtre
layout.addWidget(box_matiere)			# Ajout du menu déroulant à la fenêtre
layout.addWidget(l_revetement)
layout.addWidget(box_revetement)
layout.addWidget(l_diametre)
layout.addWidget(box_diametre)
layout.addWidget(l_nb_dent)
layout.addWidget(box_dent)
layout.addStretch()  					# Ajout séparateur
layout.addWidget(resultat)  				# Ajout zone texte à la fenêtre
layout.addStretch()  
layout.addWidget(btn)

l_matiere.setText(f"Matière")  
l_revetement.setText(f"Revêtement")  
l_diametre.setText(f"Diamètre")  
l_nb_dent.setText(f"Nombre de dents")  

w.setLayout(layout)  					# Ajouter layout à la fentre



def calcul():							# Création d'une fonction

	diam = int(box_diametre.currentText()) # Récupération de la valeur du menu déroulant
	mat = box_matiere.currentText()
	rev = box_revetement.currentText()
	nb_d = box_dent.currentText()
	
	filtre = fichier_coupe.query("matiere == @mat & diametre == @diam & revetement == @rev & nb_dent == @nb_d") # isolé ligne en fonction de paramètre
	vc = filtre["vitesse_coupe"].iloc[0]	# Récupération de la première donnée de la colonne spécifiée
	fz = filtre["avance_dent"].iloc[0]
	n_d = filtre["nb_dent"].iloc[0]

	vitesse_rotation = round((1000 * vc) / (pi * diam))
	if vitesse_rotation > 25000:
		vitesse_rotation = 25000 
	vitesse_avance_outil = round(vitesse_rotation * fz * n_d) # round == arrondi
	resultat.setText(f"La vitesse de rotation sera de {vitesse_rotation} tr/min \nLa vitesse d'avance de l'outil sera de {vitesse_avance_outil} mm/min")
	# afficher le texte dans la zone de texte resultat créée précedemment
	
	return vitesse_rotation, vitesse_avance_outil

btn.clicked.connect(calcul)

w.show()  # affichage fenetre

app.exec_()