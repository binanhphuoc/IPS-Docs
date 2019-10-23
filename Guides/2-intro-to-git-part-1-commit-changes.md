# Article 2
# Introduction to Git - Part 1: Commit Changes

Git is an essential tool for version control and collaboration in a code project. If you still have confusions, don't worry. We will dive into every aspect of this tool later.

Because Git has many complexities, we will break down the series __Introduction to Git__ into 4 parts:
- Part 1: Commit Changes
- Part 2: Create Branches
- Part 3: Push changes to a Remote Repository
- Part 4: Pull changes from a Remote Repository

## Table of Contents

[1. Introduction to Git](#1)<br>
&emsp;[1.1. What is Git?](#1.1)<br>
&emsp;[1.2. Install Git for MacOS and Windows](#1.2)<br>
[2. Why Commit Changes?](#2)<br>
[3. Visualization of Concept](#3)<br>
&emsp;[3.1. `git commit`](#3.1)<br>
&emsp;[3.2. `git log`](#3.2)<br>
&emsp;[3.3. `git checkout`](#3.3)<br>
[4. Practice with a Django project](#4)<br>
[5. What's Next?](#5)<br>
&emsp;[5.1. Share Code with Collaborators on GitHub](#5)<br>
&emsp;[5.2. How to make Project Setup easy for Collaborators](#5)<br>
&emsp;[5.3. Understand Django project settings](#5)<br>
&emsp;[5.4. Document a Django project](#5)<br>

<a id='1'></a>
## 1. Introduction to Git

<a id='1.1'></a>
#### 1.1. What is Git?

Git is a Version Control System for tracking changes happening in a project. So what is a Version Control System? There are a few ways to think about its benefits:
- You have done some changes to your project, but then it goes wrong. Now you want to change it back.
- You would like to share your project code with other people, but you don't want to download and upload to a shared drive because it's time-consuming for everyone.
- You make some changes (called A) to the project, and another person makes some other changes (called B) to the project. You need a way to merge A and B together.
Luckily, Git can save us here.

<a id='1.2'></a>
#### 1.2. Install Git for MacOS and Windows

#### Git for Mac Installer

The easiest way to install Git on a Mac is via the stand-alone installer:

&emsp;__Step 1:__ Download the latest Git for <a href='https://sourceforge.net/projects/git-osx-installer/files/'>Mac installer</a>.

&emsp;__Step 2:__ Follow the prompts to install Git.

&emsp;__Step 3:__ Open a terminal and verify the installation was successful by typing `git --version`:

```bash
> git --version
git version 2.9.2
```

&emsp;__Step 4:__ Configure your Git username and email using the following commands, replacing Emma's name with your own. These details will be associated with any commits that you create:

```bash
> git config --global user.name "Emma Paris"
> git config --global user.email "eparis@atlassian.com"
```

#### Git for Windows stand-alone installer

&emsp;__Step 1:__ Download the latest Git for [Windows installer](https://gitforwindows.org/).

&emsp;__Step 2:__ When you've successfully started the installer, you should see the Git Setup wizard screen. Follow the Next and Finish prompts to complete the installation. The default options are pretty sensible for most users.

&emsp;__Step 3:__ Open a Command Prompt (or Git Bash if during installation you elected not to use Git from the Windows Command Prompt).

&emsp;__Step 4:__ Run the following commands to configure your Git username and email using the following commands, replacing Emma's name with your own. These details will be associated with any commits that you create:

```bash
> git config --global user.name "Emma Paris"
> git config --global user.email "eparis@atlassian.com"
```

<a id='2'></a>
## 2. Why Commit Changes?

In this article, we will learn about the first basic Git concept: __Commit__. Before we dive into the details, we would like you to understand why we need to __commit changes__.

### Situation 
Imagine that you are working on a project with a very large codebase. At first, the code runs really well. Then, you develop a new feature, add some new files, and change some old code in the project. But now when you run your project again, it crashes. That's a big OOPS right there, and you just wish that you can go back to the older version of this project when it was still working.

### Resolution
Luckily, Git allows you to save each version of your project into the Git system. If the new version does not work, you can always revert back to the older versions in a snap. Sounds cool ehhh?

However, instead of calling it a `version`, we usually say a __`commit`__.

### Definition

A __commit__ is basically a snapshot of your project folder. When you make a new commit, it's like you are taking a picture of your current project folder and saving it in the Git system. As we work on our project, we will have more commits (or snapshots) in the future. Of course, you can have a look at your old commits if you want too.

> ___
> #### Definition
> ### A __commit__ is basically a snapshot of your project folder.
> ___

To make this guide more intuitive, we will divide it into two sections:
- __Visualization of Concept__: You will learn how this concept works by typing real commands and seeing the outcomes with visualization.
- __Practice with a Django project__: After you understand how it works, we will apply it in a sample Django project.

<a id='3'></a>
## 3. Visualization of Concept

First, let's open this link: http://git-school.github.io/visualizing-git/#free. We will need this to visualize our concept.

Once you open the link, look at the visualization panel. You can see a node labelled with __`master - HEAD`__ similar to the image below:

<img src='../assets/2-2.2.1-1-first_commit_node.png'/>

This node represents the current __commit__ of your project. It contains all the code files that you have created so far.

<a id='3.1'></a>
### 3.1. `git commit`
Then, let's say you just added some code for a new feature `featureA`, and you need to save this new version of your project into the Git system. In the Command Prompt on the website, type this command:

&emsp;&emsp;`git commit -m "Added featureA"`

If you do it properly, you should see a new node created and appended next to your first commit:

<img src='../assets/2-2.2.1-2-second_commit_node.png'/>

This new node represents the new commit that you just made. Now, let's say you deleted some file `file1.js` from the project, and you commit this change into the Git system with this following command:

&emsp;&emsp;`git commit -m "Delete file1.js"`

Then, you should expect the following result:

<img src='../assets/2-2.2.1-3-third_commit_node.png'/>

<a id='3.2'></a>
### 3.2. `git log`

So far, you have three commits (or versions) of your project as you can see in the image above. However, when you work in a real project, there is no visualization for you to see all the commits that you made. In this case, you can list all the commits with the following command:

&emsp;&emsp;`git log`

<img src='../assets/2-2.2.1-4-git_log.png'/>

<a id='3.3'></a>
### 3.3. `git checkout`

Now, for some reason, you want to have a look at the deleted file `file1.js`. You can do this by checking out the previous commit. In my case, the *sha-1 number* of the previous commit is `f475695`, so the checkout command would be:

&emsp;&emsp;`git checkout f475695`

<img src='../assets/2-2.2.1-5-git_checkout.png'/>

As you see, `HEAD` is now under the previous commit that you made. What does that mean? It means that, when you look at your project folder right now, all the files in your previous commit, including your deleted file `file1.js`, has been recovered. You will see this when we practice with a real project folder in the [next section](#4).

After checking that deleted file, let's say you want to get back to the most recent commit to continue working on the project. There is a fast way to do this. If you look closer to the visualization, you will see the label `master` under the most recent commit. So to checkout this commit, we can just use `master` instead of the *sha-1 number*:

&emsp;&emsp;`git checkout master`

<img src='../assets/2-2.2.1-6-git_checkout_master.png'/>

As you see, the `master` label is a bit special. As we add more commits, the `master` label will always point at the last commit that we make. Because of this characteristic, we usually call it a __branch__ instead. A __branch__ is simply a pointer to a specific commit -- nothing more.

In the image above, there is only one branch `master`, the *default* branch. In the next article, we will show you how to create a new branch as well as why we need to do so.

<a id='4'></a>
## 4. Practice with a Django project

You have now known the basics about `git commit`. In this section, we will start using it in a real Django project as follows:
- [First, initialize git for our project](#4.1).
- [Then, create the first commit](#4.2).
- [After that, modify the `SECRET_KEY` and commit](#4.3).
- [Finally, check out the first commit](#4.4).

<a id='4.1'></a>
### 4.1. Initialize Git

If you want use Git in your project, you must first initialize git for your project folder.


<a id='4.1.1'></a>
#### Step 1: Create a Django project

If you already created a Django project from [Article 1](./1-set-up-python-dev-env.html), you can move on to [Step 2](#4.1.2). Otherwise, you can download a sample Django project folder in the following link:

link

As you extract the zip file, make sure that you see a folder named `myserver` inside.

<a id='4.1.2'></a>
#### Step 2: Initialize Git for the project

Open your project folder `myserver` in VS Code, and toggle `Ctrl + ~`/`Cmd + ~` to open the Terminal/Command Prompt. If you type `git status`, you'll see that git currently does not track your project folder.

<img src='../assets/2-4.1-1-git_init.png'/>

To initialize Git for your project folder, type in the following command:

&emsp;&emsp;`git init`

If you do it properly, you should expect this following result:

<img src='../assets/2-4.1-2-git_init_2.png'/>

What happens when you initialize git? Git will create a hidden folder named `.git` inside of your project folder. This is where git stores all the commits along with other tracking information of your project.

<a id='4.2'></a>
### 4.2. Create the `first commit`

In reality, making a commit is a bit more complicated than in Visualization.

> ___
> There are two steps to make a commit:
> - Step 1: Specify what changes to commit
> - Step 2: Commit
> ___

#### Step 1: Specify what changes to commit
Before you can commit, you must tell Git what changes to commit. These changes can be newly added files, edited files, or removed files. There are a few commands to tell Git what to commit:

> ___
> (1) Some newly added file or edited file: `git add [path/to/that/file]`<br>
> (2) All newly added files and edited files in a specific folder: `git add [path/to/that/folder]`<br>
> (3) Some deleted file: `git rm [path/to/that/file/before/deleted]`<br>
> (4) All deleted files shown by "git status": `git rm $(git ls-files --deleted)`<br>
> ___

Here, all files are new to Git, so Git treats them as newly added files. You want to tell Git that you want to prepare all of them for the next commit. To do so, you can apply command (2) because all these newly added files are in the current folder `myserver`:

&emsp;&emsp;`git add .`

`.` stands for the current folder, which is `myserver`. Now, if you type `git status`, you can see all the changes to be committed as follows:

<img src='../assets/2-4.2-1-git-status.png'/>

#### Step 2: Commit

Great, now it's time to commit all these new files:

&emsp;&emsp;`git commit -m "first commit"`

<img src='../assets/2-4.2-2-git-commit.png'/>

To list all the commits so far with each commit written in one line, type:

&emsp;&emsp;`git log --oneline`

As shown, there is only one commit so far:

<img src='../assets/2-4.2-3-git-log.png'/>

<a id='4.3'></a>
### 4.3. Change something in the project and Commit

In file `myserver/myserver/settings.py`, change the value of `SECRET_KEY` to `'my_secret_key'`. Then, save the file.

<img src='../assets/2-4.3-1-make_changes.png'/>

Now, if you type `git status`, Git will say that it sees some changes like this:

<img src='../assets/2-4.3-2-git_status.png'/>

Let's commit this:

&emsp;&emsp;`git add .`<br>
&emsp;&emsp;`git commit -m "Modify the SECRET_KEY"`

Listing all commits out, you can now see your second commit in the log as follows:

<img src='../assets/2-4.3-3-git_log.png'/>

<a id='4.4'></a>
### 4.4. Checkout the first commit

Now, let's go back to the first commit:

&emsp;&emsp;`git checkout 4bd3424`

If you do it correctly, you can see that the `SECRET_KEY` has been reverted.

<img src='../assets/2-4.4-1-git_checkout.png'/>

You can also verify that you are currently at your first commit by `git log` as follows:

&emsp;&emsp;`git log --oneline --all`

<img src='../assets/2-4.4-2-git_log.png'/>

As you can see, `HEAD` is now at the first commit.

<a id='5'></a>
## 5. What's Next?

See you in Git Introduction - Part 2: Create Branches.
