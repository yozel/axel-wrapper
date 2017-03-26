import os
import subprocess


class AxelError(Exception):
    pass

def _get_arg_list(url, output_path, num_connections, headers, extra_args,
                  use_tsocks):
    arg_list = []

    if use_tsocks:
        arg_list.append('tsocks')
    arg_list.append('axel')

    params = {}
    if extra_args:
        params.update(extra_args)
    if num_connections:
        params['num-connections'] = num_connections
    if output_path:
        params['output'] = output_path

    # params to arg_list
    for param, value in params.items():
        arg_list.append('--{}={}'.format(param, value))

    # headers to arg_list
    if headers:
        for header, value in headers.items():
            arg_list.append('--header={}: {}'.format(header, value))

    arg_list.append(url)

    return arg_list

def axel(url, output_path=None, num_connections=None, headers=None,
         extra_args=None, use_tsocks=None):
    # TODO: check if python-axel installed
    # TODO: check if tsocks installed (only if use_tsocks == True)
    arg_list = _get_arg_list(url=url, output_path=output_path,
                             num_connections=num_connections, headers=headers,
                             extra_args=extra_args,
                             use_tsocks=use_tsocks)

    try:
        stdout = subprocess.check_output(arg_list, encoding='utf-8',
                                         stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        raise AxelError(e.stderr)

    path = None
    for line in stdout.split('\n'):
        if line.startswith('Opening output file '):
            path = line.split('Opening output file ', 2)[1]
            break
    if not path:
        raise AxelError("Something is wrong, path doesn't exists")

    cwd = os.getcwd()
    full_path = os.path.join(cwd, path)
    return full_path
