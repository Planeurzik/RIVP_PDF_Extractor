changer regexp : 
 chauffage  , eauchaude , equipement chauffage , equipementeauchaude


A - E | O-AB

python -m PyInstaller --clean  --add-data "tess\tesseract.exe;tess" --add-data "tess\tessdata;tess\tessdata"  app.py   --collect-all pypdfium2  --onefile