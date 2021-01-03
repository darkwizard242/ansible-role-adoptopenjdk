import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

PACKAGE = 'adoptopenjdk-11-hotspot'
PACKAGE_BINARY = '/usr/bin/java'
REPO_DEBIAN_FILE = '/etc/apt/sources.list.d/adoptopenjdk-11-hotspot.list'
REPO_EL_FILE = '/etc/yum.repos.d/adoptopenjdk-11-hotspot.repo'


def test_adoptopenjdk_package_installed(host):
    """
    Tests if adoptopenjdk-11-hotspot package is installed.
    """
    assert host.package(PACKAGE).is_installed


def test_adoptopenjdk_binary_exists(host):
    """
    Tests if java binary exists.
    """
    host.file(PACKAGE_BINARY).exists


def test_adoptopenjdk_binary_isfile(host):
    """
    Tests if java binary is a file type.
    """
    assert host.file(PACKAGE_BINARY).is_file


def test_adoptopenjdk_binary_which(host):
    """
    Tests the output to confirm java's binary location.
    """
    assert host.check_output('which java') == PACKAGE_BINARY


def test_adoptopenjdk_repofile_exists(host):
    """
    Tests if adoptopenjdk-11-hotspot repo file exists.
    """
    assert host.file(REPO_DEBIAN_FILE).exists or \
        host.file(REPO_EL_FILE).exists


def test_adoptopenjdk_repofile_isfile(host):
    """
    Tests if adoptopenjdk-11-hotspot repo file is file type.
    """
    assert host.file(REPO_DEBIAN_FILE).is_file or \
        host.file(REPO_EL_FILE).is_file
