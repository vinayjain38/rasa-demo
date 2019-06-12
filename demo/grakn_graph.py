import logging
from typing import List, Dict, Any

import grakn

logger = logging.getLogger(__name__)


class GraknGraph:
    def __init__(self, uri="localhost:48555", keyspace="banking"):
        self.client = grakn.Grakn(uri=uri)
        self.keyspace = keyspace

    def _execute_entity_query(self, query) -> List[Dict]:
        with self.client.session(keyspace=self.keyspace) as session:
            with session.transaction(grakn.TxType.READ) as tx:
                logger.debug("Executing Graql Query: " + query)
                result = tx.query(query)

                concepts = result.collect_concepts()

                entities = []

                for c in concepts:
                    attrs = c.attributes()
                    entity = {"id": c.id}
                    for each in attrs:
                        entity[each.type().label()] = each.value()
                    entities.append(entity)

                return entities

    def _execute_attribute_query(self, query) -> List[Any]:
        with self.client.session(keyspace=self.keyspace) as session:
            with session.transaction(grakn.TxType.READ) as tx:
                logger.debug("Executing Graql Query: " + query)
                result = tx.query(query)

                concepts = result.collect_concepts()
                return [c.value() for c in concepts]

    def get_attribute_of(self, entity_type="product", entity="Rasa", attribute="type"):
        return self._execute_attribute_query(
            f"match $x isa {entity_type}, has name '{entity}', has {attribute} $a; get $a;"
        )

    def get_entities(self, entity_type="product"):
        return self._execute_entity_query(f"match $x isa {entity_type}; get;")[:10]

    def lookup(self, lookup_type="mention-lookup", lookup_key="one"):
        value = self._execute_attribute_query(
            f""" 
            match
              $lookup isa {lookup_type}, has lookup-key '{lookup_key}', has lookup-value $v;
            get $v;
            """
        )

        if value and len(value) == 1:
            return value[0]

        return None
