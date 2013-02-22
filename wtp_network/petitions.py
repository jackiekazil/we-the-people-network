



class Petition(object):

    instances = {}
    api_base = 'petitions'

    def __init__(self):
        self.id = None
        # self.body = None
        # self.title = None
        # self.url = None
        # self.created = None
        # self.status = None
        # self.response = None
        # self.deadline = None
        # self.type = None
        # self.id = None
        # self.isses = None

    def update_instances(self):
        self.__class__.instances[self.id] = self







# [u'body', 
# #u'signature threshold', 
# u'title', 
# u'url', 
# #u'signatures needed', 
# u'created', 
# u'status', 
# u'response', 
# #u'signature count', 
# u'deadline', 
# u'type', 
# u'id', 
# u'issues']

  # {u'body': u"\r\nEvery year in the United States, an estimated 6 to 8 million lost, abandoned, or unwanted dogs and cats enter animal shelters and nearly half of these animals\u2014many of them healthy, young, and adoptable\u2014must be euthanized because there are too many animals and not enough good homes. \r\n\r\nThis tragedy occurs because people don't spay and neuter their animals and because greedy breeders continue to churn out more puppies. Because all dogs and cats are precious and because no more animals need to be bred when so many others go without hope of being adopted, PETA is calling for a mandatory spay-and-neuter law until all dogs and cats in the United States have a home to call their own. \r\n\r\nSign the petition calling for a mandatory spay-and-neuter law to help end the animal overpopulation crisis. \r\n",
  # u'created': 1316697387,
  # u'deadline': 1319289387,
  # u'id': u'4e7b352b4bd5046c04000000',
  # u'issues': [{u'id': u'20', u'name': u'Environment'}],
  # u'response': {u'association time': u'1325703633',
  #  u'id': u'331',
  #  u'url': u'https://petitions.whitehouse.gov/response/ending-pet-homelessness-through-responsible-pet-ownership'},
  # u'signature count': 11729,
  # u'signature threshold': 5000,
  # u'signatures needed': 0,
  # u'status': u'responded',
  # u'title': u'Stop Animal Homelessness at Its Roots',
  # u'type': u'petition',
  # u'url': u'https://petitions.whitehouse.gov/petition/stop-animal-homelessness-its-roots/kxBLFMx8'}]

