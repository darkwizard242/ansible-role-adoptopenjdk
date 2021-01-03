[![build-test](https://github.com/darkwizard242/ansible-role-adoptopenjdk/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-adoptopenjdk/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-adoptopenjdk/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-adoptopenjdk/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/52607?color=dark%20green%20) ![Ansible Role](https://img.shields.io/ansible/role/d/52607?label=role%20downloads) ![Ansible Quality Score](https://img.shields.io/ansible/quality/52607?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-adoptopenjdk&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-adoptopenjdk) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-adoptopenjdk&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-adoptopenjdk) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-adoptopenjdk&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-adoptopenjdk) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-adoptopenjdk&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-adoptopenjdk) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-adoptopenjdk?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-adoptopenjdk?color=orange&style=flat-square)

# Ansible Role: adoptopenjdk

Role to install (_by default_) [adoptopenjdk](https://adoptopenjdk.net/index.html) package for Debian based and EL based systems or uninstall (_if passed as var_) on **Debian** based and **EL** based systems.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables List:

```yaml
# Generic Variables
adoptopenjdk_app_name: adoptopenjdk-11-hotspot
adoptopenjdk_desired_state: present

# Debian Family Variables
adoptopenjdk_pre_reqs_debian:
  - apt-transport-https
  - wget
  - gnupg
adoptopenjdk_pre_reqs_debian_desired_state: present
adoptopenjdk_repo_debian_gpg_key: https://adoptopenjdk.jfrog.io/adoptopenjdk/api/gpg/key/public
adoptopenjdk_repo_debian: "deb https://adoptopenjdk.jfrog.io/adoptopenjdk/deb {{ ansible_lsb['codename'] }} main"
adoptopenjdk_repo_debian_filename: "{{ adoptopenjdk_app_name }}"
adoptopenjdk_repo_debian_desired_state: present

# EL Family Variables
adoptopenjdk_repo_el_gpg_key: https://adoptopenjdk.jfrog.io/adoptopenjdk/api/gpg/key/public
adoptopenjdk_repo_el_name: AdoptOpenJDK
adoptopenjdk_repo_el_description: AdoptOpenJDK
adoptopenjdk_repo_el: http://adoptopenjdk.jfrog.io/adoptopenjdk/rpm/centos/$releasever/$basearch
adoptopenjdk_repo_el_filename: "{{ adoptopenjdk_app_name }}"
adoptopenjdk_repo_el_gpgcheck: yes
adoptopenjdk_repo_el_enabled: yes
adoptopenjdk_repo_el_desired_state: present
```

### Variables table:

Variable                                   | Value (default)                                                                           | Description
------------------------------------------ | ----------------------------------------------------------------------------------------- | -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
adoptopenjdk_app_name                      | adoptopenjdk-11-hotspot                                                                   | Name of AdoptOpenJdk package to install by default i.e. `adoptopenjdk-11-hotspot` . You may use other packages such as `adoptopenjdk-8-openj9`, `adoptopenjdk-15-hotspot` etc.. as well.
adoptopenjdk_desired_state                 | present                                                                                   | State of the adoptopenjdk_app_name package (i.e. `adoptopenjdk-11-hotspot` package itself.). Whether to install, verify if available or to uninstall (i.e. ansible apt module values: `present`, `latest`, or `absent`)
adoptopenjdk_pre_reqs_debian               | apt-transport-https, wget, gnupg                                                          | Package required by AdoptOpenJdk on Debain based systems.
adoptopenjdk_pre_reqs_debian_desired_state | present                                                                                   | State of the adoptopenjdk_pre_reqs_debian_desired_state packages. Whether to install, verify if available or to uninstall (i.e. ansible apt module values: `present`, `latest`, or `absent`)
adoptopenjdk_repo_debian_gpg_key           | <https://adoptopenjdk.jfrog.io/adoptopenjdk/api/gpg/key/public>                           | AdoptOpenJdk GPG required on Debian based systems.
adoptopenjdk_repo_debian                   | "deb <https://adoptopenjdk.jfrog.io/adoptopenjdk/deb> {{ ansible_lsb['codename'] }} main" | Repository URL for Debian based systems.
adoptopenjdk_repo_debian_filename          | "{{ adoptopenjdk_app_name }}"                                                             | Name of the repository file that will be stored at `/etc/apt/sources.list.d/` on Debian based systems. Defaults to the variable value for "{{ adoptopenjdk_app_name }}" which is `adoptopenjdk-11-hotspot` by default.
adoptopenjdk_repo_debian_desired_state     | present                                                                                   | State of Debian family repository file for AdoptOpenJdk.
adoptopenjdk_repo_el_name                  | AdoptOpenJDK                                                                              | Repository name for AdoptOpenJDK on EL based systems.
adoptopenjdk_repo_el_gpg_key               | <https://adoptopenjdk.jfrog.io/adoptopenjdk/api/gpg/key/public>                           | AdoptOpenJdk GPG required on EL based systems.
adoptopenjdk_repo_el_description           | AdoptOpenJDK                                                                              | Description to be added in EL based repository file for AdoptOpenJDK.
adoptopenjdk_repo_el                       | <http://adoptopenjdk.jfrog.io/adoptopenjdk/rpm/centos/$releasever/$basearch>              | Repository `baseurl` for AdoptOpenJDK on EL based systems.
adoptopenjdk_repo_el_gpgcheck              | yes                                                                                       | Boolean for whether to perform gpg check against AdoptOpenJDK on EL based systems.
adoptopenjdk_repo_el_enabled               | yes                                                                                       | Boolean for whether to set AdoptOpenJDK repo as 'enabled' on EL based systems.
adoptopenjdk_repo_el_filename              | "{{ adoptopenjdk_app_name }}"                                                             | Name of the repository file that will be stored at `/etc/yum/sources.list.d/` on EL based systems. Defaults to the variable value for "{{ adoptopenjdk_app_name }}" which is `adoptopenjdk-11-hotspot` by default.
adoptopenjdk_repo_el_desired_state         | present                                                                                   | State of EL family repository file for AdoptOpenJdk.

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **adoptopenjdk-11-hotspot** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.adoptopenjdk
```

For customizing behavior of role (for e.g. installation of j9 jvm instead of hotspot, **adoptopenjdk-15-openj9** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.adoptopenjdk
  vars:
    adoptopenjdk_app_name: adoptopenjdk-15-openj9
```

For customizing behavior of role (for e.g. un-installation of **adoptopenjdk-11-hotspot** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.adoptopenjdk
  vars:
    adoptopenjdk_desired_state: absent
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-adoptopenjdk/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.linkedin.com/in/ali-muhammad-759791130/).
