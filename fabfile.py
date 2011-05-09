import re

from fabric.api import run, env, local, hosts, roles, cd, sudo

WWW_DIR_PATH = '~/Sites/'
SITE_NAME = 'testproject'
SITE_EXTENSION = 'nl'
SVN_SERVER = ''
SVN_REPO = '%s/%s/trunk' %(SVN_SERVER, SITE_NAME)

env.roledefs = {
    'local': ['localhost'],
    'staging': ['christian@lenny']
}

def host_type():
    run('uname -s')

@roles('local')
def setup_local():
    with cd('%s' %(WWW_DIR_PATH)):
        base_dir = "%s-%s" %(SITE_NAME,SITE_EXTENSION)
        local('mkdir %s-%s' base_dir)
    with cd(base_dir):
        local('virtualenv env-%s --no-site-packages' %(SITE_NAME))
        
        #Sanity check: pip is not global pip
        pip_location = local('which pip')
        if not re.match(r'env-%s' %(SITE_NAME), pip_location):
            raise Exception
            
        #Setup log files
        local('mkdir logs')
        with cd('logs'):
            local('touch error.log access.log')
            
        #Pull latest from repo
        local('svn co %s %s' %(SVN_REPO, SITE_NAME)
        local('pip install django south MySQL-python')
        
@roles('staging')
def setup_staging(name, extension):
    with cd('%s' %(WWW_DIR_PATH)):
        sudo('mkdir -p C_%s-%s/www/http_docs' %(SITE_NAME, SITE_EXTENSION))
    with cd('www'):
        sudo('virtualenv env-%s --no-site-packages' %(SITE_NAME))
        pip_location = sudo('which pip')
        if not re.match(r'env-%s' %(SITE_NAME), pip_location):
            raise Exception
        sudo('mkdir logs')
        sudo('touch error.log access.log')
    with cd('http_docs'):
        sudo('svn co %s %s' %(SVN_REPO, SITE_NAME)

@roles('staging')
def reload_staging():
    with cd('%s/C_%s-%s/www/http_docs/%s' %(WWW_DIR_PATH, SITE_NAME, SITE_EXTENSION)):
        sudo('svn update')
        sudo('touch -c ../../django.wsgi')

def deploy():
    with cd('%s/C_%s-%s/www' %(WWW_DIR_PATH, SITE_NAME, SITE_EXTENSION)):
        sudo('touch -c django.wsgi')