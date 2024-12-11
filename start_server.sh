if ! command -v pipenv &> /dev/null
then
    echo "pipenv could not be found, installing..."
    pip install pipenv
fi


echo "Installing dependencies..."
pipenv shell
pipenv install

echo "Starting Python server..."
pipenv run python src/main.py  
