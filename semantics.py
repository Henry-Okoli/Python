from rdflib import Graph, URIRef, Literal, Namespace, RDF

# Create a Graph
g = Graph()

# Create a Namespace
ex = Namespace("http://example.org/")

# Create some triples
alice = URIRef("http://example.org/alice")
doctor = URIRef("http://example.org/doctor")
g.add((alice, RDF.type, doctor))
g.add((alice, ex.name, Literal("Alice")))

# Serialize the graph in RDF/XML format
print(g.serialize(format="xml").encode("utf-8"))