from lxml import etree
import os

xml_file = 'shiporder.xml'
xsd_file = 'shiporder.xsd'


def check_file_availability(xml_path: str, xsd_path: str) -> bool:
    if os.path.isfile(xml_path) and os.path.isfile(xsd_path):
        return True
    else:
        return False


def validate(xml_path: str, xsd_path: str) -> bool:

    xmlschema_doc = etree.parse(xsd_path)
    xmlschema = etree.XMLSchema(xmlschema_doc)

    xml_doc = etree.parse(xml_path)
    result = xmlschema.validate(xml_doc)

    return result


def validate_xml(event, context):
    if check_file_availability(xml_file, xsd_file):
        if validate(xml_file, xsd_file):
            print('Valid! :)')
        else:
            print('Not valid! :(')
    else:
        print('Some file is missing')


if __name__ == '__main__':
    validate_xml('event', 'context')