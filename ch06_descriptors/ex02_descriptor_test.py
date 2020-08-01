from .ex02_descriptor import ClientClass


def test_descriptor_class():
    client = ClientClass()
    assert client.descriptor == client
