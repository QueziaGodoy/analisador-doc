import streamlit as st

from services.blob_service import upload_file_to_blob
from services.credit_card_service import extract_credit_card_info

def configure_interface():

    st.title("Upload de arquivo DIO - Desafio 1")
    uploaded_file = st.file_uploader("Escolha um arquivo para upload", type=["pdf", "docx", "txt"])

    if uploaded_file is not None:
        fileName = uploaded_file.name
        blob_url=""
        if blob_url:
            st.write(f"Arquivo '{fileName}' carregado com sucesso! URL do blob: {blob_url}")
            credit_card_info = extract_credit_card_info(blob_url)
            show_image_and_validation(blob_url, credit_card_info)
        else:
            st.write(f"erro ao carregar o arquivo '{fileName}' para o blob storage.")
        # Aqui você pode adicionar código para processar o arquivo, se necessário

def show_image_and_validation(blob_url, credit_card_info):
    st.image(blob_url, caption="Imagem do arquivo carregado", use_column_width=True)
    st.write("Informações do cartão de crédito extraídas:")
    if credit_card_info and credit_card_info["card_name"]:
        st.markdown(f'<h1 style="color": green;>Cartão Válido</h1>', unsafe_allow_html=True)
        st.write(f"Nome do titular: {credit_card_info['card_name']}")st.write(f'banco emissor: {credit_card_info["bank"]}')
        st.write(f"data de validade: {credit_card_info['expiration_date']}')")
    else:
        st.markdown(f'<h1 style="color": red;>Cartão Inválido</h1>', unsafe_allow_html=True)

if __name__ == "__main__":
    configure_interface()