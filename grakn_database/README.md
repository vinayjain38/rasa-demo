Our knowledge base implementation uses the graph database [grakn](http://grakn.ai/).

To start the grakn server run `grakn server start`, to stop it run `grakn server stop`.
In order to create the keyspace `rasa_demo` with the schema defined in `schema.gql`, you need to execute

```bash
graql console --keyspace rasa_demo --file schema.gql
```

If you want to delete data from the keyspace `rasa_demo` you need to execute the following steps:
1. Start the graql console with `graql console --keyspace rasa_demo`.
2. Delete data by typing the command `clean`. 
    You need to confirm that you really want to delete your data by typing in `confirm`. 

After you created your clean schema, you need to fill it with some data.
The initial data are located in the `data` directory as `csv` files.
To load the data into your grakn database, run `python migrate.py`. 
