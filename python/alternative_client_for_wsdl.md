http://docs.python-zeep.org/en/latest/api.html

API
Client
class zeep.Client(wsdl, wsse=None, transport=None, service_name=None, port_name=None, plugins=None)
The zeep Client.


Parameters:
wsdl – 
wsse – 
transport – Custom transport class.
service_name – The service name for the service binding. Defaults to the first service in the WSDL document.
port_name – The port name for the default binding. Defaults to the first port defined in the service element in the WSDL document.
plugins – a list of Plugin instances
bind(service_name=None, port_name=None)
Create a new ServiceProxy for the given service_name and port_name.
The default ServiceProxy instance (self.service) always referes to the first service/port in the wsdl Document. Use this when a specific port is required.
create_message(operation, service_name=None, port_name=None, args=None, kwargs=None)
Create the payload for the given operation.
create_service(binding_name, address)
Create a new ServiceProxy for the given binding name and address.


Parameters:
binding_name – The QName of the binding
address – The address of the endpoint
get_element(name)
Return the element for the given qualified name.
get_type(name)
Return the type for the given qualified name.
options(timeout)
Context manager to temporarily overrule various options.


Parameters:
timeout – Set the timeout for POST/GET operations (not used for loading external WSDL or XSD documents)
To for example set the timeout to 10 seconds use:
client = zeep.Client('foo.wsdl')
with client.options(timeout=10):
    client.service.fast_call()
service
The default ServiceProxy instance
set_default_soapheaders(headers)
Set the default soap headers which will be automatically used on all calls.
Note that if you pass custom soapheaders using a list then you will also need to use that during the operations. Since mixing these use cases isn’t supported (yet).
set_ns_prefix(prefix, namespace)
Set a shortcut for the given namespace.
type_factory(namespace)
Return a type factory for the given namespace.
Example:
factory = client.type_factory('ns0')
user = factory.User(name='John')
Transport
class zeep.Transport(cache=NotSet, timeout=300, operation_timeout=None, verify=True, http_auth=None)
The transport object handles all communication to the SOAP server.


Parameters:
cache – The cache object to be used to cache GET requests
timeout – The timeout for loading wsdl and xsd documents.
operation_timeout – The timeout for operations (POST/GET). By default this is None (no timeout).
verify – Boolean to indicate if the SSL certificate needs to be verified.
http_auth – HTTP authentication, passed to requests.
get(address, params, headers)
Proxy to requests.get()


Parameters:
address – The URL for the request
params – The query parameters
headers – a dictionary with the HTTP headers.
load(url)
Load the content from the given URL
post(address, message, headers)
Proxy to requests.posts()


Parameters:
address – The URL for the request
message – The content for the body
headers – a dictionary with the HTTP headers.
post_xml(address, envelope, headers)
Post the envelope xml element to the given address with the headers.
This method is intended to be overriden if you want to customize the serialization of the xml element. By default the body is formatted and encoded as utf-8. See zeep.wsdl.utils.etree_to_string.
AnyObject
class zeep.AnyObject(xsd_object, value)
Create an any object


Parameters:
xsd_object – the xsd type
value – The value
