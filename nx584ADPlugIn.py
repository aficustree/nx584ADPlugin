from nx584 import model
import os
import configparser
import requests


class HomeBridgePing(model.NX584Extension):
    def __init__(self, config=None):
        self._config = configparser.ConfigParser(allow_no_value=True)
        if config is None:
            searchPaths = [os.path.join(os.path.realpath('nx584ADPlugIn'), '.nx584ADPlugIn.cfg'),
                           os.path.join(os.path.expanduser('~'), '.nx584ADPlugIn.cfg'),
                           os.path.join(os.path.curdir, '.nx584ADPlugIn.cfg')]
            self._config.read(searchPaths)
        else:
            self._config.read(config)
        assert self._config['nx584ADPlugIn']['homebridgeURL'] is not None
        self.url = self._config['nx584ADPlugIn']['homebridgeURL']

    def sendPing(self):
        try:
            r = requests.get(self.url)
            if r.status_code == requests.codes.ok:
                print('ping sent')
            else:
                r.raise_for_status
        except Exception as e:
            print('Send Ping Failed: {0}'.format(e))

    def zone_status(self, zone):
        print('Zone status change for {0}'.format(zone.number))
        self.sendPing()

    def partition_status(self, part):
        print('Partition status change for {0}'.format(part.number))
        self.sendPing()
