# BIB - Benin Industrial Backbone
### Industrial Operating System for Benin (GDIZ, PAC, Agro-industry)

**BIB** est un système d'exploitation industriel de pointe conçu pour catalyser la souveraineté économique du Bénin. Il unifie la gestion de la chaîne d'approvisionnement (SCM), le pilotage de la production et l'optimisation logistique sur un socle technologique unique, robuste et scalable.

---

## 1. Vision et Objectifs
Le projet BIB vise à transformer les opérations industrielles locales en intégrant une intelligence de classe mondiale pour dominer les secteurs clés du pays.

### Focus Sectoriel
* **Transformation de la noix de cajou & de l'ananas** : Optimisation des rendements et gestion de la péremption.
* **Industrie textile (Coton)** : Traçabilité end-to-end du champ à l'exportation.
* **Zones Stratégiques** : GDIZ (Glo-Djigbé), Port Autonome de Cotonou (PAC).

---

## 2. Architecture Technique & Standards
Le système repose sur une intégration multimodale de standards globaux :
* **SCM (MIT Standards)** : Modèles stochastiques pour la gestion des stocks (SS, EOQ, ROP) intégrant la variabilité réelle des délais de livraison au Bénin.
* **ERP (SAP Paradigms)** : Structure de données alignée sur le principe de "Single Source of Truth" (SSOT) pour une scalabilité financière totale.
* **Industrial IoT (Siemens Xcelerator)** : Interopérabilité via protocole OPC-UA et monitoring du TRS/OEE pour une maintenance prédictive.

---

## 3. Structure des Modules
1. **Interface ACHAT (Smart-Negotiator)** : IA de négociation (ZOPA/PCO) calculant le Landed Cost en temps réel (TEC CEDEAO, Incoterms 2020, gestion de devises NGN/CFA).
2. **Interface WMS (Master Inventory Engine)** : Gestion de 400+ SKU avec calcul du Stock de Sécurité face à l'incertitude logistique.
3. **Interface TMS & DOCKING (RNIE Tracking)** : Optimisation du coût au kilomètre (CPK) sur les axes nationaux et détection d'anomalies de pesée (Tolérance 0.5%).
4. **Interface PRODUCTION (Atelier Prédictif)** : Diagnostic santé machine (Health Score) et optimisation énergétique (SBEE).
5. **Interface X-LINK** : Jumeau numérique et connectivité universelle des automates (PLC).

---

## 4. Stack Technologique
* **Language** : Python 3.10+ (PEP8, Typage statique)
* **Framework UI** : Streamlit (Fiori-style UX, Mobile-Ready)
* **Intelligence Artificielle** : NumPy, Scikit-learn (Régression, Random Forest pour la maintenance)
* **Infrastructure** : Edge Computing Ready / Cloud-Native
* **Conformité** : Respect strict de la loi APDP (Bénin)

---

## 5. Guide d'Installation

### Prérequis
Assurez-vous d'avoir Python 3.10+ installé.

### Installation
```bash
# 1. Cloner le dépôt
git clone [https://github.com/votre-username/benin-industrial-backbone.git](https://github.com/votre-username/benin-industrial-backbone.git)
cd benin-industrial-backbone

# 2. Installer les dépendances (Versions de production)
pip install -r requirements.txt

# 3. Lancer l'application industrielle
streamlit run App.py
