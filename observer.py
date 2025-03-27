import time
from datetime import datetime
import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# URL della pagina da monitorare (sostituisci con quello reale)
PRODUCT_URL = "https://direct.playstation.com/it-it/buy-accessories/dualsense-wireless-controller-the-last-of-us-limited-edition"

# Configura Selenium con Chrome in modalità headless (senza interfaccia grafica)
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=chrome_options)

# Streamlit UI
st.title("Monitoraggio Disponibilità Prodotto")
start_time = datetime.now().strftime("%H:%M:%S")
st.write(f"Script avviato alle: {start_time}")

try:
    # Carica la pagina del prodotto
    driver.get(PRODUCT_URL)
    # Attendi il caricamento della pagina (modifica il tempo se necessario)
    time.sleep(5)

    # Inietta il MutationObserver per monitorare l'elemento della quantità.
    observer_script = """
        var targetNode = document.getElementById('quantity-value');
        if (!targetNode) {
            window.quantityChanged = false;
            return;
        }
        window.quantityChanged = false;
        var observer = new MutationObserver(function(mutationsList, observer) {
            for (var mutation of mutationsList) {
                if (mutation.type === 'childList' || mutation.type === 'characterData' || mutation.type === 'attributes') {
                    window.quantityChanged = true;
                }
            }
        });
        observer.observe(targetNode, { attributes: true, childList: true, subtree: true, characterData: true });
    """
    driver.execute_script(observer_script)
    st.write("Monitoraggio avviato...")

    # Loop per il polling della variabile globale iniettata
    while True:
        changed = driver.execute_script("return window.quantityChanged;")
        current_time = datetime.now().strftime("%H:%M:%S")
        if changed:
            st.write(f"[{current_time}] Prodotto disponibile!")
            driver.execute_script("window.quantityChanged = false;")
        else:
            st.write(f"[{current_time}] Prodotto non disponibile...")
        time.sleep(5)  # Controlla ogni 5 secondi

finally:
    driver.quit()
