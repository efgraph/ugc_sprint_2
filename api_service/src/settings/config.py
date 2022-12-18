from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    project_name: str = Field('api', env='PROJECT_NAME')
    kafka_host: str = Field('localhost', env='KAFKA_HOST')
    kafka_port: int = Field(9092, env='KAFKA_PORT')
    kafka_topic: str = Field('rating', env='KAFKA_TOPIC')
    kafka_rating_client_id = Field('ugc_rating', env='KAFKA_RATING_CLIENT_ID')
    kafka_consumer_group = Field('group-id', env='KAFKA_CONSUMER_GROUP')


settings = Settings()
print(settings.project_name, settings.kafka_host, settings.kafka_port)