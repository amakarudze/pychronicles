import os 

env = os.getenv("DJANGO_ENV", "dev") # noqa: F405

if env == "prod":
    from .prod import * # noqa: F403
else: 
    from .dev import * # noqa: F403
