## 1.what to do first?
- open ilect  
- click 'file>new>terminal'  
- enter **`cd userspace`**  
- enter **`git clone -b develop   https://github.com/weben2018-team-f/UTalk.git`**  
- enter **`cd UTalk`**  
- enter **`git config --global user.name <yourname>`**  
- enter **`git config --global user.email <yourmail>`**  
- enter **`git checkout -b <your functions name>`**  

Then, let's start your part!

</n>　　
</n>　　
</n>　　
</n>　　

## 2.The description of folder struscture 
- UTalk
    - db  
        contain .json files
    - routes  
        the folder which contain all of .py files. 
    - static
        - css
        - js
        - images
    - templatess  
        the folder which contain html files.
- runserver.py  
    exec this file to start this app

</n>　　
</n>　　
</n>　　
</n>　　


## 3.how to develop?  
- when making .py file  
    - Make '~.py' file in 'UTalk/UTalk/routes' folder  
    - Add 'import UTalk.routes.~' in the end of 'UTalk/UTalk/\__init__.py' file.  **Do not delete! Only add!**  
    
    
- when coding  
    baseically, you develop your code on develop branch or branches you make from develop branch, not on master branch! And **do not push to maseter branch on github!**  