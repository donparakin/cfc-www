# ./x-dev: Developer Files

./x-dev contains files not specific to the run-time of the application
(instead of intermingling, placing files here avoids clutter and confusion).

## Development Environment Setup

1. Get code from Github.com
    * `git clone ...`
 
3. Create and activate a Python virtual environment
    * Windows:
      * `cd fintrakr.github`
      * `py -3.11 -m venv venv --prompt fintrakr`
      * `venv\Scripts\activate`
      * `python.exe -m pip install --upgrade pip` 
 
4. Install Python libraries:
    * Windows: 
      * `pip install -r .\x-dev\python\requirements.txt`

5. Install Node libraries:
   * Windows:
      * `cd fintrakr.github\x-dev`
      * `npm install`
      * `npm run build:dev`

6. (For Prod)
   * Windows:
      * `python manage.py collectstatic`
      * ...
