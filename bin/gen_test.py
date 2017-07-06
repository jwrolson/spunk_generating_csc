#!/usr/bin/env python

import sys, time
from splunklib.searchcommands import \
    dispatch, GeneratingCommand, Configuration, Option, validators

@Configuration()
class gentestCommand(GeneratingCommand):
    count = Option(require=True, validate=validators.Integer())

    def generate(self):
        output_dict = {}

        for i in range(self.count):
            output_dict['_time'] = time.time()
            output_dict['_raw'] = "HELLO WORLD!"
            yield output_dict

dispatch(gentestCommand, sys.argv, sys.stdin, sys.stdout, __name__)
