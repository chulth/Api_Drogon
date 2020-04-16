from setuptools import setup

setup  (

     name = 'Api',
     version = '0.0.1',
     py_modules =['api'],
     install_requires =[
         'Click',
     ],
     entry_points ='''
     [console_points]
     api = api:cli
     ''',

)   
           


