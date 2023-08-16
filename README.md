## Project Schema-Complexity-Analysis

Welcome to the Schema-Complexity-Analysis project. This guide will walk you through setting up and running the project.

## Gitana Setup
Before diving into the main setup, you need to ensure that Gitana is properly installed and set up.

### Requirements
Gitana is developed on Windows 7 and it relies on:
- Git 2.9.3 ([download](https://git-scm.com/downloads))
- MySQL Server 5.6 ([download](http://dev.mysql.com/downloads/installer/))
- Python 2.7.6 ([download](https://www.python.org/downloads/windows/))

##  Installation

Installation of Gitana is achieved by executing the setup script.
```
$> cd <...>/Gitana
$> python setup.py build
$> python setup.py install
```

### Using Gitana
Gitana is optimized for Windows, though it has been successfully executed on Linux platforms.

For a comprehensive understanding, refer to the official Gitana GitHub Repository.
```bash
virtualenv myGitanaEnv --python=python2.7.18
```
Make sure to install all the packages listed in requirements.txt within this virtual environment.

### Python3 Dependencies
Outside of the Gitana environment, you need to install the following Python3 libraries:

- selenium
- pandas
- matplotlib
- numpy
- cv2
- subprocess
- xml.etree.ElementTree
- requests
- logging


## Initial Setup

#### 1. Initial Run with initializer.py

Execute the initial script:
```bash
python initializer.py
```
#### 2. Activate the Gitana Environment with myGitanaEnv
Activate your environment using:
```python
myGitanaEnv\Scripts\activate
```
#### 3. Clone Repositories & Import Data using script.sh
Utilize Gitbash to clone the specified repositories in dbml_repositories.txt:
```bash
./script.sh
```
## Post-cloning
script.py will commence, importing your data into MySQL with Gitana.

#### 4. Process Imported Data with processor.py
Execute the script to process your data:
```bash
python processor.py
```


