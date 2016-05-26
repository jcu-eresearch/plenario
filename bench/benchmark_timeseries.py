"""benchmark_timeseries: little, medium, and large queries meant to make plenario sweat"""

import requests
import timeit


def timeseries_query(url, query, geom):
    url += '/v1/api/timeseries/?'
    geom = '&location_geom__within=' + geom
    r = requests.get(url + query + geom)
    assert r is not None

    print '.',


def main(year):
    year = str(year)

    url = 'http://plenario-benchmark-env.us-east-1.elasticbeanstalk.com'
    print '\ntimeit from: ' + year

    # chicago
    timeseries_query(
        url=url,
        query='agg=year&obs_date__ge=' + year + '-1-1',
        geom=r'{"type"%3A"Feature"%2C"properties"%3A{}%2C"geometry"%3A{"type"%3A"Polygon"%2C"coordinates"%3A[[[-87.64313936058898%2C41.88330112135344]%2C[-87.64313936058898%2C41.893460648167355]%2C[-87.61472940270323%2C41.893460648167355]%2C[-87.61472940270323%2C41.88330112135344]%2C[-87.64313936058898%2C41.88330112135344]]]}}'
    )

    # new york
    timeseries_query(
        url=url,
        query='agg=year&obs_date__ge=' + year + '-1-1',
        geom=r'{"type"%3A"Feature"%2C"properties"%3A{}%2C"geometry"%3A{"type"%3A"Polygon"%2C"coordinates"%3A[[[-74.13379666395485%2C40.6462615921222]%2C[-74.13379666395485%2C40.78782018739577]%2C[-73.83579251356423%2C40.78782018739577]%2C[-73.83579251356423%2C40.6462615921222]%2C[-74.13379666395485%2C40.6462615921222]]]}}'
    )

    # san francisco
    timeseries_query(
        url=url,
        query='agg=week&obs_date__ge=' + year + '-1-1',
        geom='{"type"%3A"Feature"%2C"properties"%3A{}%2C"geometry"%3A{"type"%3A"Polygon"%2C"coordinates"%3A[[[-122.6364898122847%2C37.53586597792038]%2C[-122.6364898122847%2C37.95069515957716]%2C[-122.21626276150344%2C37.95069515957716]%2C[-122.21626276150344%2C37.53586597792038]%2C[-122.6364898122847%2C37.53586597792038]]]}}'
    )

if __name__ == '__main__':

    # light
    print timeit.timeit(
        stmt='main(2015)',
        setup='from __main__ import main',
        number=3
    )

    # medium
    print timeit.timeit(
        stmt='main(2009)',
        setup='from __main__ import main',
        number=3
    )

    # heavy
    print timeit.timeit(
        stmt='main(2005)',
        setup='from __main__ import main',
        number=3
    )
