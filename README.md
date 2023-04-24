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

**Discussion:**</br>
The subdomain scanner project using Docker and CI/CD pipeline was a success in achieving its goal of demonstrating the use of Docker and a CI/CD pipeline in a Python project. The project showcased the automation of the build, test, and deployment process, which resulted in increased efficiency and reduced the risk of errors.

One of the key successes of the project was the successful integration of Docker and Jenkins. Docker was used to package the application and its dependencies into a container, which made it easy to deploy the application across different platforms. Jenkins was used as the CI/CD pipeline tool, which allowed for the automation of the build, test, and deployment process.

Another success of the project was the ability to extract subdomains from a given domain. The Python script was able to query the nameservers for the specified domain and extract its subdomains using the dnspython package. The Python script was also able to handle errors gracefully, which ensured that the application did not crash.

However, the project had some limitations. One limitation was that the scanner was only able to extract subdomains from a single domain. In the future, the project could be extended to support the scanning of multiple domains at once. Another limitation was that the scanner did not check for duplicate subdomains. In the future, the project could be extended to remove duplicate subdomains from the output.

Future Development:

There are several suggestions for future development of the subdomain scanner project. One suggestion is to add support for scanning multiple domains at once. This could be achieved by accepting a list of domains as input and running the scanner on each domain in the list.

Another suggestion is to remove duplicate subdomains from the output. This could be achieved by storing the subdomains in a set and checking if a subdomain has already been added before adding it to the set.

Another suggestion is to add support for scanning for open ports on subdomains. This could be achieved by using the Python socket module to scan for open ports on each subdomain in the output.

Finally, another suggestion is to create a web interface for the scanner. This would allow users to input domains and view the output in a user-friendly way. The web interface could be created using a Python web framework such as Flask or Django.

Overall, the subdomain scanner project using Docker and CI/CD pipeline was a success in achieving its goals and demonstrated the potential for automation in software development. With further development, the project could become a valuable tool for security professionals and researchers.

<h3>https://linkedin.com/in/0xd3vil</h3>
