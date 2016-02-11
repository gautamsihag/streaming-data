import requests
import json
import time
import codecs
from sys import stdout

# this script polls the meetup API, keeps track for meetup Host, venue by latitude
# and longitude of each meeting




#print ("Loading the json")
# get the meetup response from the API and setting stream to true
meetUp = requests.get("http://stream.meetup.com/2/rsvps", stream=True)
#creating an iterator for json request response 
for meetUp_next in meetUp.iter_lines():
    # loading and decoding to avoide getting a utf-error
    m = json.loads(meetUp_next.decode('utf-8'))
    # to check if the corresponding tuple of m has the key we are looking for
    try:
        if "group" in m:
            if "group_topics" in m:
                #group_topics = m["group_topics"]
                for team in m:
                    print(getitem(obj, '$.group.group_topics.' +team +'.urlkey'))
    except:
        continue
# to check if the corresponding tuple of m has the key we are looking for
    try:
        if "group" in m:
            if "rsvp_id" in m:
                name = m["member"]["member_name"]
                rid = m["rsvp_id"]
    except:
        continue
    try:
        if "member" in m:
            if "other_services" in m:
                tw = getattr(obj, '$.member.other_services.twitter.identifier')
                #tw = m["member"]["other_services"]["twitter"]["identifier"]
                #fb = m["member"]["other_services"]["facebook"]["identifier"]
                fb = getattr(obj, '$.member.other_services.fscebook.identifier')
    except:
        continue
# to check if the corresponding tuple of m has the key we are looking for
    try:
        if "visibility" in m:
            visi = m["visibility"]
            if "venue" in m:
                lat = m["venue"]["lat"]
                lon = m["venue"]["lon"]
                vid = m["venue"]["venue_id"]
                #print("Name of the person: " + name)
                #print("Location in Latitude: " + str(lat) + " & Longitude: " + str(lon))
                #print("visibility of the post:"+ visi + " & Reservation id: " + str(rid))
                print('{"Name":"%s", "Latitude":%s, "Longitude":%s, "Visibility":"%s", "ReservationId":%s, "VenueId":%s}'%(name,lon,lat,visi,rid,vid))
                stdout.flush()
    except:
        continue
