from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Agent settings
AGENT_SETTINGS = {
    'max_reflection_depth': 3,
    'validation_threshold': 0.8,
    'enable_ml': False,
    'cache_solutions': True
}

# Logging settings
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'logs' / 'agent.log',
            'formatter': 'standard',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
        },
    },
} 