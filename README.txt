# README

## Steps to set up the project

1. **Create a virtual environment**
  - This helps to keep the dependencies required by different projects separate by creating isolated python virtual environments for them.
  - Use the following command to create a new virtual environment:
    ```
    python3 -m venv venv
    ```

2. **Activate the virtual environment**
  - This will activate the isolated environment for your project.
  - On Windows, use:
    ```
    venv\Scripts\activate
    ```
  - On Unix or MacOS, use:
    ```
    source venv/bin/activate
    ```

3. **Check Python version**
  - It's important to know which version of Python you're working with. Use the following command to check:
    ```
    python --version
    ```

4. **Install packages from requirements.txt**
  - This file contains all the dependencies that your project needs. You can install them using pip.
  - Use the following command to install the required packages:
    ```
    pip install -r requirements.txt
    ```

5. **Check all installed packages**
  - To verify that the required packages are installed, you can list all the installed packages.
  - Use the following command to list the installed packages:
    ```
    pip freeze
    ```

6. **Run the Flask app**
  - Finally, you can run your Flask application.
  - Use the following command to run the app:
    ```
    flask --app app run
    ```