try:
    import json
except ImportError:
    import simplejson as json


def parse(input):
    """Parse specified file or string and return an Identity object created from it."""
    if hasattr(input, "read"):
        data = json.load(input)
    else:
        data = json.loads(input)
    return Identity.from_json(data)


class JSONBase:
    """Base class for all JSON-related objects"""
    def to_json(self):
        return json.dumps(self.to_json_dict())

    def __repr__(self):
        return self.to_json()


class FSDict(dict):
    """Convenience class to access FamilySearch-style property lists as dictionaries
    
    For example,
        [{"name": "key1", "value": "value1"}, {"name": "key2", "value": "value2"}]
    converts to
        {"key1": "value1", "key2": "value2"}
    
    """
    
    def __init__(self, pairs=None):
        if isinstance(pairs, list) and all((isinstance(pair, dict) for pair in pairs)):
            dict.__init__(self)
            for pair in pairs:
                self[pair["name"]] = pair["value"]

    def put(self, prop):
        self[prop["name"]] = prop["value"]
    
    def to_json_array(self):
        return [{"name": key, "value": self[key]} for key in self]


class Identity(JSONBase):
    @staticmethod
    def from_json(o):
        inst = Identity()
        if "statusCode" in o:
            inst.statusCode = o["statusCode"]
        if "statusMessage" in o:
            inst.statusMessage = o["statusMessage"]
        if "version" in o:
            inst.version = o["version"]
        if "properties" in o:
            inst.properties = FSDict(o["properties"])
        return inst

    def to_json_dict(self):
        d = {}
        if hasattr(self, "statusCode"):
            d["statusCode"] = self.statusCode
        if hasattr(self, "statusMessage"):
            d["statusMessage"] = self.statusMessage
        if hasattr(self, "version"):
            d["version"] = self.version
        if hasattr(self, "properties"):
            d["properties"] = self.properties.to_json_array()
        return d


class Property(JSONBase):
    @staticmethod
    def from_json(o):
        inst = Property()
        if "name" in o:
            inst.name = o["name"]
        if "value" in o:
            inst.value = o["value"]
        return inst

    def to_json_dict(self):
        d = {}
        if hasattr(self, "name"):
            d["name"] = self.name
        if hasattr(self, "value"):
            d["value"] = self.value
        return d
