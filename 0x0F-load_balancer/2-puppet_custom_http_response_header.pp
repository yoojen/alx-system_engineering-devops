#set custom header
exec {'default':
	path => '/bin/',
	command => sudo sed -i "/server_name _/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-enabled/default
}
