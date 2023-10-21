#fix nginx error for not being able to handle many request

#increasing ulimit of the server

exec { 'fix-nginx':
 command => 'sed -i "s/15/4096/" /etc/default/nginx',
 path => '/usr/local/bin/:/bin'
}

#restartgin nginx
exec { 'restart-nginx':
 command => 'nginx restart',
 path => '/etc/init.d/'
}

