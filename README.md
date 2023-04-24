**Introduction:**</br>
The internet is a vast and constantly expanding network of interconnected computers, servers, and devices. Every website and online service has a unique domain name that users can use to access it. However, many websites have subdomains that are used for various purposes, such as hosting content, managing email services, or testing new features. Subdomains can also be used to access different parts of a website or to differentiate between different regions or languages.

Knowing the subdomains of a website can be useful for various reasons, such as identifying potential vulnerabilities, finding hidden pages or directories, or discovering additional services or content. However, manually searching for subdomains can be a time-consuming and tedious task, especially for large or complex websites.

In this project, I aimed to create a simple subdomain scanner using Python, Docker, and a CI/CD pipeline. The scanner would be able to query the nameservers for a given domain and extract its subdomains. The project was designed to demonstrate how to use Docker and a CI/CD pipeline to automate the build, test, and deployment process of a Python application.

**Technologies Used:**</br>
The following technologies were used in this project:</br>

    Python 3.9: The programming language used to write the subdomain scanner script.</br>
    Docker: A containerization platform used to build and run the subdomain scanner in a containerized environment.</br>
    Jenkins: An open-source automation server used to create the CI/CD pipeline for the subdomain scanner project.</br>
    Git: A version control system used to manage the project files and track changes.

**Project Implementation**</br>
The project was implemented in the following steps:

    Set up the development environment: The first step was to set up the development environment, which included installing Python, Docker, and Jenkins. Git was used as the version control system to manage the project files.

    Create a Dockerfile: A Dockerfile was created in the project directory to define the Docker image for the subdomain scanner. The Dockerfile specified the base image (Python 3.9), installed the necessary packages (dnspython), and set the entry point to the scanner.py script.

    Create a requirements.txt file: A requirements.txt file was created to list the dependencies for the Python script.

    Create a Python script: A scanner.py script was created in the project directory to scan subdomains. The script used the dnspython package to query the nameservers for the specified domain and extract subdomains.

    Create a Jenkins pipeline script: A Jenkins pipeline script was created to automate the build, test, and deployment process of the subdomain scanner. The pipeline script set up a Docker agent, then defined three stages: build, test, and deploy. In the build stage, the Docker image was built using the Dockerfile. In the test stage, the Python unit tests were run. In the deploy stage, the Docker image was run as a container.

    Run the Jenkins pipeline: The Jenkins pipeline was run to build, test, and deploy the subdomain scanner.

**Results:**</br>
The subdomain scanner project was successfully implemented using Python, Docker, and Jenkins. The scanner was able to query the nameservers for a given domain and extract its subdomains. The Jenkins pipeline was used to automate the build, test, and deployment process of the scanner.

**Conclusion:**</br>
The subdomain scanner project demonstrated how to use Python, Docker, and Jenkins to automate the build, test, and deployment process of a Python application. The project can be extended to add more features, such as scanning for open ports on subdomains or creating a web interface for the scanner. Overall, the project was a success in achieving its goal of demonstrating the use of Docker and a CI/CD pipeline in a Python project.

<h3>https://linkedin.com/in/0xd3vil</h3>
