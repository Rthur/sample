import requests
import urllib
import json
from ansible.errors import AnsibleError, AnsibleParserError
from ansible.plugins.lookup import LookupBase

class LookupModule(LookupBase):

  def run(self, q, **kwargs):
    result = []
    question = urllib.pathname2url(q[0])
    url = 'https://8ball.delegator.com'
    path = url + '/magic/JSON/' + question
    response = requests.get(path)
    if response.ok:
      result.append(json.loads(response.content))
      return result
    else:
      raise AnsibleParserError('No reply from %s, error: %s' % (url, response.status_code))
  
