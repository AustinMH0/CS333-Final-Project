# CS333-Final-Project
Final project for Testing and DevOps at UNR

## Project Goals
The goal of this project is to:
- Implement unittests and integration tests of an object-oriented program
- Implement automatic testing, building, and deployment of a Docker image of the program using Github Actions

## Welcome to Recipe Manager

### Unittests, Integration Tests, and Package
- [Unittests and integrations tests](tests)
- [recipemanager package](recipemanager)

#### Latest Coverage Report
<img src="https://github.com/AustinMH0/CS333-Final-Project/assets/112452064/1bff7651-4a7e-4a6d-b0cb-08de78de6311" width="50%" height="50%">


### Workflows
[Workflow for automatic testing.](https://github.com/AustinMH0/CS333-Final-Project/actions/workflows/python-app.yml)
[Workflow for automatic building and deployment.](https://github.com/AustinMH0/CS333-Final-Project/actions/workflows/docker-hub.yml)


### Installation
Using `Python 3.12.1`
1) Clone the repo: `git clone https://github.com/AustinMH0/CS333-Final-Project`
2) Install Coverage: `python3 -m pip install coverage`

- `coverage run -m main_tests` to run the unittests and integration tests.
- `python3 recipe_manager_app.py` to run the driver.

### Docker Repsitory
[Here](https://hub.docker.com/repository/docker/austinmh/cs333finalproject/general) is the Docker repository that the image is automatically pushed to via Actions.
