@echo off

REM Create and initialize a Python Virtual Environment
echo Creating virtual env - .venv
python -m venv .venv

echo sourcing virtual env - .venv
REM cmd /k ".venv\Scripts\activate.bat & mkdir setup"
CALL .venv\Scripts\activate.bat

REM Create a directory to put things in
echo Creating 'setup' directory
mkdir setup

REM Move the relevant files into setup directory
echo Moving function file(s) to setup 'dir'
xcopy count_validation.py setup\
xcopy count_using_dict.py setup\
xcopy xsd_validation.py setup\
cd ./setup

REM # Install requirements 
echo pip installing requirements from requirements file in target directory
pip install -r ../requirements.txt -t .
 
REM # Prepares the deployment package
echo Zipping package
7z a ../xml_validation.zip ./* 

REM # Remove the setup directory used
echo Removing setup directory and virtual environment
cd ..
rmdir /s /q setup
CALL deactivate
rmdir /s /q .venv
REM # changing dirs back to dir from before
echo Opening folder containg function package - 'package.zip'
7z l xml_validation.zip