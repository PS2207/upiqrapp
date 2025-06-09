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

 How to Run a Windows Kivy App on Ubuntu(WSL) Terminal-
 1.Open Ubuntu(Windows Subsystem for Linux) Terminal
 2.Navigate or copy your Kivy Project directory in wsl using- 
 (rsync -av --progress --exclude .buildozer --exclude bin /mnt/c/Users/psinh/Desktop/upiqrapp/ ~/upiqrapp) then navigate- cd upiqrapp

 lets say app(upiqrapp) is on desktop path(C:\users\psinh\desktop\upiqrapp)- so change path using this- 'cd /mnt/c/users/psinh/desktop/upiqrapp'
 now run this using this command- 'python main.py'
 3.Activate your virtual environment(if you have one) or else
 create using (python3 -m venv venv_name) then,
 activate using (source venv/bin/activate)&   for deactiving venv use - (deactivate).
 4.Run your Kivy app using - (python main.py)
 5.Build your kivy app  using Buildozer to create 'apk file' for Android
