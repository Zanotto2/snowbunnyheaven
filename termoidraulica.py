import streamlit as st

# Configurazione della pagina
st.set_page_config(
    page_title="Azienda di Termoidraulica",
    page_icon="🔥",
    layout="wide"
)

# Titolo principale
st.title("Benvenuti in TermoService - Soluzioni Termoidrauliche")

# Banner immagine (puoi sostituire con un'immagine della tua azienda)
st.image("img4.jpg", use_container_width =True)

# Sezione Introduzione
st.header("Chi siamo")
st.write("""
TermoService è una società leader nel settore termoidraulico, specializzata nella progettazione, installazione e manutenzione di sistemi innovativi per il riscaldamento, la climatizzazione e l'acqua calda sanitaria. 
Con anni di esperienza alle spalle, ci impegniamo a garantire soluzioni efficienti ed economiche per soddisfare le esigenze dei nostri clienti.
""")

# Sezione Servizi
st.header("I nostri servizi")
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Riscaldamento")
    st.write("""
    Installazione e manutenzione di impianti di riscaldamento domestici e industriali. Utilizziamo tecnologie avanzate per garantire efficienza energetica e durata lunga.
    """)
    st.image("img1.jpg", use_container_width=True)

with col2:
    st.subheader("Climatizzazione")
    st.write("""
    Progettiamo e installiamo sistemi di climatizzazione personalizzati per residenze, uffici e locali commerciali. Frescura durante l'estate e comfort durante l'inverno.
    """)
    st.image("img2.jpg", use_container_width=True)

with col3:
    st.subheader("Acqua Calda Sanitaria")
    st.write("""
    Sistemi integrati per la produzione di acqua calda sanitaria, inclusi pannelli solari e caldaie ad alta efficienza. Risparmia energia e riduci le bollette.
    """)
    st.image("img3.jpg", use_container_width=True)

# Sezione Contatti
st.header("Contattaci")
st.write("""
Se hai bisogno di ulteriori informazioni o vuoi richiedere un preventivo gratuito, non esitare a contattarci!
""")
form = st.form(key='contact_form')
name = form.text_input("Nome")
email = form.text_input("Email")
message = form.text_area("Messaggio")
submit_button = form.form_submit_button(label='Invia')

if submit_button:
    st.success(f"Grazie {name}! Il tuo messaggio è stato inviato con successo. Ti risponderemo al più presto.")

# Footer
st.markdown("---")
st.write("© 2023 TermoService - Tutti i diritti riservati.")
st.write("Tel: +39 123 456 789 | Email: info@termoservice.it | Sito web: [www.termoservice.it](http://www.termoservice.it)")