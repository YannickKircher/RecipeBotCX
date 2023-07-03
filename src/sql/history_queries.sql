delete 
from `dialogflow-recipe-guide.chatbot.user_recipe_history` 
where (user_id ="my_name") and (entry_added < (
    select entry_added 
    from `dialogflow-recipe-guide.chatbot.user_recipe_history`
    where user_id ="my_name"
    order by entry_added desc 
    limit 1 
    offset 3 
));

select entry_added 
from `dialogflow-recipe-guide.chatbot.user_recipe_history` 
order by entry_added desc 
limit 1
offset 3;

insert 
into `dialogflow-recipe-guide.chatbot.user_recipe_history` 
values("1232","test2","my_name","2021-02-15 9:55:12");

delete 
from `dialogflow-recipe-guide.chatbot.user_recipe_history` 
where (user_id ="my_name");
