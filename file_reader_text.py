import easyocr

def text_reader(file_path):
    reader=easyocr.Reader(['ru', 'en'])
    result = reader.readtext(file_path, detail=0, paragraph = True)
    return result




