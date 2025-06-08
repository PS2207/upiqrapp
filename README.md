folders:
bin buildozer.spec kivy_env kivyenv pyjnius venv
*buildozer.spec: This is the configuration file used by Buildozer to package Kivy apps for Android. 
                It contains settings like- app name, version, requirements, permissions etc.
*venv- These are likely virtual environments created to isolate python packages for kivy projects. 
      source kivy_env/bin/activate , source kivyenv/bin/activate , source venv/bin/activate - used to activate different python virtual environments.
*virtual environment- This is self-contained directory that contains Python interpreter & isolated installed packages.
                     which environment is best to use among all? then it depends on which has the correct packages installed.
 System-level tools- Pyhton3, pip3, git can stay global.
 Project-specific tools- kivy, buildozer,pyjnius etc. should be installed in virtual environment.
 Always activate venv before installing or running app.
