import dotenv
import os
from langchain_community.document_loaders import PyPDFLoader


dotenv.load_dotenv()
os.environ["LANGCHAIN_TRACING_V2"] = "true"


file_path = "PDFs\Metric Ensembles for Hallucination Detection.pdf"
loader = PyPDFLoader(file_path)

docs = loader.load()

print(len(docs))
