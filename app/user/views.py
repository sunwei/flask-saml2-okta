# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, request

blueprint = Blueprint('user', __name__)


@blueprint.route('/api/user', methods=('GET',))
def get_user():
    return "my name is Dummy"

