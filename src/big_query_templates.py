def history_add_new_entry(client,db_table_to_query,recipe_id,recipe_name,user_id,timestamp):
    insert_query = f"""
    insert into {db_table_to_query} (recipe_id,recipe_name,user_id,entry_added)
    select * from (select "{recipe_id}","{recipe_name}","{user_id}",datetime("{timestamp}")) AS tmp
    where not exists (
        select 1 from {db_table_to_query} where recipe_id = "{recipe_id}" and user_id = "{user_id}"
    ) limit 1;
    """

    return client.query(insert_query)

def history_delete_old_entries(client,db_table_to_query,user_id):
    delete_query = f"""
            delete 
            from {db_table_to_query}
            where (user_id = "{user_id}") and entry_added < (
                select entry_added 
                from {db_table_to_query} 
                where user_id = "{user_id}"
                order by entry_added desc 
                limit 1 
                offset 3 
            )"""
    return client.query(delete_query)

def history_get_last_entries(client,db_table_to_query,user_id):
    last_entries_query = f"""
            select recipe_name 
            from {db_table_to_query}
            where user_id = "{user_id}"
            order by entry_added desc 
            limit 4
            """
    return client.query(last_entries_query)