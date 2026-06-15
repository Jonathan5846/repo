import streamlit as st
import google.generativeai as genai

# 1. Configuración de la interfaz de la página web
st.set_page_config(
    page_title="AgroAsistente IA - Web", 
    page_icon="🌱", 
    layout="centered"
)

# Títulos principales en la pantalla
st.title("AgroAsistente Inteligente 🌱")
st.markdown("### *Innovación Sostenible con Inteligencia Artificial Real*")
st.write("Prototipo web funcional para el análisis del uso del agua y control biológico de plagas.")
st.markdown("---")

# 2. Barra lateral para ingresar la API Key de forma segura
st.sidebar.header("Conexión con la IA")
api_key_usuario = st.sidebar.text_input(
    "Introduce tu Gemini API Key:", 
    type="password",
    help="Consigue una clave gratis en Google AI Studio para activar el backend."
)

# Mensaje de advertencia si no hay llave conectada
if not api_key_usuario:
    st.info("💡 Para activar el análisis en tiempo real, ingresa tu API Key en la barra lateral izquierda.")
else:
    # Configurar la IA real de Google con la clave provista
    genai.configure(api_key=api_key_usuario)
    # Usamos el modelo rápido y optimizado para texto
    modelo_ia = genai.GenerativeModel('gemini-1.5-flash')

    # 3. Formulario Web de Entrada de Datos
    st.subheader("Panel de Monitoreo de Cultivos")
    with st.form("formulario_agricola"):
        cultivo = st.text_input("Tipo de Cultivo (ej. Maíz, Café, Frijol):", placeholder="Escribe el cultivo...")
        humedad = st.slider("Porcentaje de Humedad de la Tierra (%):", min_value=0, max_value=100, value=50)
        sintomas = st.text_area("Síntomas u observaciones visuales de la planta:", placeholder="Ej. Hojas amarillas con manchas cafés en los bordes...")
        
        # Botón de envío del formulario
        boton_analizar = st.form_submit_button("Consultar Agente de IA")

    # 4. Procesamiento de la petición con la IA Real
    if boton_analizar:
        if not cultivo.strip() or not sintomas.strip():
            st.error("⚠️ Por favor, llena todos los campos del formulario antes de consultar.")
        else:
            # Spinner animado mientras la API responde
            with st.spinner("El agente inteligente está procesando los criterios de sostenibilidad..."):
                
                # Prompt estructurado internamente para obligar a la IA a responder bajo los ODS
                prompt_estructurado = f"""
                Actúas como un Ingeniero Agrónomo experto en Sostenibilidad e Inteligencia Artificial.
                Analiza el siguiente escenario micro-local y genera recomendaciones estrictas de mitigación:
                
                - Tipo de Cultivo: {cultivo}
                - Humedad Actual del Suelo: {humedad}%
                - Estado de la Planta / Síntomas: {sintomas}
                
                Estructura tu respuesta exactamente con los siguientes tres bloques utilizando Markdown claro:
                
                1. 💧 **OPTIMIZACIÓN DE RIEGO (Ahorro de Agua):** Analiza si con {humedad}% de humedad requiere riego, qué técnica aplicar y cómo evitar la degradación química del suelo por exceso o falta de agua.
                2. 🐛 **CONTROL BIOLÓGICO DE PLAGAS:** Diagnostica qué podría causar los síntomas '{sintomas}' y propón soluciones 100% orgánicas (biopesticidas, extractos naturales) prohibiendo el uso de agroquímicos comerciales.
                3. 📊 **EVALUACIÓN DE IMPACTO SOSTENIBLE:** Detalla brevemente el beneficio Ambiental (recursos), Económico (ahorro de costos comunitarios) y Social de seguir tus recomendaciones.
                """
                
                try:
                    # Llamada real a la API de Gemini
                    respuesta = modelo_ia.generate_content(prompt_estructurado)
                    
                    # Desplegar el resultado real devuelto por la IA en la página web
                    st.success("¡Análisis Generado de Forma Exitosa!")
                    st.markdown("### 📋 Diagnóstico Técnico de la IA")
                    st.markdown(respuesta.text)
                    
                except Exception as error:
                    st.error(f"Error de conexión: {error}. Verifica si tu API Key es correcta.")

# Pie de página académico
st.markdown("---")
st.caption("Proyecto Final - Introducción a Ingeniería en Sistemas y TICS | Universidad Panamericana 2026")
