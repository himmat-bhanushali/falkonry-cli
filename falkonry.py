import click
import cmd
import falkonryclient
import sys
import re
import json

from falkonryclient import client as Falkonry


global assessmentId
global datastreamId
global _falkonry

_falkonry = None
assessmentId = None
datastreamId = None

class REPL(cmd.Cmd):
    print "Welcome to Falkonry Shell"
    def __init__(self, ctx):
        cmd.Cmd.__init__(self)
        cmd.Cmd.prompt = '>>'
        self.ctx = ctx

    def default(self, line):
        subcommand = cli.commands.get(line)
        if subcommand:
            self.ctx.invoke(subcommand)
        else:
            return cmd.Cmd.default(self, line)

@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand is None:
        repl = REPL(ctx)
        repl.cmdloop()

@cli.command()
def login():
    """login"""
    host = click.prompt('Please enter falkonry host url')
    token = click.prompt('Please enter API token')
    if validateLogin(host,token):
        datastreams = _falkonry.get_datastreams()
        print datastreams

@cli.command()
def logout():
    """logout"""
    print "logout"

@cli.command()
def exit():
    """exit"""
    print "Exiting Falkonry Shell"
    sys.exit(0)

def validateLogin(host,token):
    """validate Login"""
    if not(not host or not token):
        p = re.compile('^(([^:/?#]+):)?(//([^/?#]*))?([^?#]*)(\?([^#]*))?(#(.*))?')
        m = p.match(host)
        if m:
            _falkonry = Falkonry(host=host, token=token)
            # test auth token validation
            try:
                datastream = _falkonry.get_datastream('test-id')
            except Exception as error:
                if hasattr(error, 'message'):
                    errorObj = json.loads(error.message)
                    if (errorObj['message'] == "Unauthorized Access"):
                        print('Unauthorized Access. Please verify your details.')
                        _falkonry = None
                        return False
                    elif (errorObj['message'] == "No such Datastream available"):
                        return True
                    else:
                        _falkonry = None
                        return False
                else:
                    _falkonry = None
                    print('Unable to connect to falkonry. Please verify your details.')
                    return False
        else:
            print "Invalid Host Url"
            return False

if __name__ == "__main__":
    cli()