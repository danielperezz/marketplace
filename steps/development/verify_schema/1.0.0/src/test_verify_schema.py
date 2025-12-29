from verify_schema import VerifySchema

class TestVerifySchema:
    def test_verify_schema_success(self):
        schema = {
            "id": int,
            "name": str,
            "active": bool
        }
        verifier = VerifySchema(name="test_verifier", context=None, schema=schema)
        event = {
            "id": 1,
            "name": "Test Event",
            "active": True
        }
        result = verifier.do(event)
        assert result == event

    def test_verify_schema_missing_key(self):
        schema = {
            "id": int,
            "name": str,
            "active": bool
        }
        verifier = VerifySchema(name="test_verifier", context=None, schema=schema)
        event = {
            "id": 1,
            "name": "Test Event"
        }
        try:
            verifier.do(event)
        except KeyError as e:
            assert "key 'active' not found in event" in str(e)

    def test_verify_schema_wrong_type(self):
        schema = {
            "id": int,
            "name": str,
            "active": bool
        }
        verifier = VerifySchema(name="test_verifier", context=None, schema=schema)
        event = {
            "id": 1,
            "name": "Test Event",
            "active": "yes"
        }
        try:
            verifier.do(event)
        except TypeError as e:
            assert "key 'active' is not of type 'bool'" in  str(e)