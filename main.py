from fastapi import FastAPI
from saxonche import PySaxonProcessor

saxon_proc = PySaxonProcessor(license=False)
app = FastAPI()


@app.get("/")
def get():
    xml = '<root><child>Test</child></root>'
    node = saxon_proc.parse_xml(xml_text=xml)
    xml = node.to_string()
    return xml


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)