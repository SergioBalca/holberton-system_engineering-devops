# Set the limit higher to solve great amount of request problem

exec {'ULLIMIT':
    command => 'sed -i "/s/15/4096/g" /etc/default/nginx; service restart',
    path    => '/usr/bin/:/bin',
}
