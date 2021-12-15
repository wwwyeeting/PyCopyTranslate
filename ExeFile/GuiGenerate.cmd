..\.venv\Scripts\pyinstaller.exe -F ^
    ..\main.py ^
    ..\Capture\__init__.py ^
    ..\Capture\ClipCapture.py ^
    ..\Common\__init__.py ^
    ..\Common\Common.py ^
    ..\Translate\__init__.py ^
    ..\Translate\Google.py ^
    ..\Translate\TranslateAbc.py ^
    --name PyCopyTranslate.exe

cd dist
copy ".\PyCopyTranslate.exe" ..\..\
pause
