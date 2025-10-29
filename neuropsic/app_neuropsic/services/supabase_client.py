from django.conf import settings
from supabase import create_client, Client

_supabase: Client | None = None

def get_supabase_client():
    global _supabase
    if _supabase is None:
        if not settings.SUPABASE_URL or not settings.SUPABASE_KEY:
            raise RuntimeError("SUPABASE_URL and SUPABASE_KEY must be set in settings.")
        _supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)
    return _supabase
