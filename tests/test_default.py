import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('glusterfs')


def test_glusterfs_repo(Package):
    glusterfs_repo = Package('centos-release-gluster')

    assert glusterfs_repo.is_installed


def test_glusterfs_package(Package):
    glusterfs_package = Package('glusterfs-server')

    assert glusterfs_package.is_installed


def test_glusterfs_started_enabled(Service):
    glusterfs = Service('glusterd')

    assert glusterfs.is_running
    assert glusterfs.is_enabled
