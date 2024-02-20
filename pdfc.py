import streamlit as st
from pdf2docx import Converter
import fitz  # PyMuPDF
import tempfile
import os
import threading
import base64

# Function to delete files after a delay
def delayed_file_delete(file_path, delay):
    def delete_file():
        try:
            os.remove(file_path)
        except OSError as e:
            print(f"Error deleting file {file_path}: {e.strerror}")
    
    timer = threading.Timer(delay, delete_file)
    timer.start()

def convert_pdf_to_docx(input_pdf_path):
    with tempfile.NamedTemporaryFile(delete=False, suffix='.docx') as output_docx:
        cv = Converter(input_pdf_path)
        cv.convert(output_docx.name, start=0, end=None)
        cv.close()
        delayed_file_delete(output_docx.name, delay=180) # 3 minutes
        return output_docx.name

def convert_pdf_to_image(input_pdf_path):
    doc = fitz.open(input_pdf_path)
    output_files = []
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)  # Load the current page
        pix = page.get_pixmap()  # Render page to an image
        img_bytes = pix.tobytes("png")  # Get PNG bytes
        with tempfile.NamedTemporaryFile(delete=False, suffix='.png', mode="wb") as output_png:
            output_png.write(img_bytes)  # Write the image bytes to the file
            output_files.append(output_png.name)
            delayed_file_delete(output_png.name, delay=180) # 3 minutes
    return output_files

def convert_pdf_to_txt(input_pdf_path):
    with tempfile.NamedTemporaryFile(delete=False, suffix='.txt', mode='w', encoding='utf-8') as output_txt:
        doc = fitz.open(input_pdf_path)
        for page in doc:
            text = page.get_text()
            output_txt.write(text)
        delayed_file_delete(output_txt.name, delay=180) # 3 minutes
        return output_txt.name

def set_bg_hack_url():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{st.session_state.bg_img}");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def main():
    st.title('PDF-C 📄 Converter')
    
    st.write("Please note: Your converted files will be automatically deleted after 3 minutes.")
    
    if 'bg_img' not in st.session_state:
        with open("bg.png", "rb") as file:
            st.session_state.bg_img = base64.b64encode(file.read()).decode("utf-8")
    set_bg_hack_url()

    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    
    if uploaded_file is not None:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_pdf:
            tmp_pdf.write(uploaded_file.getvalue())
            input_pdf_path = tmp_pdf.name
        
        output_format = st.selectbox("Select Output Format", ['DOCX', 'Image (PNG)', 'TXT'])

        if st.button('Convert'):
            with st.spinner('Converting...'):
                if output_format == 'DOCX':
                    output_docx_path = convert_pdf_to_docx(input_pdf_path)
                    st.success('Conversion Successful!')
                    with open(output_docx_path, "rb") as file:
                        st.download_button('Download DOCX', file, file_name="converted.docx")
                    
                elif output_format == 'Image (PNG)':
                    output_image_paths = convert_pdf_to_image(input_pdf_path)
                    for image_path in output_image_paths:
                        with open(image_path, "rb") as file:
                            st.download_button(f'Download Image {output_image_paths.index(image_path)}', file, file_name=os.path.basename(image_path))
                    
                elif output_format == 'TXT':
                    output_txt_path = convert_pdf_to_txt(input_pdf_path)
                    st.success('Conversion Successful!')
                    with open(output_txt_path, "rb") as file:
                        st.download_button('Download TXT', file, file_name="converted.txt")

            # Delete the input PDF after conversion
            delayed_file_delete(input_pdf_path, delay=180) # 3 minutes
footer = """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: transparent;
        color: white; /* Text color changed to white */
        text-align: center;
        padding: 10px;
    }
    </style>
    <div class="footer">
        <p>Made with ❤️ by <a href="https://github.com/shashoriginal" target="_blank" style="color: white;">Shashank</a></p>
    </div>
    """
st.markdown(footer, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
