from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: int 
    API_HASH: str 

    LOGIN_SLEEP: list[int] = [60, 360]
    MINI_SLEEP: list[int] = [5, 15]
    BIG_SLEEP: list[int] = [10800, 18000]

    BOT_MOOD_SEQUENTIAL: bool= False
    ACCOUNTS_MOOD_SEQUENTIAL: bool= True



    ACTIVE_BOTS: dict[str, dict] = {
        "blum": {"Active": True, "REF_ID": "ref_oDxBEC33Wa"},
        "catsgang": {"Active": False, "REF_ID": "crQMLYMdqEEW4rV-ui-1h"},
        "catsvsdogs": {"Active": True, "REF_ID": "558455838"},
        "cexio": {"Active": True, "REF_ID": "1716374168523141"},
        "goats": {"Active": True, "REF_ID": "37d06dc8-fa31-4272-b9df-5f74d12cb6f8"},
        "major": {"Active": True, "REF_ID": "558455838"},
        "notpixel": {"Active": True, "REF_ID": "f558455838"},
        "tomarket": {"Active": True, "REF_ID": "000079hx"}
    }
    


global_settings = Settings()