from flask import flash, render_template, redirect, request
from FlaskExercise import app


@app.route('/')
def home():
    log = request.values.get('log_button')
    # TODO: Appropriately log the different button presses
    #   with the appropriate log level.
    if log == 'info':
        app.logger.info('Info button was pressed.')
    elif log == 'warning':
        app.logger.warning('Warning button was pressed.')
    elif log == 'error':
        app.logger.error('Error buttong was pressed.')
    elif log == 'critical':
        app.logger.critical('Critical button was pressed.')
    return render_template(
        'index.html',
        log=log
    )
