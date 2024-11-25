@echo off

echo Running tests...

pytest --alluredir=Allure_Report --cov=Tests/

echo Opening Allure report...

allure serve Allure-Report
