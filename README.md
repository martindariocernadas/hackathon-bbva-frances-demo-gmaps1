#hackathon ejemplo cliente API para GoogleMaps

- https://github.com/googlemaps/google-maps-services-python

- Instalacion : pip install -U googlemaps

- Consola para KEY de developer : https://developers.google.com/console . Aqui se debe habilitar la API de Directions y Geolocation.

- Codigo Python : locate.py

- Ejecutar el codigo asi       : python locate.py
   - Si se quiere en modo debug: python -m pdb locate.py

- Resultados : Indicaciones de como llegar : Usar el comando "pretty print" del debugger, y verificar "directions_result", asi :

  (Se asumo la ejecucion con "python -m pdb locate.py" , y que ya se ejecuto la linea que recupera las indicaciones)

----------------------------------------------------------------------------------------------------------------------------------
(Pdb) pp directions_result
[{u'bounds': {u'northeast': {u'lat': -34.6028938,
                             u'lng': -58.36953519999999},
              u'southwest': {u'lat': -34.6082238, u'lng': -58.3813785}},
  u'copyrights': u'Map data \xa92017 Google',
  u'fare': {u'currency': u'ARS', u'text': u'ARS7.50', u'value': 7.5},
  u'legs': [{u'arrival_time': {u'text': u'5:44pm',
                               u'time_zone': u'America/Buenos_Aires',
                               u'value': 1507581873},
             u'departure_time': {u'text': u'5:33pm',
                                 u'time_zone': u'America/Buenos_Aires',
                                 u'value': 1507581225},
             u'distance': {u'text': u'1.7 km', u'value': 1735},
             u'duration': {u'text': u'11 mins', u'value': 648},
             u'end_address': u'Buenos Aires, Argentina',
             u'end_location': {u'lat': -34.6037014, u'lng': -58.3813785},
             u'start_address': u'Balcarce 50, Buenos Aires, Argentina',
             u'start_location': {u'lat': -34.6082238, u'lng': -58.3709904},
             u'steps': [{u'distance': {u'text': u'0.6 km', u'value': 648},
                         u'duration': {u'text': u'9 mins', u'value': 515},
                         u'end_location': {u'lat': -34.6028938,
                                           u'lng': -58.36953519999999},
                         u'html_instructions': u'Walk to Alem',
                         u'polyline': {u'points': u'jlfrEtqgcJS@C@E@C@A@ABCBEBEHUTEMEIGKKOe@a@yDJ[@sCBe@@U?eFPmFLAy@Ai@YqE'},
                         u'start_location': {u'lat': -34.6082238,
                                             u'lng': -58.3709904},
                         u'steps': [{u'distance': {u'text': u'51 m',
                                                   u'value': 51},
                                     u'duration': {u'text': u'1 min',
                                                   u'value': 58},
                                     u'end_location': {u'lat': -34.6078409,
                                                       u'lng': -58.3712622},
                                     u'html_instructions': u'Head <b>north</b> on <b>Balcarce</b> toward <b>Av. Rivadavia</b>',
                                     u'polyline': {u'points': u'jlfrEtqgcJS@C@E@C@A@ABCBEBEHUT'},
                                     u'start_location': {u'lat': -34.6082238,
                                                         u'lng': -58.3709904},
                                     u'travel_mode': u'WALKING'},
                                    {u'distance': {u'text': u'57 m',
                                                   u'value': 57},
                                     u'duration': {u'text': u'1 min',
                                                   u'value': 43},
                                     u'end_location': {u'lat': -34.6074876,
                                                       u'lng': -58.3708264},
                                     u'html_instructions': u'Turn <b>right</b> onto <b>Av. Rivadavia</b>',
                                     u'maneuver': u'turn-right',
                                     u'polyline': {u'points': u'~ifrEjsgcJEMEIGKKOe@a@'},
                                     u'start_location': {u'lat': -34.6078409,
                                                         u'lng': -58.3712622},
                                     u'travel_mode': u'WALKING'},
                                    {u'distance': {u'text': u'0.5 km',
                                                   u'value': 495},
                                     u'duration': {u'text': u'6 mins',
                                                   u'value': 385},
                                     u'end_location': {u'lat': -34.603044,
                                                       u'lng': -58.37108509999999},
                                     u'html_instructions': u'Slight <b>left</b> onto <b>25 de Mayo</b>',
                                     u'maneuver': u'turn-slight-left',
                                     u'polyline': {u'points': u'xgfrEtpgcJyDJ[@sCBe@@U?eFPmFL'},
                                     u'start_location': {u'lat': -34.6074876,
                                                         u'lng': -58.3708264},
                                     u'travel_mode': u'WALKING'},
                                    {u'distance': {u'text': u'45 m',
                                                   u'value': 45},
                                     u'duration': {u'text': u'1 min',
                                                   u'value': 29},
                                     u'end_location': {u'lat': -34.6028938,
                                                       u'lng': -58.36953519999999},
                                     u'html_instructions': u'Turn <b>right</b> onto <b>Av. Corrientes</b>',
                                     u'maneuver': u'turn-right',
                                     u'polyline': {u'points': u'~kerEhrgcJAy@Ai@YqE'},
                                     u'start_location': {u'lat': -34.603044,
                                                         u'lng': -58.37108509999999},
                                     u'travel_mode': u'WALKING'}],
                         u'travel_mode': u'WALKING'},
                        {u'distance': {u'text': u'1.1 km',
                                       u'value': 1087},
                         u'duration': {u'text': u'2 mins', u'value': 132},
                         u'end_location': {u'lat': -34.6037014,
                                           u'lng': -58.3813785},
                         u'html_instructions': u'Subway towards Juan Manuel de Rosas',
                         u'polyline': {u'points': u'`kerErhgcJdAtYDnBPnId@dRTpGBrA@Z@`A'},
                         u'start_location': {u'lat': -34.6028938,
                                             u'lng': -58.36953519999999},
                         u'transit_details': {u'arrival_stop': {u'location': {u'lat': -34.6037014,
                                                                              u'lng': -58.3813785},
                                                                u'name': u'Carlos Pellegrini'},
                                              u'arrival_time': {u'text': u'5:44pm',
                                                                u'time_zone': u'America/Buenos_Aires',
                                                                u'value': 1507581873},
                                              u'departure_stop': {u'location': {u'lat': -34.6028938,
                                                                                u'lng': -58.36953519999999},
                                                                  u'name': u'Alem'},
                                              u'departure_time': {u'text': u'5:42pm',
                                                                  u'time_zone': u'America/Buenos_Aires',
                                                                  u'value': 1507581741},
                                              u'headsign': u'Juan Manuel de Rosas',
                                              u'line': {u'agencies': [{u'name': u'Subte de Buenos Aires',
                                                                       u'phone': u'011 54 11 4555-1616',
                                                                       u'url': u'http://www.buenosaires.gob.ar/subte'}],
                                                        u'color': u'#d50000',
                                                        u'name': u'Leandro N. Alem - Juan Manuel de Rosas',
                                                        u'short_name': u'B',
                                                        u'text_color': u'#000000',
                                                        u'vehicle': {u'icon': u'//maps.gstatic.com/mapfiles/transit/iw2/6/subway2.png',
                                                                     u'name': u'Subway',
                                                                     u'type': u'SUBWAY'}},
                                              u'num_stops': 2},
                         u'travel_mode': u'TRANSIT'}],
             u'traffic_speed_entry': [],
             u'via_waypoint': []}],
  u'overview_polyline': {u'points': u'jlfrEtqgcJa@FML[^KWS[e@a@yDJoDD{@@sM^CcBYqEdAtYV~Ld@dRTpGDnB@`A'},
  u'summary': u'',
  u'warnings': [u'Walking directions are in beta.    Use caution \u2013 This route may be missing sidewalks or pedestrian paths.'],
  u'waypoint_order': []}]

