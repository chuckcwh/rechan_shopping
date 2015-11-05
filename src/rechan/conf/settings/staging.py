from base import *

DATABASES['default']['NAME'] = get_env_setting('rechan_DB_NAME', 'rechan_staging')
# DATABASES['default']['USER'] = get_env_setting('rechan_DB_USER', 'rechan')
# DATABASES['default']['PASSWORD'] = get_env_setting('rechan_DB_PASSWORD', 'jaguar_db_p@$$w0rd')
# DATABASES['default']['HOST'] = get_env_setting('rechan_DB_HOST', 'ec2-52-24-226-149.us-west-2.compute.amazonaws.com')

COMPRESS_OFFLINE = True

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_LOCATION = 'staging'
