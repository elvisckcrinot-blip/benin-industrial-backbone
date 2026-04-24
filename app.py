"""
PROJECT: BIB - Benin Industrial Backbone
AUTHOR: CRINOT Elvis 
STANDARDS: PEP8, Static Typing, Enterprise Architecture
LOGIC: MIT SCM, SAP S/4HANA (SSOT), Siemens Xcelerator
"""

import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import norm
from typing import Dict, List, Union, Any

# --- CONFIGURATION SYSTÈME ---
st.set_page_config(
    page_title="BIB - Benin Industrial Backbone",
    page_icon="🏭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- MOTEURS ALGORITHMIQUES (CORE LOGIC) ---

class BIBCoreEngine:
    """Regroupe l'intelligence métier SCM, Logistique et Production."""

    @staticmethod
    def smart_negotiator(world_price: float, exchange_rate: float, 
                         freight: float, scarcity: float, supplier_rank: float) -> Dict:
        base_landed = (world_price * exchange_rate) + freight
        leverage = (1.2 - supplier_rank) * scarcity
        target = base_landed * (1 + (leverage * 0.05))
        return {
            "landed": base_landed,
            "target": target,
            "walk_away": target * 1.15
        }

    @staticmethod
    def wms_stochastic_metrics(d_avg: float, d_std: float, lt_avg: float, 
                               lt_std: float, c_order: float, c_hold: float) -> Dict:
        k = norm.ppf(0.95) # Service Level 95%
        ss = k * np.sqrt((lt_avg * (d_std**2)) + ((d_avg**2) * (lt_std**2)))
        rop = (d_avg * lt_avg) + ss
        eoq = np.sqrt((2 * d_avg * 365 * c_order) / c_hold) if c_hold > 0 else 0
        return {"ss": int(np.ceil(ss)), "rop": int(np.ceil(rop)), "eoq": int(np.ceil(eoq))}

    @staticmethod
    def tms_analysis(dist: float, fuel_p: float, cons: float, fixed_p_day: float) -> Dict:
        fuel_cost = (dist / 100) * cons * fuel_p
        total = fuel_cost + (fixed_p_day * 1.5) # 1.5 jours moyenne
        return {"total": total, "cpk": total / dist if dist > 0 else 0}

    @staticmethod
    def production_health(temp: float, vib: float, hours: float) -> Dict:
        risk = (max(0, (temp-40)/60)*0.4) + (max(0, (vib-10)/40)*0.4) + ((hours/2000)*0.2)
        score = max(0, min(1, 1 - risk))
        return {"score": round(score * 100, 2), "maint": score < 0.35}

# --- INTERFACE UTILISATEUR (UI LAYER) ---

class BIBInterface:
    def __init__(self):
        self.engine = BIBCoreEngine()
        self.inject_custom_css()

    def inject_custom_css(self):
        st.markdown("""
            <style>
            .stMetric { background-color: #ffffff; border: 1px solid #e6e9ef; padding: 15px; border-radius: 5px; }
            .main-title { color: #1c355e; font-size: 28px; font-weight: 800; margin-bottom: 25px; }
            </style>
        """, unsafe_allow_html=True)

    def sidebar(self) -> str:
        st.sidebar.title("BIB OS v1.0")
        st.sidebar.caption("Ingénieur Système: CRINOT Elvis C. Kafui")
        st.sidebar.markdown("---")
        return st.sidebar.radio("Navigation", [
            "Tableau de Bord", "ACHAT", "WMS", "TMS", "PRODUCTION", "X-LINK"
        ])

    def render_dashboard(self):
        st.markdown("<div class='main-title'>Tour de Contrôle Stratégique</div>", unsafe_allow_html=True)
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Rentabilité Optimisée", "14.5M FCFA", "+12%")
        c2.metric("Disponibilité Usine", "94.2%", "+3.4%")
        c3.metric("Précision Inventaire", "99.9%", "Stable")
        c4.metric("Coût Énergie / Unité", "142 FCFA", "-15%")

    def render_achat(self):
        st.markdown("<div class='main-title'>ACHAT - Smart Negotiator</div>", unsafe_allow_html=True)
        col_in, col_out = st.columns([1, 1])
        with col_in:
            w_price = st.number_input("Cours Mondial ($)", value=1200.0)
            freight = st.number_input("Fret & Logistique (FCFA)", value=250000.0)
            scarcity = st.slider("Indice de Rareté Locale", 1.0, 2.0, 1.1)
        
        res = self.engine.smart_negotiator(w_price, 610, freight, scarcity, 0.9)
        with col_out:
            st.metric("Prix Cible (FCFA)", f"{res['target']:,.0f}")
            st.metric("Prix Walk-away", f"{res['walk_away']:,.0f}", delta="Seuil Critique")

    def render_wms(self):
        st.markdown("<div class='main-title'>WMS - Master Inventory Engine</div>", unsafe_allow_html=True)
        # Simulation 400 SKU
        df = pd.DataFrame({
            "SKU": [f"REF-{i:03d}" for i in range(1, 401)],
            "D_Avg": np.random.uniform(10, 500, 400),
            "LT": np.random.uniform(5, 25, 400),
            "Stock": np.random.uniform(50, 2000, 400)
        })
        # Applique le moteur stochastique sur le batch
        df['SS'] = df.apply(lambda x: self.engine.wms_stochastic_metrics(x['D_Avg'], 20, x['LT'], 3, 5000, 150)['ss'], axis=1)
        st.data_editor(df, use_container_width=True)

    def render_tms(self):
        st.markdown("<div class='main-title'>TMS - Logistics Tracking</div>", unsafe_allow_html=True)
        dist = st.number_input("Distance Trajet (km) - RNIE", value=450)
        res = self.engine.tms_analysis(dist, 700, 35, 25000)
        st.metric("Coût de Revient Estimé", f"{res['total']:,.0f} FCFA")
        st.metric("CPK (Coût au Kilomètre)", f"{res['cpk']:.2f} FCFA")

    def render_production(self):
        st.markdown("<div class='main-title'>PRODUCTION - Predictive Maintenance</div>", unsafe_allow_html=True)
        t = st.slider("Température Machine (°C)", 30, 120, 65)
        v = st.slider("Vibration (Hz)", 0, 100, 25)
        res = self.engine.production_health(t, v, 1200)
        st.metric("Health Score", f"{res['score']}%")
        if res['maint']: st.error("MAINTENANCE REQUISE IMMÉDIATE")
        else: st.success("État Machine Optimal")

# --- LANCEUR ---
if __name__ == "__main__":
    ui = BIBInterface()
    page = ui.sidebar()
    if page == "Tableau de Bord": ui.render_dashboard()
    elif page == "ACHAT": ui.render_achat()
    elif page == "WMS": ui.render_wms()
    elif page == "TMS": ui.render_tms()
    elif page == "PRODUCTION": ui.render_production()
    else: st.write("Interface X-LINK : Connectivité PLC active.")
