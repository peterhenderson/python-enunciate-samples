try:
    import json
except ImportError:
    import simplejson as json


def parse(input):
    """Parse specified file or string and return a FamilyTree object created from it."""
    if hasattr(input, "read"):
        data = json.load(input)
    else:
        data = json.loads(input)
    return FamilyTree(data)


class JSONBase:
    """Base class for all JSON-related objects"""
    def to_json(self):
        return json.dumps(self.to_json_dict())

    def __repr__(self):
        return self.to_json()


class FamilyTree(JSONBase):
    def __init__(self, o):
        if "statusCode" in o:
            self.statusCode = o["statusCode"]
        if "statusMessage" in o:
            self.statusMessage = o["statusMessage"]
        if "version" in o:
            self.version = o["version"]
        if "pedigrees" in o:
            self.pedigrees = []
            for item in o["pedigrees"]:
                self.pedigrees.append(Pedigree(item))

    def to_json_dict(self):
        d = {}
        if hasattr(self, "statusCode"):
            d["statusCode"] = self.statusCode
        if hasattr(self, "statusMessage"):
            d["statusMessage"] = self.statusMessage
        if hasattr(self, "version"):
            d["version"] = self.version
        if hasattr(self, "pedigrees"):
            a = []
            for item in self.pedigrees:
                a.append(item.to_json_dict())
            d["pedigrees"] = a
        return d


class Pedigree(JSONBase):
    def __init__(self, o):
        if "id" in o:
            self.id = o["id"]
        if "requestedId" in o:
            self.requestedId = o["requestedId"]
        if "persons" in o:
            self.persons = []
            for item in o["persons"]:
                self.persons.append(Person(item))

    def to_json_dict(self):
        d = {}
        if hasattr(self, "id"):
            d["id"] = self.id
        if hasattr(self, "requestedId"):
            d["requestedId"] = self.requestedId
        if hasattr(self, "persons"):
            a = []
            for item in self.persons:
                a.append(item.to_json_dict())
            d["persons"] = a
        return d


class Person(JSONBase):
    def __init__(self, o):
        if "id" in o:
            self.id = o["id"]
        if "assertions" in o:
            self.assertions = PersonAssertions(o["assertions"])
        if "parents" in o:
            self.parents = []
            for item in o["parents"]:
                self.parents.append(ParentsReference(item))

    def to_json_dict(self):
        d = {}
        if hasattr(self, "id"):
            d["id"] = self.id
        if hasattr(self, "assertions"):
            d["assertions"] = self.assertions.to_json_dict()
        if hasattr(self, "parents"):
            a = []
            for item in self.parents:
                a.append(item.to_json_dict())
            d["parents"] = a
        return d


class PersonAssertions(JSONBase):
    def __init__(self, o):
        if "names" in o:
            self.names = []
            for item in o["names"]:
                self.names.append(NameAssertion(item))
        if "genders" in o:
            self.genders = []
            for item in o["genders"]:
                self.genders.append(GenderAssertion(item))

    def to_json_dict(self):
        d = {}
        if hasattr(self, "names"):
            a = []
            for item in self.names:
                a.append(item.to_json_dict())
            d["names"] = a
        if hasattr(self, "genders"):
            a = []
            for item in self.genders:
                a.append(item.to_json_dict())
            d["genders"] = a
        return d


class NameAssertion(JSONBase):
    def __init__(self, o):
        if "value" in o:
            self.value = NameValue(o["value"])

    def to_json_dict(self):
        d = {}
        if hasattr(self, "value"):
            d["value"] = self.value.to_json_dict()
        return d


class NameValue(JSONBase):
    def __init__(self, o):
        if "forms" in o:
            self.forms = []
            for item in o["forms"]:
                self.forms.append(NameForm(item))

    def to_json_dict(self):
        d = {}
        if hasattr(self, "forms"):
            a = []
            for item in self.forms:
                a.append(item.to_json_dict())
            d["forms"] = a
        return d


class NameForm(JSONBase):
    def __init__(self, o):
        if "fullText" in o:
            self.fullText = o["fullText"]

    def to_json_dict(self):
        d = {}
        if hasattr(self, "fullText"):
            d["fullText"] = self.fullText
        return d


class GenderAssertion(JSONBase):
    def __init__(self, o):
        if "value" in o:
            self.value = GenderValue(o["value"])

    def to_json_dict(self):
        d = {}
        if hasattr(self, "value"):
            d["value"] = self.value.to_json_dict()
        return d


class GenderValue(JSONBase):
    def __init__(self, o):
        if "type" in o:
            self.type = o["type"]

    def to_json_dict(self):
        d = {}
        if hasattr(self, "type"):
            d["type"] = self.type
        return d


class ParentsReference(JSONBase):
    def __init__(self, o):
        if "parent" in o:
            self.parents = []
            for item in o["parent"]:
                self.parents.append(PersonReference(item))

    def to_json_dict(self):
        d = {}
        if hasattr(self, "parents"):
            a = []
            for item in self.parents:
                a.append(item.to_json_dict())
            d["parent"] = a
            d["parents"] = a
        return d


class PersonReference(JSONBase):
    def __init__(self, o):
        if "id" in o:
            self.id = o["id"]
        if "gender" in o:
            self.gender = o["gender"]

    def to_json_dict(self):
        d = {}
        if hasattr(self, "id"):
            d["id"] = self.id
        if hasattr(self, "gender"):
            d["gender"] = self.gender
        return d
