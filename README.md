# AWS Login BDD Automation

BDD framework built using Python and Behave.
This project tries to automate the login on the page [https://aws.amazon.com/].

### Prerequisities

```
Python version >= 2.7.11
```


## Getting Started

### Create a virtual environment and install dependencies

```
python -m venv .env_aws_login
source .env_aws_login/bin/activate
pip install -r requirements.txt
```


## Running the tests

```
To run scripts for uitests: behave features/modules --tags=awsLogin --junit --no-capture
```
#### or you can run a specific scenario indicating the corresponding tag of the file aws.feature

## Built with

* behave==1.2.6
* parse==1.15.0
* parse-type==0.5.2
* PyHamcrest==2.0.2
* PyYAML==5.3.1
* selenium==2.53.1
