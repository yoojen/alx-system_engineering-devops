#make ssh config file using puppet
file { 'ssh_config':
  path => '/bin/',
  command => 'echo "PasswordAuthentication no" >> /etc/ssh/ssh_config; "IdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config';
}
