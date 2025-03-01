# sample_streamlit_hello_world
#Ref: https://github.com/utkarshminds/sample_streamlit_hello_world
Sample website using streamlit and generative AI
#install git, vs code, sign in on github.com and streamlit.io, python

# 1- sign in to github.com
# 2- create a repo, create personal branch and copy clone url

# 3- clone repo on vs code and change from main to our branch
# 4- open new terminal and create virtual env

# Step 4a - To Set your github username type in terminal

git config --global user.name "username"

# Step 4b - To Set your github email type in terminal Set your email address: 

git config --global user.email "MY_NAME@example.com"

# Go to extensions on left panel of vs code
and check and install the extensions
- python debugger, isort, python, pylance

# 5- type in terminal -> python -m venv myenv_name
# 5a type in terminal -> 
# 6- activate venv -> myenv_name/Scripts/activate
# 7- type in terminal and press enter
        python.exe -m pip install --upgrade pip
        pip install streamlit
        pip install google-generativeai
        pip install numpy
        pip install pandas
        pip install matplotlib
        pip install pipreqs

# IN CASE ERROR IN STEP 5 
# Press Ctrl + Shift + P
    Type in top bar python create environment
    Select venv
    type in terminal .venv/scripts/activate
    then continue from step 7

# IN CASE ERROR IN STEP 6
# Press Ctrl + Shift + P
    type in terminal 
    Set-ExecutionPolicy RemoteSigned
    Press enter
    then continue from step 6

# Step 8 - Create a file named app.py
            Put your website code in that file

# Step 8a - Create requirements.txt file
            type in terminal pipreqs --ignore myenv_name/ --force

# 9- Add new entry to .gitignore 
      myenv_name/
    then save

# 10 - go to Source control
        click on stage change
        then stage all changes
        then add commit message
        then commit and sync

#Altenative Step 10 using terminal
    git branch branch_name (creating new branch)
    git checkout branch_name (switching from one branch to another)
    git status (finding file changes)
    git add filename.py (staging file for commit)
    git commit -m 'commit message' (commit)
    git push (sync to remote branch)

# 11 - go to github.com and compare and pull request with main. Then merge and confirm merge.

# 12 - go to streamlit.io
        click on deploy from github
        copy paste repo url
        select branch
        select file
        click deploy

