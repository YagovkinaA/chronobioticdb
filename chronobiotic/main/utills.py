from django.conf import settings

def get_agent_url():
    from decouple import config
    return config('AI_AGENT_URL')