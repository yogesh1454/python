# Create a deployment package for AWS Lambda
In order to deploy your python code to AWS Lambda we need to bundle all the script and dependecy in a zip folder with dependency placed in the root folder itself
along with the source files.
REPO
  - sample.py
  - dependency1
  - dependency2

This script will help you to bundle your source code and dependency in a zip folder using `python venv`. 

# Configuration
- Place `script-env.sh` & 'requirements.txt' file in the root folder in your project.
- Add all the project dependency in the requirements.txt file, 1 dependency per line 
- In the `script-env.sh` file under `Move the relevant files into setup directory` give the path of all your project files which need to be packaged in the bundle.

# Run
- Run this `./script-env.sh` it will create a `package.zip` file.

# Deploy
- Upload `package.zip` file to AWS Lambda.
