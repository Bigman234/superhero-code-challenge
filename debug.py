#!/usr/bin/env python3

from app import app
from server.models_test import db, Hero, Power, HeroPower

if __name__ == '__main__':
    with app.app_context():
        import ipdb; ipdb.set_trace()