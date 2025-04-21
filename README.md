# streamlist-test

# 1. Crear entorno
conda create -y -n streamlit python=3.11
conda activate streamlit

# 2. Crear archivo app
touch app.py

# 3. Streamlit
pip install streamlit
streamlit run app.py

# 4. Generar archivo de requirements.txt
pip install pipreqs
pipreqs

# 5. Dependencias
pip install folium
pip install streamlit_folium
pip install plotly
pip install scikit-learn

NOTAS
- Para parar el servidor: "crtl + C"

EXTRA
- *args: numero variable argumentos
- **kwargs: numero variable keyword arguments
