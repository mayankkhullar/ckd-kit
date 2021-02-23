#!/usr/bin/env python3

from aws_cdk import core

from app2.app2_stack import App2Stack


app = core.App()
App2Stack(app, "app2")

app.synth()
