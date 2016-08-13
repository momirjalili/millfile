exec { "yum update":
  command => "yum -y update",
  path    => "/usr/bin",
}

package {"nginx":
    ensure => present,
    require => Exec["yum update"],

}

package {"postgresql94-server":
    ensure => present,
    require => Exec["yum update"],
}

package {"postgresql94":
    ensure => present,
    require => Exec["yum update"],
}

package {"postgresql-devel":
    ensure => present,
    require => Exec["yum update"],
}

package {"zlib":
    ensure => present,
    require => Exec["yum update"],
}

package {"zlib-devel":
    ensure => present,
    require => Exec["yum update"],
}

package {"libjpeg":
    ensure => present,
    require => Exec["yum update"],
}

package {"libjpen-devel":
    ensure => present,
    require => Exec["yum update"],
}

service {"postgresql-9.4.service":
    require => Package["postgresql94-server"],
    enable  => true,
}

service {"nginx":
    enable => true,
}
