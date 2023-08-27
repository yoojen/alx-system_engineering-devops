#make ssh config file using puppet
exec { 'ssh_config':
  path => '/bin/',
  command => 'echo "PasswordAuthentication no" >> /etc/ssh/ssh_config; "IdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config';
}
