import os
from pathlib import Path
from split_settings.tools import optional, include

#DEcouple
from decouple import Csv, config
from dotmap import DotMap

#init enviromnment
ENV = DotMap({"config": config, "Csv": Csv})

BASE_DIR = Path(__file__).resolve().parent.parent

ADMIN_PATH = ENV.config("ADMIN_PATH")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = ENV.config("DEBUG", cast = bool)

DEBUG = ENV.config("ADMIN_PATH")


include(
    'base.py',
    'utils_config.py',
)

if DEBUG:
    include('development.py')
else:
    include('production.py')



