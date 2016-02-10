# Storytelling with streaming data HW1
Programming assignment 1 for CS6998 Storytelling with Streaming Data
Consuming event stream of meetup.com in specific the RSVP event stream to obtain infromation about a reservation.

Stream can be accessed at:  
http://stream.meetup.com/2/rsvps with the detailed documentation at:
http://www.meetup.com/meetup_api/docs/stream/2/rsvps/.

# Sample JSON format of a meetup API response

The detailed infromation for the data dictionary can be accessed at: http://www.meetup.com/meetup_api/docs/stream/2/rsvps/

{
  "group": {
    "group_lat": 51.45,
    "group_urlname": "I-WANTED-TO-DO-THAT-THIS-WEEKEND-Just-not-alone",
    "group_lon": -0.02,
    "group_name": "I WANTED TO DO THAT THIS WEEKEND...Just not alone!!",
    "group_id": 18452472,
    "group_country": "gb",
    "group_city": "London",
    "group_topics": [
      {
        "topic_name": "Professional Networking",
        "urlkey": "professional-networking"
      },
      {
        "topic_name": "Dancing",
        "urlkey": "dancing"
      },
      {
        "topic_name": "Singles",
        "urlkey": "singles"
      },
      {
        "topic_name": "Dining Out",
        "urlkey": "diningout"
      },
      {
        "topic_name": "Walking",
        "urlkey": "walkers"
      },
      {
        "topic_name": "Fun Times",
        "urlkey": "fun-times"
      },
      {
        "topic_name": "Expat British",
        "urlkey": "brit"
      },
      {
        "topic_name": "New In Town",
        "urlkey": "newintown"
      },
      {
        "topic_name": "Social",
        "urlkey": "social"
      },
      {
        "topic_name": "Social Networking",
        "urlkey": "socialnetwork"
      },
      {
        "topic_name": "Nightlife",
        "urlkey": "nightlife"
      },
      {
        "topic_name": "Women's Social",
        "urlkey": "women"
      },
      {
        "topic_name": "Men's Social",
        "urlkey": "men"
      },
      {
        "topic_name": "Unique and Fun Activities",
        "urlkey": "unique-and-fun-activities"
      },
      {
        "topic_name": "Happy Hour",
        "urlkey": "happy-hours"
      }
    ]
  },
  "venue": {
    "venue_id": 18886802,
    "lat": 51.521568,
    "lon": -0.08413,
    "venue_name": "Eight Moorgate Private Members Club"
  },
  "visibility": "public",
  "response": "no",
  "guests": 0,
  "member": {
    "member_name": "Mary",
    "photo": "http://photos3.meetupstatic.com/photos/member/c/c/f/8/thumb_247492472.jpeg",
    "member_id": 113668552
  },
  "rsvp_id": 1593753739,
  "mtime": 1455072752232,
  "event": {
    "event_url": "http://www.meetup.com/I-WANTED-TO-DO-THAT-THIS-WEEKEND-Just-not-alone/events/228550718/",
    "time": 1455127200000,
    "event_id": "ztfxplyvdbnb",
    "event_name": "Fashion meets Finance Mingle Mixer + Welcome Drink"
  }
}


# index.html
Web page that consumes streaming meetup with websocketd
