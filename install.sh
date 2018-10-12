echo "Installing virtual environment and requirements."
pip install --upgrade pip
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
echo "Now creating the example database."
python3 install.py
echo "You may now use the script: launch.sh to launch the app."
