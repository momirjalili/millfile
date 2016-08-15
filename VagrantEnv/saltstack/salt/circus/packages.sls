{% set zeromq_dev = {
    'RedHat': 'zeromq-devel',
    'Debian': 'libzmq-dev'
}.get(grains.os_family) %}

{% set libevent_dev = {
    'RedHat': 'libevent-devel',
    'Debian': 'libevent-dev'
}.get(grains.os_family) %}

zeromq-dev:
  pkg.installed:
    - name: {{ zeromq_dev }}

libevent-dev:
  pkg.installed:
    - name: {{ libevent_dev }}

circus_requirements:
  pip.installed:
    - requirements: salt://circus/requirements.txt

circus:
  pip.installed:
    - require:
      - pkg: python_packages
      - pkg: zeromq-dev
      - pkg: libevent-dev

/etc/circus/circus.ini:
  file.managed:
    - source: salt://circus/circus.ini
    - user: root
    - group: root
    - require:
      - file: /etc/circus/

/etc/circus/:
  file.directory:
    - user: root
    - group: root
    - dir_mode: 755
