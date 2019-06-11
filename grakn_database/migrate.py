import grakn
import csv


def build_rasa_demo_graph(data):
    client = grakn.Grakn(uri="localhost:48555")
    with client.session(keyspace="rasa_demo") as session:
        for data_obj in data:
            print(f"Loading data from [{data_obj['data_path']}] into Grakn ...")
            load_data_into_grakn(data_obj, session)


def load_data_into_grakn(data_obj, session):
    items = parse_data_to_dictionaries(data_obj)

    for item in items:
        with session.transaction(grakn.TxType.WRITE) as tx:
            graql_insert_query = data_obj["template"](item)
            tx.query(graql_insert_query)
            tx.commit()

    print(
        f"Inserted {str(len(items))} items from [{data_obj['data_path']}] into Grakn."
    )


def product_template(product):
    graql_insert_query = "insert $product isa product"
    graql_insert_query += ', has name "' + product["name"] + '"'
    graql_insert_query += ', has version "' + product["version"] + '"'
    graql_insert_query += (
        ', has documentation-link "' + product["documentation-link"] + '"'
    )
    graql_insert_query += (
        ', has installation-command "' + product["installation-command"] + '"'
    )
    graql_insert_query += ', has type "' + product["type"] + '"'
    graql_insert_query += ";"
    return graql_insert_query


def attribute_lookup_template(lookup):
    graql_insert_query = "insert $lookup isa attribute-lookup"
    graql_insert_query += ", has lookup-key '" + lookup["lookup-key"] + "'"
    graql_insert_query += ", has lookup-value '" + lookup["lookup-value"] + "'"
    graql_insert_query += ";"
    return graql_insert_query


def entity_key_lookup_template(lookup):
    graql_insert_query = "insert $lookup isa entity-key-lookup"
    graql_insert_query += ", has lookup-key '" + lookup["lookup-key"] + "'"
    graql_insert_query += ", has lookup-value '" + lookup["lookup-value"] + "'"
    graql_insert_query += ";"
    return graql_insert_query


def entity_type_lookup_template(lookup):
    graql_insert_query = "insert $lookup isa entity-type-lookup"
    graql_insert_query += ", has lookup-key '" + lookup["lookup-key"] + "'"
    graql_insert_query += ", has lookup-value '" + lookup["lookup-value"] + "'"
    graql_insert_query += ";"
    return graql_insert_query


def mention_lookup_template(lookup):
    graql_insert_query = "insert $lookup isa mention-lookup"
    graql_insert_query += ", has lookup-key '" + lookup["lookup-key"] + "'"
    graql_insert_query += ", has lookup-value '" + lookup["lookup-value"] + "'"
    graql_insert_query += ";"
    return graql_insert_query


def parse_data_to_dictionaries(input):
    items = []
    with open(input["data_path"] + ".csv") as data:  # 1
        for row in csv.DictReader(data, skipinitialspace=True):
            item = {key: value for key, value in row.items()}
            items.append(item)  # 2
    return items


if __name__ == "__main__":
    inputs = [
        {"data_path": "./data/product", "template": product_template},
        {"data_path": "./data/attribute_lookup", "template": attribute_lookup_template},
        {"data_path": "./data/mention_lookup", "template": mention_lookup_template},
        {
            "data_path": "./data/entity_key_lookup",
            "template": entity_key_lookup_template,
        },
        {
            "data_path": "./data/entity_type_lookup",
            "template": entity_type_lookup_template,
        },
    ]

    build_rasa_demo_graph(inputs)
