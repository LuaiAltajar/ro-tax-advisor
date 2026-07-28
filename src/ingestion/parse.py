from docling.document_converter import DocumentConverter

link = 'https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2016.htm'

def chunk(source: str):
    """
    @param input_file HTML input file
    @return Tuple of chunks and their metadata
    """
    converter = DocumentConverter()
    result = converter.convert(source)

    document = result.document
    markdown_text = document.export_to_markdown()
    
    chunks = markdown_text.split("\n\n")
    return chunks, []

chunks, metadata = chunk(link)
print(chunks[10015])
