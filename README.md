# Plugin for the NX584 Python Module to connect to Homebridge Alarm System Platform

This is a plugin to the [pynx584 module](https://github.com/kk7ds/pynx584) to enable connectivity to Apple's Homekit via [Homebridge](https://github.com/nfarina/homebridge) using the [AlarmDecoder Platform Homebridge Plugin](https://github.com/aficustree/homebridge-alarmdecoder-platform). This plugin is installed via pip and dynamically loaded into the pynx584 module at runtime via the [stevedore](https://docs.openstack.org/stevedore/latest/) plugin system.

## Installation

1. Clone repo `git clone https://github.com/aficustree/nx584ADPlugIn`
2. Change to directory where installed `cd nx584ADPlugIn`
3. Install via `pip3 install .`
4. Edit configuration file and place in home directory
5. Run pynx584 server module `nx584_server --serial /dev/ttyS0 --baud 38400` (or equiv)
6. Enjoy

## Configuration

System will search for a configuration file (.nx584ADPlugIn.cfg) in the pip installation folder, the working directory and your home directory (in that order). It will use the LAST FILE FOUND.

See the [sample configuration file](./.nx584ADPlugIn.cfg) for details

## License

Copyright 2018, [aficustree](https://github.com/aficustree)

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the [License](./LICENSE).