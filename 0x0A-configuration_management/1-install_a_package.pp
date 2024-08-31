# Puppet script to install flask v 2.1.0
package { 'flask':
  ensure   => '2.1.0',
  name     => 'flask',
  provider => 'pip3',
  install_options => ['--ignore-installed'],
}
