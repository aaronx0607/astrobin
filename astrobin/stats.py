from models import DeepSky_Acquisition, Image, UserProfile, Gear, User

from django.utils.translation import ugettext as _
from django.utils.encoding import smart_str
from django.db.models import Q

from datetime import datetime, timedelta
import time


def daterange(start, end):
    r = (end + timedelta(days=1) - start).days
    return [start + timedelta(days=i) for i in range(r)]


def integration_hours(user, period = 'monthly', since = 0):
    _map = {
        'yearly' : (_("Integration hours, yearly") , '%Y'),
        'monthly': (_("Integration hours, monthly"), '%Y-%m'),
        'daily'  : (_("Integration hours, daily")  , '%Y-%m-%d'),
    }

    flot_label = _map[period][0]
    flot_data = []
    flot_options = {
        'xaxis': {'mode': 'time'},
        'lines': {'show': 'true', 'fill': 'true'},
        'points': {'show': 'true'},
        'legend': {
            'position': 'nw',
            'backgroundColor': '#000000',
            'backgroundOpacity': 0.75},
        'grid': {'hoverable': 'true'},
    }

    astrobin = User.objects.get(username = 'astrobin')
    all = DeepSky_Acquisition.objects.all().exclude(date = None).order_by('date')

    if since > 0:
        all = all.filter(date__gte = datetime.today().date() - timedelta(days = since))

    if user != astrobin:
        all = all.filter(image__user = user)
    
    data = {}
    for i in all:
        integration = 0
        if i.duration and i.number:
            integration += (i.duration * i.number) / 3600.0
        key = i.date.strftime(_map[period][1])
        if key in data:
            if integration > 0:
                data[key] += integration
        else:
            data[key] = integration

    if all:
        for date in daterange(all[0].date, datetime.today().date()):
            grouped_date = date.strftime(_map[period][1])
            t = time.mktime(datetime.strptime(grouped_date, _map[period][1]).timetuple()) * 1000
            if grouped_date in data.keys():
                flot_data.append([t, data[grouped_date]])
            else:
                flot_data.append([t, 0])

    return (flot_label, flot_data, flot_options)


def integration_hours_by_gear(user, period='monthly'):
    _map = {
        'yearly' : (_("Integration hours by gear, yearly") , '%Y'),
        'monthly': (_("Integration hours by gear, monthly"), '%Y-%m'),
        'daily'  : (_("Integration hours by gear, daily")  , '%Y-%m-%d'),
    }

    flot_data = []
    flot_options = {
        'xaxis': {'mode': 'time'},
        'lines': {'show': 'true'},
        'points': {'show': 'true'},
        'legend': {
            'position': 'nw',
            'backgroundColor': '#000000',
            'backgroundOpacity': 0.7
        },
        'grid': {'hoverable': 'true'},
    }

    profile = UserProfile.objects.get(user = user)
    for g in Gear.objects.filter(Q(telescope__userprofile = profile) | Q(camera__userprofile = profile)):
        all = DeepSky_Acquisition.objects.filter(
            Q(image__user = user),
            Q(image__imaging_telescopes = g) | Q(image__imaging_cameras = g)).exclude(date = None).order_by('date')

        g_dict = {
            'label': _map[period][0] + ": " + smart_str(g.name),
            'stage_data': {},
            'data': [],
        }

        for i in all:
            integration = 0
            if i.duration and i.number:
                integration += (i.duration * i.number) / 3600.0
            key = i.date.strftime(_map[period][1])
            if key in g_dict['stage_data']:
                g_dict['stage_data'][key] += integration
            else:
                g_dict['stage_data'][key] = integration

        if all:
            for date in daterange(all[0].date, datetime.today().date()):
                grouped_date = date.strftime(_map[period][1])
                t = time.mktime(datetime.strptime(grouped_date, _map[period][1]).timetuple()) * 1000
                if grouped_date in g_dict['stage_data'].keys():
                    g_dict['data'].append([t, g_dict['stage_data'][grouped_date]])
                else:
                    g_dict['data'].append([t, 0])

        del g_dict['stage_data']
        flot_data.append(g_dict)

    return (flot_data, flot_options)


def uploaded_images(user, period='monthly'):
    _map = {
        'yearly' : (_("Uploaded images, yearly") , '%Y'),
        'monthly': (_("Uploaded images, monthly"), '%Y-%m'),
        'daily'  : (_("Uploaded images, daily")  , '%Y-%m-%d'),
    }

    flot_label = _map[period][0]
    flot_data = []
    flot_options = {
        'xaxis': {'mode': 'time'},
        'lines': {'show': 'true', 'fill': 'true'},
        'points': {'show': 'true'},
        'legend': {
            'position': 'nw',
            'backgroundColor': '#000000',
            'backgroundOpacity': 0.75},
        'grid': {'hoverable': 'true'},
    }

    astrobin = User.objects.get(username = 'astrobin')
    all = Image.objects.all().order_by('uploaded')
    if user != astrobin:
        all = all.filter(user = user)

    data = {}
    for i in all:
        key = i.uploaded.date().strftime(_map[period][1])
        if key in data:
            data[key] += 1
        else:
            data[key] = 1 

    if all:
        for date in daterange(all[0].uploaded.date(), datetime.today().date()):
            grouped_date = date.strftime(_map[period][1])
            t = time.mktime(datetime.strptime(grouped_date, _map[period][1]).timetuple()) * 1000
            if grouped_date in data.keys():
                flot_data.append([t, data[grouped_date]])
            else:
                flot_data.append([t, 0])

    return (flot_label, flot_data, flot_options)

