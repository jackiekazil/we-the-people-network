import requests as r
import settings as s

from petitions import Petition
import argparse as arg



def get_petitions(api_key):
    url = s.API_BASE_URL + Petition.api_base + '.json'
    payload = {
        'limit':1000000, 
        'offset':0,
        'key':api_key,
    }

    response = r.get(url, params=payload)
    results = response.json()['results']
    petitions = []

    for result in results:
        
        p = Petition()
        p.__dict__.update(result)
        p.update_instances()
        petitions.append(p)

    return petitions





def main(api_key):
    petitions = get_petitions(api_key)
    return petitions





def parse_args():
    """ 
    Parses commandline arguments. 
    """
    description = '#TODO'
    parser = arg.ArgumentParser(description=description)
    help = 'Api key'
    parser.add_argument('--api-key', dest='api_key', default=None, help=help)
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    main(args.api_key)

#['__class__', '__delattr__', '__dict__', '__doc__', '__format__', 
# '__getattribute__', '__hash__', '__init__', '__module__', 
#'__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', 
#'__sizeof__', '__str__', '__subclasshook__', '__weakref__', 
#'api_base', u'body', u'created', u'deadline', 'id', 'instances', 
#u'issues', u'response', u'signature count', u'signature threshold', 
#u'signatures needed', u'status', u'title', u'type', 
#'update_instances', u'url']
