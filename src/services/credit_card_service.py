from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentintelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from utils import get_env_variable

def analize_credit_card(image_url):

    credential = AzureKeyCredential(config.Key)
    client = DocumentintelligenceClient(config.Endpoint, credential)
    image_url = document_Client.begin_analyze_document_from_url("prebuilt-idDocument", AnalyzeDocumentRequest(url_source=image_url))
    result = image_url.result()
    

    for document in result.documents:
        fields = document.get('fields', {})

        return{
            "card_name": fields.get('CardholderName', {}).get('value', ''),
            "bank_name": fields.get('Issuer', {}).get('value', ''),
            "expiration_date": fields.get('ExpirationDate', {}).get('value', '')
        }