from flask import (
  Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from werkzeug.exceptions import abort

bp = Blueprint('pred', __name__)

@bp.route('/')
def index():
  return render_template('pred/index.html')