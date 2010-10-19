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
    return FamilyTree.from_json(data)


class JSONBase:
    """Base class for all JSON-related objects"""
    def to_json(self):
        return json.dumps(self.to_json_dict())

    def __repr__(self):
        return self.to_json()


class FamilyTree(JSONBase):
    @staticmethod
    def from_json(o):
        inst = FamilyTree()
        if "statusCode" in o:
            inst.statusCode = o["statusCode"]
        if "statusMessage" in o:
            inst.statusMessage = o["statusMessage"]
        if "version" in o:
            inst.version = o["version"]
        if "pedigrees" in o:
            inst.pedigrees = []
            for item in o["pedigrees"]:
                inst.pedigrees.append(Pedigree.from_json(item))
        return inst

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
    @staticmethod
    def from_json(o):
        inst = Pedigree()
        if "id" in o:
            inst.id = o["id"]
        if "requestedId" in o:
            inst.requestedId = o["requestedId"]
        if "persons" in o:
            inst.persons = []
            for item in o["persons"]:
                inst.persons.append(Person.from_json(item))
        return inst

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
    @staticmethod
    def from_json(o):
        inst = Person()
        if "id" in o:
            inst.id = o["id"]
        if "assertions" in o:
            inst.assertions = PersonAssertions.from_json(o["assertions"])
        if "parents" in o:
            inst.parents = []
            for item in o["parents"]:
                inst.parents.append(ParentsReference.from_json(item))
        return inst

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
    @staticmethod
    def from_json(o):
        inst = PersonAssertions()
        if "names" in o:
            inst.names = []
            for item in o["names"]:
                inst.names.append(NameAssertion.from_json(item))
        if "genders" in o:
            inst.genders = []
            for item in o["genders"]:
                inst.genders.append(GenderAssertion.from_json(item))
        return inst

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
    @staticmethod
    def from_json(o):
        inst = NameAssertion()
        if "value" in o:
            inst.value = NameValue.from_json(o["value"])
        return inst

    def to_json_dict(self):
        d = {}
        if hasattr(self, "value"):
            d["value"] = self.value.to_json_dict()
        return d


class NameValue(JSONBase):
    @staticmethod
    def from_json(o):
        inst = NameValue()
        if "forms" in o:
            inst.forms = []
            for item in o["forms"]:
                inst.forms.append(NameForm.from_json(item))
        return inst

    def to_json_dict(self):
        d = {}
        if hasattr(self, "forms"):
            a = []
            for item in self.forms:
                a.append(item.to_json_dict())
            d["forms"] = a
        return d


class NameForm(JSONBase):
    @staticmethod
    def from_json(o):
        inst = NameForm()
        if "fullText" in o:
            inst.fullText = o["fullText"]
        return inst

    def to_json_dict(self):
        d = {}
        if hasattr(self, "fullText"):
            d["fullText"] = self.fullText
        return d


class GenderAssertion(JSONBase):
    @staticmethod
    def from_json(o):
        inst = GenderAssertion()
        if "value" in o:
            inst.value = GenderValue.from_json(o["value"])
        return inst

    def to_json_dict(self):
        d = {}
        if hasattr(self, "value"):
            d["value"] = self.value.to_json_dict()
        return d


class GenderValue(JSONBase):
    @staticmethod
    def from_json(o):
        inst = GenderValue()
        if "type" in o:
            inst.type = o["type"]
        return inst

    def to_json_dict(self):
        d = {}
        if hasattr(self, "type"):
            d["type"] = self.type
        return d


class ParentsReference(JSONBase):
    @staticmethod
    def from_json(o):
        inst = ParentsReference()
        if "parent" in o:
            inst.parents = []
            for item in o["parent"]:
                inst.parents.append(PersonReference.from_json(item))
        return inst

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
    @staticmethod
    def from_json(o):
        inst = PersonReference()
        if "id" in o:
            inst.id = o["id"]
        if "gender" in o:
            inst.gender = o["gender"]
        return inst

    def to_json_dict(self):
        d = {}
        if hasattr(self, "id"):
            d["id"] = self.id
        if hasattr(self, "gender"):
            d["gender"] = self.gender
        return d
