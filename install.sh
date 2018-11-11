echo "Installing virtual environment and requirements."
python3 -m venv venv
. venv/bin/activate
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo "Now installing the example database."
python3 install.py
echo "You may now use the script: launch.sh to launch the app."
