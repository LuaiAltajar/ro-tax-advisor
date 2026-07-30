from docling.document_converter import DocumentConverter
from langchain_text_splitters import MarkdownHeaderTextSplitter


def chunk(source: str):
    """
    @param input_file HTML input file
    @return Tuple of chunks and their metadata
    """
    converter = DocumentConverter()
    result = converter.convert(source)

    document = result.document
    markdown_text = document.export_to_markdown()

    headers_to_split_on = [("ART.", "Header")]

    splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
    splits = splitter.split_text(markdown_text)
    
    chunks = [split.page_content for split in splits]
    metadata = [split.metadata for split in splits]
    return chunks, metadata

