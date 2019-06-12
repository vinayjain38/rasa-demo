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
    graql_insert_query += ", has _id " + product["_id"]
    graql_insert_query += ', has name "' + product["name"] + '"'
    graql_insert_query += ", has version " + product["version"]
    graql_insert_query += (
        ', has installation-command "' + product["installation-command"] + '"'
    )
    graql_insert_query += ', has type "' + product["type"] + '"'
    graql_insert_query += (
        ", has minimal-python-version " + product["minimal-python-version"]
    )
    graql_insert_query += (
        ", has recommended-python-version " + product["recommended-python-version"]
    )
    graql_insert_query += (
        ', has documentation-link "' + product["documentation-link"] + '"'
    )
    graql_insert_query += ', has source-code "' + product["source-code"] + '"'
    graql_insert_query += ";"
    return graql_insert_query


def company_template(company):
    graql_insert_query = "insert $company isa company"
    graql_insert_query += ", has _id " + company["_id"]
    graql_insert_query += ', has name "' + company["name"] + '"'
    graql_insert_query += ', has short-name "' + company["short-name"] + '"'
    graql_insert_query += ', has headquarter "' + company["headquarter"] + '"'
    graql_insert_query += ', has forum-link "' + company["forum-link"] + '"'
    graql_insert_query += ', has blog-link "' + company["blog-link"] + '"'
    graql_insert_query += ', has website "' + company["website"] + '"'
    graql_insert_query += ";"
    return graql_insert_query


def rasa_documentation_template(docu):
    graql_insert_query = "insert $docu isa rasa-documentation"
    graql_insert_query += ", has _id " + docu["_id"]
    graql_insert_query += ', has name "' + docu["name"] + '"'
    graql_insert_query += ', has link "' + docu["link"] + '"'
    graql_insert_query += ";"
    return graql_insert_query


def rasa_x_documentation_template(docu):
    graql_insert_query = "insert $docu isa rasa-x-documentation"
    graql_insert_query += ", has _id " + docu["_id"]
    graql_insert_query += ', has name "' + docu["name"] + '"'
    graql_insert_query += ', has link "' + docu["link"] + '"'
    graql_insert_query += ";"
    return graql_insert_query


def rasa_x_ee_documentation_template(docu):
    graql_insert_query = "insert $docu isa rasa-x-ee-documentation"
    graql_insert_query += ", has _id " + docu["_id"]
    graql_insert_query += ', has name "' + docu["name"] + '"'
    graql_insert_query += ', has link "' + docu["link"] + '"'
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


def includes_template(include):
    graql_insert_query = (
        'match $documentation isa documentation, has _id "'
        + include["_documentation"]
        + '";'
    )
    graql_insert_query += (
        ' $product isa product, has _id "' + include["_product"] + '";'
    )
    graql_insert_query += (
        " insert (_product: $product, _documentation: $documentation) isa includes;"
    )
    return graql_insert_query


def owns_template(include):
    graql_insert_query = (
        'match $company isa company, has _id "' + include["_company"] + '";'
    )
    graql_insert_query += (
        ' $product isa product, has _id "' + include["_product"] + '";'
    )
    graql_insert_query += (
        " insert (_product: $product, _company: $company) isa includes;"
    )
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
        {"data_path": "./data/company", "template": company_template},
        {
            "data_path": "./data/rasa-documentation",
            "template": rasa_documentation_template,
        },
        {
            "data_path": "./data/rasa-x-documentation",
            "template": rasa_x_documentation_template,
        },
        {
            "data_path": "./data/rasa-x-ee-documentation",
            "template": rasa_x_ee_documentation_template,
        },
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
