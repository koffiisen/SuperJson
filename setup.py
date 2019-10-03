from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()
    setup(
        name='smartjson',
        version='2.0.1',
        author="J. Koffi ONIPOH",
        author_email="jolli644@gmail.com",
        description="Tool to convert Class, object and dict to Json and Json to Object",
        long_description=long_description,
        long_description_content_type='text/markdown',
        url="https://github.com/koffiisen/SmartJson",
        keywords=['Json', 'Class', 'Object to json', 'Class to json',
                  'json to object', 'json to class', 'Tool', 'convert Class',
                  'object and dict', 'to Json', 'Json to Object',
                  'Class', 'date', 'datetime', 'set',
                  'OrderedDict', 'deque', 'list',
                  'int', 'float', 'bool', 'complex', 'tuple', 'str',
                  'dict', 'bytes', 'None'],
        packages=find_packages(),
        python_requires='>=2.7',
        include_package_data=False,
        classifiers=[
            "Programming Language :: Python",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.1",
            "Programming Language :: Python :: 3.2",
            "Programming Language :: Python :: 3.3",
            "Programming Language :: Python :: 3.4",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.7.4",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
    )
