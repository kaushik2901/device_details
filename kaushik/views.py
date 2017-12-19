from django.http import HttpResponse

def index(request):
    html = "Device details"
    #request.user_agent.browser  # returns Browser(family=u'Mobile Safari', version=(5, 1), version_string='5.1')
    html = html + "<br />Browser : " + request.user_agent.browser.family  # returns 'Mobile Safari'
    html = html + "<br />Browser version : " + request.user_agent.browser.version_string  # returns (5, 1)

    # Operating System properties
    #request.user_agent.os  # returns OperatingSystem(family=u'iOS', version=(5, 1), version_string='5.1')
    html = html + "<br />Os : " + request.user_agent.os.family  # returns 'iOS'
    html = html + "<br />Os version : " + request.user_agent.os.version_string  # returns '5.1'

    # Device properties
    #request.user_agent.device  # returns Device(family='iPhone')
    html = html + "<br />Device : " + request.user_agent.device.family  # returns 'iPhone'

    return HttpResponse(html)
