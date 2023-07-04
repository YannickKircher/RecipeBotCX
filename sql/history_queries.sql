delete 
from `dialogflow-recipe-guide.chatbot.user_recipe_history` 
where user_id ="example_user_id" and entry_added < (
    select entry_added 
    from `dialogflow-recipe-guide.chatbot.user_recipe_history`
    where user_id ="example_user_id"
    order by entry_added desc 
    limit 1 
    offset 3 
);


#get history
select recipe_name 
from `dialogflow-recipe-guide.chatbot.user_recipe_history`
where user_id ="my_name"
order by entry_added desc 
limit 4;


# insert into user_recipe_history
INSERT INTO `dialogflow-recipe-guide.chatbot.user_recipe_history` (recipe_id,recipe_name,user_id,entry_added)
SELECT * FROM (SELECT "649f430b789dc8b6c1385d90","test2","example_user_id",datetime("2021-02-15 9:55:12")) AS tmp
WHERE NOT EXISTS (
    SELECT 1 FROM `dialogflow-recipe-guide.chatbot.user_recipe_history` WHERE recipe_id = "649f430b789dc8b6c1385d90" and user_id = "example_user_id"
) LIMIT 1;