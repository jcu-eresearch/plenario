from plenario.sensor_network.sensor_models import NetworkMeta, NodeMeta, FeatureOfInterest, Sensor
from plenario.database import session, Base, app_engine, session
from geoalchemy2.elements import WKTElement
import random
from sqlalchemy import Table, MetaData

aot = NetworkMeta(name='ArrayOfThings', info={
    "website": "aot.org",
    "contact": "admin@aot.org"
})

node = NodeMeta(id='00A',
                sensor_network='ArrayOfThings',
                location=WKTElement(
                    'POINT(87.6298 41.8781)',
                    srid=4326),
                info={
                    "height": {
                        "value": 5,
                        "unit": "meters"
                    },
                    "orientation": {
                        "value": "NE",
                        "unit": "Cardinal directions. One of N, NE, E, SE, S, SW, W, NW"
                    }
                })

gas = FeatureOfInterest(name='gasConcentration',
                        observed_properties=[
                            {
                                "name": "SO2",
                                "type": "numeric",
                                "unit": "ppm",
                                "description": "Sulfur dioxide concentration"
                            },
                            {
                                "name": "H2S",
                                "type": "numeric",
                                "unit": "ppm",
                                "description": "Hydrogen sulfide concentration"
                            },
                            {
                                "name": "O3",
                                "type": "numeric",
                                "unit": "ppm",
                                "description": "Ozone concentration"
                            },
                            {
                                "name": "NO2",
                                "type": "numeric",
                                "unit": "ppm",
                                "description": "Nitrous oxide concentration"
                            },
                            {
                                "name": "CO",
                                "type": "numeric",
                                "unit": "ppm",
                                "description": "Carbon monoxide concentration"
                            },
                        ])

sensor1 = Sensor(name='Sulfur Dioxide', observed_properties=['gasConcentration.SO2'], info={"datasheet": "http://www.mcs.anl.gov/research/projects/waggle/downloads/datasheets/chemsense/so2.pdf", "range": "0 to 20 ppm", "accuracy": "+-3% of reading"})
sensor2 = Sensor(name='Hydrogen Sulfide', observed_properties=['gasConcentration.H2S'], info={"datasheet": "http://www.mcs.anl.gov/research/projects/waggle/downloads/datasheets/chemsense/h2s.pdf", "range": "0 to 20 ppm", "accuracy": "+-3% of reading"})
sensor3 = Sensor(name='Ozone', observed_properties=['gasConcentration.O3'], info={"datasheet": "http://www.mcs.anl.gov/research/projects/waggle/downloads/datasheets/chemsense/o3.pdf", "range": "0 to 20 ppm", "accuracy": "+-3% of reading"})
sensor4 = Sensor(name='Nitrous Oxide', observed_properties=['gasConcentration.NO2'], info={"datasheet": "http://www.mcs.anl.gov/research/projects/waggle/downloads/datasheets/chemsense/no2.pdf", "range": "0 to 20 ppm", "accuracy": "+-3% of reading"})
sensor5 = Sensor(name='Carbon Monoxide', observed_properties=['gasConcentration.CO'], info={"datasheet": "http://www.mcs.anl.gov/research/projects/waggle/downloads/datasheets/chemsense/co.pdf", "range": "0 to 20 ppm", "accuracy": "+-3% of reading"})


# # init db
# Base.metadata.create_all(app_engine)

# NEW
# session.add(aot)
# session.add(gas)
session.add(node)
node.sensors.append(sensor1)
node.sensors.append(sensor2)
node.sensors.append(sensor3)
node.sensors.append(sensor4)
node.sensors.append(sensor5)

session.commit()


