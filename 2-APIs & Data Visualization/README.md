# 2. APIs & Data Visualization - Ahmet Uysal - 09.12.2019

This workshop provides a sample of how you can use Python to collect and visualize data from the internet. We chose a social example to hopefully make this workshop interesting for everyone. However, you can easily apply what you will learn to other topics. The main takeaway from this workshop is that you can create Python programs to automate almost everything you do online. Running this programs in large scale is powerful and generates valuable data.

## What you'll build

We will write a program that utilizes Instagram's API to collect information about usernames, profile visibility, follow and follower counts of given names. We will also look into public profiles to find the most liked post of the class.

## What you'll need

You'll only need basic Python knowledge and a computer with standard Python installation & internet access.

## Starter Code

You can find both the starter code and the final program in this repository. Please get the starter code from [here](https://kinolien.github.io/gitzip/?download=koltpython/python-workshops/tree/master/2-APIs%20&%20Data%20Visualization).

## 1. Create a Virtual Environment(venv)

We recommend you to create and a activate a virtual environment before we start. However, you can skip to [Step 2](#2-install-required-packages-using-pip).

To get more information about why using virtual environments is beneficial you can visit [_The Python Tutorial_](https://docs.python.org/3/tutorial/venv.html).

To create a new venv for the workshop:

Run `$ python3 -m venv workshop-env`

// in mac and linux

Run `$ source workshop-env/bin/activate`

// in windows

Run `$ workshop-env\Scripts\activate.bat`

## 2. Install Required Packages Using pip

Run `$ pip install -r requirements.txt`

## 3. Run the starter project.

Run `$ python main.py`

## Summary

This workshop aims to show how can Python be used to collect and visualize data. Using your Python skills, you can directly tap into data sources by sending requests to APIs.

## Links

Links to get more information about the demo, tools, other guides, etc.

- [[Video] What is an API?](https://www.youtube.com/watch?v=s7wmiS2mSXY)
- [A collective list of free APIs](https://github.com/public-apis/public-apis)
- [[Workshop] _NICAR 2018: Mining the Social Web_](https://github.com/lamthuyvo/social-media-data-scripts)
- [Matplotlib Website](https://matplotlib.org/)
- [requests library documentation](https://requests.readthedocs.io/en/master/)
