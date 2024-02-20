# PDF-C 📄 Converter

PDF-C 📄 Converter is a user-friendly Streamlit application that enables you to swiftly and effortlessly convert your PDF files into DOCX, PNG, or TXT formats. Designed with simplicity and efficiency in mind, this tool ensures that your documents are handled securely, with an auto-deletion feature that removes your files from the server after 3 minutes, guaranteeing your privacy and data security.

## Features 🚀

- **Simple Upload**: Drag and drop your PDF into the app.
- **Multiple Formats**: Convert your PDF to DOCX, PNG, or TXT.
- **Instant Download**: Access your converted files immediately.
- **Auto-Deletion**: Files are automatically deleted after 3 minutes for enhanced security.
- **Local Processing**: All conversions are processed locally for speed and privacy.

## How to Use 🛠️

1. **Choose a PDF File**: Click on the upload area or drag and drop your PDF file onto it.
2. **Select Output Format**: Choose from DOCX, PNG, or TXT as your conversion output format.
3. **Convert**: Hit the 'Convert' button and wait for the process to complete.
4. **Download**: Click the 'Download' button next to your converted file(s).
5. **Auto-delete**: The file will be automatically removed from the server after 3 minutes, so no need to worry about manual deletion.

## Installation 📥

Before running this application, ensure you have the following Python libraries installed:

```bash
pip install streamlit pdf2docx PyMuPDF Pillow
```

## Running the App 🏃‍♂️

To run the app locally, navigate to the app's directory in your terminal and run:

```bash
streamlit run app.py
```

## Deployment 🌐

This app can be easily deployed on platforms like Streamlit Sharing, Heroku, or a VPS. Make sure to comply with the hosting service's filesystem and data handling policies due to the app's file manipulation features.

## Background Customization 🎨

To set a custom background:

1. Replace the `bg.png` file with your desired background image.
2. Ensure the image is named `bg.png` or update the `main()` function in `app.py` to match the new file name.

## Security and Privacy 🔒

- Files are never stored longer than necessary.
- Auto-deletion is enforced with a 3-minute timer to enhance privacy.
- No third-party services are involved in the file conversion process.

## Author ✒️

**Shashank Raj**
- GitHub: [shashoriginal](https://github.com/shashoriginal)

## Contributions 🤝

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/shashoriginal/pdf-c-converter/issues).

## Show Your Support 💖

Give a ⭐️ if this project helped you!

---

Happy Converting! 🎉
