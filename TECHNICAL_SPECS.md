# Spécifications Techniques : Moteurs Algorithmiques BIB
## Système d'Exploitation Industriel du Bénin

Ce document détaille la logique mathématique et les principes d'ingénierie implémentés dans l'application **Bénin Industrial Backbone (BIB)**. Le système est conçu pour répondre aux standards de haute performance de la GDIZ et du Port Autonome de Cotonou.

---

## 1. Moteur SCM & Inventaire (Normes MIT CTL)
Le module WMS (Warehouse Management System) abandonne les modèles déterministes pour une approche stochastique, indispensable pour absorber la volatilité des délais de livraison au Bénin.

### A. Gestion de l'Incertitude (Stock de Sécurité)
Le calcul du Stock de Sécurité ($SS$) dans le fichier `App.py` (via `BIBCoreEngine.wms_stochastic_metrics`) modélise l'incertitude combinée de la demande et du délai :

$$SS = k \cdot \sqrt{(L_{avg} \cdot \sigma_D^2) + (D_{avg}^2 \cdot \sigma_L^2)}$$

* **$k$ (Facteur de service) :** Défini à 1.65 pour garantir un niveau de service de 95% (Cycle Service Level).
* **$\sigma_L$ (Variabilité du Lead-time) :** Ce paramètre critique permet d'ajuster dynamiquement le stock en fonction des retards constatés aux frontières ou au port.

### B. Optimisation de Commande (EOQ)
La quantité économique de commande est calculée selon la formule de Wilson, optimisant l'arbitrage entre le coût de passation et le coût de possession ($H$) :

$$EOQ = \sqrt{\frac{2 \cdot D \cdot S}{H}}$$

---

## 2. Moteur de Production & Maintenance (Siemens Xcelerator)
L'intelligence de production repose sur le monitoring en temps réel du TRS et un algorithme de scoring pour la maintenance prédictive.

### A. Calcul du TRS (OEE)
Le taux de rendement synthétique est le produit de trois vecteurs d'efficacité :
* **Disponibilité :** Temps de marche / Temps requis.
* **Performance :** Vitesse réelle / Vitesse nominale.
* **Qualité :** Produits conformes / Total produit.

### B. Health Score & Maintenance Prédictive
Le score de santé de la machine est une fonction de risque pondérée :
$$Score = 1 - (w_t \cdot R_t + w_v \cdot R_v + w_u \cdot R_u)$$

Où :
* $w_t=0.4$ (Température), $w_v=0.4$ (Vibrations Hz), $w_u=0.2$ (Usage/Heures).
* Un score inférieur à **35%** déclenche une alerte critique et une réservation automatique des pièces de rechange dans le module WMS.

---

## 3. Moteur Logistique & CPK (RNIE Tracking)
La maîtrise des coûts de transport sur les axes RNIE repose sur la décomposition analytique du coût au kilomètre (CPK).

### A. Coût de Revient Réel
Le modèle de calcul intègre les charges variables spécifiques au corridor béninois :
$$Total = \sum (Consommation \cdot Prix_{Gasoil}) + Péages + Frais_{Route} + Charges_{Fixes}$$

### B. Algorithme de Validation Docking
Pour prévenir les pertes de vrac, le système compare les masses départ/arrivée avec un seuil de tolérance technique de **0.5%** ($T$) :
$$\text{Status} = \begin{cases} \text{Conforme} & \text{si } \frac{|M_d - M_a|}{M_d} \le T \\ \text{Litige} & \text{sinon} \end{cases}$$

---

## 4. Architecture de Données & Conformité
* **Single Source of Truth (SSOT) :** Toute donnée saisie dans le module ACHAT impacte immédiatement les moteurs WMS et PRODUCTION.
* **Edge-Ready :** Logiciel conçu pour la synchronisation MQTT, permettant un fonctionnement offline sur site industriel avec synchronisation dès retour du réseau.
* **Conformité APDP :** Chiffrement des données sensibles et respect de la législation béninoise sur la protection des données personnelles.

---
**Auteur :** CRINOT Elvis C. Kafui  
**Version :** 1.0.0 (Production Ready)  
**Standard :** Enterprise Grade Python (PEP8)
