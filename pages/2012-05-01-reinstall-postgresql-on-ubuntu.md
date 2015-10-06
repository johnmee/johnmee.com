title: Reinstall Postgresql on Debian and Ubuntu
published: 2012-05-01
tag: technical
comments: Yes


## How to purge and reinstall postgresql on ubuntu?

Somehow I managed to completely bugger the install of postgresql on Ubuntu.  Now I want to start over from scratch, but when I "purge" the package with apt-get it still leaves traces behind such that 
the reinstall configuration doesn't run properly.

After I've done:

    apt-get purge postgresql
    apt-get install postgresql

It said

    Setting up postgresql-8.4 (8.4.3-0ubuntu9.10.1) ...
    Configuring already existing cluster (configuration: /etc/postgresql/8.4/main, data: /var/lib/postgresql/8.4/main, owner: 108:112)
    Error: move_conffile: required configuration file     /var/lib/postgresql/8.4/main/postgresql.conf does not exist
    Error: could not create default cluster. Please create it manually with

      pg_createcluster 8.4 main --start

    or a similar command (see 'man pg_createcluster').
    update-alternatives: using /usr/share/postgresql/8.4/man/man1/postmaster.1.gz to provide /usr/share/man/man1/postmaster.1.gz (postmaster.1.gz) in auto mode.

    Setting up postgresql (8.4.3-0ubuntu9.10.1) ...


I have a "/etc/postgresql" with nothing in it and "/etc/postgresql-common/" has a 'pg_upgradecluser.d' directory and root.crt and user_clusters files.

The /etc/passwd has a postgres user; the purge script doesn't appear to touch it.  There's been a bunch of symptoms which I work through only to expose the next. 

Right this second, when I run that command "pg_createcluster..." it complains that '/var/lib/postgresql/8.4/main/postgresql.conf does not exist', so I'll go find one of those but I'm sure that won't be the end of it.

Is there not some easy one-liner (or two) which will burn it completely and let me start over?


## Answer

First: If your install isn't already damaged, you can drop unwanted PostgreSQL servers ("clusters") in Ubuntu using `pg_dropcluster`. Use that in preference to a full purge and reinstall if you just want to start with a freshly `initdb`'d PostgreSQL instance.

If you really need to do a full purge and reinstall, first make sure PostgreSQL isn't running. `ps -C postgres` should show no results.

Now run:

    apt-get --purge remove postgresql\*

to remove everything PostgreSQL from your system. Just purging the `postgres` package isn't enough since it's just an empty meta-package.

Once all PostgreSQL packages have been removed, run:

    rm -r /etc/postgresql/
    rm -r /etc/postgresql-common/
    rm -r /var/lib/postgresql/
    userdel -r postgres
    groupdel postgres

You should now be able to:

    apt-get install postgresql

or for a complete install:

    apt-get install postgresql-8.4 postgresql-contrib-8.4 postgresql-doc-8.4
