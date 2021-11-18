# Language Classifier

This project focuses on training an algorithm to correctly identify the language that the user types in.

The algorithms I used were:
  - K Nearest Neighbors
  - Multinomial Naive Bayes
  - Random Forest

Out of these three algorithms, **multinomial nayes bayes** performed the best (although random forest was a close second).

*Note:* In case you're wondering how I chose the parameters for each algorithm: I used `RandomizedSearchCV` from the sci-kit learn library to arrive at those parameters. I did not include the code for this because it took a long time to run each time.

# How to Run the Application
There are two ways to run the Streamlit web application:

### Visit the website
The simplest way to view the web app is by visiting the following link: https://share.streamlit.io/johng034/language-classifier/app.py

### Run locally
If you wish to run the application on your machine, then complete the following steps:
1. [**Clone** the repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
2. **Open the folder of this repository** in your editor of choice (or in the terminal/command prompt)
3. In the terminal, **install the packages** with `pip install requirements.txt` (you may want to install using a [virtual environment](https://docs.python.org/3/tutorial/venv.html) for this)
4. Once the packages are installed, you can **run the streamlit application** by typing `streamlit run app.py` in the terminal
