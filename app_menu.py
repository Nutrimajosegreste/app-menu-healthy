import streamlit as st
import random

st.title("Generador de Menú Saludable")

# Definición de menús
menus = {
    "bajar de peso": {
        "desayuno": [
            "Smoothie verde con avena",
            "Yogurt con fresas y chía",
            "Pan integral con aguacate"
        ],
        "comida": [
            "Ensalada de atún con garbanzos",
            "Tacos de lechuga con pollo",
            "Sopa de verduras con arroz integral"
        ],
        "cena": [
            "Calabacitas rellenas de tofu",
            "Crema de zanahoria con nuez",
            "Ensalada de espinaca con huevo"
        ]
    },
    "ganar músculo": {
        "desayuno": [
            "Omelette de claras con avena",
            "Hotcakes de plátano y huevo",
            "Smoothie de proteína con frutas"
        ],
        "comida": [
            "Pechuga de pollo con quinoa y brócoli",
            "Carne magra con arroz y espinacas",
            "Ensalada de lentejas con huevo"
        ],
        "cena": [
            "Yogurt griego con nueces",
            "Wrap de atún con hummus",
            "Tostadas integrales con pollo"
        ]
    },
    "salud digestiva": {
        "desayuno": [
            "Papaya con chía y yogurt natural",
            "Avena con manzana y linaza",
            "Pan integral con plátano"
        ],
        "comida": [
            "Lentejas con arroz integral",
            "Sopa de verduras y aguacate",
            "Pescado al vapor con batata"
        ],
        "cena": [
            "Caldo de verduras",
            "Tortitas de avena y zanahoria",
            "Puré de papa con espinaca"
        ]
    }
}

dias_semana = ["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]

objetivo = st.selectbox("¿Qué tipo de menú quieres?", list(menus.keys()))
if st.button("Generar menú semanal"):
    st.write(f"### Menú semanal para **{objetivo}**")
    for dia in dias_semana:
        st.markdown(f"**{dia}**")
        st.write("- Desayuno:", random.choice(menus[objetivo]["desayuno"]))
        st.write("- Comida:   ", random.choice(menus[objetivo]["comida"]))
        st.write("- Cena:     ", random.choice(menus[objetivo]["cena"]))
        st.write("---")