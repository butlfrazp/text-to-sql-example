from config import config, Config
from langchain.llms import AzureOpenAI
from langchain.chat_models import ChatOpenAI
from langchain import SQLDatabase
from chains.sql_database_non_execution_chain import SQLDatabaseNonExecutingChain


def _create_llm(config: Config):
    llm = None
    if config.is_azure_openai_api:
        llm = AzureOpenAI(deployment_name="chatgpt", model_name="gpt-35-turbo")
    else:
        llm = ChatOpenAI(model="gpt-3.5-turbo")
    return llm


def main(config: Config):
    print('starting the main function...')

    llm = _create_llm(config)
    db = SQLDatabase.from_uri(config.db_uri)
    db_chain = SQLDatabaseNonExecutingChain.from_llm(llm, db)

    query = input("Enter a query in english: ")

    results = db_chain.run(query)
    print("Results:", results)

if __name__ == "__main__":
    main(config)
