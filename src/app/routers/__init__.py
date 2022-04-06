from importlib import import_module
from pathlib import Path
from pkgutil import iter_modules


def auto_include_routers(app):
    package_dir = Path(__file__).resolve().parent
    for a, package_name, b in iter_modules([package_dir]):
        module_dir = package_dir.joinpath(package_name)
        for _, module_name, _ in iter_modules([module_dir]):
            module = import_module(f"{__name__}.{package_name}.{module_name}")
            app.include_router(module.router)
