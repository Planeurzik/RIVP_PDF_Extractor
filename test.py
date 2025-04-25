import os
def resource_path(relative):
    return os.path.join(
        os.environ.get(
            "_MEIPASS2",
            os.path.abspath(".")
        ),
        relative
    )
print(resource_path(r'.\tess\tesseract.exe'))

import re

if __name__ =="__main__":
    text = """
CEPARI DIAG | Tél : 0147208899 | Dossier : 014201B0005_DPE_20230428 Page 1/14
Diagnostic de performance
énergétique (logement)
N°ADEME : 2375E2032917C
Etabli le : 19/06/2023
Valable jusqu’au : 18/06/2033
Ce document vous permet de savoir si votre logement est économe en énergie et préserve le climat. Il vous donne également des pistes pour
améliorer ses performances et réduire vos factures. Pour en savoir plus : https://www.ecologie.gouv.fr/diagnostic-performance-energetique-dpe
DPE réalisé à partir des données de l’immeuble
Adresse : 20 RUE du Docteur Magnan
75013 PARIS 13
Bat. 014201B0005, N° de lot: 014201H0025_DPE_20230427
Type de bien : Appartement
Année de construction : 2008
Surface habitable : 34,69 m²
Propriétaire : RIVP
Adresse : 13, Avenue de la Porte d'Italie 75621 Paris Cedex 13
Performance énergétique et climatique
Estimation des coûts annuels d’énergie du logement
Les coûts sont estimés en fonction des caractéristiques de votre logement et pour une utilisation standard sur 5 usages (chauffage, eau chaude sanitaire, climatisation,
éclairage, auxiliaires) voir p.3 pour voir les détails par poste.
entre 370 € et 550 € par an
Prix moyens des énergies indexés au 1er janvier 2021 (abonnements compris)
Informations diagnostiqueur
CEPARI DIAG
6 boulevard Flandrin
75116 PARIS
tel : 0147208899
Diagnostiqueur : JURAD
Email : contact@ceparidiag.com
N° de certification : B2C 0338
Organisme de certification : B.2.C
À l’attention du propriétaire du bien au moment de la réalisation du DPE : Dans le cadre du Règlement général sur la protection des données (RGPD), l’Ademe vous informe que vos données personnelles (Nom-Prénom-Adresse) sont stockées dans la base de
données de l’observatoire DPE à des fins de contrôles ou en cas de contestations ou de procédures judiciaires. Ces données sont stockées jusqu’à la date de fin de validité du DPE. Vous disposez d’un droit d’accès, de rectification, de portabilité, d’effacement ou
une limitation du traitement de ces données. Si vous souhaitez faire valoir votre droit, veuillez nous contacter à l’adresse mail indiquée à la page «Contacts» de l’Observatoire DPE (https://observatoire-dpe.ademe.fr/).
Comment réduire ma facture d’énergie ? Voir p. 3
Ce logement émet 983 kg de CO₂ par an,
soit l’équivalent de 5 096 km parcourus
en voiture.
Le niveau d’émissions dépend
principalement des types d’énergies
utilisées (bois, électricité, gaz, fioul, etc.)
Le niveau de consommation énergétique dépend de l’isolation du
logement et de la performance des équipements.
Pour l'améliorer, voir pages 4 à 6
CEPARI DIAG | Tél : 0147208899 | Dossier : 014201B0005_DPE_20230428 Page 7/14
DPE / ANNEXES p.7
Fiche technique du bâtiment
Cette fiche liste les caractéristiques techniques du bien diagnostiqué renseignées par le diagnostiqueur pour obtenir les résultats
présentés dans ce document. En cas de problème, contactez la personne ayant réalisé ce document ou l’organisme certificateur
qui l’a certifiée (diagnostiqueurs.din.developpement-durable.gouv.fr).
Le présent rapport est établi par une personne dont les compétences sont certifiées par :
B.2.C - 24 rue des Prés 67380 LINGOLSHEIM (détail sur www.info-certif.fr)
Référence du logiciel validé : LICIEL Diagnostics v4 [Moteur TribuEnergie: 1.4.25.1]
Référence du DPE : 014201B0005_DPE_20230428
Date de visite du bien : 26/04/2023
Invariant fiscal du logement : N/A
Référence de la parcelle cadastrale :
Méthode de calcul utilisée pour l’établissement du DPE : 3CL-DPE 2021
Numéro d’immatriculation de la copropriété : N/A
Justificatifs fournis pour établir le DPE :
Néant
Explications personnalisées sur les éléments pouvant amener à des différences entre les consommations estimées et les
consommations réelles :
Les consommations de ce DPE sont calculées pour des conditions d'usage fixées (on considère que les occupants les utilisent
suivant des conditions standard), et pour des conditions climatiques moyennes du lieu. Il peut donc apparaître des divergences
importantes entre les factures d'énergie que vous payez et la consommation conventionnelle pour plusieurs raisons : suivant la
rigueur de l'hiver ou le comportement réellement constaté des occupants, qui peuvent s'écarter fortement de celui choisi dans les
conditions standard et également les frais d'énergie qui font intervenir des valeurs qui varient sensiblement dans le temps. Ce DPE
utilise des valeurs qui reflètent les prix moyens des énergies que l'Observatoire de l'Énergie constate au niveau national et donc
peut s'écarter du prix de votre abonnement. De plus, ce DPE a été réalisé selon une modélisation 3CL (définie par arrêté) qui est
sujette à des modifications dans le temps qui peuvent également faire évoluer les résultats.
Généralités
Donnée d’entrée Origine de la donnée Valeur renseignée
Département Observé / mesuré 75 Paris
Altitude Donnée en ligne 59 m
Type de bien Observé / mesuré Immeuble Complet
Année de construction Estimé 2008
Surface habitable de l'immeuble Observé / mesuré 712 m²
Nombre de niveaux du logement Observé / mesuré -
Nombre de niveaux de l'immeuble Observé / mesuré 4
Hauteur moyenne sous plafond Observé / mesuré 2,5 m
Nb. de logements du bâtiment Observé / mesuré 14
Liste des logements visités Observé / mesuré
014201H0025_DPE_2023, 014201H0030_DPE_2023,
014201H0035_DPE_2023
Type de répartition du chauffage Observé / mesuré Système de chauffage collectif sans individualisation des frais
Type de répartition de l'eau chaude sanitaire Observé / mesuré Système d'ecs collectif
Menuiseries, systèmes de ventilation et chauffage
similaires sur tous les appartements Observé / mesuré Oui
Enveloppe
Donnée d’entrée Origine de la donnée Valeur renseignée
Mur 1 Sud
Surface du mur Observé / mesuré 149 m²
Type de local adjacent Observé / mesuré l'extérieur
Matériau mur Observé / mesuré Mur en béton banché
Epaisseur mur Observé / mesuré ≤ 20 cm
Isolation Observé / mesuré oui
Epaisseur isolant Observé / mesuré 10 cm
Mur 2 Est
Surface du mur Observé / mesuré 217 m²
Type de local adjacent Observé / mesuré l'extérieur
Matériau mur Observé / mesuré Mur en béton banché
Epaisseur mur Observé / mesuré ≤ 20 cm
Isolation Observé / mesuré oui
Epaisseur isolant Observé / mesuré 10 cm
Mur 3 Ouest Surface du mur Observé / mesuré 249 m²
émissions
166|23

    """

    res = re.findall(
                "Surface habitable de l\'immeuble (.*) mesuré (\d+,*\d+) m", text)
    print(res)
    print("hello")

