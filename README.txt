STEP 1.
RUN appication with following python command

python main.py

STEP 
INSTALL pytest on the system for testing with following command

pip install pytest

STEP 2.
RUN Python weather app test cases with following command

pytest test_weather_app.py


STEP 
INSTALL paytest-cov on the system for code coverage with following command
python -m pip install pytest-cov

STEP 3.
RUN Python weather app code coverage with following command

python -m pytest --cov=weather_app test_weather_app.py

STEP 4. (Optional to generate HTML format Report)
RUN Python weather app code coverage with following command

python -m pytest --cov=weather_app --cov-report=html test_weather_app.py