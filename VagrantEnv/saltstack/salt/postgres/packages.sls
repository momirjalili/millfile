{% set postgresql = {
    'RedHat': 'postgresql94',
    'Debian': 'postgresql-9.4',
}.get(grains.os_family) %}

{% set postgresql_client = {
    'RedHat': 'postgresql94-client',
    'Debian': 'postgresql-client-9.4',
}.get(grains.os_family) %}

postgresql:
  pkg.installed:
    - name: {{ postgresql }}

postgresql-client:
  pkg.installed:
    - name: {{ postgresql_client }}

libpq-dev:
  pkg.installed
