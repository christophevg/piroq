import sys
import os
from honcho.command import _procfile_path, _procfile, _parse_concurrency, _read_env, _parse_quiet, Manager, Printer, environ

def _choose_procfile(app_root=".", env=".env", procfile=None):
  env = _read_env(app_root, env)
  env_procfile = env.pop('PROCFILE', None)

  if procfile is not None:
    return procfile
  elif env_procfile is not None:
    return env_procfile
  else:
    return "Procfile"

def _choose_port(port=None, env={}):
  env_port = env.pop('PORT', None)
  os_env_port = os.environ.pop('PORT', None)

  if port is not None:
    return port
  elif env_port is not None:
    return int(env_port)
  elif os_env_port is not None:
    return int(os_env_port)
  else:
    return 5000

def start(app_root='.', port=None, command='start', concurrency=None, env='.env', no_colour=False, no_prefix=False, processes=[], procfile=None, quiet=None):
  procfile_path = _procfile_path(app_root, _choose_procfile(app_root, env, procfile))
  procfile = _procfile(procfile_path)

  concurrency = _parse_concurrency(concurrency)
  env = _read_env(app_root, env)
  quiet = _parse_quiet(quiet)
  port = _choose_port(port, env)

  if processes:
    processes = compat.OrderedDict()
    for name in processes:
      try:
        processes[name] = procfile.processes[name]
      except KeyError:
        raise CommandError("Process type '{0}' does not exist in Procfile".format(name))
  else:
    processes = procfile.processes

  manager = Manager(Printer(sys.stdout, colour=(not no_colour), prefix=(not no_prefix)))

  for p in environ.expand_processes(processes, concurrency=concurrency,	env=env, quiet=quiet,	port=port):
    e = os.environ.copy()
    e.update(p.env)
    manager.add_process(p.name, p.cmd, quiet=p.quiet, env=e)

  manager.loop()
  return manager.returncode
