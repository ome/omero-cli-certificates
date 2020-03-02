#!/usr/bin/env python

import logging
import os
from omero.cli import BaseControl
from .certificates import create_certificates

DEFAULT_LOGLEVEL = logging.WARNING


def _omerodir(ctx):
    omerodir = os.getenv("OMERODIR")
    if not omerodir or not os.path.isdir(omerodir):
        ctx.die(100, "OMERODIR not set")
    return omerodir


class CertificatesControl(BaseControl):
    def _configure(self, parser):
        parser.set_defaults(func=self.certificates)
        parser.add_argument(
            "--verbose",
            "-v",
            action="count",
            default=0,
            help="Increase verbosity (can be used multiple times)",
        )

    def certificates(self, args):
        loglevel = max(DEFAULT_LOGLEVEL - 10 * args.verbose, 10)
        logging.getLogger("omero_certificates").setLevel(level=loglevel)
        omerodir = _omerodir(self.ctx)
        # try:
        create_certificates(omerodir)
        # except Exception as e:
        #     self.ctx.die(100, e)