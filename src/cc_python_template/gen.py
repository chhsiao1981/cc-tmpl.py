import os
import re

from cookiecutter.main import cookiecutter


def _dash_to_underscore(the_str):
    '''
    dash style to underscore style.

    ex:
    the-str => the_str
    '''
    return re.sub(r'-', '_', the_str)


def _underscore_to_uppercase(the_str):
    '''
    underscore style to UPPERCASE style.

    ex:
    the_str => THE_STR
    '''
    return the_str.upper()


def _underscore_to_pascal_case(the_str):
    '''
    underscore style to PascalCase style.

    ex:
    the_str => TheStr
    '''
    the_list = the_str.split('_')
    return ''.join([each_str.title() for each_str in the_list])


def _underscore_to_camelcase(the_str):
    '''
    underscore style to camelCase style.

    ex:
    the_str => theStr
    '''
    the_list = the_str.split('_')
    return the_list[0] + ''.join([each_str.title() for each_str in the_list[1:]])


def generate(tmpl_dir: str, full_name: str, is_force):
    project_with_dash = os.path.basename(os.getcwd())
    project = _dash_to_underscore(project_with_dash)

    full_name_ = _dash_to_underscore(full_name)

    project_full_name_list = [project] + full_name_.split('.')

    pkg = '.'.join(project_full_name_list[:-1])
    module = project_full_name_list[-1]

    pkg_name = pkg
    project_name = project
    include_pkg = pkg

    package_dir = '/'.join(project_full_name_list[:-1])

    include_package_dir = package_dir

    test_package_dir = '/'.join(['test_' + each_pkg for each_pkg in project_full_name_list[1:-1]])

    the_dict = {
        'full_name': full_name,

        'pkg': pkg,
        'module': module,
        # 'project': project, # XXX already included in cookiecutter.

        'pkg_name': pkg_name,
        'project_name': project_name,
        'project_name_with_dash': project_with_dash,

        'include_pkg': include_pkg,

        'package_dir': package_dir,
        'include_package_dir': include_package_dir,
        'test_package_dir': test_package_dir,

        'full_name_': full_name_,

        'PKG': _underscore_to_uppercase(pkg),
        'MODULE': _underscore_to_uppercase(module),
        'PROJECT': _underscore_to_uppercase(project),
        'PKG_NAME': _underscore_to_uppercase(pkg_name),
        'PROJECT_NAME': _underscore_to_uppercase(project_name),
        'INCLUDE_PKG': _underscore_to_uppercase(include_pkg),
        'PACKAGE_DIR': _underscore_to_uppercase(package_dir),
        'INCLUDE_PACKAGE_DIR': _underscore_to_uppercase(include_package_dir),
        'TEST_PACKAGE_DIR': _underscore_to_uppercase(test_package_dir),
        'FULL_NAME': _underscore_to_uppercase(full_name_),

        'Pkg': _underscore_to_pascal_case(pkg),
        'Module': _underscore_to_pascal_case(module),
        'Project': _underscore_to_pascal_case(project),
        'PkgName': _underscore_to_pascal_case(pkg_name),
        'ProjectName': _underscore_to_pascal_case(project_name),
        'IncludePkg': _underscore_to_pascal_case(include_pkg),
        'PackageDir': _underscore_to_pascal_case(package_dir),
        'IncludePackageDir': _underscore_to_pascal_case(include_package_dir),
        'TestPackageDir': _underscore_to_pascal_case(test_package_dir),
        'FullName': _underscore_to_pascal_case(full_name_),

        'pkgCamel': _underscore_to_camelcase(pkg),
        'moduleCamel': _underscore_to_camelcase(module),
        'projectCamel': _underscore_to_camelcase(project),
        'pkgName': _underscore_to_camelcase(pkg_name),
        'projectName': _underscore_to_camelcase(project_name),
        'includePkg': _underscore_to_camelcase(include_pkg),
        'packageDir': _underscore_to_camelcase(package_dir),
        'includePackageDir': _underscore_to_camelcase(include_package_dir),
        'testPackageDir': _underscore_to_camelcase(test_package_dir),
        'fullName': _underscore_to_camelcase(full_name_),
    }

    skip_if_file_exists = not is_force
    cookiecutter(
        str(tmpl_dir),
        extra_context=the_dict,
        no_input=True,
        overwrite_if_exists=True,
        skip_if_file_exists=skip_if_file_exists,
    )
