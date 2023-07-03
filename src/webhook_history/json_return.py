def json_history_selection(into_message,recipe_names,content_type="chips"):
  return {
    "fulfillment_response":{
      "messages":[
          {
            "text": {
              "text": [into_message]
            }
          },
          { 
            "payload":{
                "richContent": [
                  [ 
                    {
                      "options": [{"text": "show "+recipe} for recipe in recipe_names],
                      "type": content_type
                    }
                  ]
                ]
            }
          }
      ]
    }
  }

def json_recipe_data(recipe_id,into_message,recipe_name,ingredients,directions):
  
  lines = [into_message]+[recipe_name]+["\n".join(["Ingredients:"]+ingredients)]+["\n".join(["Directions:"]+directions)]
  
  return {
   "fulfillment_response": {
     "messages": [
       {
         "text": {
           "text": [line]
         }
       } for line in lines 
     ]
   },
   "sessionInfo": {
     "parameters": {
          "recipe_id": recipe_id
     }
   }
 }
  

def json_text_response(text):
  return {
   "fulfillment_response": {
     "messages": [
       {
         "text": {
           "text": [text]
         }
       } 
     ]
   }
 }