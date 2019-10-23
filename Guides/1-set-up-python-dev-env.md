# Article 1: Set Up a Python Development Environment

From Section 1 to Section 3, we will briefly introduce you to a few necessary dev-tools for Python development. You can jump to [Installation in Section 4](#4) if you are not in the mood of reading.

## Table of Contents

[1. Development Tools to Use](#1)<br>
&emsp;[1.1. Visual Studio Code](#1.1)<br>
&emsp;[1.2. Anaconda](#1.2)<br>
[2. Django and other Python Web Frameworks](#2)<br>
[3. SymPy - a Symbolic Library in pure Python](#3)<br>
[4. Installation](#4)<br>
&emsp;[4.1. Download Visual Studio Code and Anaconda](#4.1)<br>
&emsp;[4.2. Configure Conda Command for Windows User](#4.2)<br>
[5. Create a Simple Application Server locally](#5)<br>
&emsp;[5.1. Create a Conda Environment for our Project](#5.1)<br>
&emsp;[5.2. Install Python, JupyterLab, Django, SymPy in the Environment](#5.2)<br>
&emsp;[5.3. Create a Django project](#5.3)<br>
[6. What's Next?](#6)<br>
&emsp;[6.1. How to share code with other Collaborators on GitHub](#6)<br>
&emsp;[6.2. Create a new feature for Django projects](#6)<br>

<a id='1'></a>

## 1. Development Tools to Use

In this section, we will briefly introduce a few tools to use for Python development. You can start downloading these tools as you read. We will dive the workflow in other sections.

<a id='1.1'></a>
#### 1.1. Visual Studio Code

VS Code is a customizable editor for writing and debugging code. This editor can recognize many popular programming languages and provide the appropriate development tools with a simple interface. Furthermore, VS Code has a built-in terminal which can be toggled with [Ctrl + ~]/[Cmd + ~].

Download: https://code.visualstudio.com/

<img src="../assets/VS_Code.png"/>

<a id='1.2'></a>
#### 1.2. Anaconda

Anaconda is a Python package manager for creating virtual environments, installing Python and non-Python packages in virtual environments, deploying applications, and providing other tools that make coding in Python easier.

Download: https://www.anaconda.com/distribution/

<img src="../assets/Anaconda.png"/>

In the image above, we can see Jupyter Lab and Jupyter Notebook already installed inside of Anaconda. These two applications together can launch an interactive environment for live-testing new Python libraries.

<a id='2'></a>
## 2. Django and other Python Web Frameworks

A Python Web Framework provides some basic setup to help developers get started without worrying about the configurations. There are many Python Web Frameworks to choose from. Here are the top 10 Python Web Frameworks in 2019: https://hackernoon.com/top-10-python-web-frameworks-to-learn-in-2018-b2ebab969d1a

The framework that we will use for our application is Django, a fullstack web framework that has been set up with basic libraries and a project structure for web services. Because our goal is to create a secure and scalable Application Server that serves complex computations from authenticated requests, Django is suitable to our use case.

<br><img src="../assets/Django.png"/><br>

We will cover how to download and use this framework in another section. For now, if you need more information on what Django is, we include some materials below:

- Django Official Website: https://www.djangoproject.com/
- When to Use Django: https://medium.com/crowdbotics/when-to-use-django-and-when-not-to-9f62f55f693b
- Compare Django vs Flask: http://www.mindfiresolutions.com/blog/2018/05/flask-vs-django/

<a id='3'></a>
## 3. SymPy - a Symbolic Library in pure Python

SymPy is a Python library for symbolic mathematics. It aims to become a full-featured computer algebra system (CAS) while keeping the code as simple as possible in order to be comprehensible and easily extensible. SymPy is written entirely in Python. For more information: https://www.sympy.org/en/index.html

MapleSoft and Wolfram Language are also symbolic languages, but they are very strict for what we want to achieve: a free and easy project setup that is compatible with other software-dev tools. Therefore, SymPy is a great choice because it is written entirely in Python, a popular programming language that is backed by an extensive pool of users and businesses.

<img src='../assets/Sympy_logo.svg'/>

<a id='4'></a>
## 4. Installation

<a id='4.1'></a>
#### &emsp;&emsp;Step 1: Download Visual Studio Code and Anaconda

If you have already downloaded and installed these dev-tools from Section 1, you can jump to [Step 2](#4.2).

Download VS Code: https://code.visualstudio.com/<br>
Download Anaconda: https://www.anaconda.com/distribution/

Install VS Code and Anaconda following the window prompts. Contact me if you have any questions.

<a id='4.2'></a>
#### &emsp;&emsp;Step 2: Configure <code>conda</code> Command for Windows User

If you are using MacOS, you can now start [Creating a Simple Application Server locally](#4.3).

For Windows user, in order to use command <code>conda</code> in the <a href='https://www.lifewire.com/command-prompt-2625840'>Command Prompt</a>, you have to add Anaconda to your path variables following these steps below:
- Hit "Windows Key" and type "variable" in search bar.
- Click "Edit environment variables for your account".
- In the new "Environment Variables" window click on variable "Path" for your [user account], then click "Edit...".
- A new window should show up. Click "New" to add these two paths:

&emsp;&emsp;<code>C:\xxxx\yyyy\Anaconda3</code><br>
&emsp;&emsp;<code>C:\xxxx\yyyy\Anaconda3\Script</code>

&emsp;If you install Anaconda at <code>C:\Program Files\Anaconda3</code>, then your two paths should be:

&emsp;&emsp;<code>C:\Program Files\Anaconda3</code><br>
&emsp;&emsp;<code>C:\Program Files\Anaconda3\Script</code><br>

See the following image for reference.

<img src='../assets/Conda_command.png'/>

<a id='5'></a>
## 5. Create a Simple Application Server locally

<a id='5.1'></a>
#### 5.1. Create a Conda Environment for our Project

If you wonder what a conda environment is, here is the explanation from the Anaconda documentation.

A conda environment is a directory that contains a specific collection of conda packages that you have installed. For example, you may have one environment with NumPy 1.7 and its dependencies, and another environment with NumPy 1.6 for legacy testing. If you change one environment, your other environments are not affected. You can easily activate or deactivate environments, which is how you switch between them. You can also share your environment with someone by giving them a copy of your <code>environment.yaml</code> file. For more information, see <a href='https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html'>Managing environments</a>.
    
&emsp;__Step 1: Open the Terminal/Command Prompt__

&emsp;__Step 2: Create a new conda environment__

&emsp;Anaconda has a default environment called <code>base</code> that is activated automatically whenever we open a Terminal/Command Prompt. To create a new conda environment with the name <code>simple-app-server</code>, use the following command:

&emsp;&emsp;&emsp;<code>conda create --name simple-app-server</code>

&emsp;You can verify that your new environment is created by listing all the environments as below:

&emsp;&emsp;&emsp;<code>conda env list</code>

&emsp;__Step 3: Activate and Deactivate a conda environment__

&emsp;By default, Anaconda automatically activates the <code>base</code> environment whenever we open a Terminal/Command Prompt. To activate our environment <code>simple-app-server</code>, we need to first deactivate the <code>base</code> environment:

&emsp;&emsp;&emsp;<code>conda deactivate</code><br>

&emsp;Then we can activate our <code>simple-app-server</code> environment:

&emsp;&emsp;&emsp;<code>conda activate simple-app-server</code>

<a id='5.2'></a>
#### 5.2. Install Python, JupyterLab, Django, SymPy in the Environment

&emsp;__Step 1: Open the Terminal/Command Prompt__

&emsp;Skip to the next step if you've already opened a Terminal/Command Prompt.

&emsp;__Step 2: Activate our <code>simple-app-server</code> environment__

&emsp;Skip to the next step if you've already activated in [section 5.1](#5.1). Otherwise, you can activate the <code>simple-app-server</code> environment as follows:

&emsp;&emsp;&emsp;<code>conda deactivate && conda activate simple-app-server</code><br>

&emsp;__Step 3: Install Python, JupyterLab, Django, SymPy__

&emsp;&emsp;&emsp;<code>conda install -c conda-forge python jupyterlab django sympy</code>

<a id='5.3'></a>
#### 5.3. Create a Django project

&emsp;__Step 1: Create a folder to contain our project__

&emsp;&emsp;&emsp;Create a folder with any name you want. This name does not affect your project settings. In the image below, the folder name is <code>simple-app-server</code>.

<img src='../assets/5.3-step1.png'/>

&emsp;__Step 2: In VS Code, open the newly created folder__

&emsp;&emsp;&emsp;To open the newly created folder in VS Code, on the menu bar:

&emsp;&emsp;&emsp;<code>File > Open...</code>

&emsp;&emsp;&emsp;If you do it properly, you should see this view below.

<img src='../assets/5.3-step2.png'/>

&emsp;__Step 3: Toggle on the Terminal/Command Prompt__

&emsp;&emsp;&emsp;On Windows, press <code>Ctrl + ~</code><br>
&emsp;&emsp;&emsp;On MacOS, press <code>Cmd + ~</code><br>

Then, the view should look like this:

<img src='../assets/5.3-step3.png'/>

&emsp;__Step 4: Activate the <code>simple-app-server</code> environment__

&emsp;&emsp;&emsp;Now type <code>conda deactivate && conda activate simple-app-server</code> in the Terminal/Command Prompt above.

&emsp;__Step 5: Create a Django project named <code>myserver</code>__

&emsp;&emsp;&emsp;In the Terminal/Command Prompt, type in <code>django-admin startproject myserver</code> to create a Django project. If you do it properly, you should see this view:

<img src='../assets/5.3-step4.png'/>

&emsp;__Step 6: Run the Server__

&emsp;&emsp;&emsp;In the Terminal/Command Prompt:
- Move to the <code>myserver</code> directory: <code>cd myserver</code>
- Run the server: <code>python manage.py runserver</code>

<img src='../assets/5.3-step6.png'/>

- Now open the browser and access this link: http://127.0.0.1:8000/ or <a href='http://localhost:8000/'>localhost:8000</a>

<img src='../assets/5.3-step6-2.png'/>


#### Feel free to edit something in the code. If you have some experience in Python and would like to write your own server, this project template above is a very great start.
#### Otherwise, we will dive into the project settings and start coding in another post. In case you want to learn these project settings yourself, here is the reference link: https://docs.djangoproject.com/en/2.2/intro/tutorial01/

<a id='6'></a>
## 6. What's Next?

#### 6.1. How to share code with other Collaborators on GitHub

You may have some questions like:
- How do other collaborators work with me on my project?
- Do they have to set up everything from the beginning, or is there any shortcut to make it fast?

#### 6.2. Create a new feature for Django projects
