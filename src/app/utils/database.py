from configs.app_settings import settings

# this is WIP 

DATABASE_URL = "postgresql://{}:{}@{}:{}/{}?sslmode={}".format(
        settings.db_username, settings.db_password, settings.host_server, settings.db_server_port, settings.database_name, settings.ssl_mode
    )