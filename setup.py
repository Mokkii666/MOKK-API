import setuptools

with open("README.md", encoding='utf-8', mode="r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mokiapi",                                         
    version="0.0.1",                         
    author="mokkii666 ",                              
    author_email="nibcmubd@hotmail.com",                  
    description="一个聚合了很多api的python库",               
    long_description=long_description,                  
    long_description_content_type="text/markdown",        
    url="https://github.com/Mokkii666/MOKK-API/",                              
    packages=setuptools.find_packages(),                   
    classifiers=[                                          
        "Programming Language :: Python :: 3.8.6",              
        "License :: OSI Approved :: MIT License",         
        "Operating System :: OS Independent",              
    ],
)