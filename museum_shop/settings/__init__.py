from .base import *
env_type = config('ENV_NAME')

if env_type == 'production':
    from .prod import *
elif env_type == 'local':
    from .local import *
elif env_type == 'staging':
    from .staging import *
else:
    print('No environment chosen!')