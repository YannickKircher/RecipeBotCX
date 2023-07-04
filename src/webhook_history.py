from google.cloud import bigquery
import pymongo
from configparser import ConfigParser
from json_return import json_history_selection, json_text_response, json_recipe_data
from big_query_templates import history_get_last_entries
from pandas import DataFrame

def main(request):

    request_json = request.get_json(silent=True)
    
    intent = request_json.get("intentInfo",{"None":None}).get("displayName",None)
    webhook_call_tag = request_json["fulfillmentInfo"]['tag']
    
    if webhook_call_tag == "history display":
        client = bigquery.Client()
        db_table_to_query = "`dialogflow-recipe-guide.chatbot.user_recipe_history`"
        query_job = history_get_last_entries(client,db_table_to_query,"example_user_id")
        result_df = DataFrame([dict(row) for row in query_job])
        recipe_names = result_df["recipe_name"].tolist()
        
        #response
        return json_history_selection("Those are the last ones, pick one.",recipe_names)
    
    elif webhook_call_tag == "history get recipe":
        print(webhook_call_tag)
        recipe_name = request_json["text"].lstrip("show ")
        
        #read mogodb password from config file
        config = ConfigParser()
        config.read("secrets_recipe_bot.ini")
        MONGO_DB_PW = config["SECRETS"]["MONGO_DB_PW"]

        # mongo db init
        mongo_client = pymongo.MongoClient(f"mongodb+srv://kircheryannick:{MONGO_DB_PW}@cluster0.fvwxqpp.mongodb.net/?retryWrites=true&w=majority")
        recipes_collection = mongo_client["chatbot"]["recipes"]
        
        recipe = [x for x in recipes_collection.find({"title": {"$regex" : recipe_name, "$options" : "i"}}).limit(1)][0]

        recipe_id = str(recipe["_id"])
        recipe_name = recipe["title"]
        recipe_ingredients = recipe["ingredients"]
        recipe_instructions = recipe["directions"]
        
        return json_recipe_data(recipe_id,
                            "",
                            recipe_name,
                            recipe_ingredients,
                            recipe_instructions
                            )

    else:
        return json_text_response("I don't know what to do.")